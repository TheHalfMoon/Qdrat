# Qudra Implementation Extension 2 — Data Workbench, Agent Workforce and Local Reasoning

Status: **IMPLEMENTATION-READY PLANNING EXTENSION**

This extension adds bounded child-work candidates derived from DBX, Paperclip and Synaplan research. It does not bypass the sealed canonical DAG or the first Qudra execution extension. Each item becomes a real SpecGrain child node only when its named parent contracts/gates are accepted at live repository truth.

## QD-F17 — Data Workbench and Schema Snapshot

Parent dependencies:
- G2-01 connector manifests/DataSources;
- G1 Trust/policy acceptance;
- G8-07 API/SDK conventions.

Deliver:
- source-family-specific workspaces;
- connection health/capability matrix;
- DataSchemaSnapshot;
- metadata search;
- ER/relationship view;
- schema diff baseline;
- permission-aware saved query metadata.

Acceptance:
- no second DataSource registry;
- source family capability matrix is explicit;
- credentials remain references;
- metadata search obeys object/field permissions;
- schema snapshot is digest-bound/rebuildable;
- unsupported operations fail explicitly;
- Arabic/English/RTL and keyboard journeys pass.

Risk: R2.

## QD-F18 — Governed Query, Transfer and Lineage

Parent dependencies:
- QD-F17;
- G2 data connection/import/reconciliation contracts;
- G3 Action/Run semantics;
- G4-03 Company Twin/provenance where lineage maps to company objects.

Deliver:
- DataQueryPlan;
- query-effect classifier;
- explain/preview;
- bounded query execution;
- field lineage;
- import/export/transfer Run;
- reconciliation ledger.

Acceptance:
- read/write class cannot be model-declared authority;
- write/DDL/admin operations obey policy/approval;
- row/time/result bounds enforced;
- transfers are resumable/idempotent;
- counts/checksums/rejected records reconcile;
- inferred lineage remains labeled/inexact;
- no raw credentials in prompts/logs/evidence.

Risk: R3.

## QD-F19 — Goal Graph and Agent Profile

Parent dependencies:
- G1 Principal/authorization contracts;
- G6 Work object contracts;
- QD-F01 DecisionCase where relevant.

Deliver:
- Goal Graph projection;
- AgentProfile over Principal;
- explicit role/supervisor/assignment records;
- goal ancestry context builder;
- agent pause/expiry state.

Acceptance:
- agent is not represented as legal employee status;
- goal ancestry cannot grant permission;
- assignments are tenant-scoped/versioned;
- revoked/expired agent cannot start new work;
- every material AgentRun links to its WorkItem/DecisionCase and business-purpose ancestry when available.

Risk: R2.

## QD-F20 — Atomic Work Lease and Duty Cycle

Parent dependencies:
- QD-F19;
- G3 durable Run/concurrency contracts;
- G6 Work assignment/dependency contracts.

Deliver:
- WorkLease;
- atomic claim/renew/release/takeover;
- stale-worker fencing;
- scheduled/event duty cycles;
- wakeup coalescing;
- pause/kill handling.

Acceptance:
- concurrent claim fixture yields one active exclusive lease;
- lost lease generation cannot commit side effects;
- wakeups do not duplicate work;
- catch-up policy is explicit;
- paused/revoked agent does not wake into execution;
- UNKNOWN_OUTCOME blocks automatic re-execution.

Risk: R3.

## QD-F21 — Agent Resource Budgets, Skills and Evaluation

Parent dependencies:
- QD-F19;
- QD-F20;
- QD-F02 Capability Graph;
- QD-F08 outcome/calibration store;
- G9-06 evaluation contracts.

Deliver:
- local resource budget policy;
- AgentSkill lifecycle;
- evaluation packs;
- outcome/performance views;
- skill/runtime provenance;
- warnings/throttle/hard-stop semantics.

Acceptance:
- budget accounting includes local compute/resource dimensions;
- budget exhaustion fails safely;
- skill version and evaluation pack bind every qualified run;
- no automatic skill/policy promotion from outcomes;
- secrets excluded from exported skills/templates;
- safety/outcome measures outrank raw throughput.

Risk: R2.

## QD-F22 — Agent Workforce UX and Portable Team Packs

Parent dependencies:
- QD-F19 through QD-F21;
- QD-F10 shared Qudra UX;
- G8 Studio/extension packaging.

Deliver:
- agent workforce dashboard;
- current work/goal/budget/skill/run status;
- pause/resume/terminate controls;
- portable team packs with secret scrubbing;
- manager/supervisor views.

Acceptance:
- no anthropomorphic People/employee record confusion;
- every management action uses normal authorization;
- team export contains no secret/tenant IDs unless explicitly portable;
- import collision handling and preview;
- mobile/responsive manager journey supported.

Risk: R2.

## QD-F23 — Local Reasoning Graph

Parent dependencies:
- QD-F04 Option Engine;
- QD-F11 Decision-to-Action compiler;
- QD-F16 durable operation boundary;
- G3 Flow boundary accepted.

Deliver:
- ReasoningGraph/ReasoningNode;
- dependency scheduler;
- bounded parallelism;
- progressive results;
- node provenance;
- cancellation/timeouts;
- zero-side-effect enforcement.

Acceptance:
- ReasoningGraph cannot directly call side-effecting business Actions;
- effect proposal compiles to CapabilityPlan;
- node dependency/order deterministic from graph revision;
- partial/failure state explicit;
- user can distinguish analysis progress from business execution;
- no second durable workflow authority.

Risk: R3.

## QD-F24 — Local Engine Router and Readiness Inventory

Parent dependencies:
- G9-01 local engine registry;
- QD-F03 typed decision adapters;
- QD-F13 Classification Fabric;
- QD-F15 Edge Runtime Profiles;
- G11-03 measured performance profiles.

Deliver:
- LocalEngineProfile;
- readiness/health inventory;
- smallest-qualified-engine router;
- task/node capability matching;
- capacity/context validation;
- routing evidence.

Acceptance:
- no remote fallback;
- only READY + DecisionType-qualified engine may be selected;
- model/runtime/tokenizer digests verified;
- context overflow detected before invocation;
- router decisions reproducible from recorded inputs/profile;
- quality threshold beats cheapest/fastest preference.

Risk: R2.

## QD-F25 — Optional Local Sidecars and Air-Gap Capability Lifecycle

Parent dependencies:
- QD-F24;
- G10-02 offline bundle;
- G10 install/upgrade/backup contracts;
- G9 local OCR/RAG/voice/sandbox capabilities as applicable.

Deliver:
- LocalServiceCapability;
- optional sidecar readiness/health;
- clean enable/disable lifecycle;
- capability registration/removal;
- air-gap manifest/checks;
- independently qualified upgrade/rollback where supported.

Acceptance:
- disabled sidecar leaves no false-positive UI/control;
- unrelated core features remain healthy;
- no runtime download in air-gap profile;
- model/service/image/plugin artifacts fully inventoried/digest-bound;
- network-disabled install/start/readiness test passes;
- sidecar removal invalidates only dependent capabilities.

Risk: R2.

## Cross-package architecture invariants

1. PostgreSQL/Qdrat domain contracts remain business authority.
2. Data Workbench does not bypass Data Fabric or Trust.
3. Agent roles do not become legal employment records.
4. Goal context does not grant permission.
5. Work leases prevent duplicate effects but do not replace Flow idempotency.
6. Reasoning Graph is analytical/ephemeral; Flow remains durable business orchestration.
7. Local Engine Router cannot select cloud providers.
8. Optional sidecars never become hidden mandatory dependencies.
9. Every imported donor path requires exact provenance and notices.
10. All new behavior remains disabled until parent gates and exact-revision qualification permit activation.

## Rollout order

Recommended refinement order after parents unlock:

```text
QD-F17
  -> QD-F18

QD-F19
  -> QD-F20
  -> QD-F21
  -> QD-F22

QD-F23
  -> QD-F24
  -> QD-F25
```

The branches are mostly independent but share Trust, Capability Fabric, Run/Evidence and release/offline contracts.
