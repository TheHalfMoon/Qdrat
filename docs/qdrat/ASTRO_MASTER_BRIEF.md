# Qdrat — Astro Master Planning Brief

## Purpose

This document is the canonical handoff to Astro for building the implementation plan for Qdrat.

Astro must treat the repository as the source of truth. This brief is intentionally self-contained at the strategic level, but the linked canonical documents contain the detailed product, architecture, source, authorization, UX, provenance, and roadmap evidence that must constrain the plan.

The requested output from Astro is not a generic SaaS roadmap. It must be an executable, dependency-ordered engineering and product plan for building Qdrat from the current repository state.

## Founder goal

Build **the best software for companies**: one private, local-first operating system in which a company can run essentially everything it needs without being forced into a collection of disconnected SaaS products.

The desired end state is:

> Everything the company needs is available through one Qdrat experience, one governed company model, one permission system, one automation layer, one knowledge/search plane, one audit/evidence system, and one AI runtime — while the customer remains free to use its own databases, servers, storage, models, networks, and existing applications.

Qdrat must be usable by a small company on a single server and remain architecturally capable of growing into a large enterprise deployment. It must not require a Qdrat-hosted cloud control plane.

## Competitive ambition

Qdrat must be planned as a simpler private functional superset of the valuable jobs currently spread across Jira/Jira Service Management, Zendesk/Intercom-class customer service, ServiceNow-class enterprise service management, modern work/project tools, collaboration, knowledge, internal tools, analytics and agent automation.

Read `COMPETITIVE_SUPERSET.md` as a product requirement, not marketing copy. The plan must identify which capabilities are required to reach parity, which Qdrat-native unifications make the product materially better, and which legacy competitor features should intentionally not be copied because they add configuration tax without proportional value.

Read `SOURCE_EXPANSION.md` together with `SOURCE_AUTHORIZATIONS.md`. The first contains newly discovered public sources; the second records founder-supplied sources and standing authorization. Astro must evaluate both landscapes and produce one donor/intake map while preserving the difference in provenance class.

## Product category

Qdrat is not merely:

- HR software;
- ERP;
- CRM;
- a low-code platform;
- a project manager;
- a helpdesk;
- a BI tool;
- a document system;
- an AI chatbot;
- an identity system.

Qdrat is a **private Company Operating System** that unifies these categories through shared primitives and adds native suites over time.

`Qdrat People` is the first complete suite because the repository already inherits the Horilla HR foundation and because people, organization, roles, reporting lines, skills, cost centers, positions, approvals, and lifecycle changes are foundational company concepts.

The platform must be designed so People is the first proof of the kernel, not an architectural trap that makes every future suite look like an HR plugin.

## Strategic model: Connect, Understand, Govern, Automate, Replace

Trying to replace every company system on day one would fail. Qdrat should expand through five stages that can coexist per capability.

### 1. Connect

Connect to the customer's existing databases, servers, storage systems, APIs, identity systems, event streams, files, applications, models, and internal services.

### 2. Understand

Map connected data into a canonical company semantic model and Company Graph without pretending that all sources share one schema.

### 3. Govern

Apply Qdrat permissions, classifications, lineage, audit, retention, egress controls, policy, and AI visibility rules.

### 4. Automate

Use Qdrat Flow, Rules, agents, events, approvals, and tools to coordinate work across both Qdrat-native and external systems.

### 5. Replace where valuable

When a native Qdrat module is mature enough, a customer may replace a fragmented external product. Replacement is optional; connection and governance remain valid long-term modes.

This strategy is essential to the goal of becoming the company's primary operating layer without requiring a dangerous big-bang migration.

## Non-negotiable product laws

Astro must preserve these laws in the plan.

1. **Local-first by default.** Customer-controlled infrastructure is the baseline assumption.
2. **Privacy by architecture.** No hidden telemetry, hidden model calls, or hidden data egress.
3. **Infrastructure freedom.** Customers choose where Qdrat, databases, models, files, and supporting services run.
4. **Data freedom.** Qdrat can work with customer-owned systems without demanding that all operational data be copied into Qdrat.
5. **One company identity.** Do not create separate user/person/team models per suite.
6. **One authorization vocabulary.** UI hiding is never treated as security.
7. **One event/audit fabric.** Material actions must be attributable and inspectable.
8. **One workflow/rules model.** Suites reuse Qdrat Flow and Rules instead of inventing local automation engines.
9. **One knowledge/search plane.** Permissions must survive indexing and AI retrieval.
10. **One governed AI runtime.** Agents are capability-scoped users of Qdrat, not privileged bypasses.
11. **Strong core, flexible edge.** Regulated/core objects remain strongly typed; Qdrat Studio handles governed extension.
12. **Effective dating and history.** The company can answer what was true, what is true, and what is planned to become true.
13. **Arabic and English first-class.** RTL/LTR cannot be a late localization retrofit.
14. **Air-gap is real.** A disconnected deployment must install, operate, update, back up, restore, search, and use enabled local AI without internet dependency.
15. **Modular monolith first.** Services split only for real runtime, scale, isolation, or security reasons.
16. **Evidence over claims.** No phase is complete because a document says it is complete.
17. **No donor-driven architecture.** Source availability never decides the Qdrat domain model.
18. **Standing founder authority.** Routine source-use and implementation permissions must not be re-requested. See `FOUNDER_AUTHORITY.md` and `SOURCE_AUTHORIZATIONS.md`.

## The Qdrat moat

The moat is not "more features" by itself.

### 1. Company Digital Twin

Qdrat models the company as connected typed objects: people, legal entities, organization units, positions, jobs, teams, skills, projects, customers, vendors, assets, locations, policies, documents, tickets, contracts, access entitlements, invoices, workflows, events, and future custom objects.

The transactional source remains relational where appropriate. A graph projection makes relationships traversable and explainable.

This enables questions and automations that fragmented products struggle to answer safely, such as:

- Which critical projects depend on skills concentrated in employees with succession risk?
- Which former workers still have devices, credentials, application access, or unresolved obligations?
- Which policies, contracts, and regulations affect a proposed organizational change?
- Which service incidents correlate with a location, device class, onboarding cohort, vendor, or team?
- What is the projected people and operating cost of a future company structure?
- Which customer commitments are at risk because of staffing, asset, vendor, or project dependencies?

### 2. Qdrat Studio

Authorized customers create governed business objects, fields, relations, forms, views, formulas, lifecycle states, permissions, workflows, rules, reports, dashboards, APIs, and AI tools without forking Qdrat.

Examples: `Vehicle`, `Clinic`, `Branch`, `Permit`, `Grant`, `Research Study`, `Machine`, `Property`, `Franchise`, `Training Cohort`, `Vendor Qualification`, or a company-specific process object.

Studio must not replace strongly typed regulated domains with an unrestricted EAV database.

### 3. Qdrat Data Fabric

Qdrat connects to existing infrastructure using explicit `NATIVE`, `LINKED_READ`, `SYNCED`, `MATERIALIZED`, and `WRITE_THROUGH` modes.

The platform owns a connector SDK, source registry, schema discovery, mapping, lineage, sync/CDC, health, conflict, policy, and execution model. See `DATA_FABRIC.md`.

The goal is architectural universality, not a false claim that every database and protocol ships on day one.

### 4. Qdrat Flow + Qdrat Rules

Flow manages durable processes. Rules manages deterministic decisions. Both are versioned, testable, auditable, effective-dated where needed, and reusable by every suite.

### 5. Governed local AI

AI is not a chatbot bolted onto screens. Qdrat AI is a local-first model/tool/agent runtime with permission-aware context, typed tools, model registry, prompt/version registry, evaluation suites, approvals, traces, and source lineage.

Qdrat AI must also define two explicit subplanes:

- **Agent Execution Plane** — substrate-independent secure sandboxes for code/browser/GUI/file/tool execution, with network egress policy, credential brokering, resource/time budgets, artifact capture, trace correlation, approval gates and circuit breakers. OpenSandbox is a leading implementation candidate, not a mandatory permanent dependency.
- **Voice Plane** — local-first dictation, transcription, meeting capture, diarization where enabled, voice commands, transcript-to-knowledge ingestion, retention/redaction policy and offline model packs. OpenWhispr/OpenSuperWhisper are primary donor/reference candidates.

Multi-agent orchestration must use Qdrat principals and policy: supervisor/dispatcher, per-agent identities, scoped memory/mailboxes, task ledger, delegation, autonomy levels, approval queues and loop/cost controls. Munder Difflin is a strong pattern source.

### 6. One UX

A user should experience one product even if optional services run behind it. The UX centers on role-based Home, `My Work`, global search, command palette, common object pages, common timeline/comments, inbox/notifications, and `Ask Qdrat`.

## Product surface

The eventual horizontal product should support the following suites, all sharing the kernel.

### Qdrat Platform

Kernel, object model, Studio, permissions, events, audit, files, search, graph, Flow, Rules, notifications, integration fabric, extension SDK, feature flags, localization, country packs, AI runtime, deployment administration, and source/data governance.

### Qdrat People

Core HR, employee/manager self-service, org/position management, recruiting, onboarding/crossboarding/offboarding, time, scheduling, leave, payroll, benefits, compensation, performance, goals, skills, learning, succession, workforce planning, employee experience, employee relations, HR service delivery, compliance, assets/access lifecycle triggers, and country packs.

### Qdrat Work

Projects, programs, tasks, issues, cycles, milestones, dependencies, calendars, resource planning, meetings, comments, approvals, workspaces, goals, portfolio views, workload, project cost allocation, and cross-functional execution.

### Qdrat Service

Employee service, HR service, IT service, customer/internal cases, requests, tickets, incidents, queues, SLAs, escalation, service catalog, knowledge-assisted resolution, and workflow-driven fulfillment.

### Qdrat Knowledge

Wiki/pages, policies, document management, records, OCR/parsing, tagging, metadata, collaborative content, generated diagrams, search, retention, legal holds, acknowledgements, citations, semantic retrieval, and knowledge graph.

### Qdrat Data

Custom objects/tables, relational spreadsheet experiences, forms, surveys, dashboards, reports, metric registry, cohorts, funnels, pivots, operational analytics, embedded advanced BI, natural-language analytics, and governed analytical datasets.

### Qdrat Ops

Assets, devices, software licenses, facilities, locations, fleets, equipment, inventory-like operational records, maintenance, events, registrations, field operations, health checks, and operational service workflows.

### Qdrat Trust

Authentication, MFA, federation, SCIM, joiner/mover/leaver access, entitlement review, secrets/integration credentials boundaries, audit evidence, privacy operations, segregation of duties, data governance, risk/compliance evidence, and AI governance.

### Qdrat Sales / CRM

Later native capability: accounts, contacts, leads, opportunities, pipelines, activities, proposals, customer relationships, commitments, revenue operations, and customer lifecycle. Until mature, external CRM systems should connect through the Data Fabric.

### Qdrat Finance

Later native capability: expenses, purchasing, budgets, AP/AR, invoices, payments, payroll-to-GL, accounting, financial reporting, and controls. Until mature, finance systems should connect through contracts and canonical mappings.

### Qdrat Procurement and Vendor Operations

Requests, approvals, sourcing, vendors, qualifications, contracts, purchase workflows, renewals, supplier evidence, and spend linkage. Some capability may begin inside Ops/Finance before becoming a dedicated suite.

### Industry Packs

Healthcare, professional services, construction, retail, manufacturing, education, public sector, hospitality, nonprofit, and other verticals should be built as combinations of Studio schemas, workflows, rules, reports, integrations, country packs, and selected native modules — not as unrelated forks.

## Universal infrastructure model

Qdrat must support customers that want different operational topologies.

### Deployment profiles

- developer/laptop;
- single server;
- on-prem VM or bare metal;
- Docker/Podman-class containers;
- private cloud VMs;
- Kubernetes/OpenShift-class clusters when justified;
- disconnected/air-gapped environments;
- multi-site environments connected by controlled bridges.

### Default runtime philosophy

Keep the minimum required stack small. A normal Qdrat deployment should not require dozens of services.

Baseline target:

- Qdrat application/web;
- Qdrat worker;
- PostgreSQL;
- local filesystem or configured object storage;
- optional Redis when a use case justifies it;
- optional local AI runtime when AI is enabled.

Advanced search, vector retrieval, BI, PDF/document services, identity providers, workflow engines, observability systems, and other components are capability profiles or sidecars rather than mandatory dependencies.

### qdratctl

A first-class CLI should manage install, preflight, configuration, secrets references, start/stop/status, migrations, backup, restore verification, connector checks, model installation, offline bundles, diagnostics, support evidence, upgrade, rollback, SBOM/license reports, and egress checks.

## Data Fabric architecture

Astro must treat `DATA_FABRIC.md` as a core platform specification.

The connector system must support database/server independence through a stable adapter contract.

Priority source families:

- PostgreSQL;
- MySQL/MariaDB;
- Microsoft SQL Server;
- later Oracle and other enterprise SQL systems;
- MongoDB/document stores;
- Elasticsearch/OpenSearch;
- Qdrant/pgvector/vector engines;
- local/network files;
- S3-compatible object storage;
- SFTP;
- REST/OpenAPI;
- GraphQL;
- SOAP where legacy demand requires it;
- webhooks;
- Kafka/Redpanda-class event streams;
- LDAP/Active Directory;
- OIDC/SAML/SCIM;
- IMAP/SMTP and calendar/mail adapters;
- MCP and approved AI/tool endpoints;
- customer-built private connectors through the SDK.

### Qdrat Bridge

A lightweight bridge/runner should allow Qdrat to connect to protected remote networks and sites without requiring broad inbound access. It should support signed jobs, mTLS, local secret handling, network allowlists, execution budgets, buffering, and offline update bundles.

## Data authority model

Astro must not design Qdrat as a giant replication warehouse.

For each object/field, the source authority must be explicit. Qdrat may be the system of record, an operational projection, a search/analytics projection, or a governed client of an external authoritative system.

Cross-source analytics and AI should prefer canonical mappings and materialized datasets for repeatable critical workloads. Unbounded distributed joins are not an acceptable architecture.

## AI architecture

### Model freedom

Qdrat must allow customer-selected model runtimes where qualified. Local models are the default privacy posture; an administrator may explicitly enable remote providers.

### Retrieval order

Prefer deterministic evidence before model inference:

1. structured lookup;
2. deterministic relationship/graph traversal;
3. lexical search;
4. approved analytical query;
5. vector/hybrid retrieval;
6. model inference.

### Tool safety

Every agent tool declares input/output schema, permissions, classifications touched, read/write scope, risk tier, dry-run behavior, approval requirement, idempotency behavior, rollback/compensation semantics, allowed models/agents, and audit payload.

### Agent families

Employee, Manager, HR, Recruiter, Payroll, Compliance, Service, Analytics, Career Coach, Builder, Finance, Sales, Operations, Executive, and future industry-specific agents should all reuse the same governed runtime.

High-impact employment, legal, financial, security, or similarly consequential actions require explicit policy and human authorization appropriate to the risk.

## Security and privacy posture

Astro must plan security as platform architecture, not a final hardening sprint.

Required concepts include:

- deny-by-default network/egress model;
- connector scopes and service identities;
- encrypted credential references;
- MFA and federation;
- role/attribute/relationship/object/field authorization;
- purpose-aware access where appropriate;
- export controls and bulk-operation safeguards;
- append-only sensitive audit evidence;
- source-aware lineage;
- retention, deletion/anonymization, and legal hold;
- break-glass access with reason and enhanced logging;
- signed release artifacts;
- reproducible/offline dependency bundles;
- SBOM, provenance, dependency/license evidence;
- secret scanning and vulnerability management;
- backup encryption and automated restore verification;
- AI prompt/tool/model/trace governance;
- data classification inheritance into search, analytics, and AI contexts.

## Product UX doctrine

Do not build a menu containing fifty unrelated mini-apps.

Every major business object should use a common page grammar: header/identity, primary fields, actions, relationships, timeline/activity, files, comments, workflow state, permissions, analytics, and Ask Qdrat context.

Common views should be reusable across domains: table/grid, form, cards, kanban, calendar, timeline/Gantt, graph, dashboard, and report.

A user should have:

- one Home adapted to role;
- one `My Work` queue across approvals/tasks/cases/reviews/signatures/actions;
- one global search;
- one command palette;
- one inbox/notification model;
- one Ask Qdrat entry point;
- one preference/localization identity;
- one audit-visible account.

Admin complexity may be deep, but ordinary workflows should be simpler than the specialist products Qdrat replaces.

## Donor/source strategy

The founder has granted standing authorization for the supplied source landscape. Astro must not ask the founder to reconfirm ordinary source-use permission.

Canonical authorization: `SOURCE_AUTHORIZATIONS.md`.

Technical classification: `SOURCE_LANDSCAPE.md` and `DONOR_REGISTRY.md`.

Key source roles already identified include:

- Horilla: inherited HR functional base;
- Graphify + code-graph-rag: deterministic graph extraction, explained edges, graph retrieval patterns;
- Baserow + Grist + Corteza + Odoo + Strapi: object/platform/low-code/product extensibility patterns;
- GoRules Zen/JDM: deterministic rule execution and visual decision modeling;
- Apache Superset + Nao + Umami + PostHog patterns: analytics, metrics, evaluation, events;
- AnythingLLM + Onyx + OpenRAG: local/enterprise agent, connector, retrieval, and orchestration patterns;
- `chaitanyagiri/munder-difflin`: multi-agent supervisor, provider abstraction, terminal-agent lifecycle, mailboxes, durable task ledger, memory, approval queue and circuit-breaker patterns;
- `opensandbox-group/OpenSandbox`: secure execution plane for coding/GUI/tool agents with SDK/MCP contracts, runtime isolation, network policy and credential injection;
- `OpenWhispr/openwhispr` + `Starmel/OpenSuperWhisper`: local/private voice, dictation, transcription, meeting capture and native voice UX patterns;
- `jaredrhod/fullstack-agent`: persistent memory + voice + visual interaction + conversational installer/self-repair patterns; treat public AGPL posture and founder grant provenance explicitly;
- Cal.diy/Rallly: scheduling;
- Gotenberg + Stirling PDF + Paperless patterns + Kroki: document/PDF/records/diagram capabilities;
- Infisical: credentials/secrets platform patterns;
- ZITADEL/Keycloak-class architecture: identity/federation reference boundaries;
- Huly, Plane, Taiga: work/project/collaboration architecture and UX reference;
- Papercups, UVdesk, Peppermint, Chaskiq: service/support patterns;
- Snipe-IT: asset lifecycle reference;
- Bigcapital/Akaunting/Odoo: finance/accounting domain references;
- EspoCRM/Odoo: CRM reference;
- Mattermost/Element/MiroTalk/HumHub: communications/community reference;
- Flagsmith: feature rollout/configuration patterns;
- PostGIS: geospatial capability;
- Label Studio: human review/evaluation workflows;
- LocalStack: offline emulation/testing philosophy, not core dependency.

Astro must prefer capability extraction behind Qdrat contracts over whole-application merging.

## Source permissions and evidence

`FOUNDER_AUTHORITY.md` establishes standing project authority.

`SOURCE_AUTHORIZATIONS.md` records every supplied source as founder-authorized.

This authorization is not a reason to discard provenance. For code intake, the plan must require exact source repository, commit/tag, source path, destination path, observed notices/license conditions, modifications, review, tests, and removal/replacement strategy.

Source/license analysis determines **how** code enters Qdrat; it must not become a recurring permission question.

## Commercial/reference sources

Qdrat should learn from major HCM and company-software products without copying proprietary implementation or protected assets. Existing research includes BambooHR, Zoho People, Workday, Oracle HCM, SAP SuccessFactors, Rippling, Deel, Personio, HiBob, Factorial, and relevant standards/datasets/regulatory sources.

See `FEATURE_BENCHMARK.md` and `REFERENCE_SOURCES.md`.

## Standards and interoperability direction

The plan should preserve room for:

- HR Open Standards;
- SCIM;
- OIDC/OAuth2/SAML;
- OpenAPI;
- webhooks;
- MCP;
- OpenTelemetry;
- ESCO/O*NET-style skill taxonomies where qualified;
- SCORM/xAPI for learning when justified;
- common accounting/export contracts;
- standard calendar/email protocols where appropriate.

Do not implement standards merely because they exist. Prioritize standards that reduce customer integration cost and vendor lock-in.

## Saudi Arabia first-class launch advantage

Saudi Arabia should be a first-class country pack and product proving ground, not hard-coded into global core.

The plan should include Arabic/RTL, Hijri/Gregorian support, Saudi employment document needs, Qiwa integration/state mapping where officially available, Nitaqat-oriented views, Mudad/Wage Protection adapters where authorized/available, GOSI-related payroll data/rules, Saudi holidays, labor-rule effective dating, and PDPL privacy operations.

All statutory logic belongs in versioned/effective-dated country packs with source evidence and tests.

## Architecture sequencing

The existing roadmap defines Gates 0–13. Astro may refine unit granularity but must preserve dependency ordering and justify any gate movement.

Current frontier is **Gate 0 — Inherited baseline and provenance**.

Immediate units already defined:

1. `G0-01 Reproducible Dependencies`
2. `G0-02 Baseline Build`
3. `G0-03 Baseline Tests`
4. `G0-04 Supply-Chain Baseline`
5. `G0-05 System Inventory`
6. `G0-06 Gate Evidence`

The plan must not jump directly into copying donor code or building AI while the inherited base is not reproducibly built, tested, inventoried, and understood.

## Recommended product expansion sequence

Astro should use this strategic order unless repository evidence shows a better dependency sequence.

### Phase A — Trustworthy foundation

Reproducibility, supply chain, kernel boundaries, PostgreSQL, audit, authorization, events/outbox, egress controls, backup/restore, bilingual design system, qdratctl basics.

### Phase B — Extensibility foundation

Studio object contract, custom fields/objects, reusable views, module manifests, stable APIs/events, DataSource registry, connector SDK, first database/API/file connectors.

### Phase C — Company model

Canonical legal entity/org/location/cost center/person/principal/worker/employment/job/position/team/relationship models, effective dating, Company Graph projection, migration adapters.

### Phase D — Automation foundation

Flow, Rules, My Work, approval inbox, timers/SLA, integration actions, reconciliation, idempotency, simulation, execution evidence.

### Phase E — Knowledge and data

Files, records, policies, document parsing, search, semantic/graph retrieval, lineage, metrics, dashboards, analytical datasets, advanced BI profile.

### Phase F — Governed AI

Local model runtime, model registry, tool registry, context builder, evals, traces, Ask Qdrat read-only capabilities, then progressively write-capable agents.

### Phase G — Qdrat People excellence

Finish the first full commercial-quality suite and Saudi pack. Do not dilute execution before People proves the kernel in real workflows.

### Phase H — Horizontal expansion

Service, Work, Ops, Data depth, Trust depth; connect external CRM/finance first.

### Phase I — Native business-suite expansion

Finance, CRM/Sales, Procurement, and industry packs only after the platform and People are stable enough to prevent duplicated infrastructure.

## What Astro must produce

Astro's plan must be repository-ready and implementation-facing, not presentation prose.

Required deliverables:

### 1. Repository truth report

Reverify current branch, PR, head commit, inherited Horilla baseline, module structure, build/test commands, deployment files, database assumptions, CI, and current canonical documents.

### 2. Gap analysis

For each major platform objective, classify current state as `PRESENT`, `PARTIAL`, `MISSING`, `CONFLICT`, `UNKNOWN`, or `DEFERRED`, with repository evidence.

### 3. Target architecture

Produce the concrete package/module boundaries, data ownership boundaries, runtime topology, event model, permission boundaries, connector architecture, extension architecture, search/graph/AI boundaries, and deployment profiles.

### 4. Dependency-ordered implementation graph

Break the work into small executable units with explicit dependencies. Every unit must state scope, files/modules likely affected, acceptance criteria, tests/evidence required, and what becomes unblocked when complete.

### 5. Gate definitions

Refine Gates 0–13 with machine-verifiable or human-reviewable exit evidence. No vague "done" criteria.

### 6. Donor intake map

Map each authorized source capability to one of `COPY_COMPONENT`, `ADAPT_PATTERN`, `RUN_AS_SERVICE`, `DEPENDENCY`, `REFERENCE_ONLY`, or `REJECT`, with the target Qdrat boundary and provenance requirements.

### 7. Data connector plan

Define connector SDK v1, DataSource model, first certified connector set, Qdrat Bridge, mapping/lineage contracts, sync/checkpoint/conflict semantics, and connector conformance tests.

### 8. Migration plan

Show how inherited Horilla structures migrate or adapt into canonical Qdrat objects without a big-bang rewrite or data loss.

### 9. UX implementation plan

Translate `UX_NORTH_STAR.md` into shell/design-system/view/object-page milestones, Arabic/RTL requirements, accessibility gates, and progressive replacement strategy for inherited Horilla screens.

### 10. AI implementation and evaluation plan

Define model/provider abstraction, local runtime support, tool contract, retrieval hierarchy, permission enforcement, eval datasets, trace schema, risk tiers, approval semantics, and rollout from read-only to write-capable agents.

### 11. Security/privacy plan

Threat model workstream, egress controls, connector security, credential boundaries, audit, export controls, break-glass, backup/restore, supply chain, release signing, privacy operations, and AI-specific controls.

### 12. Test strategy

Unit, integration, contract, migration, permission, property/invariant, end-to-end, accessibility, RTL, performance, offline install, backup/restore, connector conformance, workflow determinism, rules, AI eval, and upgrade/rollback tests.

### 13. Release strategy

Define `dev`, `single-node`, `standard/private`, `enterprise`, and `air-gapped` deployment profiles; artifacts; signed offline bundles; SBOM/provenance; upgrade policy; compatibility policy; and diagnostics/support bundles.

### 14. Risk register

At minimum: scope explosion, donor coupling, license/provenance error, data-model instability, auth fragmentation, workflow fragmentation, performance, connector reliability, schema drift, AI data leakage, prompt/tool escalation, local-model resource constraints, upgrade complexity, country-rule drift, UX complexity, and operational burden.

### 15. Explicit non-goals by phase

Each phase must say what it intentionally does **not** build yet. This is required to protect the one-Qdrat vision from destroying execution focus.

## Planning quality bar

The plan is unacceptable if it:

- recommends a big-bang rewrite;
- creates microservices without evidence;
- makes cloud services mandatory;
- duplicates identity, permissions, workflow, audit, search, files, or AI governance across suites;
- assumes all customer data must migrate into Qdrat;
- treats AI as privileged or outside normal authorization;
- uses donor code as the domain model;
- proposes "support everything" without a connector SDK and certification strategy;
- hides licensing/provenance boundaries;
- ignores offline installation/update/backup/restore;
- ignores Arabic/RTL;
- delays security/privacy until the end;
- measures progress only by feature count;
- asks for routine founder permission already covered by standing authorization.

## Success definition

Qdrat succeeds when a company can choose it as the primary operating layer because it offers:

- one coherent place to operate the company;
- freedom to run on customer-selected infrastructure;
- freedom to keep and connect existing databases/systems;
- strong privacy and local operation;
- safe extension without source forks;
- unified automation and approvals;
- unified search/knowledge;
- governed local AI;
- rich native suites where replacement is valuable;
- strong integrations where replacement is unnecessary;
- trustworthy audit, provenance, and historical truth;
- deployment from a small private server through larger enterprise environments;
- a simpler user experience than the fragmented specialist stack it replaces.

The long-term competitive statement is:

> A company should not have to choose between owning its data and having world-class software. Qdrat should provide one private operating system for the company, while letting the company decide where every database, server, model, file, and integration lives.

## Canonical reading order for Astro

Before finalizing the plan, Astro must read these repository documents in order:

1. `docs/qdrat/README.md`
2. `docs/qdrat/FOUNDER_AUTHORITY.md`
3. `docs/qdrat/ASTRO_MASTER_BRIEF.md`
4. `docs/qdrat/MASTER_PLAN.md`
5. `docs/qdrat/COMPANY_OS_STRATEGY.md`
6. `docs/qdrat/CAPABILITY_ARCHITECTURE.md`
7. `docs/qdrat/DATA_FABRIC.md`
8. `docs/qdrat/ARCHITECTURE.md`
9. `docs/qdrat/UX_NORTH_STAR.md`
10. `docs/qdrat/EXECUTION_ROADMAP.md`
11. `docs/qdrat/SOURCE_AUTHORIZATIONS.md`
12. `docs/qdrat/SOURCE_LANDSCAPE.md`
13. `docs/qdrat/DONOR_REGISTRY.md`
14. `docs/qdrat/REFERENCE_SOURCES.md`
15. `docs/qdrat/FEATURE_BENCHMARK.md`
16. `docs/qdrat/UPSTREAM.md`
17. `docs/qdrat/BASELINE_STATUS.md`

After reading the documents, Astro must reverify live repository truth before relying on hashes, branch state, test state, CI, or implementation claims.