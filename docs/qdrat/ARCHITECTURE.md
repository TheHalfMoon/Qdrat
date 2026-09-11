# Qdrat People — Local-First Architecture

## Architecture decision

Use Horilla 2.x as the inherited Django foundation and evolve it through a strangler-style migration. Do not perform a big-bang backend rewrite. Preserve working HR modules while introducing Qdrat-owned domain boundaries and APIs module by module.

## Deployment topology

A standard single-customer deployment consists of:

- `qdrat-web`: Django application, domain services, admin surfaces, APIs, and legacy-compatible screens.
- `qdrat-ui`: incrementally introduced React/TypeScript PWA for interaction-heavy Qdrat experiences.
- PostgreSQL: authoritative transactional and effective-dated people data.
- Redis: cache, coordination, and asynchronous-work support where required.
- Qdrant: local semantic index for permission-aware knowledge, skills, and retrieval use cases.
- Local model runtime: Ollama for convenient deployments and llama.cpp-compatible runtimes where tighter control is required.
- Docling: local parsing pipeline for policies, resumes, contracts, and other supported documents.
- Optional Keycloak: enterprise OIDC/SAML federation and identity brokering.
- Optional OpenFGA: relationship-based authorization when Django-native policy evaluation is insufficient.
- Optional Temporal: durable long-running workflows after the native automation layer reaches its complexity boundary.

No component requires a public SaaS endpoint. An air-gapped profile must be supported.

## Canonical domain model

The core data model separates Person, Worker, Employment, Contract, Job, Position, Organization Unit, Legal Entity, Location, Cost Center, Skill, Credential, Compensation, Benefit, Schedule, Time Entry, Absence, Candidate, Requisition, Goal, Review, Learning Item, Asset, Identity, Access Entitlement, Case, Policy, Workflow, and Agent Action.

Changes that affect employment or organizational structure are effective-dated. Important entities expose a complete timeline and point-in-time query semantics.

## Integration model

All new integrations should use versioned interfaces rather than vendor logic inside domain modules. Use REST/OpenAPI for synchronous APIs, an outbox/event layer for reliable domain events, signed webhooks where appropriate, import/export contracts, and standards mappings such as HR Open Standards and SCIM.

## Workflow model

Qdrat workflows are event-driven and declarative. A workflow may contain conditions, actions, approvals, parallel branches, timers, SLAs, escalations, human tasks, integration calls, and agent-assisted steps. Every run is replayable from an immutable execution record. AI-produced mutations require the same authorization checks as human actions.

## AI architecture

The AI plane contains a model registry, model router, prompt/template registry, tool/capability registry, retrieval layer, policy enforcement point, evaluation suite, and audit store. Retrieval is permission-aware: a document or chunk is never visible to the model if the requesting principal cannot access its source object.

Agent execution uses least privilege. Each tool declares input schema, required permissions, risk tier, dry-run support, idempotency behavior, and whether human approval is mandatory. The system stores model/runtime identity, inputs, referenced sources, tool calls, approvals, outputs, and final mutations.

## Security and privacy

- No telemetry or outbound network calls by default.
- Configurable egress allowlist with an air-gap mode.
- Encryption in transit and deployment-level encryption at rest; field-level protection for designated high-sensitivity values.
- MFA and enterprise federation support.
- Record-, field-, company-, legal-entity-, and relationship-aware authorization.
- Immutable security/audit events with exportable evidence.
- Break-glass access with explicit reason and elevated logging.
- Data retention, anonymization, deletion, and legal-hold controls.
- Sensitive export controls, watermarking options, and bulk-action safeguards.
- Encrypted backups plus automated restore verification.
- Software bill of materials, dependency scanning, secret scanning, and reproducible release artifacts.

## Frontend migration

Existing Horilla views remain usable while Qdrat introduces a coherent design system and React/TypeScript surfaces for new modules. APIs become the boundary. Existing screens are replaced only when the Qdrat version reaches feature parity and migration tests pass. Arabic/English and RTL/LTR behavior are tested as part of the design system.

## Service-splitting rule

Do not create microservices for organizational fashion. A module leaves the modular monolith only when it requires independent scaling, failure isolation, a distinct runtime/security boundary, or materially different release cadence.
