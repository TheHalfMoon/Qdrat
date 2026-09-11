# Qdrat — Company Operating System Strategy

## Thesis

Qdrat should become the private, local-first operating system for a company, with Qdrat People as the first complete suite. The product wins by replacing fragmented SaaS categories with one coherent data model, one identity and permission system, one workflow/rules engine, one search and knowledge plane, one analytics model, one audit trail, and one governed AI runtime.

The goal is not to clone every listed product. The goal is to absorb the capabilities that companies repeatedly buy as separate tools and make them native modules on a shared kernel.

## Product hierarchy

### Qdrat Platform
The shared kernel every module uses: tenants/legal entities, identity, authorization, object model, relationships, events, workflow, rules, files, notifications, search, knowledge, analytics primitives, audit, localization, integration contracts, extension SDK, feature flags, AI tools, and deployment management.

### Qdrat People
Core HR, organization and position management, recruiting, onboarding, attendance, leave, payroll, benefits, compensation, performance, skills, learning, employee experience, workforce planning, succession, employee relations, HR service delivery, compliance, and country packs.

### Qdrat Work
Projects, tasks, issues, cycles, goals, calendars, scheduling, meetings, comments, approvals, docs, team spaces, and cross-functional work. It should reuse People identities, permissions, skills, teams, workload and cost data rather than create parallel user/team models.

### Qdrat Service
Employee service, IT service, HR cases, customer/internal tickets, SLAs, queues, knowledge-assisted responses, asset requests, incidents and service catalog workflows.

### Qdrat Knowledge
Policies, wiki, documents, records, OCR, semantic search, knowledge graph, collaborative pages, diagrams, retention, legal holds, acknowledgements, and governed RAG.

### Qdrat Data
Custom tables/objects, relational spreadsheet views, forms, dashboards, metrics, reports, surveys, event analytics, natural-language analytics and embedded advanced BI.

### Qdrat Ops
Assets, devices, software licenses, facilities, locations, fleets, maintenance, events, field work, health checks and operational inventories.

### Qdrat Trust
SSO/federation, MFA, SCIM, access lifecycle, integration credentials, secrets boundaries, audit, data governance, privacy controls, compliance evidence and AI governance.

### Qdrat Finance
A later suite for expenses, purchasing, invoices, budgets, payroll-to-GL and accounting. Qdrat People must expose clean finance contracts before Qdrat Finance is attempted.

## The unification moat

A company should never need to reconcile separate copies of the same fact. A person is one object whether viewed in HR, a project, a ticket, a document approval, an asset assignment or an analytics query. A department, location, cost center, customer, vendor, document, project and asset follow the same principle.

This creates a company digital twin that can answer questions other HR systems cannot answer safely and consistently, for example:

- Which critical projects depend on skills held by employees likely to leave?
- Which contractors still hold assets or application access after an engagement ended?
- What payroll cost is attached to a future org-design scenario?
- Which policies affect a proposed workflow change and who has not acknowledged them?
- Which service incidents correlate with a location, device type, team or onboarding cohort?

## One shell, not a suite of glued products

Every module must share:

1. Global navigation and command palette.
2. Universal search over permitted objects.
3. A common activity timeline and comments model.
4. Consistent object pages, tables, cards, kanban, calendar, timeline and graph views.
5. One notification and inbox model.
6. One workflow/rules builder.
7. One custom-field/custom-object system.
8. One report/dashboard system.
9. One permission vocabulary and audit trail.
10. One `Ask Qdrat` AI entry point that can delegate to specialized agents.

The user should experience Qdrat as one product even when some advanced capabilities run as isolated local services internally.

## Qdrat Studio

Qdrat Studio is a strategic differentiator, not an administrator afterthought. It lets an authorized customer create a new business object without writing code: schema, fields, relationships, validation, views, forms, permissions, lifecycle states, rules, workflows, notifications, reports and AI tools.

Core regulated domains remain strongly typed in code. Studio extends them instead of replacing relational integrity with an unrestricted EAV model. Custom fields use typed metadata and JSONB where appropriate; custom objects receive explicit schemas, indexes and permission policies.

Patterns to learn from Baserow, Grist, Corteza, Odoo and Strapi:

- metadata-driven records and views;
- extensible plugin/module manifests;
- generated APIs;
- formulas and derived values;
- form and app builders;
- reusable permission checks;
- migration/version semantics;
- safe extension points rather than source forks.

## Qdrat Flow and Qdrat Rules

Qdrat Flow handles durable business processes: triggers, conditions, human tasks, approvals, parallel branches, timers, SLAs, escalations, integrations and agent-assisted steps.

Qdrat Rules handles deterministic decisions separately from workflows. Use a versioned JSON decision model and testable decision tables/graphs inspired by GoRules. Rules must be explainable, diffable, simulatable and promotable between environments. AI may draft a rule but cannot silently activate or deploy it.

Examples include overtime eligibility, leave routing, probation rules, candidate screening criteria, payroll validations, expense policy, access approval and country-specific compliance calculations.

## Qdrat Graph

The platform maintains a typed relationship graph over company objects. The authoritative records remain in PostgreSQL; the graph is a projection/index optimized for traversal, explanation and AI context.

Graph edges carry provenance:

- `SYSTEM`: derived deterministically from authoritative relational data.
- `EXTRACTED`: parsed from a document, configuration or structured source.
- `INFERRED`: created by a model or heuristic and always carries confidence, source references and review status.

Graphify and code-graph-rag demonstrate two useful principles to reuse: deterministic local extraction before model inference, and graph traversal as a complement to vector retrieval rather than replacing all search with embeddings.

Qdrat maintains multiple connected graph spaces: company graph, skills graph, knowledge graph, workflow graph, access graph and optionally a code/configuration graph for administrators and developers.

## Qdrat AI

AI is a governed runtime across the platform, not a chatbot bolted onto each module.

Core services:

- local model registry and router;
- prompt/instruction registry with versions;
- tool registry with typed input/output schemas;
- permission-aware retrieval across SQL, full text, vectors and graph traversal;
- context builder that records sources and purpose;
- agent execution engine;
- human approval service;
- evaluation suites and regression datasets;
- trace/audit store;
- memory scopes with retention controls;
- MCP-compatible tool gateway for approved external/local tools.

Agents are role-specific views over the same capability plane: Employee, Manager, HR, Recruiter, Payroll, Compliance, Analytics, Service, IT/Ops, Knowledge and Builder agents.

Every high-impact tool declares its risk tier, required permissions, dry-run capability, idempotency, approval requirements and reversible/irreversible effects. AI-generated employment decisions remain recommendations unless an explicit governed workflow authorizes a human decision.

## Local-first deployment promise

Qdrat must be usable in four profiles without changing product semantics:

- `Lite`: one host, small organizations, minimal optional services.
- `Standard`: web/app workers, PostgreSQL, Redis, local search/vector service and local model runtime.
- `Enterprise`: HA database/storage, SSO, isolated workers, advanced BI/search, observability and backup targets.
- `Air-gapped`: signed offline images/packages/models, no network dependency during install or upgrade, explicit egress deny policy.

Cloud-hosted operation can exist later, but the local product cannot become a crippled edition.

## What Qdrat should not build itself

Being the only application a company needs does not mean reimplementing every infrastructure primitive. Prefer proven local dependencies behind stable adapters for PDF conversion, advanced BI, model inference, object storage, identity federation, email/SMS gateways and observability when that reduces risk.

The product moat is the unified model, workflow, UX, policy and AI control plane—not writing a new PDF renderer, SQL database, video codec or identity protocol implementation.

## Product discipline

Qdrat People must become excellent before breadth turns into distraction. Every new suite capability must pass three gates:

1. It reuses the Qdrat kernel rather than creating a parallel subsystem.
2. It removes a meaningful external tool or manual reconciliation step for customers.
3. It does not weaken local-first deployment, permission integrity or auditability.

This is how Qdrat can become a company's default system without becoming an unmaintainable collection of copied applications.
