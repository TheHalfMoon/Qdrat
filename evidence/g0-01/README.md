# G0-01 execution evidence - SG-000001

Task: `G0-01 - Freeze Linux amd64 Python 3.12 dependency artifacts`.
`docs/qdrat/plan/tasks/tasks.json` requires `scope-and-base`, `contract-tests`,
`recovery-proof`, `diffcipline-proof`, `independent-review` and `accepted-head`.
This directory holds the machine evidence for the first five; the accepted head
is the commit that contains them.

## What was actually executed

Base: `144935cd6bb64d3448ec3927fa7d1569bee93ca0` (live
`codex/qdrat-canonical-plan`, equal to `refs/pull/2/head`, reverified against the
remote before any edit). Target: `linux-amd64-py312` only.

| Step | Command (abbreviated) | Result |
| --- | --- | --- |
| Resolution A | `acquire.sh` in container `qdrat-g0-01-a` (network enabled) | exit 0 |
| Resolution B | `acquire.sh` in container `qdrat-g0-01-b` (network enabled) | exit 0 |
| Agreement | byte comparison of both normalized resolutions and both artifact-hash listings | identical |
| Freeze | `lockfile.py build` (refuses to emit unless A and B are identical) | exit 0 |
| Installation proof | `prove-offline.sh` in container `qdrat-g0-01-proof` with `--network none` | exit 0 |
| `pip check` | inside the proof environment | `No broken requirements found.` |
| Inventory reconcile | `lockfile.py verify` | PASS, 149 locked, 150 installed, `pip` excluded as tooling |
| Artifact hashes | `lockfile.py verify --wheelhouse` | PASS, 149/149 artifacts re-hashed and matched |

## Files

| File | Proves |
| --- | --- |
| `environment.json` | Exact builder image digest, interpreter, libc, pip version, bootstrap tool and network policy. |
| `acquire-a.log`, `acquire-b.log` | The literal acquisition output of each isolated run: every source URL pip fetched and every artifact it saved. |
| `resolution-a.json`, `resolution-b.json` | Normalized resolutions fed into the freeze step. |
| `resolution-agreement.json` | Hashes of both resolutions, both pip reports and both artifact listings, with the agreement verdict. |
| `wheelhouse-a.sha256`, `wheelhouse-b.sha256` | Independent byte hashes of the 149 artifacts on disk in each run. |
| `install.log` | The `--no-index --find-links ... --require-hashes` install with networking disabled, including the offline builds of `pyzk` and `svglib` from their locked sdists. |
| `pip-check.log` | `pip check` in the proven environment. |
| `installed.json` | The installed distribution inventory reconciled against the lock. |
| `licenses.json` | License metadata read from the installed distributions, merged into the artifact inventory. |
| `verify.log` | The reconciliation verdict, including the explicit `pip` exclusion. |

## Reproduction

```sh
python -m unittest discover -s requirements/tests -p "test_*.py"
python requirements/tools/lockfile.py verify \
  --target linux-amd64-py312 \
  --lock requirements/locks/linux-amd64-py312.txt \
  --artifacts requirements/artifacts/linux-amd64-py312.json \
  --installed evidence/g0-01/installed.json \
  --wheelhouse <wheelhouse-from-acquisition> \
  --tool-distribution pip
```

## Recovery proof

No database, service or production state is touched by this task, so recovery is
discard-and-revert, and it was exercised rather than asserted: the first offline
install attempt created its virtual environment on the host bind mount and was
abandoned after 19 minutes with 44 of 150 distributions installed. The container
was killed, `prove-offline.sh` was corrected to build its environment on
container-local storage, and the proof was re-run from scratch to exit 0 in under
three minutes. `acquire.sh` deletes its own run directory before use, so a re-run
cannot inherit partial state. Reverting this change deletes `requirements/locks/`,
`requirements/artifacts/`, `requirements/tools/`, `requirements/tests/`,
`requirements/README.md` and this directory, and reverts nothing else:
`requirements.txt` and the `Dockerfile` are untouched.

## Negative evidence and unresolved items

* The first offline-proof attempt **did not complete**. It was slow rather than
  failing, and it is recorded here as a recovered execution problem, not as a
  test result that passed.
* `google-crc32c` ships no license metadata; the inventory records it under
  `license_unknown` instead of inventing a license.
* Two of 149 distributions are sdists built locally during the offline install.
  Their rebuilt wheels are **not** byte-reproducible and are deliberately not
  recorded; only the source sdists are hash-bound. Comparing rebuilt wheels
  across runs will show different digests - that is expected, not drift.
* The application `Dockerfile` still installs from `requirements.txt`. Wiring the
  frozen lock into the image build changes shipped behavior and belongs to a
  later task, so it is deliberately not done here.
* No CI run is claimed for this change. The repository workflows trigger only on
  `dev/v2.0` and `2.0`, so a PR stacked on the planning branch cannot be validated
  by them; that gap is recorded rather than worked around.
