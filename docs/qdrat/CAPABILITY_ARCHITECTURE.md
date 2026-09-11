# Qdrat Capability Architecture

## Architectural objective

Qdrat must feel like one application while remaining internally modular. Start as a modular monolith around PostgreSQL, then split only capabilities that require different scaling, runtime, security or operational boundaries.

The architecture deliberately avoids copying the 30+ service topology of mature platforms such as Huly. Qdrat borrows the transaction/event/search/storage separation but keeps the default deployment small enough for a private customer installation.

## Layer 1 — Qdrat Kernel

The kernel owns concepts every suite must share.

### Tenant and organization foundation
- tenant/customer instance
- legal entity
- organization unit
- location
- cost center
- team
- person/principal
- role and relationship
- locale, calendar and country pack

### Identity and authorization
- local authentication
- MFA
- OIDC/SAML federation adapters
- SCIM provisioning
- role, attribute, relationship and object policies
- delegation and temporary elevation
- break-glass access
- field masking and export policy

Do not import an entire identity server into the monolith. Keep the current Qdrat/Horilla authentication path for baseline compatibility, build standards-based adapters, and allow isolated Keycloak/ZITADEL-class providers later.

### Object platform
Core regulated objects use explicit relational models. Qdrat Studio adds typed custom objects and extensions through metadata.

Each object type declares:
- schema and field types;
- relationships;
- indexes and uniqueness rules;
- lifecycle states;
- ownership and permission rules;
- event contracts;
- allowed views/actions;
- retention/privacy classification;
- searchable and AI-visible fields.

### Event ledger
Every material mutation produces an immutable domain event after the transaction commits through a transactional outbox.

Events power:
- audit timelines;
- notifications;
- workflow triggers;
- search/index projection;
- analytics/event streams;
- integration webhooks;
- AI context updates;
- future service extraction.

An event records actor, principal, tenant, object, before/after or semantic delta, correlation/causation IDs, request source, timestamp and policy decision evidence.

### Permission engine
Authorization is centralized at the capability boundary. UI hiding is never security.

Policies can reference:
- role;
- legal entity/company;
- organizational hierarchy;
- manager/reporting relationships;
- object ownership;
- employment relationship;
- data classification;
- purpose of access;
- workflow state;
- delegated authority;
- time-bound grants.

### Audit and evidence
Security audit, business audit and AI audit are separate logical streams with a common evidence envelope. Sensitive audit events are append-only and exportable.

## Layer 2 — Qdrat Studio

Patterns come from Baserow, Grist, Corteza, Odoo and Strapi, but Qdrat owns its schema contracts.

Studio contains:
- object/schema designer;
- form builder;
- table/grid view;
- kanban;
- calendar;
- timeline/Gantt where appropriate;
- graph/relationship view;
- dashboard/report builder;
- formula/derived fields;
- validation rules;
- lifecycle/status designer;
- permission editor;
- extension/plugin registry.

A custom object created in Studio automatically receives versioned APIs, audit, search hooks, workflow triggers and permission enforcement.

## Layer 3 — Qdrat Flow and Rules

### Flow
A durable process definition contains versioned nodes for trigger, condition, action, human approval, task, timer, SLA, parallel branch, integration call, notification and agent step.

Runtime requirements:
- idempotent step execution;
- retries/backoff;
- explicit compensation where possible;
- human wait states;
- complete execution history;
- version pinning for in-flight runs;
- dry run/simulation;
- replayable evidence;
- concurrency guards;
- safe cancellation.

Use the existing Horilla automation layer only as bootstrap. Introduce a Qdrat-owned process contract before adopting a heavier orchestrator. Temporal remains optional when native persistence/worker semantics become insufficient.

### Rules
GoRules Zen/JDM is the strongest permissive donor candidate for deterministic decisions. Keep decision logic separate from process orchestration.

A rule package contains:
- decision model;
- inputs/outputs schema;
- test fixtures;
- effective dates;
- jurisdiction/country scope;
- owner/approvers;
- version;
- release state;
- explanation output.

## Layer 4 — Data, Search and Graph

### PostgreSQL
PostgreSQL is authoritative. Prefer extensions over new infrastructure when practical:
- JSONB for bounded custom metadata;
- full-text search for baseline lexical retrieval;
- `ltree` or recursive relations for organization hierarchies;
- PostGIS for geofencing/location operations;
- pgvector where simple vector workloads are sufficient.

### Search abstraction
Expose one search contract with pluggable implementations. Start with PostgreSQL where possible. Qdrant/OpenSearch-class services are optional profiles for scale or advanced hybrid retrieval.

### Qdrat Graph
Build graph projections from events and authoritative records. Do not make a graph database the transactional source of truth.

Edge provenance follows `SYSTEM`, `EXTRACTED`, `INFERRED`. Inferred edges include confidence, model/runtime version, source references and review state.

Use Graphify patterns for deterministic extraction and explained graph edges. Use code-graph-rag patterns for graph traversal plus retrieval. Extend the idea from source code to company knowledge, policies, skills, access and work relationships.

## Layer 5 — Files, Documents and Knowledge

### File service
One Qdrat file contract handles uploads, ownership, object attachment, ACL checks, hashes, malware scanning hooks, retention class, legal hold and audit.

Storage adapters:
- local filesystem for Lite/dev;
- S3-compatible local object storage for Standard/Enterprise;
- customer-provided object storage where allowed.

### Document processing
Recommended boundaries:
- Docling-class parser for structured document extraction;
- Gotenberg for deterministic office/HTML-to-PDF conversion;
- selected Stirling PDF capabilities for merge/split/OCR/redaction where license-qualified;
- Kroki for generated diagrams;
- e-sign capability implemented natively or isolated behind a service contract after legal/security qualification.

Paperless-ngx is a domain reference for indexing, tagging and archival—not a code foundation under the current policy.

### Knowledge service
Knowledge consists of pages, policies, documents, records, discussions and structured objects. It exposes lexical search, semantic retrieval, graph neighborhood retrieval and citations through the same permission checks.

## Layer 6 — Analytics

### Native analytics
Every Qdrat suite ships operational dashboards that understand Qdrat semantics and permissions.

The metric layer defines:
- canonical metric name;
- SQL/semantic definition;
- dimensions;
- owner;
- sensitivity class;
- aggregation/privacy rules;
- refresh behavior;
- lineage/version.

### Advanced BI
Apache Superset is a strong Apache-2.0 candidate for an isolated advanced analytics workspace with Qdrat SSO, theme and dataset provisioning. Do not force ordinary HR users into Superset for normal reports.

### Analytics agent
Nao provides useful patterns: explicit context packages, agent evaluation, feedback and transparent sources. Qdrat Analytics Agent must execute only approved read queries/datasets and enforce aggregation/privacy policy.

## Layer 7 — Qdrat AI runtime

Patterns from AnythingLLM, Onyx and OpenRAG are useful, but Qdrat's agent runtime must be domain-governed rather than generic chat-first.

### Core components
- model registry;
- local inference adapter;
- embedding/reranking adapters;
- prompt/instruction registry;
- tool registry;
- connector registry;
- context builder;
- retrieval router;
- agent planner/executor;
- memory service;
- approval service;
- eval runner;
- trace store;
- cost/resource accounting even for local models.

### Tool contract
Every tool declares:
- JSON input/output schema;
- permissions;
- data classifications touched;
- risk tier;
- read/write scope;
- dry-run behavior;
- idempotency key support;
- human approval requirement;
- rollback/compensation semantics;
- audit payload;
- allowed models/agents.

### Retrieval hierarchy
Prefer deterministic evidence before generative inference:
1. direct structured lookup;
2. deterministic relationship traversal;
3. lexical/full-text search;
4. vector/hybrid retrieval;
5. model inference.

The answer records which tier supplied each material claim.

## Layer 8 — Product suites

All suites are modules on the kernel, not independent products with duplicated infrastructure.

- `people`: HR/HCM/payroll/talent/workforce planning.
- `work`: projects/tasks/calendars/team collaboration.
- `service`: cases/helpdesk/service catalog/SLAs.
- `knowledge`: docs/wiki/policies/records/search.
- `data`: custom objects/tables/forms/surveys/analytics.
- `ops`: assets/facilities/devices/events/field operations.
- `trust`: identity/access/compliance/credentials.
- `sales`: later CRM/accounts/leads/opportunities/customer lifecycle/revenue operations.
- `finance`: later accounting/purchasing/expenses/budgeting/AP/AR/payments/financial reporting.
- `procurement`: later sourcing/vendor/contract/purchase workflows, potentially beginning as shared Ops/Finance capability.
- `industry packs`: governed combinations of Studio schemas, rules, workflows, reports, connectors and selected native modules rather than repository forks.

## Layer 9 — Integration and Data Fabric

All integrations use versioned adapters, never vendor-specific logic scattered through domain code. `DATA_FABRIC.md` defines the canonical source-authority and connector model.

The platform supports explicit `NATIVE`, `LINKED_READ`, `SYNCED`, `MATERIALIZED`, and `WRITE_THROUGH` modes so external systems can remain authoritative where appropriate.

Core fabric components:
- first-class `DataSource` registry;
- connector manifest/SDK and conformance tests;
- schema/resource discovery;
- canonical mapping and versioned semantic mappings;
- sync/CDC checkpoints and reconciliation;
- lineage and freshness metadata;
- connector health and schema-drift states;
- read/write scopes and execution budgets;
- optional `qdrat-bridge` runner for remote or segmented networks.

Supported patterns and families include:
- PostgreSQL, MySQL/MariaDB, Microsoft SQL Server, and certified enterprise SQL adapters;
- document/NoSQL stores such as MongoDB-class systems;
- REST/OpenAPI, GraphQL, SOAP where legacy demand requires it, and private HTTP/RPC adapters;
- signed webhooks and event subscriptions;
- scheduled imports/exports and CDC where qualified;
- local/network files, S3-compatible storage, and SFTP;
- Kafka/Redpanda-class streams and future queue adapters;
- email/calendar ingestion;
- SCIM/OIDC/SAML/LDAP/Active Directory boundaries;
- MCP for explicitly approved AI tools;
- customer-built private connectors through the same SDK.

Connector secrets are encrypted and isolated from ordinary application data. Reads are preferred over writes; write-through requires explicit scope, idempotency, conflict, audit, and compensation semantics. Qdrat must never require all connected data to be copied into its own database.

## Layer 10 — Runtime and operations

### Default deployment
Keep required services small:
- Qdrat app/web;
- Qdrat worker;
- PostgreSQL;
- Redis only where justified;
- local model runtime only when AI is enabled.

Advanced components are profiles rather than hard requirements.

### qdratctl
A first-class administration CLI should own:
- install/bootstrap;
- preflight checks;
- start/stop/status;
- migrations;
- backup/restore/verify;
- offline bundle import;
- model install/verify;
- diagnostics/support bundle;
- upgrade/rollback;
- license/SBOM report;
- egress policy check;
- health checks.

### Offline release
A release is not air-gap ready until a fresh machine can install from signed local artifacts without contacting PyPI, npm, GitHub, model registries or container registries.

## Donor adoption rule

A donor is valuable only if it reduces risk or materially accelerates a Qdrat capability. Never inherit a foreign domain model merely because code is available. Prefer extracting algorithms/components behind Qdrat contracts over importing an entire application.
