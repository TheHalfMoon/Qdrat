# Qdrat — Local-First Architecture

## Architecture decision

Use Horilla 2.x as the inherited Django HR foundation and evolve it through a strangler-style migration. Do not perform a big-bang rewrite and do not merge complete donor applications into one repository architecture.

Build a Qdrat-owned Company OS kernel around stable domain, permission, event, workflow, object and AI contracts. `Qdrat People` is the first complete suite on that kernel. Existing Horilla capabilities remain usable until Qdrat replacements reach migration and regression gates.

See `CAPABILITY_ARCHITECTURE.md` for the detailed layers and `COMPANY_OS_STRATEGY.md` for suite boundaries.

## Default deployment topology

The baseline private deployment should require as few moving parts as possible:

- `qdrat-app`: Django domain services, APIs, compatibility screens and server-side product surfaces.
- `qdrat-worker`: background jobs, outbox delivery, indexing and workflow execution.
- `qdrat-ui`: incrementally introduced React/TypeScript PWA and shared design system; it can be served with the application in simpler profiles.
- PostgreSQL: authoritative transactional store, metadata store and baseline lexical/search capabilities.

Additional components are capability profiles, not universal requirements:

- Redis for cache/pub-sub/coordination when deployment scale or a selected capability requires it.
- local model runtime such as Ollama/llama.cpp when AI is enabled.
- Qdrant/OpenSearch-class retrieval service when PostgreSQL search/vector capabilities no longer meet the workload.
- Docling-class parser for advanced local document extraction.
- Gotenberg for document-to-PDF conversion.
- Apache Superset for advanced embedded BI.
- S3-compatible local object storage for larger/HA file deployments.
- enterprise identity provider such as Keycloak or customer-provided OIDC/SAML infrastructure.
- Temporal-class durable orchestration only after the native Qdrat Flow engine reaches a proven complexity boundary.

No component may require a public SaaS endpoint for the product to function. An air-gapped release profile is mandatory.

## Canonical company model

The shared model starts with Tenant, Legal Entity, Organization Unit, Team, Location, Cost Center, Person/Principal, Worker, Employment, Contract, Job, Position and Relationship.

Qdrat People extends it with Skill, Credential, Compensation, Benefit, Schedule, Time Entry, Absence, Candidate, Requisition, Goal, Review, Learning Item, Asset, Identity, Access Entitlement, Case and Policy.

Other suites reuse the same company objects and add Project, Task, Ticket, Customer, Vendor, Document, Knowledge Page, Event and other explicit types. Studio-created types extend the platform under the same permission, event, audit and search contracts.

Important state and organization changes are effective-dated. Strategic objects expose complete timelines and point-in-time query semantics.

## Strongly typed core + governed extensibility

Do not replace the core with an unrestricted EAV model. Regulated and integrity-sensitive domains remain normal relational models with explicit constraints and migrations.

Qdrat Studio adds typed custom fields and custom object definitions. Custom schemas declare fields, relationships, validation, lifecycle, indexes, permissions, search visibility, retention and event contracts.

## Event model

New Qdrat-owned domain mutations write a transactional outbox entry with correlation and causation metadata. Events become the stable integration seam for audit, notifications, workflows, indexing, analytics and future service extraction.

The event log is not a substitute for the relational source of truth. It is an immutable record of material changes and their context.

## Integration model

All new integrations use versioned interfaces rather than vendor logic inside domain modules.

Preferred patterns:
- REST/OpenAPI for synchronous APIs;
- signed webhooks with replay protection;
- transactional outbox/domain events;
- scheduled imports/exports;
- SCIM/OIDC/SAML for identity;
- standards mappings such as HR Open Standards;
- MCP only for explicitly approved AI tool integration.

Connector secrets are encrypted and isolated from ordinary business data.

## Workflow and rules

Qdrat Flow is event-driven and declarative. A flow may contain triggers, conditions, actions, approvals, parallel branches, timers, SLAs, escalations, human tasks, integration calls and agent-assisted steps. Runs are version-pinned and retain complete execution evidence.

Qdrat Rules is a separate deterministic decision layer. Rules are versioned, testable, simulatable, effective-dated and explainable. GoRules Zen/JDM is the leading permissive donor candidate for this layer after provenance/security qualification.

AI-generated mutations pass through the same authorization, workflow and approval controls as human actions.

## Search, graph and knowledge

PostgreSQL provides the initial structured and lexical search base. Vector and external search engines are adapters behind a Qdrat search contract.

The Qdrat Graph is a projection over authoritative objects, not a second source of truth. Graph edges carry provenance:

- `SYSTEM`: deterministically derived from authoritative data;
- `EXTRACTED`: parsed from a source document/configuration;
- `INFERRED`: generated by a model/heuristic with confidence and review metadata.

This applies Graphify/code-graph-RAG ideas to company objects, skills, policies, work, access and knowledge while preserving inspectability.

## AI architecture

The AI plane contains a model registry/router, instruction registry, tool registry, connector registry, context builder, retrieval router, agent executor, approval service, memory scopes, evaluation suites and trace store.

Retrieval is permission-aware: a record, document, chunk or graph edge is not exposed to a model if the requesting principal cannot access its source.

Every tool declares input/output schema, required permissions, data classification, risk tier, dry-run support, idempotency behavior, approval requirements and rollback/compensation semantics.

The system stores model/runtime identity, prompt/instruction version, inputs, sources, tool calls, approvals, outputs and final mutations.

## Security and privacy

- No telemetry or outbound network calls by default.
- Explicit egress allowlist and verifiable air-gap mode.
- Encryption in transit and deployment-level encryption at rest; field-level protection for designated high-sensitivity values.
- MFA and enterprise federation support.
- Record-, field-, legal-entity-, relationship-, purpose- and workflow-aware authorization.
- Immutable security/business/AI audit evidence.
- Break-glass access with reason, scope, expiry and elevated logging.
- Data retention, anonymization, deletion and legal-hold controls.
- Sensitive export controls and bulk-action safeguards.
- Encrypted backups plus automated restore verification.
- SBOM, dependency/license scanning, secret scanning and reproducible signed release artifacts.

## Frontend architecture

Existing Horilla views remain usable while Qdrat introduces one coherent design system and React/TypeScript surfaces for new interaction-heavy modules.

The long-term shell provides global navigation, command palette, universal search, object pages, activity timeline, inbox/notifications, common views and `Ask Qdrat`. Existing screens are removed only after replacement parity and migration tests pass.

Arabic/English and RTL/LTR behavior are test requirements, not post-release translation work.

## Service-splitting rule

Do not copy Huly's mature 30+ microservice topology into the default Qdrat installation. Split a capability from the modular monolith only when at least one of these is demonstrated:

- materially different scaling profile;
- failure isolation requirement;
- distinct runtime/language that provides clear value;
- stronger security boundary;
- independent lifecycle/release cadence;
- heavy processing that should not share application resources.

Even after a split, the capability remains behind Qdrat-owned contracts so the user experiences one product.
