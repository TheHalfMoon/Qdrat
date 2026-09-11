# Qdrat People — Execution Roadmap

## Gate 0 — Inherited baseline and provenance

- Preserve Horilla Git history, LGPL notices, and the exact accepted upstream commit.
- Establish upstream sync procedure and donor-license registry.
- Reproduce the inherited development and production stacks.
- Run smoke/unit/coverage gates and record inherited failures without weakening them.
- Generate initial SBOM, dependency inventory, secret scan, and vulnerability baseline.
- Inventory every inherited module, table, endpoint, background job, permission, and integration.

Exit condition: Qdrat can reproduce, test, and explain the inherited system before large functional changes begin.

## Gate 1 — Qdrat platform foundation

- Introduce Qdrat branding and design tokens without obscuring upstream provenance.
- Add canonical Qdrat module namespace and architecture decision records.
- Make PostgreSQL the supported production database and formalize backup/restore tests.
- Add explicit egress policy and `air-gapped` deployment profile.
- Establish bilingual Arabic/English design system and RTL test coverage.
- Harden role/record/field authorization and audit boundaries.
- Define versioned API, domain events, outbox, and integration contracts.

Exit condition: a privacy-first, reproducible Qdrat platform exists before feature expansion.

## Gate 2 — People graph and workforce structure

- Separate person, worker, employment, contract, job, and position concepts.
- Add effective dating and point-in-time organizational views.
- Add legal entities, org units, locations, cost centers, positions, vacancies, and headcount ownership.
- Build lifecycle event timeline and migration adapters from inherited records.
- Introduce configurable custom fields without bypassing authorization or audit.

Exit condition: all strategic modules can depend on a stable workforce model.

## Gate 3 — Workflow and service layer

- Build declarative workflow definitions, triggers, conditions, approvals, timers, SLAs, and escalations.
- Add execution history, replay/debug views, idempotency rules, and human tasks.
- Migrate lifecycle journeys, service requests, and approvals to the common workflow model incrementally.

Exit condition: HR operations are programmable without hard-coded per-customer forks.

## Gate 4 — Local AI and knowledge plane

- Integrate an optional local model runtime behind a provider-neutral model router.
- Add Qdrant-based semantic retrieval and permission-aware document indexing.
- Add local document parsing pipeline and provenance-preserving chunk metadata.
- Implement capability-scoped agent tools, dry-runs, approval gates, and immutable action traces.
- Ship `Ask Qdrat` for safe navigation, policy Q&A with citations, and read-only people analytics first.
- Add model/prompt/evaluation registries and regression tests before write-capable agents.

Exit condition: AI can answer and assist locally without silently leaking data or bypassing permissions.

## Gate 5 — Talent and skills operating system

- Skills graph seeded from qualified ESCO data with customer extensions and optional O*NET mappings.
- Skills evidence, proficiency, gaps, role profiles, career paths, internal mobility, mentorship, and succession.
- Modern recruiting, interview scorecards, talent pools, offers, referrals, and controlled AI assistance.
- Onboarding/crossboarding/offboarding journeys with knowledge, training, access, and assets.
- Performance, goals, feedback, calibration, learning, certification, employee listening, and recognition.

Exit condition: Qdrat manages both employment records and workforce capability.

## Gate 6 — Workforce planning, compensation, time, and payroll

- Headcount and workforce-cost scenarios aligned with Finance and Recruiting.
- Compensation bands, review cycles, budgets, pay equity, and total rewards.
- Scheduling, attendance, overtime, leave, time banks, project/cost-center time, and exceptions.
- Payroll simulation, validation, retroactivity, variable pay, payslips, payment files, and GL export.
- Country-pack rule framework with versioned effective dates.

Exit condition: operational and strategic workforce decisions share one data model.

## Gate 7 — Saudi Arabia country pack

- Arabic-first employment documents and Hijri/Gregorian date handling.
- Qiwa contract state/adaptor model and documented-contract reconciliation.
- Nitaqat-oriented workforce compliance views based on verified source data.
- Mudad/Wage Protection export/integration adapters where officially available and authorized.
- GOSI payroll data and configurable statutory contributions based on verified effective rules.
- Saudi labor-law leave/time/overtime/end-of-service rules with effective dating and test fixtures.
- PDPL privacy operations: data inventory, purpose/legal-basis records, retention, destruction/anonymization, processing records, breach workflow, and transfer controls.

Exit condition: Saudi customers can operate core HR/payroll/compliance workflows without shadow spreadsheets.

## Gate 8 — Identity, access, devices, and enterprise interoperability

- LDAP/AD, OIDC, SAML, and SCIM adapters.
- Joiner-mover-leaver access workflows and entitlement recertification.
- Local identity-provider integration and optional fine-grained authorization service.
- Asset/device lifecycle orchestration with pluggable MDM and inventory adapters.
- HR Open Standards mappings and hardened import/export contracts.

Exit condition: employment changes can safely drive the operational access lifecycle.

## Gate 9 — Productization and release readiness

- Accessibility, mobile/PWA, localization, performance, upgrade, and migration suites.
- Threat model, privacy impact templates, AI risk documentation, red-team/evaluation suites, and disaster recovery.
- Offline installer/update bundle, signed artifacts, SBOM, provenance attestations, and upgrade rollback.
- Administrator migration/import tooling and implementation diagnostics.

Exit condition: Qdrat People is deployable and supportable as an enterprise product, not only a development repository.
