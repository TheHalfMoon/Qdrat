"""Static contract tests for the image and the local deployment surface.

These are the checks that can run anywhere, including a host with no container
runtime. The runtime half of the same acceptance criteria - the clean no-cache
build, the compose validation, the empty-database migrations, the repeated and
concurrent bootstrap and the digest binding - is executed and recorded under
evidence/g0-02/.

Run from the repository root:

    python -m unittest discover -s docker/tests -p "test_*.py"
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DOCKERFILE = REPO_ROOT / "Dockerfile"
COMPOSE = REPO_ROOT / "docker-compose.yml"
COMPOSE_PROD = REPO_ROOT / "docker-compose.prod.yml"
ENTRYPOINT = REPO_ROOT / "docker" / "entrypoint.sh"
RELEASE_TASKS = REPO_ROOT / "docker" / "release_tasks.py"
DIGESTS = REPO_ROOT / "docker" / "image-digests.json"

DIGEST_PATTERN = re.compile(r"@sha256:[0-9a-f]{64}\b")


def load_release_tasks():
    spec = importlib.util.spec_from_file_location("qdrat_release_tasks", RELEASE_TASKS)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


release_tasks = load_release_tasks()


def recorded_digests() -> dict[str, str]:
    payload = json.loads(DIGESTS.read_text(encoding="utf-8"))
    return {item["reference"]: item["digest"] for item in payload["images"]}


class DockerfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = DOCKERFILE.read_text(encoding="utf-8")
        cls.from_lines = [
            line for line in cls.text.splitlines() if line.upper().startswith("FROM ")
        ]

    def test_every_stage_pins_its_base_by_digest(self):
        self.assertTrue(self.from_lines)
        for line in self.from_lines:
            self.assertIn("@sha256:", line, line)
            self.assertTrue(DIGEST_PATTERN.search(line), line)

    def test_base_digest_matches_the_recorded_resolution(self):
        expected = recorded_digests()["python:3.12-slim"]
        for line in self.from_lines:
            self.assertIn(expected, line, line)

    def test_image_installs_the_frozen_lock_not_the_input_ranges(self):
        self.assertIn("requirements/locks/linux-amd64-py312.txt", self.text)
        self.assertIn("docker/lock-requirements.py", self.text)
        self.assertIn("--require-hashes", self.text)
        self.assertNotIn("-r requirements.txt", self.text)

    def test_no_unpinned_resolver_upgrade_remains(self):
        # Comments explain why the step is gone, so only real instructions count.
        for line in self.text.splitlines():
            if line.strip().startswith("#"):
                continue
            self.assertNotIn("pip install --upgrade pip", line, line)
        self.assertNotIn("SPACY_MODEL_VERSION", self.text)

    def test_build_identity_is_available_to_the_entrypoint(self):
        for name in ("QDRAT_BUILD_VERSION", "QDRAT_BUILD_REVISION", "QDRAT_BUILD_DATE"):
            self.assertIn(name, self.text)


class ComposeTests(unittest.TestCase):
    def test_every_service_image_is_digest_pinned(self):
        text = COMPOSE.read_text(encoding="utf-8")
        images = [
            line.strip()[len("image:") :].strip()
            for line in text.splitlines()
            if line.strip().startswith("image:")
        ]
        self.assertTrue(images)
        for image in images:
            self.assertIn("@sha256:", image, image)

    def test_service_digests_match_the_recorded_resolution(self):
        recorded = recorded_digests()
        text = COMPOSE.read_text(encoding="utf-8")
        for reference, digest in recorded.items():
            if reference == "python:3.12-slim":
                continue
            self.assertIn(f"{reference}@{digest}", text, reference)

    def test_build_identity_is_passed_through_for_both_built_services(self):
        text = COMPOSE.read_text(encoding="utf-8")
        self.assertEqual(text.count("VCS_REF: ${QDRAT_VCS_REF:-unknown}"), 2)
        self.assertEqual(text.count("BUILD_DATE: ${QDRAT_BUILD_DATE:-unknown}"), 2)

    def test_scheduler_never_runs_release_tasks(self):
        text = COMPOSE.read_text(encoding="utf-8")
        self.assertIn("HORILLA_SKIP_RELEASE_TASKS=1", text)
        prod = COMPOSE_PROD.read_text(encoding="utf-8")
        self.assertIn('HORILLA_SKIP_RELEASE_TASKS: "1"', prod)

    def test_compose_does_not_bind_mount_media_into_nginx(self):
        text = COMPOSE.read_text(encoding="utf-8")
        nginx = text.split("  nginx:", 1)[1].split("\nvolumes:", 1)[0]
        for line in nginx.splitlines():
            if line.strip().startswith("#"):
                continue
            self.assertNotIn("media", line, line)


class EntrypointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = ENTRYPOINT.read_text(encoding="utf-8")

    def test_startup_logs_the_baked_build_identity(self):
        self.assertIn("Qdrat image build:", self.text)
        for name in ("QDRAT_BUILD_VERSION", "QDRAT_BUILD_REVISION", "QDRAT_BUILD_DATE"):
            self.assertIn(name, self.text)

    def test_release_tasks_run_through_the_locked_runner(self):
        self.assertIn("python docker/release_tasks.py", self.text)
        self.assertNotIn("manage.py migrate", self.text)
        self.assertNotIn("manage.py collectstatic", self.text)

    def test_skip_gate_still_precedes_the_release_tasks(self):
        skip = self.text.index("HORILLA_SKIP_RELEASE_TASKS")
        runner = self.text.index("python docker/release_tasks.py")
        self.assertLess(skip, runner)


class ReleaseTaskTests(unittest.TestCase):
    """The serialisation knobs must be explicit and refuse nonsense."""

    def setUp(self):
        self._saved = {
            name: os.environ.get(name)
            for name in ("QDRAT_RELEASE_LOCK_KEY", "QDRAT_RELEASE_LOCK_TIMEOUT")
        }

    def tearDown(self):
        for name, value in self._saved.items():
            if value is None:
                os.environ.pop(name, None)
            else:
                os.environ[name] = value

    def test_default_lock_key_is_stable(self):
        os.environ.pop("QDRAT_RELEASE_LOCK_KEY", None)
        self.assertEqual(release_tasks.lock_key(), 0x5144524154)
        self.assertEqual(release_tasks.lock_key(), release_tasks.DEFAULT_LOCK_KEY)

    def test_default_timeout_is_bounded(self):
        os.environ.pop("QDRAT_RELEASE_LOCK_TIMEOUT", None)
        self.assertEqual(
            release_tasks.lock_timeout_seconds(),
            release_tasks.DEFAULT_LOCK_TIMEOUT_SECONDS,
        )

    def test_invalid_key_is_refused(self):
        os.environ["QDRAT_RELEASE_LOCK_KEY"] = "not-a-number"
        with self.assertRaises(release_tasks.ReleaseTaskError):
            release_tasks.lock_key()

    def test_out_of_range_key_is_refused(self):
        os.environ["QDRAT_RELEASE_LOCK_KEY"] = str(2**63)
        with self.assertRaises(release_tasks.ReleaseTaskError):
            release_tasks.lock_key()

    def test_invalid_timeout_is_refused(self):
        os.environ["QDRAT_RELEASE_LOCK_TIMEOUT"] = "-1"
        with self.assertRaises(release_tasks.ReleaseTaskError):
            release_tasks.lock_timeout_seconds()


if __name__ == "__main__":
    unittest.main()
