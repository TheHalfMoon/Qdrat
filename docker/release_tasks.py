#!/usr/bin/env python3
"""Run the container's release tasks under a PostgreSQL advisory lock.

The web container runs `migrate` and `collectstatic` before it starts serving.
That is correct for one container and wrong for two: both containers run the
same release tasks against the same database and the same staticfiles volume.

This is not hypothetical. Two copies of this image started together against an
empty database were run as part of G0-02, and one of them died:

    psycopg2.errors.UniqueViolation: duplicate key value violates unique
    constraint "pg_type_typname_nsp_index"
    DETAIL:  Key (typname, typnamespace)=(django_migrations, 2200) already exists.
    django.db.migrations.exceptions.MigrationSchemaMissing: Unable to create the
    django_migrations table (duplicate key value violates unique constraint ...)

The loser exits non-zero, so an orchestrator restart-loops it until the winner
has finished - which looks like flakiness rather than a schema race. The same
mechanism is why `collectstatic --clear` is inside the critical section too:
two containers sharing the staticfiles volume would wipe each other's output.

PostgreSQL advisory locks serialise them without adding a coordinator: every
container takes the same session-level lock before running release tasks and
releases it afterwards. The lock is held on the connection, so a container that
dies mid-migration also drops it, and the next one proceeds against whatever
state the database is actually in - which is what `migrate` is designed for.

Environment:

    QDRAT_RELEASE_LOCK_KEY      integer advisory-lock key (default 0x5144524154)
    QDRAT_RELEASE_LOCK_TIMEOUT  seconds to wait for the lock before failing
                                loudly (default 900; 0 means wait forever)
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

# Running `python docker/release_tasks.py` puts `docker/` on sys.path, not the
# project root, so `import horilla` fails even though the project sits one level
# up - manage.py never hits this because it lives at the root. The first
# concurrent-bootstrap probe caught exactly that:
# ModuleNotFoundError: No module named 'horilla'. Bind the root explicitly
# instead of relying on the caller's working directory.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# "QDRAT" as ASCII, chosen once and asserted by a test so a change is deliberate.
DEFAULT_LOCK_KEY = 0x5144524154
DEFAULT_LOCK_TIMEOUT_SECONDS = 900
MAX_LOCK_KEY = 2**63 - 1


class ReleaseTaskError(RuntimeError):
    """A deterministic refusal to run the release tasks."""


def lock_key() -> int:
    raw = os.environ.get("QDRAT_RELEASE_LOCK_KEY")
    if raw is None or raw.strip() == "":
        return DEFAULT_LOCK_KEY
    try:
        value = int(raw, 10)
    except ValueError as exc:
        raise ReleaseTaskError(
            f"QDRAT_RELEASE_LOCK_KEY must be an integer, got {raw!r}"
        ) from exc
    if value < 0 or value > MAX_LOCK_KEY:
        raise ReleaseTaskError(
            f"QDRAT_RELEASE_LOCK_KEY must be between 0 and {MAX_LOCK_KEY}, got {value}"
        )
    return value


def lock_timeout_seconds() -> int:
    raw = os.environ.get("QDRAT_RELEASE_LOCK_TIMEOUT")
    if raw is None or raw.strip() == "":
        return DEFAULT_LOCK_TIMEOUT_SECONDS
    try:
        value = int(raw, 10)
    except ValueError as exc:
        raise ReleaseTaskError(
            f"QDRAT_RELEASE_LOCK_TIMEOUT must be an integer, got {raw!r}"
        ) from exc
    if value < 0:
        raise ReleaseTaskError(
            f"QDRAT_RELEASE_LOCK_TIMEOUT must not be negative, got {value}"
        )
    return value


def acquire(cursor, key: int, timeout_seconds: int) -> float:
    """Take the session-level advisory lock; return how long the wait took."""
    if timeout_seconds > 0:
        cursor.execute("SET lock_timeout = %s", (f"{timeout_seconds}s",))
    else:
        cursor.execute("SET lock_timeout = 0")
    started = time.monotonic()
    cursor.execute("SELECT pg_advisory_lock(%s)", (key,))
    return time.monotonic() - started


def release(cursor, key: int) -> None:
    cursor.execute("SELECT pg_advisory_unlock(%s)", (key,))


def run(collect_static: bool) -> int:
    import django
    from django.core.management import call_command
    from django.db import connection
    from django.db.utils import OperationalError

    key = lock_key()
    timeout = lock_timeout_seconds()
    # Same default manage.py and wsgi.py use: the dev compose stack does not set
    # this variable, and a bare `django.setup()` without it fails closed.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "horilla.settings")
    django.setup()

    try:
        with connection.cursor() as cursor:
            waited = acquire(cursor, key, timeout)
            print(
                f"Qdrat release lock {key} acquired after {waited:.1f}s"
                + (f" (timeout {timeout}s)" if timeout else " (no timeout)"),
                flush=True,
            )
            try:
                call_command("migrate", interactive=False)
                if collect_static:
                    # --clear is deliberate and documented in the entrypoint:
                    # STATIC_ROOT is a volume that outlives the image, and
                    # stale pre-compressed siblings were served after upgrades.
                    call_command("collectstatic", interactive=False, clear=True)
            finally:
                release(cursor, key)
    except OperationalError as exc:
        message = str(exc)
        if "lock timeout" in message or "canceling statement" in message:
            raise ReleaseTaskError(
                f"another container held the release lock for more than {timeout}s; "
                "refusing to run migrations concurrently. Raise "
                "QDRAT_RELEASE_LOCK_TIMEOUT if the first bootstrap is legitimately "
                "slower than that on this host."
            ) from exc
        raise
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-collectstatic",
        action="store_true",
        help="run migrations only (used when static files are not served from this image)",
    )
    args = parser.parse_args(argv)
    try:
        return run(collect_static=not args.skip_collectstatic)
    except ReleaseTaskError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
