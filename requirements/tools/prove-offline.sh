#!/bin/sh
# Network-disabled installation proof for the frozen target.
#
#   prove-offline.sh <run-dir> <bootstrap-dir> <proof-dir>
#
# Must run inside the pinned builder image with networking disabled. It installs
# the frozen lock with --require-hashes without any index access, then checks the
# environment and reconciles the installed inventory against the lock.
#
# `pip` itself is the installer under test, not an application dependency: it is
# excluded from the application inventory explicitly and recorded as excluded.
#
# The virtual environment is built inside the container, not on the mounted
# output directory: creating ~150 distributions as many small files over a
# host bind mount dominates the runtime and adds nothing to the proof. Only the
# resulting logs and evidence files are copied back to <proof-dir>.
set -eu

run_dir="${1:?run directory required}"
bootstrap_dir="${2:?bootstrap directory required}"
proof_dir="${3:?proof directory required}"

lock=/repo/requirements/locks/linux-amd64-py312.txt
artifacts=/repo/requirements/artifacts/linux-amd64-py312.json
lockfile=/repo/requirements/tools/lockfile.py
work=/tmp/qdrat-offline-proof
venv="$work/venv"

rm -rf "$work"
mkdir -p "$work" "$proof_dir"

# The evidence is most valuable exactly when a step fails, so copy whatever was
# produced before exiting rather than only on the success path.
copy_evidence() {
    status=$?
    cp "$work/install.log" "$work/pip-check.log" "$work/installed.json" \
        "$work/licenses.json" "$work/verify.log" "$proof_dir/" 2>/dev/null || true
    exit "$status"
}
trap copy_evidence EXIT

# Work from container-local storage: one sequential copy in, then every read and
# write during the install happens on the container filesystem.
cp -r "$run_dir/wheelhouse" "$work/wheelhouse"
wheelhouse="$work/wheelhouse"
if [ -d "$bootstrap_dir" ]; then
    cp -r "$bootstrap_dir" "$work/bootstrap"
    bootstrap_dir="$work/bootstrap"
fi

python -m venv "$venv"

set -- --no-index --find-links "$wheelhouse"
if [ -d "$bootstrap_dir" ]; then
    set -- "$@" --find-links "$bootstrap_dir"
fi

"$venv/bin/python" -m pip install "$@" --require-hashes -r "$lock" \
    > "$work/install.log" 2>&1

"$venv/bin/python" -m pip check > "$work/pip-check.log" 2>&1
"$venv/bin/python" -m pip list --format=json > "$work/installed.json"
"$venv/bin/python" "$lockfile" license-inventory --out "$work/licenses.json"

# pip hash-checks the locked requirement set, not the isolated build
# environments it creates for sdist-only distributions, so the bootstrap wheel
# is bound here instead: its bytes must match the hash recorded in the artifact
# inventory before it is treated as a verified input.
set --
if [ -d "$bootstrap_dir" ]; then
    set -- --bootstrap-dir "$bootstrap_dir"
fi
"$venv/bin/python" "$lockfile" verify \
    --target linux-amd64-py312 \
    --lock "$lock" \
    --artifacts "$artifacts" \
    --installed "$work/installed.json" \
    --wheelhouse "$wheelhouse" \
    --tool-distribution pip "$@" > "$work/verify.log" 2>&1
