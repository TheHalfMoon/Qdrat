# Qdrat — Execution Roadmap

The roadmap keeps Qdrat People as the first complete commercial-quality suite while deliberately building the shared Company OS kernel first. Gates are dependency-ordered; later breadth must not bypass earlier integrity, privacy, deployment or data-model gates.

## Gate 0 — Inherited baseline and provenance

- Preserve Horilla Git history, LGPL notices, and exact accepted upstream commits.
- Reproduce inherited development and production stacks without hidden internet assumptions.
- Run smoke/unit/coverage gates and record inherited failures without weakening them.
- Generate SBOM, dependency inventory, secret scan, vulnerability baseline and donor provenance registry.
- Inventory inherited modules, tables, endpoints, jobs, permissions and integrations.
- Produce signed/offline dependency caches or mirrors for deterministic builds.

Exit condition: Qdrat can reproduce, test, explain and update its inherited base.

## Gate 1 — Qdrat Kernel

- Establish Qdrat namespace, ADR process and stable internal package boundaries.
- Make PostgreSQL the supported production system of record.
- Introduce tenant/legal-entity context, correlation IDs and common error contracts.
- Define versioned APIs, domain events and transactional outbox.
- Centralize permission checks and business/security audit envelopes.
- Establish egress policy, local-only defaults and air-gapped profile.
- Build bilingual Arabic/English design system with RTL/LTR tests.
- Formalize backup/restore verification and migration safety.

Exit condition: Qdrat has a privacy-first platform kernel independent of legacy screen structure.

## Gate 2 — Object Platform and Qdrat Studio

- Define object type, field, relationship, view, action and lifecycle metadata contracts.
- Keep regulated/core objects relational and strongly typed; add typed custom fields safely.
- Add custom-object schemas with indexes, permissions, audit and retention metadata.
- Build reusable table/grid, form, kanban, calendar, timeline and relationship views.
- Generate versioned APIs and events for Studio-created objects.
- Add plugin/module manifests and stable UI/backend extension points.
- Add formula/derived field framework with deterministic execution and dependency tracking.

Exit condition: customers can extend Qdrat without source forks or parallel databases.

## Gate 3 — Company Graph and canonical People model

- Separate person, principal, worker, employment, contract, job and position.
- Add legal entities, organization units, locations, cost centers, teams, positions and vacancies.
- Add effective dating and point-in-time organization queries.
- Create typed relationship graph projection with edge provenance.
- Migrate inherited employee structures through explicit adapters and reconciliation reports.
- Build reusable object timelines and relationship views.

Exit condition: every later suite can refer to one stable company and workforce model.

## Gate 4 — Qdrat Flow and Qdrat Rules

- Define durable workflow model: triggers, conditions, actions, approvals, tasks, timers, SLAs, parallel branches and integration calls.
- Add execution history, retries, idempotency, compensation metadata, cancellation and version pinning.
- Introduce human work queues and approval inbox.
- Introduce a separate deterministic decision/rules contract.
- Qualify GoRules Zen/JDM as the leading permissive donor for rule execution/editor patterns.
- Require test fixtures, simulation and effective dates for regulated rules.
- Incrementally migrate inherited approval/automation logic to the common model.

Exit condition: business behavior is configurable, testable and auditable without customer-specific forks.

## Gate 5 — Files, documents, search and knowledge

- Build a single permission-aware file service with hashes, classification, retention and legal hold metadata.
- Add local structured document parsing and OCR pipeline.
- Add PDF conversion/processing adapters using qualified local components.
- Add policies, knowledge pages, records and acknowledgements.
- Implement lexical search first, then pluggable semantic and graph retrieval.
- Add deterministic graph extraction/provenance concepts inspired by Graphify.
- Add citations/source lineage to search and knowledge results.

Exit condition: company knowledge can be found and explained locally without bypassing source permissions.

## Gate 6 — Qdrat AI runtime

- Add local model registry/router with Ollama/llama.cpp-class adapters.
- Add tool registry with typed schemas, permissions, risk tiers, dry-runs and approval requirements.
- Add context builder and permission-aware retrieval over structured data, search, vectors and graph traversal.
- Add agent execution trace, prompt/version registry, memory scopes and retention controls.
- Add evaluation datasets, regression gates and user-feedback loops before write-capable agents.
- Ship `Ask Qdrat` first for navigation, cited policy Q&A and read-only analytics.
- Add specialized People/Manager/HR/Recruiter/Payroll/Compliance/Service/Builder agents incrementally.

Exit condition: local AI is useful, measurable and governed rather than an unrestricted chatbot.

## Gate 7 — Complete Qdrat People

- Core employee/manager self-service and lifecycle transactions.
- Position/headcount management and workforce planning.
- Recruiting, interview plans, talent pools, offers and onboarding.
- Attendance, scheduling, overtime, leave and time allocation.
- Payroll, benefits, compensation, total rewards and payroll-to-finance contracts.
- Performance, goals, 1:1s, feedback, calibration and succession.
- Skills graph, career paths, learning, certifications, internal mobility and mentorship.
- Employee listening, recognition, communities and HR service/case management.
- Assets and joiner-mover-leaver triggers.

Exit condition: Qdrat People independently competes with full modern HCM suites while remaining private/local-first.

## Gate 8 — Qdrat Data and Analytics

- Canonical metric registry with ownership, lineage and privacy class.
- Native operational dashboards for every suite.
- Custom reports, cohorts, funnels, pivots and exports.
- Embedded advanced BI profile using Apache Superset or equivalent qualified component.
- Natural-language analytics with approved datasets/read-only queries and evaluation.
- Surveys and feedback framework with reusable targeting and anonymity controls.
- Privacy-first product/usage analytics for the local Qdrat instance; telemetry remains off by default and customer-controlled.

Exit condition: customers can answer operational and strategic questions without exporting data to a separate SaaS BI stack.

## Gate 9 — Qdrat Service, Work and Ops

- Unified internal/employee service catalog, cases, tickets, SLAs and knowledge-assisted resolution.
- Projects, tasks, issues, calendars, scheduling, comments and approvals using the same people/team model.
- Asset, device, license, facility, location and operational inventory modules.
- Events/registration and training-session logistics where business demand justifies them.
- Realtime notifications and collaboration primitives without cloning a full chat platform into the kernel.
- Optional integrations/isolated services for advanced chat/video collaboration.

Exit condition: common company operations no longer require parallel identity, workflow and audit systems.

## Gate 10 — Saudi Arabia and country-pack framework

- Arabic-first employment documents and Hijri/Gregorian date handling.
- Qiwa contract state/adaptor model and reconciliation.
- Nitaqat-oriented workforce compliance views based on verified source data.
- Mudad/Wage Protection adapters where officially available and authorized.
- GOSI-related payroll data and configurable statutory calculations using versioned effective rules.
- Saudi labor leave/time/overtime/end-of-service rules with fixtures and effective dating.
- PDPL privacy operations: inventories, purposes, retention, deletion/anonymization, breach workflow and transfer controls.
- Generalize all statutory logic into versioned country packs rather than Saudi-specific conditionals in core code.

Exit condition: Saudi organizations can run core people/payroll/compliance operations without shadow systems, and the same framework can add other jurisdictions.

## Gate 11 — Qdrat Trust and enterprise interoperability

- LDAP/AD, OIDC, SAML and SCIM adapters.
- Joiner-mover-leaver access workflows and entitlement recertification.
- Integration credential isolation and rotation interfaces.
- Fine-grained relationship/attribute policy extensions where native authorization reaches its boundary.
- HR Open Standards and hardened import/export mappings.
- OpenTelemetry traces/metrics/log contracts and local health/incident dashboards.
- Segregation-of-duties checks, break-glass process and evidence exports.

Exit condition: Qdrat can become an enterprise system of record without becoming an identity or secrets protocol implementation project.

## Gate 12 — Distribution and productization

- Accessibility, mobile/PWA, localization and performance qualification.
- Upgrade/migration compatibility suites and rollback procedures.
- Threat model, privacy impact templates, AI risk documentation and red-team/evaluation suites.
- Signed offline installer/update bundles, images, packages and model manifests.
- SBOM, provenance attestations, dependency/license policy and release evidence.
- `qdratctl` for install, preflight, migration, backup, restore verification, model management, diagnostics and upgrades.
- Administrator migration/import tooling and implementation diagnostics.

Exit condition: Qdrat is supportable as a product in connected, private-network and air-gapped environments.

## Gate 13 — Additional company suites

Only after the shared kernel and Qdrat People are stable:

- `Qdrat Finance`: expenses, purchasing, AP/AR, budgeting and accounting.
- deeper CRM/sales capabilities if market demand justifies replacing specialist CRM.
- marketing automation only if it can reuse Qdrat contacts, consent, events and workflow safely.
- advanced communications only where native collaboration produces clear customer value.

Exit condition: breadth is added because it removes real customer tool fragmentation, not because source code is available.

## Global gate

No phase is complete if it introduces a new source of truth for identities, companies, teams, permissions, workflows, files, search, audit or AI governance outside the Qdrat kernel without an explicit ADR explaining why the boundary is necessary.
