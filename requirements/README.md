# Frozen dependency artifacts

`requirements.txt` is the dependency **intent** for the application and is not
changed by this directory. Everything here is derived from it: the artifacts
below record what that intent resolved to, byte for byte, for one qualified
target.

Qualified target: **linux/amd64, CPython 3.12, glibc**. Nothing else is
qualified, and nothing else may reuse these files - see *Unsupported platforms*
below.

## Files

| Path | Meaning |
| --- | --- |
| `../requirements.txt` | Unchanged input. Its sha256 is bound into the inventory. |
| `locks/linux-amd64-py312.txt` | Complete transitive lock. Every line is `name==version` plus a `--hash=sha256:` of the exact artifact that will be installed. Installs with `--require-hashes` and no index access. |
| `artifacts/linux-amd64-py312.json` | Machine-readable inventory: for every distribution the source URL, artifact filename, byte hash, kind (wheel/sdist), direct-URL flag and license metadata, plus the resolver, builder image and bootstrap tools. |
| `tools/lockfile.py` | Deterministic normalizer, lock writer and verifier. Never resolves, downloads or installs. |
| `tools/acquire.sh` | Network-enabled acquisition stage executed inside the pinned builder image. |
| `tools/prove-offline.sh` | Network-disabled installation proof executed inside the pinned builder image. |
| `tests/test_lock_contract.py` | Offline contract tests for the lock, the inventory and the two explicit behaviors G0-01 requires (two resolutions must agree; unsupported targets are rejected). |

## Resolver and bootstrap

Resolution is pip's own resolver inside an immutable builder, not a
re-implementation:

* builder image `python@sha256:2f17fc044b579bab302c2e8054d3a686e2cb9a83de48e70534b94cd8ebbe06a9`
  (the `python:3.12-slim` family the application `Dockerfile` already builds
  from; the digest is the binding, the tag is not);
* CPython 3.12.14, glibc 2.41, pip 25.0.1;
* one bootstrap tool outside the application dependency set:
  `wheel==0.47.0`, needed only to build the two sdist-only distributions
  (`pyzk==0.9`, `svglib==1.5.1`) while the network is disabled. `setuptools` is
  already an application requirement (`setuptools==84.0.0`), so it is locked
  rather than bootstrapped.

pip hash-checks the requirement set it resolves from the lock file; it does not
hash-check the isolated build environments it creates for sdist-only projects.
The bootstrap wheel is therefore bound explicitly instead:
`prove-offline.sh` runs `lockfile.py verify --bootstrap-dir`, which recomputes
that wheel's sha256 and compares it with the hash recorded in the artifact
inventory before the artifact is treated as a verified input. A tampered or
missing bootstrap artifact fails the proof.

`acquire.sh` deletes and recreates its own run directory, so it refuses a run
directory before any deletion happens unless it is an absolute, canonical path at
least two levels deep: relative paths, `//`, `/.`, `/tmp/..` and `/work/../..`
are all rejected, because a string comparison against `/` alone does not cover the
paths the shell actually means.

Artifact file names are taken after percent-decoding but never as paths: a URL
whose final segment decodes to `..` or to something containing a separator is
refused, and every artifact path is checked for containment inside its directory
before it is opened or hashed.

Because the wheelhouse itself is not committed, the R2 verification command in
`.diffcipline/tasks/G0-01.toml` reconciles three independent records instead: the
lock, the artifact inventory, and `evidence/g0-01/wheelhouse-a.sha256`, the
sha256sum listing produced over the real artifacts during acquisition. Comparing
only the two documents would let a hash altered consistently in both pass.

## Procedure

Both stages run inside the pinned builder image and share the repository and a
scratch directory. `acquisition` is run twice, in two separate containers,
before anything is frozen.

```sh
# 1. Acquisition - run once as A and once as B, in separate containers.
docker run --rm --name qdrat-g0-01-a \
  -v "$PWD:/repo" -v "<scratch>:/work" \
  python@sha256:2f17fc044b579bab302c2e8054d3a686e2cb9a83de48e70534b94cd8ebbe06a9 \
  sh /repo/requirements/tools/acquire.sh /work/input/requirements.txt /work/run-a

# 2. Freeze - refuses to emit anything unless both resolutions are identical.
python requirements/tools/lockfile.py build \
  --resolution-a /work/run-a/resolution.json \
  --resolution-b /work/run-b/resolution.json \
  --input requirements.txt --input-label requirements.txt \
  --lock-out requirements/locks/linux-amd64-py312.txt \
  --lock-label requirements/locks/linux-amd64-py312.txt \
  --artifacts-out requirements/artifacts/linux-amd64-py312.json \
  --artifacts-label requirements/artifacts/linux-amd64-py312.json \
  --wheelhouse-label "isolated wheelhouse" \
  --bootstrap-dir /work/bootstrap --bootstrap "wheel=wheel-0.47.0-py3-none-any.whl" \
  --resolver-version 25.0.1 \
  --builder-image "python@sha256:2f17fc044b579bab302c2e8054d3a686e2cb9a83de48e70534b94cd8ebbe06a9"

# 3. Installation proof - networking disabled, no index access.
docker run --rm --network none \
  -v "$PWD:/repo" -v "<scratch>:/work" \
  python@sha256:2f17fc044b579bab302c2e8054d3a686e2cb9a83de48e70534b94cd8ebbe06a9 \
  sh /repo/requirements/tools/prove-offline.sh /work/run-a /work/bootstrap /work/proof

# 4. Contract tests - offline, deterministic.
python -m unittest discover -s requirements/tests -p "test_*.py"
```

## Unsupported platforms

The lock is not portable and must not be extended by guesswork. `verify` fails
closed with exit code 3 for every target other than `linux-amd64-py312`,
including `windows-amd64-py312`, `linux-arm64-py312`, `linux-amd64-py311` and
`darwin-arm64-py312`. `build` refuses to emit a lock for an unsupported target
at all. Additional platforms are added by a later task that runs this same
procedure for that platform, never by editing these files by hand.

## Known limitations

* **Two distributions have no upstream wheel.** `pyzk==0.9` and `svglib==1.5.1`
  are locked as sdists by hash and are built from that exact sdist during the
  offline install, using the pinned bootstrap backend. The resulting local wheel
  is not byte-identical between runs and is therefore deliberately *not*
  recorded as an artifact; the hash-bound object is the sdist.
* **`google-crc32c` publishes no license field** in its distribution metadata.
  It is listed in `license_unknown` in the inventory rather than guessed.
* **Availability is not reproducibility over time.** Re-running acquisition on a
  later date can resolve different versions, because `requirements.txt`
  intentionally contains ranges for compiled packages and a moving `Django~=5.2`
  range. That is a property of the input, not of the lock; refreshing the lock is
  a reviewed change with the same evidence obligations, and never a silent
  upgrade.
