# Evidence-based test strategy

Baseline first: reproduce supported Python/Linux image, PostgreSQL migrations, inherited smoke/unit/coverage checks and production configuration. Preserve the Makefile floor of 26 and existing meaningful correctness checks. CI must target actual Qdrat branches/PR bases; absent runs are NOT_RUN. Dependency/network failure is INCONCLUSIVE, never PASS.

Test layers: pure domain/rules units; PostgreSQL transaction/constraint tests; API/policy contracts; fake-provider connector conformance; migration and restore fixtures; browser journeys; supported-profile installation; performance and recovery. Use synthetic or appropriately authorized minimized data. Snapshot fixtures include source and expected revision. Do not use production employee records in CI.

Every writable primitive needs happy path, rejection, concurrent revision conflict, idempotent repeat and permission-denied cases. Durable effects additionally need crash before/after commit, lost response, lease expiry, cancellation and reconciliation. Security tests are defensive contract checks; no autonomous offensive scanning workflow is implied.

People/payroll: effective dates, decimals, cohorts, leave accrual, rounding, retro adjustments, closed-period correction, segregation and parallel payroll comparison. Service: channel dedupe/audience, calendar/SLA clocks and lost sends. Data: drift, tombstones, missing versus inaccessible fields, watermark loss and ACL revocation. Search/AI: permission-preserving citations, stale evidence, untrusted content, abstention and forbidden action denial.

UI journeys run English/Arabic, LTR/RTL, keyboard, zoom/reflow, screen reader and mobile viewport. Automated axe supplements manual evidence. No-AI/no-voice and air-gap profiles run the same essential People journey with remote access disabled. Optional profiles fail closed and visibly degrade.

Evidence receipt binds task/SpecNode revision, packet digest, base/head/tree, test command, environment/image digest, start/end, exit status, log/artifact hashes, fixture revision and reviewer identity. Redacted logs remain inspectable. Required check missing/skipped is not success. Flaky/quarantined tests need owner, expiry and a replacement correctness check; no automatic retry-until-green masking.

Tests run only on reviewed code/config in an isolated environment. PR code cannot supply its own trusted release approval. Independent verification checks exact current head and acceptance, not merely author's reported output.
