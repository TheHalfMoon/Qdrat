# Qdrat Canon

This directory is the canonical product, architecture, source-intake, authorization, reference-source, and execution record for Qdrat.

## Product definition

Qdrat is a private, local-first Company Operating System for the AI era. `Qdrat People` is the first complete suite and the initial market entry. The long-term goal is that essentially everything a company needs can be operated through one Qdrat experience while the customer remains free to choose its own databases, servers, storage, models and existing systems. The platform unifies people, work, service, knowledge, data, operations, trust, sales/CRM, finance, procurement and future industry capabilities on one company model, one identity and permission system, one workflow/rules layer, one integration/data fabric, one search/knowledge plane, one audit trail, and one governed AI runtime.

Qdrat is intentionally not a bundle of copied applications. External projects are sources of capabilities, implementation patterns, components, and isolated services. Qdrat owns the product model, contracts, UX, governance, and integration boundaries.

## Canonical documents

| Document | Authority |
|---|---|
| `MASTER_PLAN.md` | Product thesis, complete People/HCM scope, differentiators and Saudi-first direction |
| `COMPANY_OS_STRATEGY.md` | Company OS product hierarchy, unification moat, Studio, Graph, Flow/Rules and suite boundaries |
| `CAPABILITY_ARCHITECTURE.md` | Detailed platform capability architecture and subsystem boundaries |
| `DATA_FABRIC.md` | Bring-your-own database/server connector model, source authority, mapping, lineage and Qdrat Bridge |
| `AUTOMATION_FABRIC.md` | Shared typed execution substrate for Flow, Rules, connectors, skills, enrichment, provider waterfalls, signals, approvals and app surfaces |
| `ASTRO_MASTER_BRIEF.md` | Canonical planning handoff and required plan outputs for Astro |
| `ASTRO_PROMPT.md` | Ready-to-run Astro planning directive and required repository artifacts |
| `ARCHITECTURE.md` | Local-first deployment, canonical domain model, APIs/events, AI, security and service-splitting rules |
| `UX_NORTH_STAR.md` | Unified product shell, role-based home, My Work, search, command palette, object pages and Ask Qdrat |
| `EXECUTION_ROADMAP.md` | Dependency-ordered Gates 0–13 and exit conditions |
| `SOURCE_LANDSCAPE.md` | Technical classification of all researched source repositories and organizations |
| `SOURCE_EXPANSION.md` | Additional public source research closing Jira/Zendesk/ServiceNow/platform capability gaps |
| `COMPETITIVE_SUPERSET.md` | Canonical capability target for exceeding work, support, ITSM and collaboration competitors |
| `FOUNDER_AUTHORITY.md` | Standing founder execution authority and no-routine-permission directive |
| `SOURCE_AUTHORIZATIONS.md` | Standing founder authorization register for every supplied source-code repository/organization |
| `REFERENCE_SOURCES.md` | Commercial competitor, standards, dataset and official regulatory references with permission/use class |
| `DONOR_REGISTRY.md` | Qualified donor/dependency/reference registry and supply-chain gate |
| `UPSTREAM.md` | Horilla upstream/provenance synchronization policy |
| `BASELINE_STATUS.md` | Verified inherited baseline evidence and known gaps |
| `FEATURE_BENCHMARK.md` | Competitor capability benchmark and parity requirements |

## Non-negotiable product principles

1. Local-first and deployable on customer-controlled infrastructure without public cloud dependencies.
2. Air-gapped operation is a supported profile, not a marketing claim.
3. No telemetry, model calls, or data egress unless explicitly enabled by an authorized administrator.
4. PostgreSQL is the authoritative production system of record.
5. One canonical company graph/model prevents duplicate identities, teams, permissions, workflows, files and audit systems.
6. Core regulated domains remain strongly typed; Qdrat Studio extends the platform without weakening integrity.
7. Effective dating and point-in-time history are first-class.
8. AI is permission-aware, provenance-preserving, evaluated, auditable, dry-runnable, and human-governed for high-impact actions.
9. Arabic/English and RTL/LTR are first-class product requirements.
10. Start as a modular monolith. Split services only for justified scale, security, runtime or failure-isolation boundaries.
11. Donor code is never imported merely because it is available. Every copied file requires provenance and license/intake evidence.
12. Qdrat should reduce the number of separate systems a company needs, not recreate their fragmentation inside one repository.

## Platform hierarchy

- `Qdrat Platform`: kernel, object model, permissions, events, workflow, rules, files, search, graph, analytics primitives, audit, extension SDK, feature flags and AI runtime.
- `Qdrat People`: HR/HCM, workforce structure/planning, recruiting, journeys, time, payroll, rewards, performance, skills, learning, employee experience, HR service and country packs.
- `Qdrat Work`: projects, tasks, issues, cycles, calendars, meetings, docs and cross-functional work.
- `Qdrat Service`: internal/employee service, IT/HR cases, tickets, SLAs, service catalog and incidents.
- `Qdrat Knowledge`: wiki, policies, documents, records, OCR, retention, search, knowledge graph and governed RAG.
- `Qdrat Data`: custom objects/tables, relational spreadsheet views, forms, reports, dashboards, metrics, surveys and analytics agents.
- `Qdrat Ops`: assets, devices, licenses, facilities, locations, fleets, events and operational inventories.
- `Qdrat Trust`: identity/federation, SCIM, access lifecycle, audit, privacy, compliance evidence, secrets boundaries and AI governance.
- `Qdrat Finance`: later suite after People and the shared kernel are stable.

## Core differentiators

### Company Digital Twin
A typed company graph connects people, positions, skills, teams, projects, policies, documents, assets, access, locations, vendors, customers and workflows. Relationships carry provenance and support point-in-time reasoning.

### Qdrat Studio
Authorized administrators can define custom business objects, fields, relationships, forms, views, lifecycle states, permissions, formulas, workflows, reports and APIs without source forks.

### Qdrat Flow and Qdrat Rules
Durable processes are separated from deterministic decisions. Workflows handle tasks, approvals, timers, SLAs and integrations; rules remain versioned, testable, simulatable and explainable.

### Governed local AI
`Ask Qdrat` is the common entry point to specialized agents. The AI runtime uses local models by default, permission-aware context, SQL/full-text/vector/graph retrieval, typed tools, approval gates, evaluation suites and immutable traces. A governed Agent Execution Plane isolates code/browser/GUI/tool execution, while a local-first Voice Plane provides dictation, transcription, meeting capture and voice commands without requiring customer data to leave controlled infrastructure.

### One UX
Role-based Home, `My Work`, global search, command palette, common object pages, common notifications/inbox and Ask Qdrat make the platform feel like one product even when advanced capabilities run as local sidecars.

## Source-use policy

The founder has granted standing permission to copy, use, adapt, refactor and integrate the complete source code of the sources recorded in `SOURCE_AUTHORIZATIONS.md`. That authorization is recorded as `FOUNDER_STANDING_AUTHORIZATION` and must not be repeatedly questioned or re-requested during ordinary project execution. `FOUNDER_AUTHORITY.md` is the canonical execution directive.

Engineering intake remains controlled by `SOURCE_LANDSCAPE.md` and `DONOR_REGISTRY.md`. License, attribution, dependency, contributor, patent, trademark and path-specific analysis determines the correct intake method and provenance obligations; it does not reopen the founder-permission question. Preserve applicable notices and provenance in the intake record.

Commercial competitors, standards, public datasets, and government/regulatory sites are recorded separately in `REFERENCE_SOURCES.md` so product research is not confused with source-code authorization.

## Current repository baseline

Qdrat `main` was initialized from the Horilla 2.x source history at commit `e2d288940aab52af881786678b2fc86dfa5c272a`, preserving upstream provenance. The foundation work is carried on `foundation/qdrat-people-blueprint` through PR #1 until governance documents are accepted.

## Execution rule

Follow `EXECUTION_ROADMAP.md` in dependency order under the standing authority in `FOUNDER_AUTHORITY.md`. The default action is to continue: after an execution unit is evidenced, reverify repository truth and proceed automatically to the next executable dependency without asking for routine founder approval. Breadth does not override integrity gates. No phase is complete if it creates a competing source of truth for company identity, permissions, workflow, files, search, audit or AI governance without an explicit architecture decision explaining the exception.

Current frontier: `Gate 0 — Inherited baseline and provenance`.
