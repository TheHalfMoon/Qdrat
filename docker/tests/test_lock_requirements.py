"""Contract tests for the image requirements generator.

Run from the repository root:

    python -m unittest discover -s docker/tests -p "test_*.py"

Everything here is offline and deterministic: it reads the frozen lock and
artifact inventory that G0-01 sealed, renders the file the image installs from,
and checks every refusal path.
"""

from __future__ import annotations

import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO_ROOT / "docker" / "lock-requirements.py"
LOCK_PATH = REPO_ROOT / "requirements" / "locks" / "linux-amd64-py312.txt"
INVENTORY_PATH = REPO_ROOT / "requirements" / "artifacts" / "linux-amd64-py312.json"


def load_tool():
    spec = importlib.util.spec_from_file_location("qdrat_lock_requirements", TOOL_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


tool = load_tool()


class TempInputs:
    """A synthetic lock plus inventory, so each refusal is isolated."""

    def __init__(self, test: unittest.TestCase) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        test.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)

    def write(self, lock_text: str, distributions: list[dict]) -> tuple[Path, Path]:
        lock = self.root / "lock.txt"
        lock.write_text(lock_text, encoding="utf-8", newline="\n")
        inventory = self.root / "artifacts.json"
        inventory.write_text(
            json.dumps(
                {
                    "schema": "qdrat.dependency-artifacts/v1",
                    "target": "linux-amd64-py312",
                    "distributions": distributions,
                }
            ),
            encoding="utf-8",
            newline="\n",
        )
        return lock, inventory


def distribution(name, version, digest, url, direct=False) -> dict:
    return {
        "name": name,
        "normalized_name": name,
        "version": version,
        "sha256": digest,
        "url": url,
        "direct": direct,
    }


class FrozenInputTests(unittest.TestCase):
    """The real frozen artifacts must render into an installable requirements file."""

    @classmethod
    def setUpClass(cls):
        if not LOCK_PATH.is_file() or not INVENTORY_PATH.is_file():
            raise unittest.SkipTest("frozen artifacts are not present")
        cls.entries, cls.direct_urls = tool.parse_lock(LOCK_PATH)
        cls.direct_inventory = tool.inventory_direct(INVENTORY_PATH)
        cls.text = tool.render(cls.entries, cls.direct_urls, cls.direct_inventory)

    def test_every_locked_distribution_is_rendered(self):
        body = [
            line
            for line in self.text.splitlines()
            if line and not line.startswith("#")
        ]
        self.assertEqual(len(body), len(self.entries))

    def test_every_rendered_line_carries_a_hash(self):
        for line in self.text.splitlines():
            if not line or line.startswith("#"):
                continue
            self.assertRegex(line, r"sha256[=:][0-9a-f]{64}$")

    def test_indexed_distributions_stay_pinned_equalities(self):
        for line in self.text.splitlines():
            if not line or line.startswith("#") or " @" in line:
                continue
            self.assertRegex(
                line, r"^[A-Za-z0-9][A-Za-z0-9._-]*==[^\s;]+ --hash=sha256:[0-9a-f]{64}$"
            )

    def test_the_direct_artifact_is_a_url_with_its_hash(self):
        direct = [line for line in self.text.splitlines() if " @" in line]
        self.assertEqual(len(direct), 1)
        self.assertTrue(direct[0].startswith("en_core_web_sm @ https://github.com/explosion/"))
        entry = next(item for item in self.entries if item[0] == "en_core_web_sm")
        self.assertTrue(direct[0].endswith(f"#sha256={entry[2]}"))

    def test_output_is_lf_and_deterministic(self):
        self.assertNotIn(b"\r", self.text.encode("utf-8"))
        self.assertEqual(
            tool.render(self.entries, self.direct_urls, self.direct_inventory), self.text
        )

    def test_main_writes_the_file_and_reports_counts(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "requirements.lock.txt"
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                code = tool.main(
                    [
                        "--lock",
                        str(LOCK_PATH),
                        "--artifacts",
                        str(INVENTORY_PATH),
                        "--out",
                        str(out),
                    ]
                )
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(stdout.getvalue())["requirements"], len(self.entries))
            self.assertNotIn(b"\r", out.read_bytes())


class RefusalTests(unittest.TestCase):
    """Anything the two records disagree about must abort, not be guessed."""

    def _fixture(self, lock_text, distributions):
        project = TempInputs(self)
        return project.write(lock_text, distributions)

    def run_tool(self, lock, inventory):
        stderr = io.StringIO()
        with redirect_stderr(stderr), redirect_stdout(io.StringIO()):
            code = tool.main(
                [
                    "--lock",
                    str(lock),
                    "--artifacts",
                    str(inventory),
                    "--out",
                    str(lock.parent / "out.txt"),
                ]
            )
        return code, stderr.getvalue()

    def test_unpinned_lock_line_is_refused(self):
        digest = "a" * 64
        lock, inventory = self._fixture(
            "demo>=1.0\n",
            [distribution("demo", "1.0", digest, "https://example.invalid/demo.whl")],
        )
        code, message = self.run_tool(lock, inventory)
        self.assertEqual(code, 3)
        self.assertIn("not a pinned, hashed requirement", message)

    def test_duplicate_distribution_is_refused(self):
        digest = "a" * 64
        lock, inventory = self._fixture(
            f"demo==1.0 --hash=sha256:{digest}\nDemo==1.0 --hash=sha256:{digest}\n",
            [distribution("demo", "1.0", digest, "https://example.invalid/demo.whl")],
        )
        code, message = self.run_tool(lock, inventory)
        self.assertEqual(code, 3)
        self.assertIn("repeats distribution", message)

    def test_direct_artifact_without_an_inventory_url_is_refused(self):
        digest = "b" * 64
        lock, inventory = self._fixture(
            f"# direct source: https://example.invalid/demo.whl\n"
            f"demo==1.0 --hash=sha256:{digest}\n",
            [distribution("demo", "1.0", digest, "https://example.invalid/demo.whl")],
        )
        code, message = self.run_tool(lock, inventory)
        self.assertEqual(code, 3)
        self.assertIn("disagree about which artifacts are direct", message)

    def test_direct_url_mismatch_is_refused(self):
        digest = "c" * 64
        lock, inventory = self._fixture(
            f"# direct source: https://example.invalid/one.whl\n"
            f"demo==1.0 --hash=sha256:{digest}\n",
            [distribution("demo", "1.0", digest, "https://example.invalid/two.whl", True)],
        )
        code, message = self.run_tool(lock, inventory)
        self.assertEqual(code, 3)
        self.assertIn("the lock records direct source", message)

    def test_non_https_direct_url_is_refused(self):
        digest = "d" * 64
        lock, inventory = self._fixture(
            f"# direct source: http://example.invalid/demo.whl\n"
            f"demo==1.0 --hash=sha256:{digest}\n",
            [distribution("demo", "1.0", digest, "http://example.invalid/demo.whl", True)],
        )
        code, message = self.run_tool(lock, inventory)
        self.assertEqual(code, 3)
        self.assertIn("is not https", message)

    def test_missing_hash_is_refused(self):
        lock, inventory = self._fixture(
            "demo==1.0\n",
            [distribution("demo", "1.0", "e" * 64, "https://example.invalid/demo.whl")],
        )
        code, message = self.run_tool(lock, inventory)
        self.assertEqual(code, 3)
        self.assertIn("not a pinned, hashed requirement", message)


if __name__ == "__main__":
    unittest.main()
