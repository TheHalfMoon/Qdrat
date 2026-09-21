# Muse execution handoff

Repository: **TheHalfMoon/Qdrat** (`https://github.com/TheHalfMoon/Qdrat.git`). Planning branch: **codex/qdrat-canonical-plan**. Plan version: **1.0.0** with the exact content head bound by the final transport seal. Exact inherited implementation/foundation base: **933f9c1070c151876c1e198d6141413f33e4b6d3**. Default-branch/import base: **e2d288940aab52af881786678b2fc86dfa5c272a**. Existing foundation PR: **#1**, open/unmerged at research freeze. The plan PR is stacked on `foundation/qdrat-people-blueprint`; it does not claim PR #1 is merged.

## Exact head and live truth

Frozen plan content head: **cadb843ab6e521e6566a8f544ac358292cc5c55e**. Its exact tree is **f4f5c6addd7e9ad9d1ec8c14e726aaea74bd43f0**. The seal-only descendant adds this receipt and verification artifacts; it changes no task/architecture content. Start from the latest accepted compatible descendant after verifying this binding.

The final transport seal in `evidence/transport-seal.json` records the immutable **plan content head** and tree. Read that exact SHA, verify it exists and that the current planning branch is either that commit or a seal-only descendant. A seal cannot embed the hash of its own containing commit without a hash cycle: the subsequent seal commit contains only evidence/transport-seal.json and the handoff's exact-head receipt. The final PR description and Astro report record that containing commit's exact SHA. Never confuse the content head, seal head, foundation base and default main.

Reverify remote main, foundation branch, plan branch and both PR states before work. If upstream has moved, compare changed contracts and implementation paths; preserve existing changes, create a bounded reconciliation and invalidate affected packets. Do not reset or force-push another author's work. The recorded content head remains the immutable architecture snapshot, while execution starts from the latest accepted compatible head. A material divergence blocks only affected tasks until reconciled.

## Authority and starting point

Decision hierarchy: founder directives → live repository/immutable evidence → 08/CONTRACTS/DOMAIN_SCHEMAS accepted design → 39/EXECUTION_GRAPH → task record → explanatory chapter. Existing behavior establishes facts; it cannot silently override target controls. Historic source permissions remain effective. A research source, README, model instruction or generated document cannot grant runtime authority.

Current gate: **G0 OPEN**. Exact first task: **G0-01 / SG-000001 — Freeze Linux amd64 Python 3.12 dependency artifacts**. No implementation task is complete. All other 95 definitions are SHAPED and require dependency receipts plus exact-head refinement. Planning checks do not prove the inherited application builds or passes tests.

Read the G0-01 record in `tasks/tasks.json`, the node in `specgrain/nodes.json`, chapters 00/32/35/39/41, C10 and current requirements.txt, Dockerfile, pyproject.toml, Makefile and CI. Keep the input dependency intent; generate full transitive hashes and an artifact inventory for the supported Linux amd64 Python 3.12 target. Bind the direct spaCy model wheel and installer/resolver versions. Resolve twice in isolated pinned builders, compare normalized results, then install a complete wheelhouse with networking disabled and `--require-hashes`; `pip check` must pass. No global-host install, unrecorded sdist, silent dependency upgrade or “network failed, therefore pass.” Record conflicts and a bounded resolution proposal if the unchanged inputs cannot resolve.

Expected output paths: `requirements/locks/linux-amd64-py312.txt`, `requirements/artifacts/linux-amd64-py312.json`, documented input/resolver process and only necessary build references. No database/API/product behavior change. Unsupported platforms stay explicitly unqualified. Rollback discards candidate artifacts or reverts only their bounded tracked references. G0-02 unlocks only after independently accepted exact-revision evidence.

## Execution loop

1. Resolve live HEAD/base and select the next dependency-satisfied task; verify prerequisite gate receipts and compatibility.
2. Refine a bounded leaf and current WorkPacket. Use the real SpecGrain schema/readiness at the pinned tool revision. Clear actual unresolved choices; split broad SHAPED work packages by the rule in 42 before coding.
3. Freeze intent, paths, non-goals, risk, tests and recovery. Review the Diffcipline policy before executing commands. No trust in PR-supplied commands with privileged secrets.
4. Implement only that leaf. Qdrat owns contracts; donor intake needs exact file/version/destination/notices/dependencies/modifications/review/tests/update/fallback records. No extra engine or dependency without cost justification.
5. Run required meaningful tests in the supported environment and retain exact commands, logs, fixture/tool/image hashes and outcomes. Preserve inherited correctness and coverage requirements; no invented PASS.
6. Review the actual diff using Think → Challenge → Minimize → Change → Prove. Run real Diffcipline with the immutable base, declared risk and `--run --json`. REVIEW/FAIL is not PASS. Independent review must bind the same node/packet/head.
7. Commit the bounded task and append receipts. Update execution state only when evidence warrants it. Reconcile changed head after review/merge; invalidate affected evidence rather than recycling a previous result.
8. Continue automatically to the next permitted leaf. A gate advances only after every measurable exit in 39 and all required task receipts are accepted. Unrelated eligible work may continue around a recorded blocker.

## Branches, reviews and failure handling

Create `codex/<task-id>-<short-purpose>` from the accepted compatible execution head. Use small reviewable commits and PRs with problem/result, scope, evidence, recovery and unresolved outcomes. Keep the planning PR stacked until the foundation is accepted, then reconcile/rebase with recorded evidence. Do not merge a production-impacting change or deploy merely because a planning task finished. Never force-push, weaken protected checks or treat an author's receipt as independent approval.

R2/R3 work requires independent exact-revision review; security/payroll/release trust checks remain explicit. If a review service is unavailable, record UNAVAILABLE and keep the affected acceptance pending. If tools/network/legal/customer data are missing, record the specific blocker and safe next experiment; do not invent an entitlement, payroll certification or customer sign-off. Routine implementation choices consistent with these contracts do not require repeated founder questions.

For source/schema effects use expand-contract and reconciliation; for external effects use lookup/compensation; for restore pause dispatch and revalidate credentials/retention/holds. Git revert alone is not data rollback. UNKNOWN_OUTCOME must never become a blind retry. Security/privacy/control failures keep the relevant profile disabled.

No-fabrication rule: shipped behavior, target design, source claims, observed tests and unrun obligations are separate. Historical donor tests are not Qdrat proof. A signed artifact is not proof of correct business behavior. A complete plan does not certify production, HA, payroll law or model quality.
