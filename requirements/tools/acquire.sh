#!/bin/sh
# Network-enabled acquisition stage for one dependency-freeze target.
#
#   acquire.sh <input-requirements> <run-dir> [wheelhouse-dir-name]
#
# Runs inside the pinned linux/amd64 CPython 3.12 builder image, which is the
# only environment whose resolution is qualified. It never installs into the
# running interpreter: `pip download` only writes into <run-dir>.
#
# Produces under <run-dir>:
#   wheelhouse/          every resolved artifact exactly as pip downloaded it
#   report.json          pip's resolution report: name, version, source URL, hash
#   resolution.json      normalized resolution consumed by `lockfile.py build`
#   wheelhouse.sha256    independent byte hashes of the artifacts on disk
set -eu

input="${1:?input requirements file required}"
run_dir="${2:?run directory required}"
wheelhouse_name="${3:-wheelhouse}"
wheelhouse="$run_dir/$wheelhouse_name"
lockfile=/repo/requirements/tools/lockfile.py

rm -rf "$run_dir"
mkdir -p "$wheelhouse"

# 1. Acquire every artifact the unchanged inputs resolve to. Nothing is
#    installed on the host and no global interpreter is modified.
python -m pip download --no-cache-dir --dest "$wheelhouse" -r "$input"

# 2. Resolve a second time through pip's resolver to capture the authoritative
#    name/version/source-URL/hash mapping for the artifacts just downloaded.
python -m pip install --dry-run --ignore-installed --no-cache-dir \
    --report "$run_dir/report.json" -r "$input"

# 3. Normalize, refusing to emit anything the wheelhouse cannot account for.
python "$lockfile" resolve \
    --wheelhouse "$wheelhouse" \
    --report "$run_dir/report.json" \
    --out "$run_dir/resolution.json"

( cd "$wheelhouse" && sha256sum ./* > "$run_dir/wheelhouse.sha256" )
