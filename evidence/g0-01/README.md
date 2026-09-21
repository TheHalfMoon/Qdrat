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

## Independent review

Reviewer: **Alibaba Open Code Review v1.12.8** (binary sha256
`150812b67201e5a5fffc4acdd05a468b0737a10606ae109f0ba08541c1bc4a18`, matched
against the release's published `sha256sum.txt`), running the model
`deepseek-v4-pro` over its own deterministic file selection and rule resolution.
Neither the tool nor the model is the author of this change, and the credential
used for the model endpoint is supplied through environment variables only and is
never written to the repository or to any log.

`independent-review.json` holds all four rounds: the binding (base, reviewed head,
exact command), the coverage numbers, every finding verbatim, and the disposition
of each one. Thirteen findings were raised in total and none remain open against
the frozen artifacts.

Round 1 raised five findings:

| # | Severity | Finding | Disposition |
| --- | --- | --- | --- |
| 1 | medium | Empty repository `expected_files` leaves a change without a task policy bounded only by ceilings and forbidden surfaces | partially mitigated: the sealed plan is now a repository-level forbidden surface; the rest is accepted residual risk, because a fallback contract is not implementable under monotonic layering, and named as successor `QDRAT-GOV-TASK-POLICY-MANDATORY` |
| 2 | medium | The un-hashed `wheel` bootstrap would make the offline proof fail | false positive against deterministic evidence (the proof exits 0 and builds both sdists), but it exposed a real fragility, so the bootstrap artifact is now hash-verified at proof time |
| 3 | low | `rm -rf` on a caller-supplied directory with no guard | fixed |
| 4 | low | Evidence is only copied on the success path | fixed with an `EXIT` trap |
| 5 | low | Unreadable lock and malformed inventory entries raise raw tracebacks | fixed, with tests |

Round 2 reviewed the corrected head `8f630e2333c2bb0eea2c03a5e9eb961c7865f9ca`
in a fresh session and raised six more findings, three of them substantive:

| # | Severity | Finding | Disposition |
| --- | --- | --- | --- |
| 1 | medium | Sealing `docs/qdrat/plan/**` contradicts the comment that the plan-scoped contract is unchanged in `plan-policy.toml` | accepted with correction: the reconciliation path is now stated explicitly - reopening a sealed surface must be its own reviewed commit that removes the entry first |
| 2 | low | The unittest pattern in the task policy is unquoted, so some shells would glob it | fixed: quoted. Diffcipline runs commands through `cmd /C` on Windows, which does not glob, but quoting removes the dependency on that detail |
| 3 | high | The run-directory guard only rejected `/`, so `//`, `/.` and `/work/../..` still reached the filesystem root before `rm -rf` | fixed: the guard now requires a canonical absolute path at least two levels deep |
| 4 | medium | `unquote` after basename let `..%2fsecret` become the path `../secret`, which `verify` then joined onto the wheelhouse with no containment check | fixed: decoding happens before the final segment is taken, and every artifact path is now containment-checked |
| 5 | low | `build` re-validated nothing, so two resolutions with the same duplicate name could be frozen even though `verify` would later reject them | fixed: `build` re-validates names, fields and uniqueness before rendering |
| 6 | low | The committed R2 gate never re-hashed an artifact, so a hash altered consistently in both the lock and the inventory would pass | fixed: the gate now reconciles the committed sha256sum listing as a third, independently produced record (`verified_listing_entries: 149`) |

Round 2's coverage stayed at 20 of 26 files; the same lock file and contract test
suite remain excluded from first-class review by OCR's default rules.

Round 3 reviewed the round-2 response as an incremental range
(`8f630e2...HEAD`) and raised two more findings, one of them critical and both
correct:

| # | Severity | Finding | Disposition |
| --- | --- | --- | --- |
| 1 | critical | `"/$run_dir/"` always contains `//` because `run_dir` starts with `/`, so the canonical-path guard rejected every absolute path - including the one the pipeline uses | fixed: only a trailing slash is appended, so `/` still becomes `//` while `/work/run-a` stays canonical. `run-dir-guard-matrix.log` records the corrected behaviour across all seven bypass forms plus one accepted path |
| 2 | low | `read_sha256_listing` percent-decoded filesystem names, double-decoding a wheel whose name legitimately contains a `%` sequence | fixed: the listing holds filesystem names, so only the `./` prefix is stripped |

The critical finding is worth stating plainly: the guard that review round 2 asked
for was written in a way that broke every valid invocation, and the deterministic
gates did not catch it because acquisition had already run before the guard was
strengthened. It was found by re-reviewing the response rather than by trusting
it, which is the argument for reviewing the fix and not only the fix request.

Round 4 reviewed the round-3 fix as an incremental range (`bd55d03...HEAD`) and
returned **no findings**. That is where the loop was closed: not because a reviewer
stopped looking, but because the last delta survived a fresh pass.

The review is not a substitute for the deterministic gates, and it did not always
point the right way. Round 2 asked for the unittest pattern to be quoted; quoting
it made `cmd /C` hand the quotes to Python, unittest discovered zero tests, and
the gate returned FAIL. That failure is preserved verbatim in
`diffcipline-attempt-3-quoted-pattern.log` and the suggestion was not adopted.
Each finding is dispositioned on its evidence, not on its severity label.

One correction to an earlier commit message rather than to history: commit
`3ee0178` says the round-2 findings are dispositioned in
`evidence/g0-01/independent-review-round-2.json`. No such split file was created;
every round lives in the single `evidence/g0-01/independent-review.json`, which is
the source of record.

The review also recorded a coverage limitation that is worth carrying forward:
OCR's default rules excluded `requirements/locks/linux-amd64-py312.txt` and
`requirements/tests/test_lock_contract.py` from first-class review, which are the
two artifacts most central to this task. The reviewing agent read them as context,
but that is not the same as reviewing them.

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
* The frozen artifacts were reproduced end to end after the review response -
  two fresh acquisitions, a fresh freeze and a fresh offline proof - and every
  digest came out identical (`lock.sha256` `e951f4c1...`, artifact inventory
  `ffef04fc...`, resolution `c85f76b7...`). That is a positive result, not a
  claim that an arbitrary future date would resolve the same versions.

## Reverification at the exact head and the acceptance state

The sealed work was reverified against the live remote and the exact head before
any successor task was considered. Head
`ca5ceb361798ff8ba78a8ac86c47de0bc440058e` (tree
`0dcc5fc5d851a37bcbbc4644b99608dd73e5db51`) equals the remote branch object, the
worktree was clean, and neither the plan pull request nor its foundation base had
moved.

Every deterministic check in this directory reproduces at that head: the plan
validator with the pinned SpecGrain checkout, its seven negative tests, the 29
lock contract tests, the Diffcipline R2 proof and the lock/artifact/listing
reconciliation. The digests recorded above (`e951f4c1...`, `ffef04fc...`,
`c85f76b7...`) recompute byte for byte.

Four things did not reproduce cleanly and are recorded rather than smoothed over:

* The aggregate counts inside `diffcipline.json` describe the previous revision,
  not the sealed one: it records 12,390 added lines, which is exactly the total at
  `7f06517`, while the sealed head totals 12,550 for the same 40 files. The verdict
  and the scope result do reproduce at the sealed head.
* The independent review is bound to `7f06517`. The one later commit changes
  evidence files only, so it is treated as an evidence-only descendant under
  chapter 41 rather than as an invalidating change. No fresh review round could be
  executed for it in this session because no model-endpoint credential was
  available.
* The required `accepted-head` evidence item does not exist yet, and it cannot
  honestly be produced before the revision is accepted. See `acceptance-state.json`.
  (Superseded later in this file: acceptance was granted, and `accepted-head.json`
  now exists.)
* The pull request still has no CI: the inherited workflows trigger only on
  `dev/v2.0` and `2.0`, and both third-party reviewers either skipped or reported
  that reviews are disabled for this base branch.

`reverification.json` holds the machine record, `acceptance-state.json` holds the
per-item evidence status and the exact unlock conditions, and the new files under
`evidence/jev/G0-01/` hold the typed decisions taken at this checkpoint.

## Founder execution acceptance, the repair it required, and the accepted head

The repository owner then granted explicit execution acceptance, recorded verbatim
and classified by Jev in `evidence/jev/G0-01/execution-predecessor-acceptance.json`
and `evidence/g0-01/founder-execution-acceptance.json`. It accepts
`ca5ceb361798ff8ba78a8ac86c47de0bc440058e` as the execution predecessor for
`G0-02 / SG-000002`, permits that successor to be developed as stacked work while
PR #3 stays open, and removes the previous `BLOCKED_PENDING_OWNER_ACCEPTANCE`
boundary - on one stated condition: live re-verification that the named revision
still matches the independently verified implementation and that no later change
invalidated its evidence.

That condition is what forced the first clean-checkout run of this task's own
gates, and that run failed. From a detached worktree at the named revision,
`test_lock_file_hash_matches_the_inventory` expected `e951f4c1...` and observed
`6e50df34...`, and the R2 gate over the whole change returned FAIL with "verification
failed: python -m unittest discover -s requirements/tests -p test_*.py". The cause
was not the resolution: the lock recorded its own digest over the generating
Windows working copy (CRLF) while `.gitattributes` pins `*.txt` to LF, so the record
described a machine rather than the committed artifact. `lock-digest-repair.json`
holds the reproduction, the mechanism, the blast radius and the repair;
`lock-digest-repair-verification.json` proves the repaired record from a clean
checkout, and `lock-digest-repair-diffcipline.json` proves the repair itself.

The repaired revision was then reviewed as a packet in its own right, its own
packet bound was reconciled on the record because the cumulative range exceeds the
sealed 40-file ceiling, and the cumulative gate was re-run. The accepted head is
`b4531988f4a32143407c5aa2de4d7090d33e4930`, where
`accepted-head-diffcipline.json` records verdict PASS over
`144935cd..b4531988f` with 46 files and all four verification commands green.
`execution-acceptance-reverification.json` holds both sides of that comparison:
every failing check at the named revision, preserved, and every passing check at
the accepted head.

`accepted-head.json` is the sixth required evidence item. What it does **not** claim
matters as much as what it does: PR #3 is still open and unmerged, nothing is
released, G0 is still open and `evidence/gates/G0.json` does not exist, no CI
validates this branch, and the repair delta `ca5ceb3..b4531988f` has **no independent
review** - the last completed review is bound to `7f06517`, and Open Code Review
could not run here because no LLM endpoint credential exists in this environment.
Under chapter 41 that is ABSTAIN/UNAVAILABLE, which is not approval.
