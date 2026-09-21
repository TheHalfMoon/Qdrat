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

# This script deletes and recreates its own run directory, so the guard has to
# hold for the paths the shell actually means, not just for the literal string.
# `//`, `/.`, `/tmp/..` and `/work/../..` all reach the filesystem root, so the
# check normalises by rejecting any non-canonical form and requires the run
# directory to be at least two levels deep - it may never be a mount root.
case "$run_dir" in
    /*) ;;
    *) echo "acquire: run_dir must be an absolute path, got '$run_dir'" >&2; exit 2 ;;
esac
# Only a trailing slash is appended: prefixing one as well would make every
# absolute path contain "//" and reject all valid input. With "/" appended, the
# root case "/" becomes "//" and is still caught.
case "${run_dir}/" in
    *//* | */./* | */../*)
        echo "acquire: run_dir must be a canonical path without '.' or '..', got '$run_dir'" >&2
        exit 2
        ;;
esac
case "${run_dir#/}" in
    */*) ;;
    *) echo "acquire: run_dir must be at least two levels deep, got '$run_dir'" >&2; exit 2 ;;
esac

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
