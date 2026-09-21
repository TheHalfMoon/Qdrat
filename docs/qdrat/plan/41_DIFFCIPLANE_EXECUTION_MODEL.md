# SpecGrain and Diffcipline execution model

The requested “Diffciplane” is resolved to the accessible founder repository **TheHalfMoon/Diffcipline**. No distinct accessible repository with the requested spelling was found. Its inspected main is `1e6d14f77b95bb132b42276f10d67f1018ab5bb6`; the immutable v1.0.0 release is `5cb1c77340b75649f6168e0e8f66479ea047ea96`. SpecGrain was inspected at `5de7d6499bb0a9e3a191fc0934399cf099d1980a`. These are explicit tool versions, not invented Qdrat conventions. See [SpecGrain source](https://github.com/TheHalfMoon/SpecGrain/tree/5de7d6499bb0a9e3a191fc0934399cf099d1980a) and [Diffcipline release](https://github.com/TheHalfMoon/Diffcipline/releases/tag/v1.0.0).

## Actual SpecGrain behavior and Qdrat adapter

`SpecNode.from_dict` validates the real schema. Nodes have stable `SG-000001` style IDs, scope, acceptance, dependencies, risk, context budget, change surface, evidence, state and metadata. Semantic `revision_digest` excludes lifecycle state; changing acceptance or scope invalidates revision-bound downstream evidence. `validate_refinement` checks parent/child structure. `evaluate_grain_readiness(candidate, forest)` requires a REFINING leaf with scope, acceptance, bounded context, recovery, evidence, minimality/safety declarations and no unresolved decisions. It returns a report, not permission to assert implementation success.

Qdrat stores a portable node array in `specgrain/nodes.json`, full task records in `tasks/tasks.json`, and its own `qdrat.execution-graph/v1` graph in JSON-form YAML 1.2. This is an adapter, not an upstream-native scheduler or storage format. A task and node must agree on outcome, acceptance and dependencies. `catalog.psv` is a human editing reference; the JSON records and graph are authoritative.

At the frontier, reconcile the accepted repository head, read only relevant source/contracts, refine physical paths and test commands, estimate actual context and form a WorkPacket with source IDs/provenance, revisions/digests, byte/token cost and required evidence. DRAFT → SHAPED → REFINING → GRAIN is specification refinement. Qdrat's execution states (selected, running, blocked, implemented, independently VERIFIED) are separate evidence states. Do not relabel every future SHAPED target GRAIN. Readiness cannot establish that dependencies passed or a test ran.

Split broad future work packages before coding when the bounds in chapter 42 are exceeded. New child IDs are appended, never recycled; preserve parent scope/acceptance, update edges and invalidate impacted packets. Resolving exact paths at a future head is expected refinement. Choosing another canonical datastore or bypassing authority requires an explicit architecture reconciliation, not routine refinement.

## Actual Diffcipline behavior and Qdrat adapter

Apply **Think → Challenge → Minimize → Change → Prove** to each grain. Freeze previous state, intended delta, boundaries, non-goals and risk before editing. Challenge whether existing primitives suffice. Minimize the change while preserving correctness, security, usability and compatibility. Implement only that delta. Prove with the reviewed checks and exact diff.

The real CLI is `diffcipline check --base <immutable-base> --risk R0|R1|R2|R3 --run --json`. It reads `.diffcipline.toml`; a reviewed external policy can be supplied with `--enterprise-policy <path>`. `--run` executes configured verification; omitting it cannot yield a clean proof when checks are required. A missing requested risk profile fails closed. Exit codes: 0 PASS, 1 REVIEW, 2 FAIL, 64 usage/execution error. JSON schema is `diffcipline.proof/v1`. Diffcipline does not schedule this graph or independently certify the truth of prose.

With `--base`, the inspected implementation compares `<base>...HEAD`, so staged-but-uncommitted additions do not constitute that commit-range proof. First inspect/stage the bounded change, make the reviewable local content commit, then run the exact-base proof against it. Also check that the worktree/index is clean; uncommitted edits must not be hidden by a committed-range PASS. The initial pre-commit trial correctly returned REVIEW for no committed change. Verification commands can write their own stdout before the JSON proof; consumers must locate the `diffcipline.proof/v1` record rather than assume stdout is a single JSON document.

Policy must include exact allowed paths, forbidden surfaces, reviewed size bounds, dependency/lock handling and concrete commands for the requested risk. Do not weaken policy after a failure. If the accepted task legitimately requires broader scope, revise/review its packet first and retain the original failure. For implementation, use R2 for cross-module/data/migration/dependency behavior and R3 for authentication, authorization, payroll release, secrets, sandbox, destructive recovery or release trust. R0 is prose-only; R1 is bounded non-runtime tooling. No risk label suppresses relevant tests.

The planning change uses `plan-policy.toml` as an explicit external policy, with only this directory allowed and the plan validator as its executed R1 check. This policy is intentionally not installed as the runtime repository's general policy. Its larger documentation bounds cover the requested canonical plan, not permission for large feature commits. Future implementation packets need their own reviewed policy and product tests.

## Evidence and state transitions

Receipt fields: task/node ID and semantic revision; packet digest; repository/base/head/tree; diff scope and policy digest; tool version/binary hash; checks with command, environment, time, exit, artifact/log hashes; acceptance mapping; recovery result; reviewer identity and disposition. Outcomes are PASS, FAIL, NOT_RUN, INCONCLUSIVE or UNAVAILABLE. Required results other than PASS do not unlock successors. Reviewer ABSTAIN/UNAVAILABLE is not approval. A CLI PASS alone cannot authorize a release.

Independent review binds the exact implementation commit. A later code, fixture, policy or dependency change invalidates affected receipts. Merge/rebase requires reconciliation against the new accepted base and appropriate reruns. The trusted verifier must not execute arbitrary PR-supplied policy with privileged secrets. Evidence is append-oriented; redacted content is stored separately from safe digests and summaries.

The graph's task dependencies require accepted exact-revision receipts, plus predecessor gate acceptance. Select the next eligible leaf; if blocked, record reason and affected descendants, then select an unrelated eligible leaf. Do not bypass missing baseline, invent customer/legal approval or call network failure a passed build. Gate advancement requires chapter 39's measurable exits and a signed/accountable gate disposition.

Rollback is not just Git revert: distinguish source/config reversal, expand-contract repair, data restore and compensating external actions. Unknown effects remain quarantined/reconciling. Reverting policy or restoring a database cannot revive revoked credentials or erase subsequent legal holds.

## Tool-execution qualification

The local Rust source build failed because `link.exe` was unavailable. The Windows v1.0.0 release executable was instead acquired from the immutable release and its SHA-256 matched GitHub's published asset digest `5fee721d3837ab86f2c36003d02ca67ebac793ff8dadcdb3b7eea074690e57a8`. This verifies the downloaded bytes against the release metadata; a full independent Sigstore attestation verification was not performed. The binary is a temporary planning tool, not a new product dependency. Actual validator/SpecGrain/Diffcipline outputs are retained in `evidence/verification/`; they must be read for outcomes, not inferred from this description.
