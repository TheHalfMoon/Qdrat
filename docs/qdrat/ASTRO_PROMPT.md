# Qdrat — Astro Planning Prompt

Continue `TheHalfMoon/Qdrat` from exact live GitHub/repository truth.

You are the planning architect for Qdrat. Your task is to produce the canonical executable implementation plan for the entire product. Do not implement product runtime code yet. First build the plan to engineering-grade completeness.

## Primary objective

Qdrat must become the best private Company Operating System for companies: one coherent product through which a company can run essentially everything it needs, while retaining control of its own databases, servers, storage, models, networks, and existing applications.

Qdrat is local-first and privacy-first. Public cloud must never be required. Customers may deploy on a laptop, one server, on-prem infrastructure, private cloud, larger clusters, or air-gapped environments. Qdrat must connect to existing systems instead of requiring a big-bang migration.

The strategic expansion model is:

`CONNECT -> UNDERSTAND -> GOVERN -> AUTOMATE -> REPLACE WHERE VALUABLE`

`Qdrat People` is the first complete suite and market wedge, but the platform architecture must support the full Company OS vision without turning future suites into HR plugins.

## Mandatory authority

The founder has granted standing ordinary project authority and standing source-use authorization. Do not ask the founder to reconfirm routine approval or source permission.

Read:
- `docs/qdrat/FOUNDER_AUTHORITY.md`
- `docs/qdrat/SOURCE_AUTHORIZATIONS.md`

Source/license/provenance analysis determines the correct intake method and evidence; it does not reopen the founder-permission question.

## Mandatory first action

Reverify live repository truth before planning. Confirm at minimum:

- repository and default branch;
- current planning branch and PR state;
- exact branch/head/base SHAs;
- inherited Horilla baseline and provenance;
- working tree state if local access is available;
- build/test commands and CI configuration;
- current module/app structure;
- deployment/container files;
- database/runtime assumptions;
- existing canonical Qdrat documents.

Never trust stale hashes, previous summaries, or prior completion claims over live repository truth.

## Mandatory reading order

Read every document below before finalizing the plan:

1. `docs/qdrat/README.md`
2. `docs/qdrat/FOUNDER_AUTHORITY.md`
3. `docs/qdrat/ASTRO_MASTER_BRIEF.md`
4. `docs/qdrat/MASTER_PLAN.md`
5. `docs/qdrat/COMPANY_OS_STRATEGY.md`
6. `docs/qdrat/CAPABILITY_ARCHITECTURE.md`
7. `docs/qdrat/DATA_FABRIC.md`
8. `docs/qdrat/AUTOMATION_FABRIC.md`
9. `docs/qdrat/ARCHITECTURE.md`
10. `docs/qdrat/UX_NORTH_STAR.md`
11. `docs/qdrat/EXECUTION_ROADMAP.md`
12. `docs/qdrat/COMPETITIVE_SUPERSET.md`
13. `docs/qdrat/SOURCE_AUTHORIZATIONS.md`
14. `docs/qdrat/SOURCE_LANDSCAPE.md`
15. `docs/qdrat/SOURCE_EXPANSION.md`
16. `docs/qdrat/DONOR_REGISTRY.md`
17. `docs/qdrat/REFERENCE_SOURCES.md`
18. `docs/qdrat/FEATURE_BENCHMARK.md`
19. `docs/qdrat/UPSTREAM.md`
20. `docs/qdrat/BASELINE_STATUS.md`

Also inspect the actual inherited codebase, not only the planning documents.

## Architecture invariants

Your plan must preserve these invariants:

- local-first and air-gap capable;
- no hidden telemetry/model calls/data egress;
- bring-your-own infrastructure;
- bring-your-own data and existing systems;
- PostgreSQL authoritative for Qdrat-native transactional data;
- external systems may remain authoritative through explicit source modes;
- one identity/company model across suites;
- one authorization vocabulary;
- one event/audit fabric;
- one workflow/rules architecture;
- one file/knowledge/search plane;
- one governed AI runtime;
- strongly typed regulated/core objects plus governed Studio extensibility;
- effective-dated historical and future state;
- Arabic/English and RTL/LTR first-class;
- modular monolith first;
- no donor-driven domain model;
- no big-bang rewrite;
- no broad data replication requirement;
- evidence-based gates only.

## Data Fabric requirement

Treat `DATA_FABRIC.md` as a foundation specification, not a late integration appendix.

The plan must define:

- `DataSource` model;
- source-authority modes: `NATIVE`, `LINKED_READ`, `SYNCED`, `MATERIALIZED`, `WRITE_THROUGH`;
- connector manifest and SDK;
- connector conformance suite;
- schema/resource discovery;
- canonical mapping and semantic layer;
- lineage and freshness;
- sync/CDC checkpoints;
- conflict/reconciliation;
- schema drift handling;
- secrets/scopes/network policies;
- query/execution budgets;
- connector health model;
- `qdrat-bridge` for segmented/remote networks;
- first certified connector set;
- customer/partner private connector path.

Do not claim universal database support as an immediate feature. Design a universal connector architecture and a staged certification plan.

## Product scope to plan for

Plan the shared platform so it can eventually host:

- Qdrat Platform / Studio / Flow / Rules / Graph / Data Fabric / AI;
- Qdrat People;
- Qdrat Work;
- Qdrat Service;
- Qdrat Knowledge;
- Qdrat Data;
- Qdrat Ops;
- Qdrat Trust;
- later Qdrat Sales / CRM;
- later Qdrat Finance;
- later Procurement / Vendor Operations;
- industry packs assembled from shared primitives rather than forks.

Do not build every suite at once. The plan must protect execution focus while preserving the long-term architecture.

## Source landscape

Use the authorized source landscape strategically. Prefer capability extraction behind Qdrat-owned contracts over merging whole products.

You must produce a donor intake decision for each supplied source using one of:

- `COPY_COMPONENT`
- `ADAPT_PATTERN`
- `RUN_AS_SERVICE`
- `DEPENDENCY`
- `REFERENCE_ONLY`
- `REJECT`

For every non-reference intake, record target Qdrat boundary, exact source version/commit strategy, provenance requirements, license/notice handling, test strategy, upgrade strategy, and removal/replacement strategy.

For sources in `SOURCE_AUTHORIZATIONS.md`, preserve the standing founder-authorization provenance. For sources in `SOURCE_EXPANSION.md`, record them as discovered public sources and base intake on the exact observed public license/path. Never collapse these provenance classes.

The donor map must explicitly evaluate `BraaMohammed/bricks`, `clay.com`, `n8n-io/n8n`, `activepieces/activepieces`, `refly-ai/refly`, `Rheosoph/flow-like`, `livecontext-ai/livecontext-ce`, `raghav3600/Altclay` (OpenClay), `eigent-ai/eigent`, `block/buzz`, `chaitanyagiri/munder-difflin`, `jaredrhod/fullstack-agent`, `opensandbox-group/OpenSandbox`, `OpenWhispr/openwhispr`, `Starmel/OpenSuperWhisper`, `langflow-ai/openrag`, Chatwoot, LiveHelperChat, Kanboard, OpenProject, GLPI, NetBox, Backstage, Temporal, Flowable, Apache Camel, Debezium, Activepieces, Zulip, Keycloak, Frappe Framework, OpenFGA, OPA, OpenTelemetry Collector, Prometheus and other verified candidates in `SOURCE_EXPANSION.md`; none is automatically selected merely because it appears there.

## Required planning artifacts

Create a planning directory and produce these repository-ready artifacts:

- `docs/qdrat/plan/README.md` — planning index, current verified truth, plan version and assumptions.
- `docs/qdrat/plan/00_REPOSITORY_TRUTH.md` — exact live repository/build/CI/runtime truth.
- `docs/qdrat/plan/01_GAP_ANALYSIS.md` — `PRESENT`, `PARTIAL`, `MISSING`, `CONFLICT`, `UNKNOWN`, `DEFERRED` with evidence.
- `docs/qdrat/plan/02_TARGET_ARCHITECTURE.md` — concrete package/module/data/runtime boundaries.
- `docs/qdrat/plan/03_IMPLEMENTATION_GRAPH.md` — dependency-ordered executable work graph.
- `docs/qdrat/plan/04_GATE_PLAN.md` — refined Gates 0–13 with objective exit evidence.
- `docs/qdrat/plan/05_DONOR_INTAKE_MAP.md` — all authorized sources mapped to Qdrat boundaries.
- `docs/qdrat/plan/06_DATA_CONNECTOR_PLAN.md` — Data Fabric/connector SDK/Bridge/certification plan.
- `docs/qdrat/plan/07_MIGRATION_PLAN.md` — Horilla-to-Qdrat strangler migration and reconciliation strategy.
- `docs/qdrat/plan/08_UX_IMPLEMENTATION_PLAN.md` — shell/design system/views/object pages/RTL/accessibility migration.
- `docs/qdrat/plan/09_AI_IMPLEMENTATION_PLAN.md` — model/tool/retrieval/evals/traces/risk/approval rollout, including multi-agent supervisor/task-ledger/memory semantics, an Agent Execution Plane (sandbox/network/credential/resource policy), and a local-first Voice Plane (dictation/transcription/meetings/voice commands).
- `docs/qdrat/plan/10_SECURITY_PRIVACY_PLAN.md` — threat/privacy/egress/credentials/audit/supply-chain/AI security.
- `docs/qdrat/plan/11_TEST_STRATEGY.md` — unit through offline/upgrade/connector/AI evaluation coverage.
- `docs/qdrat/plan/12_RELEASE_STRATEGY.md` — deployment profiles, artifacts, offline bundles, upgrades, rollback, support evidence.
- `docs/qdrat/plan/13_RISK_REGISTER.md` — technical/product/operational/compliance/source risks and mitigations.
- `docs/qdrat/plan/14_PHASE_NON_GOALS.md` — explicit non-goals per phase to control scope.
- `docs/qdrat/plan/15_MASTER_EXECUTION_PLAN.md` — final integrated plan and recommended execution frontier.
- `docs/qdrat/plan/16_COMPETITIVE_PARITY_AND_SUPERSET.md` — competitor-by-competitor job map for Jira/JSM, Zendesk-class support, ServiceNow-class ITSM/ESM, collaboration, knowledge, workflow automation and Clay-class enrichment; mark `PARITY_REQUIRED`, `QDRAT_ADVANTAGE`, `CONNECT_FIRST`, or `INTENTIONAL_NON_GOAL`, with evidence and phase.
- `docs/qdrat/plan/17_AUTOMATION_FABRIC_PLAN.md` — typed Action/Connector/Skill/Run/Signal/Waterfall contracts, visual/text authoring, durable execution, HITL, app surfaces, connector ecosystem and local execution.
- `docs/qdrat/plan/18_ENRICHMENT_RESEARCH_PLAN.md` — object/table enrichment, provider waterfalls, web/browser research, provenance, confidence, budgets, signals, data-use/consent/suppression controls and CRM/Data Fabric synchronization.
- `docs/qdrat/plan/EXECUTION_GRAPH.yaml` — machine-readable units, dependencies, gates, acceptance evidence, and status vocabulary.

## Work-unit quality bar

Every implementation unit in the plan must include:

- stable ID;
- title;
- objective;
- dependencies;
- exact scope;
- likely repository paths/modules affected;
- interfaces/contracts introduced or changed;
- migration/data implications;
- security/privacy implications;
- donor/dependency implications;
- acceptance criteria;
- required tests/evidence;
- rollback/recovery considerations;
- what the unit unblocks;
- explicit non-goals.

Prefer small reviewable units over giant milestones.

## Current frontier

The current canonical execution frontier is Gate 0. Reverify before relying on this statement.

Expected immediate units are currently:

- `G0-01 Reproducible Dependencies`
- `G0-02 Baseline Build`
- `G0-03 Baseline Tests`
- `G0-04 Supply-Chain Baseline`
- `G0-05 System Inventory`
- `G0-06 Gate Evidence`

Do not jump into donor imports, AI implementation, or broad UI replacement before Gate 0 evidence is real.

## Planning rules

Do not:

- big-bang rewrite Horilla;
- invent microservices for organizational fashion;
- require public cloud;
- create parallel identities/permissions/workflow/audit/search/file/AI systems;
- force migration of every external dataset into Qdrat;
- assume arbitrary distributed queries are cheap or safe;
- give AI privileged access outside normal authorization;
- copy whole donor applications because permission exists;
- claim tests/CI/builds/benchmarks that were not run;
- mark gates complete based on prose;
- postpone privacy/security/localization/offline concerns until release;
- ask the founder for routine permission already granted.

## Final planning test

Before considering the plan complete, verify that it explains how Qdrat can realistically move from the current Horilla-derived codebase to a product where:

1. a small company can install it privately without a DevOps department;
2. an enterprise can connect existing databases and internal systems without surrendering data ownership;
3. a customer can run fully offline where required;
4. users experience one product rather than glued applications;
5. customers can extend the product without forks;
6. Qdrat can progressively replace fragmented software without demanding replacement on day one;
7. every important action, automation, AI answer, and data projection can be traced and governed;
8. future suites reuse the same platform primitives rather than rebuilding them.

Do not stop at high-level strategy. Produce the repository artifacts and a concrete dependency-ordered execution plan grounded in the actual codebase.
