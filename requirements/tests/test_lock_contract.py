"""Contract tests for the frozen Linux amd64 CPython 3.12 dependency artifacts.

These tests are deterministic and offline: they exercise the emitted lock and
artifact inventory, and prove the two behaviours the G0-01 acceptance calls for
explicitly - that two isolated resolutions must agree before anything is frozen,
and that an unsupported platform is rejected rather than served a lock.

Run from the repository root:

    python -m unittest discover -s requirements/tests -p "test_*.py"
"""

from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO_ROOT / "requirements" / "tools" / "lockfile.py"
LOCK_NAME = "linux-amd64-py312"


def load_tool():
    spec = importlib.util.spec_from_file_location("qdrat_lockfile", TOOL_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


lockfile = load_tool()


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def write_artifact(directory: Path, filename: str, payload: bytes = b"artifact") -> str:
    path = directory / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    return sha256_bytes(payload)


def report_entry(name: str, version: str, filename: str, digest: str, url: str) -> dict:
    return {
        "download_info": {"url": url, "archive_info": {"hashes": {"sha256": digest}}},
        "is_direct": False,
        "metadata": {"name": name, "version": version},
        "requested": False,
    }


class TempProject:
    """Minimal synthetic builder used to isolate each deterministic refusal."""

    def __init__(self, test: unittest.TestCase) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        test.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)

    def wheelhouse(self, entries):
        """Create wheelhouse files plus the matching pip resolution report."""
        wheelhouse = self.root / "wheelhouse"
        wheelhouse.mkdir(parents=True, exist_ok=True)
        report = []
        for name, version, filename, payload in entries:
            digest = write_artifact(wheelhouse, filename, payload)
            url = f"https://files.pythonhosted.org/packages/{filename}"
            report.append(report_entry(name, version, filename, digest, url))
        report_path = self.root / "report.json"
        report_path.write_text(json.dumps({"install": report}), encoding="utf-8")
        return wheelhouse, report_path


def run_cli(argv):
    stderr = io.StringIO()
    with redirect_stderr(stderr), redirect_stdout(io.StringIO()):
        code = lockfile.main(argv)
    return code, stderr.getvalue()


def build_argv(root, resolution_a, resolution_b):
    return [
        "build",
        "--resolution-a",
        str(resolution_a),
        "--resolution-b",
        str(resolution_b),
        "--input",
        str(REPO_ROOT / "requirements.txt"),
        "--input-label",
        "requirements.txt",
        "--lock-out",
        str(root / "lock.txt"),
        "--lock-label",
        "requirements/locks/linux-amd64-py312.txt",
        "--artifacts-out",
        str(root / "artifacts.json"),
        "--artifacts-label",
        "requirements/artifacts/linux-amd64-py312.json",
        "--wheelhouse-label",
        "wheelhouse",
        "--resolver-version",
        "25.0.1",
        "--builder-image",
        "python@sha256:" + "0" * 64,
    ]


class FrozenArtifactTests(unittest.TestCase):
    """Assertions about the lock that is actually committed."""

    @classmethod
    def setUpClass(cls):
        cls.lock_path = REPO_ROOT / "requirements" / "locks" / f"{LOCK_NAME}.txt"
        cls.artifacts_path = REPO_ROOT / "requirements" / "artifacts" / f"{LOCK_NAME}.json"
        if not cls.lock_path.is_file() or not cls.artifacts_path.is_file():
            raise unittest.SkipTest("frozen artifacts are not present")
        cls.artifacts = json.loads(cls.artifacts_path.read_text(encoding="utf-8"))
        cls.lock = lockfile.parse_lock(cls.lock_path)

    def test_every_requirement_is_pinned_and_hashed(self):
        self.assertTrue(self.lock)
        for name, (version, hashes) in self.lock.items():
            self.assertTrue(version, name)
            self.assertTrue(hashes, name)
            for digest in hashes:
                self.assertRegex(digest, r"^[0-9a-f]{64}$")

    def test_lock_matches_artifact_inventory_exactly(self):
        inventory = {
            item["normalized_name"]: (item["version"], [item["sha256"]])
            for item in self.artifacts["distributions"]
        }
        self.assertEqual(self.lock, inventory)

    def test_inventory_binds_source_url_hash_and_license(self):
        for item in self.artifacts["distributions"]:
            self.assertTrue(item["url"], item["name"])
            self.assertRegex(item["sha256"], r"^[0-9a-f]{64}$")
            self.assertIn(item["kind"], {"wheel", "sdist"})
            self.assertEqual(item["license"]["source"], "installed-distribution-metadata")

    def test_input_is_bound_by_hash(self):
        requirements = REPO_ROOT / "requirements.txt"
        self.assertEqual(
            self.artifacts["input"]["sha256"], sha256_bytes(requirements.read_bytes())
        )

    def test_lock_file_hash_matches_the_inventory(self):
        self.assertEqual(
            self.artifacts["lock"]["sha256"], sha256_bytes(self.lock_path.read_bytes())
        )

    def test_only_the_single_qualified_target_is_declared(self):
        self.assertEqual(self.artifacts["target"], LOCK_NAME)
        self.assertEqual(self.artifacts["supported_targets"], [LOCK_NAME])

    def test_direct_spacy_model_wheel_is_bound_by_url_and_hash(self):
        direct = [item for item in self.artifacts["distributions"] if item["direct"]]
        self.assertEqual([item["name"] for item in direct], ["en_core_web_sm"])
        self.assertTrue(direct[0]["url"].startswith("https://github.com/explosion/"))
        self.assertEqual(direct[0]["kind"], "wheel")


class UnsupportedTargetTests(unittest.TestCase):
    """The lock must refuse unsupported platforms instead of degrading."""

    def test_verify_rejects_every_unsupported_target(self):
        for target in (
            "windows-amd64-py312",
            "linux-arm64-py312",
            "linux-amd64-py311",
            "darwin-arm64-py312",
        ):
            code, message = run_cli(
                [
                    "verify",
                    "--target",
                    target,
                    "--lock",
                    "unused",
                    "--artifacts",
                    "unused",
                    "--installed",
                    "unused",
                ]
            )
            self.assertEqual(code, 3, target)
            self.assertIn("unsupported target", message)

    def test_build_rejects_an_unsupported_target(self):
        argv = build_argv(Path("."), "a", "b")
        argv[argv.index("build") + 1 : argv.index("build") + 1] = [
            "--target",
            "windows-amd64-py312",
        ]
        code, message = run_cli(argv)
        self.assertEqual(code, 3)
        self.assertIn("unsupported target", message)


class ResolutionAgreementTests(unittest.TestCase):
    """Two isolated resolutions must agree before a lock may exist."""

    def _resolve(self, entries):
        project = TempProject(self)
        wheelhouse, report = project.wheelhouse(entries)
        out = project.root / "resolution.json"
        code, message = run_cli(
            [
                "resolve",
                "--wheelhouse",
                str(wheelhouse),
                "--report",
                str(report),
                "--out",
                str(out),
            ]
        )
        self.assertEqual(code, 0, message)
        return json.loads(out.read_text(encoding="utf-8"))

    def test_identical_resolutions_agree(self):
        entries = [("Demo", "1.0", "demo-1.0-py3-none-any.whl", b"demo")]
        self.assertEqual(
            self._resolve(entries)["distributions"],
            self._resolve(entries)["distributions"],
        )

    def test_digest_drift_between_resolutions_is_refused(self):
        first = self._resolve([("Demo", "1.0", "demo-1.0-py3-none-any.whl", b"demo")])
        second = self._resolve([("Demo", "1.0", "demo-1.0-py3-none-any.whl", b"other")])
        project = TempProject(self)
        (project.root / "a.json").write_text(json.dumps(first), encoding="utf-8")
        (project.root / "b.json").write_text(json.dumps(second), encoding="utf-8")
        code, message = run_cli(
            build_argv(project.root, project.root / "a.json", project.root / "b.json")
        )
        self.assertEqual(code, 3)
        self.assertIn("disagree", message)
        self.assertFalse((project.root / "lock.txt").exists())


class IncompleteEvidenceTests(unittest.TestCase):
    """A partial or unaccounted artifact set must never become a lock."""

    def test_artifact_without_a_resolution_entry_is_refused(self):
        project = TempProject(self)
        wheelhouse, report = project.wheelhouse(
            [("Demo", "1.0", "demo-1.0-py3-none-any.whl", b"demo")]
        )
        write_artifact(wheelhouse, "stray-9.9-py3-none-any.whl", b"stray")
        code, message = run_cli(
            [
                "resolve",
                "--wheelhouse",
                str(wheelhouse),
                "--report",
                str(report),
                "--out",
                str(project.root / "out.json"),
            ]
        )
        self.assertEqual(code, 3)
        self.assertIn("not accounted for", message)

    def test_empty_wheelhouse_is_refused(self):
        project = TempProject(self)
        wheelhouse = project.root / "wheelhouse"
        wheelhouse.mkdir(parents=True)
        report = project.root / "report.json"
        report.write_text(json.dumps({"install": []}), encoding="utf-8")
        code, message = run_cli(
            [
                "resolve",
                "--wheelhouse",
                str(wheelhouse),
                "--report",
                str(report),
                "--out",
                str(project.root / "out.json"),
            ]
        )
        self.assertEqual(code, 3)
        self.assertIn("no resolved distributions", message)

    def test_resolution_without_a_local_artifact_is_refused(self):
        project = TempProject(self)
        wheelhouse = project.root / "wheelhouse"
        wheelhouse.mkdir(parents=True)
        write_artifact(wheelhouse, "something-1.0-py3-none-any.whl", b"x")
        report = project.root / "report.json"
        report.write_text(
            json.dumps(
                {
                    "install": [
                        report_entry(
                            "Demo",
                            "1.0",
                            "demo-1.0-py3-none-any.whl",
                            "0" * 64,
                            "https://files.pythonhosted.org/packages/demo-1.0-py3-none-any.whl",
                        )
                    ]
                }
            ),
            encoding="utf-8",
        )
        code, message = run_cli(
            [
                "resolve",
                "--wheelhouse",
                str(wheelhouse),
                "--report",
                str(report),
                "--out",
                str(project.root / "out.json"),
            ]
        )
        self.assertEqual(code, 3)
        self.assertIn("does not contain the artifact", message)

    def test_unpinned_lock_line_is_refused(self):
        project = TempProject(self)
        lock = project.root / "lock.txt"
        lock.write_text("demo>=1.0\n", encoding="utf-8")
        with self.assertRaises(lockfile.ToolError):
            lockfile.parse_lock(lock)


class InstalledInventoryTests(unittest.TestCase):
    """The installed distribution set must reconcile with the frozen lock."""

    def _fixture(self):
        project = TempProject(self)
        lock = project.root / "lock.txt"
        lock.write_text(
            "demo==1.0 --hash=sha256:" + "a" * 64 + "\n"
            "other==2.0 --hash=sha256:" + "b" * 64 + "\n",
            encoding="utf-8",
        )
        artifacts = project.root / "artifacts.json"
        artifacts.write_text(
            json.dumps(
                {
                    "schema": lockfile.ARTIFACTS_SCHEMA,
                    "target": LOCK_NAME,
                    "supported_targets": [LOCK_NAME],
                    "distributions": [
                        {"name": "demo", "version": "1.0", "sha256": "a" * 64},
                        {"name": "other", "version": "2.0", "sha256": "b" * 64},
                    ],
                }
            ),
            encoding="utf-8",
        )
        return lock, artifacts, project.root

    def _installed(self, root, records):
        path = root / "installed.json"
        path.write_text(json.dumps(records), encoding="utf-8")
        return path

    def _verify(self, lock, artifacts, installed):
        return run_cli(
            [
                "verify",
                "--target",
                LOCK_NAME,
                "--lock",
                str(lock),
                "--artifacts",
                str(artifacts),
                "--installed",
                str(installed),
            ]
        )

    def test_matching_inventory_passes(self):
        lock, artifacts, root = self._fixture()
        installed = self._installed(
            root,
            [{"name": "Demo", "version": "1.0"}, {"name": "other", "version": "2.0"}],
        )
        code, message = self._verify(lock, artifacts, installed)
        self.assertEqual(code, 0, message)

    def test_missing_extra_and_version_drift_are_refused(self):
        lock, artifacts, root = self._fixture()
        installed = self._installed(
            root,
            [
                {"name": "demo", "version": "1.1"},
                {"name": "surprise", "version": "1.0"},
            ],
        )
        code, message = self._verify(lock, artifacts, installed)
        self.assertEqual(code, 3)
        self.assertIn("missing=['other']", message)
        self.assertIn("unexpected=['surprise']", message)
        self.assertIn("mismatched=", message)


if __name__ == "__main__":
    unittest.main()
