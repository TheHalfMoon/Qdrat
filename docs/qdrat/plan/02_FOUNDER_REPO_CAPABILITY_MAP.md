# Founder repository capability map

Snapshot: 20–21 September 2026. All 36 accessible repositories were enumerated, including seven private repositories. Exact default heads, branch counts, sampled file blob IDs, manifest paths, test paths and open PR heads are retained in [the inventory](evidence/founder-inventory.json). All branch names were enumerated; this is not an exhaustive review of every historical branch implementation. No private source text is republished here.

The classifications below are architectural decisions, not claims that donor tests passed. ADAPT_PATTERN means reimplement the named invariant behind a Qdrat contract; it does not import that runtime. For implementation reuse, the intake record in chapter 35 must additionally bind exact files, notices, transitive dependencies, changes, tests, update owner and exit strategy. Founder authorization is already established.

## TheHalfMoon/Ascout

**ADAPT_PATTERN → Execution governance.** Candidate admission and discriminating verification. TypeScript implementation sampled.

- Evidence: [main @ 5eddf9cd46f64bb2835677572d9aef4a4da99ae7](https://github.com/TheHalfMoon/Ascout/tree/5eddf9cd46f64bb2835677572d9aef4a4da99ae7); public; 496 branches enumerated. Selected paths: `src/quality/admission.ts`.
- Dependency/architecture evidence: `package.json`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `tests/agent-integration-admission.contract.test.ts`, `tests/agent-receipt.contract.test.ts`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Exact proposal/source-tree gates and accountable admission. Avoid: Do not import entire evaluation supervisor.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Balott

**REFERENCE_ONLY → UX.** Arabic/localized product specifications. Planning corpus; no relevant engine qualified.

- Evidence: [main @ ed720142ca48105bed8322f3c1b61e7d091f0c82](https://github.com/TheHalfMoon/Balott/tree/ed720142ca48105bed8322f3c1b61e7d091f0c82); public; 1 branches enumerated. Selected paths: README/root tree; no implementation file qualified.
- Dependency/architecture evidence: No build manifest in inspected default tree. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: No test path established by inventory. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Bilingual requirements and bounded game-state design as reference. Avoid: Card-game runtime and assets.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Coddev

**ADAPT_PATTERN → CI.** Signthos qualification receipts. Private CI evidence repository; receipts not rerun.

- Evidence: [main @ c0315e72254e476c37c6d4eed92f92313b7097a2](https://github.com/TheHalfMoon/Coddev/tree/c0315e72254e476c37c6d4eed92f92313b7097a2); private; 1 branches enumerated. Selected paths: `verification/signthos-grain-h-result.json`.
- Dependency/architecture evidence: No build manifest in inspected default tree. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: No test path established by inventory. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Machine-readable exact-result evidence. Avoid: Historical PASS as current Qdrat proof.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/commandF

**ADAPT_PATTERN → Data/source intake.** FHIR package resolver/diff graph. Rust modules sampled; medical-specific.

- Evidence: [main @ 18819c7fdaee618f4aa86c6c3279b1acb70ec9f2](https://github.com/TheHalfMoon/commandF/tree/18819c7fdaee618f4aa86c6c3279b1acb70ec9f2); public; 105 branches enumerated. Selected paths: `crates/commandf-pkg/src/lib.rs`.
- Dependency/architecture evidence: `Cargo.toml`, `crates/commandf-cli/Cargo.toml`, `crates/commandf-pkg/Cargo.toml`, `fuzz/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `crates/commandf-cli/tests/check_behavior.rs`, `crates/commandf-cli/tests/check_exit_contract.rs`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Artifact identity, resolver provenance, compatibility reporting. Avoid: FHIR semantics as company object model.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/commandMed

**ADAPT_PATTERN → AI evaluation.** Frozen research asset evidence. Python offline evidence code sampled.

- Evidence: [main @ ce5dc8f4dda49270e5bb4bebc936ce7514a9b9e9](https://github.com/TheHalfMoon/commandMed/tree/ce5dc8f4dda49270e5bb4bebc936ce7514a9b9e9); public; 361 branches enumerated. Selected paths: `src/commandmed/spec007/research_tournament_asset_evidence.py`.
- Dependency/architecture evidence: No build manifest in inspected default tree. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `tests/__init__.py`, `tests/eval_contract`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Rights and contamination identity with deterministic benchmark inputs. Avoid: Clinical/model-performance claims.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Delethos

**ADAPT_PATTERN → Trust/evidence.** Delegation and independent review outcomes. TypeScript implementation sampled.

- Evidence: [main @ 5b8f5f28239bbd0b2a366824fd14c1b6c01058b8](https://github.com/TheHalfMoon/Delethos/tree/5b8f5f28239bbd0b2a366824fd14c1b6c01058b8); public; 117 branches enumerated. Selected paths: `packages/core/src/evidence.ts`.
- Dependency/architecture evidence: `package.json`, `packages/adapters/package.json`, `packages/core/package.json`, `packages/runtime/package.json`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `packages/adapters/test/claude.test.ts`, `packages/adapters/test/codex.test.ts`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: PASS/ABSTAIN/UNAVAILABLE distinctions. Avoid: A second agent authority or review engine.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Diffcipline

**DEPENDENCY → Planning/CI.** Bounded change and proof CLI. Dependency-free Rust CLI at pinned main.

- Evidence: [main @ 1e6d14f77b95bb132b42276f10d67f1018ab5bb6](https://github.com/TheHalfMoon/Diffcipline/tree/1e6d14f77b95bb132b42276f10d67f1018ab5bb6); public; 101 branches enumerated. Selected paths: README/root tree; no implementation file qualified.
- Dependency/architecture evidence: `Cargo.toml`, `crates/diffcipline-cli/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `benchmarks/fixtures/f01-shared-root-cause/repo/tests/test_session.py`, `benchmarks/fixtures/f02-stdlib-query/repo/tests/test_query.py`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Use actual policy/risk/proof semantics. Avoid: Pretending CLI schedules dependencies or verifies unrun checks.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Ecra

**REFERENCE_ONLY → Execution plane.** Browser trust-domain contracts. Design/contracts with active planning.

- Evidence: [main @ 0e2ff8c687c93e6f158da6984a7a6915339b5f3f](https://github.com/TheHalfMoon/Ecra/tree/0e2ff8c687c93e6f158da6984a7a6915339b5f3f); public; 10 branches enumerated. Selected paths: README/root tree; no implementation file qualified.
- Dependency/architecture evidence: `Cargo.toml`, `crates/ecra-core/Cargo.toml`, `crates/ecra-run/Cargo.toml`, `crates/ecra-verify/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `crates/ecra-core/tests/action_digest.rs`, `crates/ecra-core/tests/canonicalization.rs`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Explicit origin/session authority as reference. Avoid: Ambient browser credential inheritance.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Fanatir

**REFERENCE_ONLY → Pack architecture.** Afia-linked engineering blueprint. Private mixed skeleton; sampled program is placeholder.

- Evidence: [main @ 04e9120c0e9350daff68238e0e49e2c5d7e5c9d9](https://github.com/TheHalfMoon/Fanatir/tree/04e9120c0e9350daff68238e0e49e2c5d7e5c9d9); private; 11 branches enumerated. Selected paths: `docs/product/v1-engineering-program.md`.
- Dependency/architecture evidence: `Cargo.toml`, `_archived/apps-desktop/src-tauri/Cargo.toml`, `_archived/apps-desktop/ui/package.json`, `_archived/crates/afia-ai/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `_archived/apps-desktop/ui/src/test/.gitkeep`, `_archived/crates/afia-ai/tests/.gitkeep`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Reference only for domain separation. Avoid: Treating draft health architecture as implemented.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Flake

**ADAPT_PATTERN → Knowledge/memory.** Fehrest-derived local work memory. Rust derived-index code sampled.

- Evidence: [main @ a85f906fa579f611c4c05f6464f955805cd8fd32](https://github.com/TheHalfMoon/Flake/tree/a85f906fa579f611c4c05f6464f955805cd8fd32); public; 71 branches enumerated. Selected paths: `src/derived.rs`.
- Dependency/architecture evidence: `Cargo.toml`, `desktop/package.json`, `desktop/src-tauri/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `tests/fixtures`, `tests/fixtures/canonical`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Rebuildable FTS and non-authoritative locators. Avoid: Second company memory/authorization store.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Golam

**REFERENCE_ONLY → AI execution.** Agent operating-system concepts. Rust source/tree; runtime not qualified here.

- Evidence: [main @ 13a379ac478a3abaff7ed1da3db14ff9c1ac2188](https://github.com/TheHalfMoon/Golam/tree/13a379ac478a3abaff7ed1da3db14ff9c1ac2188); public; 33 branches enumerated. Selected paths: README/root tree; no implementation file qualified.
- Dependency/architecture evidence: `Cargo.toml`, `crates/golam-core/Cargo.toml`, `crates/golam-effects/Cargo.toml`, `crates/golam-ipc/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `crates/golam-core/tests/spec004_state_model.rs`, `crates/golam-effects/tests/qualification_properties.rs`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Explicit runtime boundaries as reference. Avoid: Whole Agent OS inside Qdrat.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Golam-research

**REJECT → Rejected runtime intake.** Reconstructed desktop research. Unofficial reconstructed binary provenance.

- Evidence: [main @ a9f633e09d49a85829b8236331b9e21f7e612634](https://github.com/TheHalfMoon/Golam-research/tree/a9f633e09d49a85829b8236331b9e21f7e612634); public; 1 branches enumerated. Selected paths: README/root tree; no implementation file qualified.
- Dependency/architecture evidence: `package.json`, `src/app/package.json`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `source/packages/local-exec/tests/common.ts`, `tests/backend-mcp-exec-json.test.mjs`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: No source intake recommendation. Avoid: Reconstructed binary/dependency chain.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/HarnessMind

**ADAPT_PATTERN → Connector discovery.** Read-only harness discovery fidelity. Private Python model sampled.

- Evidence: [master @ ef628cdf9f97e38822ffaa80c9491636ef508dc0](https://github.com/TheHalfMoon/HarnessMind/tree/ef628cdf9f97e38822ffaa80c9491636ef508dc0); private; 7 branches enumerated. Selected paths: `src/harnessmind/core/model.py`.
- Dependency/architecture evidence: `pyproject.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `.specify/bugs/hm-ci-001-canonical-branch-ci-trigger-mismatch/test.md`, `.specify/bugs/hm-ci-002-macos-mypy-unreachable-platform-branches/test.md`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: UNKNOWN cannot silently become truth; partial/inferred fidelity. Avoid: Advertising discovered config as enforced control.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Hikma

**REFERENCE_ONLY → Reference only.** Named concept repository. Private README-only default.

- Evidence: [main @ db5415e66963e042313f1ecfbef1a72b582c0e3c](https://github.com/TheHalfMoon/Hikma/tree/db5415e66963e042313f1ecfbef1a72b582c0e3c); private; 1 branches enumerated. Selected paths: README/root tree; no implementation file qualified.
- Dependency/architecture evidence: No build manifest in inspected default tree. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: No test path established by inventory. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: No reusable implementation established. Avoid: Inventing capabilities from name.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Himsat

**ADAPT_PATTERN → Voice.** Capture session lifecycle. Rust typed core sampled.

- Evidence: [main @ 8b6c619750646c454fa754671c9eb3d34114b28c](https://github.com/TheHalfMoon/Himsat/tree/8b6c619750646c454fa754671c9eb3d34114b28c); public; 214 branches enumerated. Selected paths: `crates/himsat-core/src/capture_session.rs`.
- Dependency/architecture evidence: `Cargo.toml`, `crates/himsat-core/Cargo.toml`, `crates/himsat-events/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `crates/himsat-core/tests/b005d_journal_kill.rs`, `crates/himsat-core/tests/b204_recovery_negative.rs`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Capture source/session separation and cancellation. Avoid: Whole desktop capture product.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Inercative

**ADAPT_PATTERN → Digital Twin/Studio.** Ineractive product graph. Typed design contracts; no production engine proved.

- Evidence: [main @ e8014ea1feb9cb9c37a05f2399f23b33465490fa](https://github.com/TheHalfMoon/Inercative/tree/e8014ea1feb9cb9c37a05f2399f23b33465490fa); public; 7 branches enumerated. Selected paths: `docs/canonical/PRODUCT_GRAPH.md`.
- Dependency/architecture evidence: `package.json`, `packages/program-tasks/package.json`, `packages/protocol/package.json`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: No test path established by inventory. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Versioned semantic requirements/actions/integration nodes. Avoid: Second source-of-truth graph database.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/kernux

**ADAPT_PATTERN → Trust/Execution.** Authority envelopes and policy. Rust policy source sampled.

- Evidence: [main @ ecca499f6ce4a06f596c9ce1f5f2434825c51d94](https://github.com/TheHalfMoon/kernux/tree/ecca499f6ce4a06f596c9ce1f5f2434825c51d94); public; 135 branches enumerated. Selected paths: `crates/kernux-policy/src/envelope.rs`.
- Dependency/architecture evidence: `Cargo.toml`, `crates/kernux-contracts/Cargo.toml`, `crates/kernux-identity/Cargo.toml`, `crates/kernux-policy/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `crates/kernux-contracts/tests/adversarial.rs`, `crates/kernux-contracts/tests/compatibility.rs`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Bound subject/action/resource/revision/constraints/provenance. Avoid: Whole daemon OS or blanket sandbox claims.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Kodac

**ADAPT_PATTERN → Trust/evidence.** Receipt and approval identity. TypeScript runtime source sampled.

- Evidence: [main @ 406b335277f2df1e3dedf24cdb45847dff919d44](https://github.com/TheHalfMoon/Kodac/tree/406b335277f2df1e3dedf24cdb45847dff919d44); public; 679 branches enumerated. Selected paths: `packages/kodac-runtime/src/evidence/receipt.ts`.
- Dependency/architecture evidence: `nexusmcp/omni-bridge/package.json`, `packages/kodac-runtime/package.json`, `pyproject.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `nexusmcp/omni-bridge/tests/unit`, `nexusmcp/omni-bridge/tests/unit/audit.test.ts`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Input digests, exact approval instances and confinement binding. Avoid: Global privileged coding agent.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/kodac-phase-b-gate

**ADAPT_PATTERN → Release governance.** Trusted CI gate. Private Go implementation sampled.

- Evidence: [main @ 79a5e3a5c3b0f4882e8c9c864e314c0fab3c9a40](https://github.com/TheHalfMoon/kodac-phase-b-gate/tree/79a5e3a5c3b0f4882e8c9c864e314c0fab3c9a40); private; 2 branches enumerated. Selected paths: `internal/gate/evaluate.go`.
- Dependency/architecture evidence: `go.mod`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: No test path established by inventory. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Exact repository/head/PR/app/config allowlists. Avoid: Assuming in-repo policy alone is trusted enforcement.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/MedScale

**ADAPT_PATTERN → Data Fabric.** Data source fabric. Rust platform plus planning candidate.

- Evidence: [main @ ae0441918296c2d1510a71061249c7e55e65d760](https://github.com/TheHalfMoon/MedScale/tree/ae0441918296c2d1510a71061249c7e55e65d760); public; 63 branches enumerated. Selected paths: `docs/planning/DATA_SOURCE_FABRIC_PLAN.md`.
- Dependency/architecture evidence: `Cargo.toml`, `crates/medscale-cli/Cargo.toml`, `crates/medscale-contracts/Cargo.toml`, `crates/medscale-core/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `crates/medscale-contracts/tests/object_no_coercion.rs`, `crates/medscale-contracts/tests/object_roundtrip.rs`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Source/snapshot contracts without second storage authority. Avoid: Clinical capability or research plan as shipped.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/MESC

**ADAPT_PATTERN → AI evaluation.** Snapshot-bound benchmark specification. Python research implementation sampled.

- Evidence: [main @ a2baa30752be719f700c118363c37cc143336601](https://github.com/TheHalfMoon/MESC/tree/a2baa30752be719f700c118363c37cc143336601); public; 494 branches enumerated. Selected paths: `src/medscale/bench/spec.py`.
- Dependency/architecture evidence: `pyproject.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `tests/_mesc_b2a_portability.py`, `tests/_mesc_p01_04b2d_fixtures_v1.py`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Hash-bound dataset/model evaluation; explicit unsupported cases. Avoid: Unimplemented clinical reasoning advertised as valid.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Morize

**ADAPT_PATTERN → Memory/Data.** Memory mutation outcomes/scopes. Rust type definitions; state machine explicitly absent.

- Evidence: [main @ 04f1d5658405ce02d14aba978cc0397242755871](https://github.com/TheHalfMoon/Morize/tree/04f1d5658405ce02d14aba978cc0397242755871); public; 50 branches enumerated. Selected paths: `crates/morize-core/src/mutation.rs`, `crates/morize-core/src/scope.rs`.
- Dependency/architecture evidence: `Cargo.toml`, `crates/morize-core/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: No test path established by inventory. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: COMMITTED/REJECTED/FAILED/UNKNOWN distinction. Avoid: Assuming enum defines complete recovery implementation.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/MSTR

**ADAPT_PATTERN → AI evaluation.** Bounded training/research loop contracts. Research schemas; no trained Qdrat model established.

- Evidence: [main @ e87328872232471fa0e1eb05d74223bc0aeaafd3](https://github.com/TheHalfMoon/MSTR/tree/e87328872232471fa0e1eb05d74223bc0aeaafd3); public; 1290 branches enumerated. Selected paths: `schemas/mstr-loop-contract-v0.schema.json`.
- Dependency/architecture evidence: `pyproject.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `tests/contract`, `tests/contract/test_adaptive_inference_contract.py`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Iteration/time/repair bounds and independent verification. Avoid: Training stack/model dependency in baseline.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Paina

**REFERENCE_ONLY → Reference only.** Product research branch. Private default README; active PR metadata inspected.

- Evidence: [main @ 3758b746d88014b95c03f07d28705f1ac98e7548](https://github.com/TheHalfMoon/Paina/tree/3758b746d88014b95c03f07d28705f1ac98e7548); private; 2 branches enumerated. Selected paths: README/root tree; no implementation file qualified.
- Dependency/architecture evidence: No build manifest in inspected default tree. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: No test path established by inventory. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: No implementation reuse established. Avoid: Assuming active PR merged or runtime mature.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/ProtocolWISE

**REFERENCE_ONLY → Reference only.** Protocol research. Private default README; active PR metadata inspected.

- Evidence: [main @ 7ed9f8670c041794c8fa3397d80ae41d9cf310a4](https://github.com/TheHalfMoon/ProtocolWISE/tree/7ed9f8670c041794c8fa3397d80ae41d9cf310a4); private; 3 branches enumerated. Selected paths: README/root tree; no implementation file qualified.
- Dependency/architecture evidence: No build manifest in inspected default tree. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: No test path established by inventory. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Research planning only. Avoid: Medical protocol engine in core.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Qdrat

**ADAPT_PATTERN → Whole product.** Inherited People foundation. Django implementation plus unmerged planning PR.

- Evidence: [main @ e2d288940aab52af881786678b2fc86dfa5c272a](https://github.com/TheHalfMoon/Qdrat/tree/e2d288940aab52af881786678b2fc86dfa5c272a); public; 2 branches enumerated. Selected paths: README/root tree; no implementation file qualified.
- Dependency/architecture evidence: `pyproject.toml`, `requirements.txt`, `static/build/vendor/ionicons/@stencil/core/cli/package.json`, `static/build/vendor/ionicons/@stencil/core/compiler/package.json`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `accessibility/tests/__init__.py`, `accessibility/tests/test_middleware_access.py`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Preserve history, functional migration and baseline tests. Avoid: Foundation documents as implemented Company OS.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Sentrdel

**ADAPT_PATTERN → Trust/governance.** Monotonic policy/evidence constraints. Rust narrowing source sampled.

- Evidence: [main @ f5747319a50831ef7cee983d253c0ca5503c9a64](https://github.com/TheHalfMoon/Sentrdel/tree/f5747319a50831ef7cee983d253c0ca5503c9a64); public; 434 branches enumerated. Selected paths: `crates/sentrdel-policy/src/narrowing.rs`.
- Dependency/architecture evidence: `Cargo.toml`, `crates/sentrdel-cli/Cargo.toml`, `crates/sentrdel-engine/Cargo.toml`, `crates/sentrdel-graph/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `crates/sentrdel-cli/tests/r3_t015_graph_projection.rs`, `crates/sentrdel-cli/tests/r3_t016_scip_bridge.rs`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Constraints may tighten; unknown cannot weaken evidence. Avoid: Autonomous offensive scan workflow.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Signthos

**ADAPT_PATTERN → Documents.** Document identity admission. JavaScript provider code sampled.

- Evidence: [main @ f945f12fd1a2b600c2c61493162e3654b4d5b50c](https://github.com/TheHalfMoon/Signthos/tree/f945f12fd1a2b600c2c61493162e3654b4d5b50c); public; 292 branches enumerated. Selected paths: `packages/providers/src/content-identity-admission.js`.
- Dependency/architecture evidence: `package.json`, `packages/providers/package.json`, `tools/provenance/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `packages/providers/test/content-identity-admission.test.js`, `packages/providers/test/pdf-active-content-nonexecution.test.js`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Canonical original versus derivative identity and refusal outcomes. Avoid: Legal signature assurance without jurisdiction qualification.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/SpecGrain

**DEPENDENCY → Planning.** Specification lifecycle/readiness. Python stdlib core inspected and cloned.

- Evidence: [main @ 5de7d6499bb0a9e3a191fc0934399cf099d1980a](https://github.com/TheHalfMoon/SpecGrain/tree/5de7d6499bb0a9e3a191fc0934399cf099d1980a); public; 81 branches enumerated. Selected paths: README/root tree; no implementation file qualified.
- Dependency/architecture evidence: `pyproject.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `tests/test_adapter.py`, `tests/test_attempt.py`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Real SpecNode IDs/readiness/revision/work-packet semantics. Avoid: Fake future READY state or native executor claims.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Tarif

**ADAPT_PATTERN → Action contract.** Typed Action IR. Specification and active PR; design-stage evidence.

- Evidence: [main @ b1b3cecc7c2de32a4ecdba02a6bb752ae7a050c5](https://github.com/TheHalfMoon/Tarif/tree/b1b3cecc7c2de32a4ecdba02a6bb752ae7a050c5); public; 8 branches enumerated. Selected paths: `specs/002-action-ir-canonicalization/spec.md`.
- Dependency/architecture evidence: No build manifest in inspected default tree. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: No test path established by inventory. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Canonical argument distinction and request identity. Avoid: MCP/context visibility as authority.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Trcel

**REFERENCE_ONLY → Reference only.** Empty repository. No commits/branches/source.

- Evidence: [main @ EMPTY](https://github.com/TheHalfMoon/Trcel); public; 0 branches enumerated. Selected paths: README/root tree; no implementation file qualified.
- Dependency/architecture evidence: No build manifest in inspected default tree. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: No test path established by inventory. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: No reusable capability established. Avoid: Guessing intended product.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/wepld

**ADAPT_PATTERN → Governance.** Engineering OS architecture. Contracts/design with source tree.

- Evidence: [main @ 100d5c3c0049fd97e3a1e5d54c5cc9fcc6ca9bde](https://github.com/TheHalfMoon/wepld/tree/100d5c3c0049fd97e3a1e5d54c5cc9fcc6ca9bde); public; 343 branches enumerated. Selected paths: `docs/canonical/ARCHITECTURE_INVARIANTS.md`.
- Dependency/architecture evidence: `Cargo.toml`, `apps/desktop/src-tauri/Cargo.toml`, `crates/contracts/Cargo.toml`, `crates/core/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `crates/contracts/tests/project_v1.rs`, `crates/contracts/tests/protocol_v1.rs`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Findings/reviews never grant effects; no silent fallback. Avoid: Whole parallel engineering platform.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Winds

**ADAPT_PATTERN → Testing.** Independent exact-commit verification. Repository code/README/tree inspected.

- Evidence: [main @ ec214544d94d90b23fe4a0156d0040a2faf0622c](https://github.com/TheHalfMoon/Winds/tree/ec214544d94d90b23fe4a0156d0040a2faf0622c); public; 270 branches enumerated. Selected paths: README/root tree; no implementation file qualified.
- Dependency/architecture evidence: `Cargo.toml`, `desktop/package.json`, `desktop/src-tauri/Cargo.toml`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `desktop/tests/command-palette-model.test.mjs`, `desktop/tests/dependencies.test.mjs`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Detached revision-bound verification and inspectable checks. Avoid: Historical reports as current pass.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Wispral

**ADAPT_PATTERN → Voice.** Voice trust invariants. Canonical design inspected.

- Evidence: [main @ edacdf7504302cc91ff7138bc6ac2d391e4df1f4](https://github.com/TheHalfMoon/Wispral/tree/edacdf7504302cc91ff7138bc6ac2d391e4df1f4); public; 186 branches enumerated. Selected paths: `docs/canonical/ARCHITECTURE_INVARIANTS.md`.
- Dependency/architecture evidence: No build manifest in inspected default tree. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: No test path established by inventory. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Raw capture/transcript/intent/authorization separation. Avoid: Speech recognition as consent or authorization.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## TheHalfMoon/Zyara

**ADAPT_PATTERN → Kernel events.** Atomic events and tenant scoping. SQL migration sampled.

- Evidence: [main @ 151a8111c359523d8e30dd9899c0583ca24f8ea4](https://github.com/TheHalfMoon/Zyara/tree/151a8111c359523d8e30dd9899c0583ca24f8ea4); public; 77 branches enumerated. Selected paths: `db/migrations/004_durable_events.sql`.
- Dependency/architecture evidence: `apps/api/package.json`, `apps/web/package.json`, `apps/worker/package.json`, `experiments/search/package.json`. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: `tests/accessibility`, `tests/accessibility/foundation.test.ts`. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Outbox/inbox + explicit tenant-context patterns. Avoid: Copying destructive development rollback into production.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.

## wepld/wepld

**ADAPT_PATTERN → Governance.** Organization engineering contracts. Additional accessible org repository; design.

- Evidence: [main @ 993b2fb55af038091f365ad29d0740bdb1bd6c9e](https://github.com/wepld/wepld/tree/993b2fb55af038091f365ad29d0740bdb1bd6c9e); public; 9 branches enumerated. Selected paths: `docs/canonical/ARCHITECTURE_INVARIANTS.md`.
- Dependency/architecture evidence: No build manifest in inspected default tree. Exact transitive dependency qualification is deferred to any code intake; no donor stack is silently inherited.
- Test evidence: No test path established by inventory. Presence is not execution; no donor test results are adopted as Qdrat results.
- Reuse: Cross-repo artifact/review boundary ideas. Avoid: Duplicate of TheHalfMoon/wepld runtime.
- Security/upgrade boundary: translate the invariant into C01–C10 conformance tests; keep Qdrat authority and storage. Pin any later intake to this evidence or a separately reviewed update. If upstream disappears, keep the contract tests and replace the adapter; do not fetch unpinned code.
