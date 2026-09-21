#!/usr/bin/env python3
"""Deterministic dependency lock and artifact-inventory tooling for Qdrat.

This module is deliberately narrow. It never resolves, downloads or installs
anything: pip does that inside the pinned Linux amd64 CPython 3.12 acquisition
environment. This module only turns the facts pip observed there into two
committed artifacts:

* ``requirements/locks/<target>.txt`` - a requirements file that reinstalls the
  exact distribution set with ``--require-hashes`` and no index access;
* ``requirements/artifacts/<target>.json`` - a machine-readable inventory that
  binds every distribution to its source URL, byte hash, artifact kind and
  license, plus the resolver and bootstrap tools used to produce it.

Two invariants shape the code:

1. Nothing is emitted that is not fully accounted for. An artifact with no
   matching resolution entry, a resolution entry with no matching artifact, a
   missing hash or a duplicate distribution name all abort instead of producing
   a partial lock.
2. Exactly one target is supported. Any other target is rejected explicitly,
   because a lock frozen for linux/amd64 CPython 3.12 cannot be honoured
   anywhere else and must never be silently reused.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

RESOLUTION_SCHEMA = "qdrat.dependency-resolution/v1"
ARTIFACTS_SCHEMA = "qdrat.dependency-artifacts/v1"
LOCK_HEADER_SCHEMA = "qdrat.dependency-lock/v1"

# The single qualified target. Every other platform is rejected in `verify`.
SUPPORTED_TARGETS = ("linux-amd64-py312",)
TARGET_PLATFORM = {
    "linux-amd64-py312": {
        "os": "linux",
        "arch": "amd64",
        "libc": "glibc",
        "python_implementation": "CPython",
        "python_version": "3.12",
    },
}

WHEEL_SUFFIXES = (".whl",)
SDIST_SUFFIXES = (".tar.gz", ".zip", ".tar.bz2")


class ToolError(RuntimeError):
    """A deterministic refusal to emit or accept an artifact."""


class UnsupportedTargetError(ToolError):
    """The requested target is not a qualified platform for this lock."""


def normalized_name(name: str) -> str:
    """PEP 503 name normalisation, used for every cross-artifact comparison."""
    return re.sub(r"[-_.]+", "-", name).strip().lower()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_text_bytes(path: Path) -> bytes:
    """Return a generated text artifact's bytes with CRLF normalised to LF.

    `Path.write_text` translates `\n` to the host's line separator, so on
    Windows the lock on disk was CRLF while the committed object was LF (this
    repository pins `*.txt text eol=lf`). Hashing the raw bytes therefore bound
    one machine's working tree instead of the artifact in the repository, and
    every re-derivation from a fresh checkout disagreed with the record. The
    canonical form is what git stores, so it is what the digest must describe.
    """
    return path.read_bytes().replace(b"\r\n", b"\n")


def sha256_text_file(path: Path) -> str:
    """Hash a generated text artifact by its LF-canonical content."""
    return hashlib.sha256(canonical_text_bytes(path)).hexdigest()


def write_text_lf(path: Path, text: str) -> None:
    """Write a generated text artifact with LF newlines on every platform."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def read_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ToolError(f"missing required input: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ToolError(f"{path} is not valid JSON: {exc}") from exc


def write_json(path: Path, payload: object) -> None:
    write_text_lf(
        path,
        json.dumps(payload, indent=2, sort_keys=False, ensure_ascii=False) + "\n",
    )


def artifact_filename(url: str) -> str:
    """Return the artifact file name, refusing anything that is not one path segment.

    The URL is percent-decoded *before* the final segment is taken: decoding
    afterwards would turn `..%2fsecret` into `../secret`, which is a path and not
    a file name, and the caller would then join it onto a directory.
    """
    name = Path(unquote(urlparse(url).path)).name
    if not name or name in {".", ".."} or "/" in name or "\\" in name:
        raise ToolError(f"artifact URL does not name a single file: {url}")
    return name


def contained_path(directory: Path, name: str) -> Path:
    """Join `name` onto `directory`, refusing anything that escapes it."""
    candidate = (directory / name).resolve()
    root = directory.resolve()
    if candidate.parent != root:
        raise ToolError(f"artifact path escapes {directory}: {name}")
    return candidate


def read_sha256_listing(path: Path) -> dict[str, str]:
    """Parse a `sha256sum` listing into {filename: sha256}.

    The listing is produced by GNU sha256sum over the acquired artifacts, so it
    is an independent computation from pip's own recorded hashes. Committing it
    lets the lock and the inventory be re-checked byte-for-byte without the
    wheelhouse itself.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ToolError(f"cannot read sha256 listing {path}: {exc}") from exc
    listing: dict[str, str] = {}
    for number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        fields = line.split(None, 1)
        if len(fields) != 2 or not re.fullmatch(r"[0-9a-f]{64}", fields[0]):
            raise ToolError(f"{path}:{number} is not a sha256sum line: {raw!r}")
        # These are filesystem names produced by sha256sum, not URLs, so they are
        # deliberately not percent-decoded: decoding a literal '%' sequence would
        # turn a real name into a different one and break the comparison.
        name = Path(fields[1].strip().lstrip("*")).name
        if not name or name in {".", ".."}:
            raise ToolError(f"{path}:{number} does not name a file: {raw!r}")
        if name in listing:
            raise ToolError(f"{path}:{number} repeats {name}")
        listing[name] = fields[0]
    if not listing:
        raise ToolError(f"{path} contains no sha256 entries")
    return listing


def artifact_kind(filename: str) -> str:
    lowered = filename.lower()
    if lowered.endswith(WHEEL_SUFFIXES):
        return "wheel"
    if lowered.endswith(SDIST_SUFFIXES):
        return "sdist"
    raise ToolError(f"unrecognised distribution artifact: {filename}")


def archive_sha256(download_info: dict) -> str:
    """Read pip's recorded sha256 for one downloaded artifact."""
    archive = download_info.get("archive_info")
    if not isinstance(archive, dict):
        raise ToolError(f"resolution entry has no archive_info: {download_info!r}")
    hashes = archive.get("hashes")
    if isinstance(hashes, dict) and isinstance(hashes.get("sha256"), str):
        return hashes["sha256"].lower()
    recorded = archive.get("hash")
    if isinstance(recorded, str) and recorded.startswith("sha256="):
        return recorded.split("=", 1)[1].lower()
    raise ToolError(f"resolution entry has no sha256 hash: {download_info!r}")


def cmd_resolve(args: argparse.Namespace) -> int:
    """Normalise one wheelhouse plus pip's own resolution report."""
    report = read_json(Path(args.report))
    entries = report.get("install") if isinstance(report, dict) else None
    if not isinstance(entries, list) or not entries:
        raise ToolError(f"{args.report} contains no resolved distributions")

    wheelhouse = Path(args.wheelhouse)
    if not wheelhouse.is_dir():
        raise ToolError(f"wheelhouse directory not found: {wheelhouse}")
    files = sorted(item for item in wheelhouse.iterdir() if item.is_file())
    if not files:
        raise ToolError(f"wheelhouse is empty: {wheelhouse}")

    by_hash: dict[str, list[str]] = {}
    for item in files:
        by_hash.setdefault(sha256_file(item), []).append(item.name)

    distributions = []
    claimed: set[str] = set()
    seen_names: dict[str, str] = {}
    for entry in entries:
        metadata = entry.get("metadata") or {}
        name, version = metadata.get("name"), metadata.get("version")
        if not isinstance(name, str) or not isinstance(version, str):
            raise ToolError(f"resolution entry lacks name/version metadata: {entry!r}")
        download_info = entry.get("download_info") or {}
        url = download_info.get("url")
        if not isinstance(url, str) or not url:
            raise ToolError(f"resolution entry lacks a download URL: {entry!r}")

        digest = archive_sha256(download_info)
        filename = artifact_filename(url)
        if filename not in by_hash.get(digest, []):
            raise ToolError(
                "wheelhouse does not contain the artifact pip resolved for "
                f"{name}=={version} (expected {filename} with sha256 {digest})"
            )
        key = normalized_name(name)
        if key in seen_names:
            raise ToolError(f"duplicate distribution in resolution: {name}")
        seen_names[key] = version
        claimed.add(filename)
        distributions.append(
            {
                "name": name,
                "normalized_name": key,
                "version": version,
                "kind": artifact_kind(filename),
                "filename": filename,
                "sha256": digest,
                "url": url,
                "direct": bool(entry.get("is_direct")),
            }
        )

    unclaimed = sorted(item.name for item in files if item.name not in claimed)
    if unclaimed:
        raise ToolError(
            "wheelhouse artifacts are not accounted for by the resolution report: "
            + ", ".join(unclaimed)
        )

    distributions.sort(key=lambda item: (item["normalized_name"], item["version"]))
    write_json(
        Path(args.out),
        {
            "schema": RESOLUTION_SCHEMA,
            "target": args.target,
            "python_version": TARGET_PLATFORM[args.target]["python_version"],
            "distributions": distributions,
        },
    )
    return 0


def _resolution_distributions(path: Path, target: str) -> list[dict]:
    payload = read_json(path)
    if not isinstance(payload, dict) or payload.get("schema") != RESOLUTION_SCHEMA:
        raise ToolError(f"{path} is not a {RESOLUTION_SCHEMA} document")
    if payload.get("target") != target:
        raise ToolError(f"{path} targets {payload.get('target')!r}, not {target!r}")
    distributions = payload.get("distributions")
    if not isinstance(distributions, list) or not distributions:
        raise ToolError(f"{path} contains no distributions")
    seen: set[str] = set()
    for item in distributions:
        if not isinstance(item, dict):
            raise ToolError(f"{path} contains a distribution entry that is not an object")
        name = item.get("normalized_name")
        if not isinstance(name, str) or not name:
            raise ToolError(f"{path} contains a distribution without a normalized name")
        for field in ("name", "version", "kind", "filename", "sha256", "url"):
            if not isinstance(item.get(field), str) or not item[field]:
                raise ToolError(f"{path}: {name} has no {field}")
        if name in seen:
            raise ToolError(f"{path} contains duplicate distribution {name}")
        seen.add(name)
    return distributions


def render_lock(target: str, distributions: list[dict], header: dict) -> str:
    lines = [
        f"# Qdrat dependency lock - {LOCK_HEADER_SCHEMA}",
        f"# target            {target}",
        f"# input             {header['input_path']} (sha256:{header['input_sha256']})",
        f"# resolver          {header['resolver_tool']} {header['resolver_version']}",
        f"# builder image     {header['builder_image']}",
        f"# inventory         {header['artifacts_path']}",
        "#",
        "# Install this exact distribution set with no index access:",
        "#   python -m pip install --no-index --find-links <wheelhouse> \\",
        f"#       --require-hashes -r {header['lock_path']}",
        "#",
        "# Every line below is pinned and carries its byte hash. Artifacts marked",
        "# 'direct source' are not published on an index and are resolved from the",
        "# recorded URL during acquisition only; the lock installs them from the",
        "# wheelhouse by name like every other distribution.",
        "",
    ]
    for item in distributions:
        if item["direct"]:
            lines.append(f"# direct source: {item['url']}")
        lines.append(f"{item['name']}=={item['version']} --hash=sha256:{item['sha256']}")
    return "\n".join(lines) + "\n"


def cmd_build(args: argparse.Namespace) -> int:
    """Emit the lock and inventory only for two agreeing isolated resolutions."""
    if args.target not in SUPPORTED_TARGETS:
        raise UnsupportedTargetError(f"unsupported target: {args.target}")
    first = _resolution_distributions(Path(args.resolution_a), args.target)
    second = _resolution_distributions(Path(args.resolution_b), args.target)
    if first != second:
        first_keys = {(d["normalized_name"], d["version"], d["sha256"]) for d in first}
        second_keys = {(d["normalized_name"], d["version"], d["sha256"]) for d in second}
        drift = sorted(
            f"{name}=={version} ({'A' if (name, version, digest) in first_keys else ''}"
            f"{'B' if (name, version, digest) in second_keys else ''})"
            for name, version, digest in first_keys ^ second_keys
        )
        raise ToolError(
            "the two isolated resolutions disagree; refusing to freeze a lock: "
            + "; ".join(drift)
        )

    input_path = Path(args.input)
    if not input_path.is_file():
        raise ToolError(f"input requirements file not found: {input_path}")
    input_sha256 = sha256_text_file(input_path)

    header = {
        "input_path": args.input_label,
        "input_sha256": input_sha256,
        "resolver_tool": "pip",
        "resolver_version": args.resolver_version,
        "builder_image": args.builder_image,
        "lock_path": args.lock_label,
        "artifacts_path": args.artifacts_label,
    }
    lock_text = render_lock(args.target, first, header)
    lock_path = Path(args.lock_out)
    write_text_lf(lock_path, lock_text)

    bootstrap = []
    for raw in args.bootstrap:
        name, _, filename = raw.partition("=")
        artifact = Path(args.bootstrap_dir) / filename
        if not artifact.is_file():
            raise ToolError(f"declared bootstrap artifact not found: {artifact}")
        parts = filename.split("-")
        if len(parts) < 2 or normalized_name(parts[0]) != normalized_name(name):
            raise ToolError(f"bootstrap artifact {filename} does not match {name}")
        bootstrap.append(
            {
                "name": name,
                "version": parts[1],
                "filename": filename,
                "sha256": sha256_file(artifact),
                "purpose": "build backend for sdist-only distributions",
            }
        )

    write_json(
        Path(args.artifacts_out),
        {
            "schema": ARTIFACTS_SCHEMA,
            "target": args.target,
            "supported_targets": list(SUPPORTED_TARGETS),
            "platform": TARGET_PLATFORM[args.target],
            "input": {"path": args.input_label, "sha256": input_sha256},
            "resolver": {
                "tool": "pip",
                "version": args.resolver_version,
                "builder_image": args.builder_image,
                "wheelhouse": args.wheelhouse_label,
            },
            "bootstrap": bootstrap,
            "lock": {
                "path": args.lock_label,
                "sha256": sha256_text_file(lock_path),
                "line_format": "name==version --hash=sha256:<hex>",
            },
            "distributions": first,
            "counts": {
                "distributions": len(first),
                "wheels": sum(1 for item in first if item["kind"] == "wheel"),
                "sdists": sum(1 for item in first if item["kind"] == "sdist"),
                "direct": sum(1 for item in first if item["direct"]),
            },
        },
    )
    return 0


LOCK_LINE = re.compile(
    r"^(?P<name>[A-Za-z0-9][A-Za-z0-9._-]*)==(?P<version>[^\s;]+)"
    r"(?P<hashes>(\s+--hash=sha256:[0-9a-f]{64})+)\s*$"
)


def parse_lock(path: Path) -> dict[str, tuple[str, list[str]]]:
    """Parse the locked distribution set, refusing anything unpinned or unhashed."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ToolError(f"cannot read lock file {path}: {exc}") from exc
    requirements: dict[str, tuple[str, list[str]]] = {}
    for number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = LOCK_LINE.match(line)
        if match is None:
            raise ToolError(f"{path}:{number} is not a pinned, hashed requirement: {raw!r}")
        hashes = re.findall(r"--hash=sha256:([0-9a-f]{64})", match.group("hashes"))
        key = normalized_name(match.group("name"))
        if key in requirements:
            raise ToolError(f"{path}:{number} repeats distribution {match.group('name')}")
        requirements[key] = (match.group("version"), hashes)
    if not requirements:
        raise ToolError(f"{path} contains no requirements")
    return requirements


def cmd_verify(args: argparse.Namespace) -> int:
    """Reject unsupported targets, then reconcile lock, inventory and install."""
    if args.target not in SUPPORTED_TARGETS:
        raise UnsupportedTargetError(
            f"unsupported target: {args.target}; this lock is qualified for "
            + ", ".join(SUPPORTED_TARGETS)
            + " only and must not be reused on another platform"
        )

    artifacts = read_json(Path(args.artifacts))
    if not isinstance(artifacts, dict) or artifacts.get("schema") != ARTIFACTS_SCHEMA:
        raise ToolError(f"{args.artifacts} is not a {ARTIFACTS_SCHEMA} document")
    if artifacts.get("target") != args.target:
        raise ToolError(
            f"inventory target {artifacts.get('target')!r} does not match {args.target!r}"
        )

    # The inventory records the digest of the lock it was frozen from. Without
    # this comparison nothing in the gate would notice a lock that no longer
    # matches its own record: the unit tests read the committed artifacts, and
    # the reconciliation below compares the lock's *contents* to the inventory,
    # not the lock's bytes. Text artifacts are hashed with CRLF normalised to
    # LF, so this compares content, not the checkout's line endings.
    recorded_lock = artifacts.get("lock")
    if not isinstance(recorded_lock, dict) or not isinstance(
        recorded_lock.get("sha256"), str
    ):
        raise ToolError(
            f"{args.artifacts} must record the frozen lock digest under lock.sha256"
        )
    observed_lock_digest = sha256_text_file(Path(args.lock))
    if observed_lock_digest != recorded_lock["sha256"]:
        raise ToolError(
            "the lock does not match the digest recorded in the inventory: "
            f"observed {observed_lock_digest}, recorded {recorded_lock['sha256']}"
        )

    lock = parse_lock(Path(args.lock))
    inventory = {
        normalized_name(item["name"]): (item["version"], [item["sha256"]])
        for item in artifacts["distributions"]
    }
    if lock != inventory:
        drift = sorted(
            f"{name}: lock={lock.get(name)} inventory={inventory.get(name)}"
            for name in set(lock) ^ set(inventory)
        )
        for name in sorted(set(lock) & set(inventory)):
            if lock[name] != inventory[name]:
                drift.append(f"{name}: lock={lock[name]} inventory={inventory[name]}")
        raise ToolError("lock and artifact inventory disagree: " + "; ".join(drift))

    installed = read_json(Path(args.installed))
    if not isinstance(installed, list):
        raise ToolError(f"{args.installed} must be a JSON list of installed distributions")
    actual = {}
    for item in installed:
        if (
            not isinstance(item, dict)
            or not isinstance(item.get("name"), str)
            or not isinstance(item.get("version"), str)
        ):
            raise ToolError(
                f"{args.installed} contains an entry without a name/version string: {item!r}"
            )
        actual[normalized_name(item["name"])] = item["version"]
    expected = {name: version for name, (version, _) in lock.items()}
    tooling = {normalized_name(name) for name in args.tool_distribution}
    collision = sorted(tooling & set(expected))
    if collision:
        raise ToolError(
            "declared tool distributions are also locked application "
            "dependencies and cannot be excluded: " + ", ".join(collision)
        )
    excluded = sorted(name for name in tooling if name in actual)
    missing = sorted(name for name in expected if name not in actual)
    unexpected = sorted(
        name for name in actual if name not in expected and name not in tooling
    )
    mismatched = sorted(
        f"{name}: installed={actual[name]} locked={expected[name]}"
        for name in expected
        if name in actual and actual[name] != expected[name]
    )
    if missing or unexpected or mismatched:
        raise ToolError(
            "installed distribution inventory does not match the lock: "
            + "; ".join(
                filter(
                    None,
                    [
                        f"missing={missing}" if missing else "",
                        f"unexpected={unexpected}" if unexpected else "",
                        f"mismatched={mismatched}" if mismatched else "",
                    ],
                )
            )
        )

    verified_artifacts = 0
    if args.wheelhouse:
        wheelhouse = Path(args.wheelhouse)
        if not wheelhouse.is_dir():
            raise ToolError(f"wheelhouse directory not found: {wheelhouse}")
        for item in artifacts["distributions"]:
            artifact = contained_path(wheelhouse, item["filename"])
            if not artifact.is_file():
                raise ToolError(f"locked artifact is missing from the wheelhouse: {artifact}")
            observed = sha256_file(artifact)
            if observed != item["sha256"]:
                raise ToolError(
                    f"{item['filename']} does not match the frozen hash: "
                    f"observed {observed}, locked {item['sha256']}"
                )
            verified_artifacts += 1

    verified_bootstrap = 0
    if args.bootstrap_dir:
        directory = Path(args.bootstrap_dir)
        if not directory.is_dir():
            raise ToolError(f"bootstrap directory not found: {directory}")
        declared = artifacts.get("bootstrap", [])
        if not isinstance(declared, list):
            raise ToolError(f"{args.artifacts} has a malformed bootstrap section")
        for entry in declared:
            artifact = contained_path(directory, entry["filename"])
            if not artifact.is_file():
                raise ToolError(f"declared bootstrap artifact is missing: {artifact}")
            observed = sha256_file(artifact)
            if observed != entry["sha256"]:
                raise ToolError(
                    f"bootstrap artifact {entry['filename']} does not match the frozen "
                    f"hash: observed {observed}, recorded {entry['sha256']}"
                )
            verified_bootstrap += 1

    verified_listing = 0
    if args.sha256_listing:
        listing = read_sha256_listing(Path(args.sha256_listing))
        recorded = {
            item["filename"]: item["sha256"] for item in artifacts["distributions"]
        }
        if listing != recorded:
            drift = sorted(
                f"{name}: listing={listing.get(name)} inventory={recorded.get(name)}"
                for name in set(listing) ^ set(recorded)
            )
            drift += sorted(
                f"{name}: listing={listing[name]} inventory={recorded[name]}"
                for name in set(listing) & set(recorded)
                if listing[name] != recorded[name]
            )
            raise ToolError(
                "the recorded sha256 listing disagrees with the artifact inventory: "
                + "; ".join(drift)
            )
        verified_listing = len(listing)

    print(
        json.dumps(
            {
                "target": args.target,
                "distributions": len(expected),
                "installed": len(actual),
                "excluded_tool_distributions": excluded,
                "verified_artifacts": verified_artifacts,
                "verified_bootstrap_artifacts": verified_bootstrap,
                "verified_listing_entries": verified_listing,
                "lock_digest": observed_lock_digest,
                "status": "PASS",
            }
        )
    )
    return 0


def cmd_license_inventory(args: argparse.Namespace) -> int:
    """Dump the license metadata of the environment this command runs inside."""
    from importlib import metadata as importlib_metadata

    records = []
    for distribution in importlib_metadata.distributions():
        meta = distribution.metadata
        classifiers = meta.get_all("Classifier") or []
        records.append(
            {
                "name": meta["Name"],
                "normalized_name": normalized_name(meta["Name"]),
                "version": meta["Version"],
                "license": (meta.get("License-Expression") or meta.get("License") or "").strip(),
                "license_classifiers": sorted(
                    item for item in classifiers if item.startswith("License ::")
                ),
            }
        )
    records.sort(key=lambda item: (item["normalized_name"], item["version"]))
    write_json(Path(args.out), records)
    return 0


def cmd_annotate(args: argparse.Namespace) -> int:
    """Merge the observed license inventory into the artifact inventory."""
    artifacts = read_json(Path(args.artifacts))
    licenses = read_json(Path(args.licenses))
    if not isinstance(artifacts, dict) or artifacts.get("schema") != ARTIFACTS_SCHEMA:
        raise ToolError(f"{args.artifacts} is not a {ARTIFACTS_SCHEMA} document")
    if not isinstance(licenses, list):
        raise ToolError(f"{args.licenses} must be a JSON list")

    observed = {item["normalized_name"]: item for item in licenses}
    unknown = []
    for entry in artifacts["distributions"]:
        record = observed.get(entry["normalized_name"])
        if record is None or record["version"] != entry["version"]:
            unknown.append(entry["name"])
            entry["license"] = {
                "declared": None,
                "classifiers": [],
                "source": "installed-distribution-metadata",
            }
            continue
        entry["license"] = {
            "declared": record["license"] or None,
            "classifiers": record["license_classifiers"],
            "source": "installed-distribution-metadata",
        }
        if not entry["license"]["declared"] and not entry["license"]["classifiers"]:
            unknown.append(entry["name"])
    artifacts["license_unknown"] = sorted(unknown)
    write_json(Path(args.out or args.artifacts), artifacts)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    resolve = sub.add_parser("resolve", help="normalise one wheelhouse + pip report")
    resolve.add_argument("--target", default=SUPPORTED_TARGETS[0], choices=SUPPORTED_TARGETS)
    resolve.add_argument("--wheelhouse", required=True)
    resolve.add_argument("--report", required=True)
    resolve.add_argument("--out", required=True)
    resolve.set_defaults(func=cmd_resolve)

    build = sub.add_parser("build", help="emit lock + inventory from two resolutions")
    build.add_argument("--target", default=SUPPORTED_TARGETS[0])
    build.add_argument("--resolution-a", required=True)
    build.add_argument("--resolution-b", required=True)
    build.add_argument("--input", required=True)
    build.add_argument("--input-label", required=True)
    build.add_argument("--lock-out", required=True)
    build.add_argument("--lock-label", required=True)
    build.add_argument("--artifacts-out", required=True)
    build.add_argument("--artifacts-label", required=True)
    build.add_argument("--wheelhouse-label", required=True)
    build.add_argument("--bootstrap-dir", default="")
    build.add_argument("--bootstrap", action="append", default=[])
    build.add_argument("--resolver-version", required=True)
    build.add_argument("--builder-image", required=True)
    build.set_defaults(func=cmd_build)

    verify = sub.add_parser("verify", help="reconcile lock, inventory and install")
    verify.add_argument("--target", default="")
    verify.add_argument("--lock", required=True)
    verify.add_argument("--artifacts", required=True)
    verify.add_argument("--installed", required=True)
    verify.add_argument(
        "--wheelhouse",
        default="",
        help="recompute the sha256 of every locked artifact on disk",
    )
    verify.add_argument(
        "--bootstrap-dir",
        default="",
        help="recompute the sha256 of every build-bootstrap artifact on disk",
    )
    verify.add_argument(
        "--sha256-listing",
        default="",
        help="reconcile a committed sha256sum listing against the artifact inventory",
    )
    verify.add_argument(
        "--tool-distribution",
        action="append",
        default=[],
        help="environment tooling excluded from the application inventory",
    )
    verify.set_defaults(func=cmd_verify)

    licenses = sub.add_parser("license-inventory", help="dump installed license metadata")
    licenses.add_argument("--out", required=True)
    licenses.set_defaults(func=cmd_license_inventory)

    annotate = sub.add_parser("annotate", help="merge licenses into the inventory")
    annotate.add_argument("--artifacts", required=True)
    annotate.add_argument("--licenses", required=True)
    annotate.add_argument("--out", default="")
    annotate.set_defaults(func=cmd_annotate)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except ToolError as exc:
        print(f"lockfile: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
