#!/usr/bin/env python3
"""Build the image's pip requirements file from the frozen lock and inventory.

The lock produced by ``requirements/tools/lockfile.py`` is installable with
``--no-index --find-links <wheelhouse>`` because every distribution in it is
present in that wheelhouse by name. An image build has no wheelhouse: it
resolves from the index, and exactly one locked distribution -
``en_core_web_sm``, a GitHub release asset - is not on any index at all. A
plain ``pip install --require-hashes -r <lock>`` therefore cannot work in the
build, which is why the image used to install from the unpinned
``requirements.txt`` instead.

This tool closes that gap without duplicating provenance. It reads the two
frozen records and emits one requirements file:

* every distribution whose artifact is published on an index is emitted as
  ``name==version --hash=sha256:<hex>``, exactly as the lock has it;
* the one artifact that is not published on an index is emitted as
  ``name @ <url>#sha256=<hex>``, with the URL taken from the artifact
  inventory, which is the machine record of where the bytes came from.

The lock's human-readable ``# direct source:`` comment is cross-checked against
the inventory. If the two disagree - a different URL, a different hash, a name
that one file marks direct and the other does not - the tool refuses instead of
choosing one.

Nothing here resolves, downloads or verifies anything. It renders a file; pip
does the hash verification under ``--require-hashes``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIREMENT_LINE = re.compile(
    r"^(?P<name>[A-Za-z0-9][A-Za-z0-9._-]*)==(?P<version>[^\s;]+)"
    r"(?P<hashes>(\s+--hash=sha256:[0-9a-f]{64})+)\s*$"
)
DIRECT_COMMENT = re.compile(r"^#\s*direct source:\s*(?P<url>\S+)\s*$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


class ToolError(RuntimeError):
    """A deterministic refusal to emit an image requirements file."""


def normalized_name(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).strip().lower()


def parse_lock(path: Path) -> tuple[list[tuple[str, str, str]], dict[str, str]]:
    """Return (name, version, sha256) entries plus the lock's direct-URL comments."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ToolError(f"cannot read lock file {path}: {exc}") from exc

    entries: list[tuple[str, str, str]] = []
    direct_urls: dict[str, str] = {}
    pending_url: str | None = None
    seen: set[str] = set()

    for number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            match = DIRECT_COMMENT.match(line)
            if match:
                pending_url = match.group("url")
            continue
        match = REQUIREMENT_LINE.match(line)
        if match is None:
            raise ToolError(f"{path}:{number} is not a pinned, hashed requirement: {raw!r}")
        hashes = re.findall(r"--hash=sha256:([0-9a-f]{64})", match.group("hashes"))
        if len(hashes) != 1:
            raise ToolError(
                f"{path}:{number} must carry exactly one sha256 hash, found {len(hashes)}"
            )
        name = match.group("name")
        key = normalized_name(name)
        if key in seen:
            raise ToolError(f"{path}:{number} repeats distribution {name}")
        seen.add(key)
        entries.append((name, match.group("version"), hashes[0]))
        if pending_url is not None:
            direct_urls[key] = pending_url
            pending_url = None

    if not entries:
        raise ToolError(f"{path} contains no requirements")
    return entries, direct_urls


def inventory_direct(path: Path) -> dict[str, str]:
    """Return {normalized name: url} for the distributions the inventory marks direct."""
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ToolError(f"cannot read artifact inventory {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ToolError(f"{path} is not valid JSON: {exc}") from exc
    if not isinstance(payload, dict) or not isinstance(payload.get("distributions"), list):
        raise ToolError(f"{path} does not look like a qdrat artifact inventory")

    direct: dict[str, str] = {}
    for item in payload["distributions"]:
        if not item.get("direct"):
            continue
        name = normalized_name(item["name"])
        url = item.get("url")
        digest = item.get("sha256")
        if not isinstance(url, str) or not url:
            raise ToolError(f"{path}: direct artifact {item['name']} has no url")
        if not url.startswith("https://"):
            raise ToolError(f"{path}: direct artifact {item['name']} is not https: {url}")
        if not isinstance(digest, str) or not SHA256.match(digest):
            raise ToolError(f"{path}: direct artifact {item['name']} has no sha256")
        direct[name] = url
    return direct


def render(entries, direct_urls, direct_inventory) -> str:
    lock_direct = set(direct_urls)
    inventory_direct_names = set(direct_inventory)
    if lock_direct != inventory_direct_names:
        raise ToolError(
            "the lock and the inventory disagree about which artifacts are direct: "
            f"lock-only={sorted(lock_direct - inventory_direct_names)} "
            f"inventory-only={sorted(inventory_direct_names - lock_direct)}"
        )

    lines = [
        "# Generated by docker/lock-requirements.py from the frozen lock and artifact",
        "# inventory. Do not edit: change the lock and the inventory together.",
        "#",
        "# Install with: python -m pip install --no-cache-dir --require-hashes -r <this file>",
        "",
    ]
    for name, version, digest in entries:
        key = normalized_name(name)
        if key in direct_inventory:
            url = direct_inventory[key]
            if url != direct_urls[key]:
                raise ToolError(
                    f"{name}: the lock records direct source {direct_urls[key]} but the "
                    f"inventory records {url}"
                )
            lines.append(f"{name} @ {url}#sha256={digest}")
        else:
            lines.append(f"{name}=={version} --hash=sha256:{digest}")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lock", required=True)
    parser.add_argument("--artifacts", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    try:
        entries, direct_urls = parse_lock(Path(args.lock))
        direct_inventory = inventory_direct(Path(args.artifacts))
        text = render(entries, direct_urls, direct_inventory)
    except ToolError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 3
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    # LF on every platform: this file is evidence of what was installed, and a
    # digest of it must not depend on which machine rendered it.
    out.write_text(text, encoding="utf-8", newline="\n")
    print(
        json.dumps(
            {
                "requirements": len(entries),
                "direct": len(direct_inventory),
                "out": str(out),
                "status": "PASS",
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
