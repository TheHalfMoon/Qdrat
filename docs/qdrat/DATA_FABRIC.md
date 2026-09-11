# Qdrat Data Fabric

## Objective

Qdrat must be able to become the operating layer for a company without requiring the company to abandon its existing databases, servers, storage systems, identity systems, event streams, internal applications, or data ownership model.

The design target is **bring your own infrastructure and bring your own data**. Qdrat runs where the customer chooses and connects to data where the customer chooses. Public cloud is optional. Customer-controlled infrastructure is the default assumption.

Qdrat must never interpret "connect to anything" as "copy everything into Qdrat". The platform uses explicit data-placement and synchronization modes so the customer can decide which system remains authoritative for each object and field.

## Data placement modes

Every connected source is registered with one of the following modes.

### `NATIVE`
Qdrat owns the authoritative record in its PostgreSQL system of record. This is the preferred mode for Qdrat-native company objects such as workflows, audit evidence, Studio metadata, agent traces, and new Qdrat domain records.

### `LINKED_READ`
The external system remains authoritative. Qdrat queries approved data through a connector without persisting a full operational copy. Metadata, lineage, cache entries, indexes, or approved projections may be stored locally.

### `SYNCED`
The external system remains authoritative or co-authoritative, but selected records are synchronized into a Qdrat projection using scheduled jobs, incremental tokens, CDC, events, or vendor APIs. Conflict policy must be explicit.

### `MATERIALIZED`
Qdrat creates a local, permission-aware analytical/search projection from one or more sources. The projection is derived data, never silently promoted to the source of truth.

### `WRITE_THROUGH`
Qdrat is permitted to perform validated mutations in an external system through a versioned adapter. Write-through is disabled by default, requires stronger permissions than reads, produces audit evidence, and must define idempotency, retry, rollback/compensation, and conflict behavior.

## Universal connector contract

Qdrat does not hard-code vendors into domain modules. Every source implements a connector contract with declared capabilities.

A connector manifest declares:

- connector identity, version, vendor/protocol, and maintainer;
- supported source types and versions;
- authentication methods;
- required network destinations;
- read, write, schema-discovery, CDC, event, file, and health-check capabilities;
- transaction semantics and consistency limits;
- pagination/incremental cursor behavior;
- rate limits and execution budgets;
- schema/type mapping;
- data classifications requested;
- row/object/field filtering support;
- retry, idempotency, and conflict semantics;
- secret requirements;
- telemetry/egress behavior;
- offline/air-gap compatibility;
- license/provenance information;
- test fixtures and compatibility evidence.

The connector SDK must allow customers and partners to add a new database, application, protocol, or private service without modifying Qdrat core.

## Connector families

The architecture should support the following families through adapters rather than one giant abstraction.

### Relational databases

Priority adapters include PostgreSQL, MySQL/MariaDB, Microsoft SQL Server, and other SQL systems through mature drivers. Oracle and additional enterprise databases can be added through the same connector contract when certified.

Capabilities may include schema discovery, typed queries, read-only views, incremental keys, CDC where available, transaction-aware writes, and query explain/budget enforcement.

### Document and NoSQL stores

MongoDB-class document stores and other non-relational databases use native connector semantics. Qdrat must not force them into fake SQL assumptions; mapping happens into explicit Qdrat objects/projections.

### Search and vector systems

Elasticsearch/OpenSearch, Qdrant, pgvector, and other search/vector engines can be registered as external indexes or Qdrat-managed profiles. They are never the authoritative company system of record unless an explicit ADR states otherwise.

### Files and object storage

Local filesystems, network shares, S3-compatible object storage, MinIO-class systems, SFTP, and approved document stores connect through the Qdrat file contract. Objects retain source URI, checksum, classification, permissions, retention, and lineage.

### Event and message systems

Kafka/Redpanda-class streams, webhooks, queues, and future NATS/AMQP-class adapters can feed Qdrat events. External events must be normalized into versioned Qdrat event envelopes while preserving original payload references and source identity.

### APIs and internal services

REST/OpenAPI, GraphQL, SOAP where required, signed webhooks, private HTTP services, and custom RPC adapters connect through the integration fabric. Generated clients are version-pinned and wrapped behind Qdrat-owned interfaces.

### Identity and directory systems

LDAP, Active Directory, OIDC, SAML, SCIM, and identity-provider APIs connect through Qdrat Trust. Authentication and identity federation are distinct from business-object authorization.

### Email and collaboration

IMAP/SMTP, approved mail APIs, calendar protocols/APIs, chat systems, meeting systems, and notification providers connect through narrow adapters. Qdrat does not embed vendor-specific logic into People, Work, or Service modules.

### AI and tool protocols

Local model runtimes, model APIs explicitly enabled by administrators, MCP servers, and tool endpoints register through the governed AI/tool registry. Models never receive broader data access than the requesting principal and tool policy allow.

## Qdrat Source Registry

Every external system is registered as a first-class `DataSource` object containing:

- owner and business purpose;
- environment and network zone;
- connector/version;
- source authority mode;
- credentials reference;
- schemas/resources enabled;
- data classification;
- residency/jurisdiction;
- retention constraints;
- sync/index policy;
- health state;
- last successful access/sync;
- lineage edges;
- allowed agents/tools;
- approved read/write scopes;
- break-glass restrictions.

This registry is the control plane for data access. A connection string hidden in application settings is not sufficient governance.

## Canonical mapping and semantic layer

Qdrat needs one company model without pretending every external schema is identical.

The mapping layer supports:

- source object -> Qdrat object mapping;
- source field -> canonical field mapping;
- type conversion and validation;
- reference/entity resolution;
- effective-date mapping;
- code/value-set translation;
- unit/currency/time-zone normalization;
- confidence and review state for inferred mappings;
- bidirectional mapping only when write-through is explicitly enabled.

Mappings are versioned and testable. Changing a mapping must produce a diff, compatibility analysis, and migration/reprojection plan.

Above mappings, Qdrat exposes a semantic layer for business meaning: `Person`, `Worker`, `Customer`, `Vendor`, `Project`, `Asset`, `Invoice`, `Policy`, `Skill`, `Ticket`, and other canonical concepts. Analytics and AI should consume this layer when possible rather than vendor-specific tables.

## Query federation

Qdrat should support governed queries across native and connected data while avoiding a promise of magical zero-cost federation.

The query planner may choose among:

1. direct query against an approved source;
2. cached result;
3. synchronized projection;
4. materialized analytical dataset;
5. search index;
6. graph projection.

The planner must account for source latency, permissions, query cost, freshness requirements, network availability, privacy constraints, and source rate limits.

Cross-source queries should prefer materialized or explicitly modeled joins for critical workloads. Ad hoc distributed joins are bounded by time, row, memory, and cost budgets.

## Qdrat Bridge

For remote sites, segmented networks, private data centers, branch offices, factories, hospitals, or customer-controlled enclaves, Qdrat should support a lightweight `qdrat-bridge` connector runner.

Bridge properties:

- runs close to the protected data source;
- supports outbound-only control channels when required;
- can operate fully local with the main Qdrat deployment;
- executes signed connector jobs;
- stores secrets locally or retrieves them from an approved local secret provider;
- supports mTLS and certificate rotation;
- enforces source-specific allowlists and budgets;
- emits signed execution evidence;
- buffers approved events during temporary network loss;
- can be updated through signed offline bundles.

The bridge prevents the central product from requiring inbound access to every protected network.

## Privacy and security model

Connectivity must not weaken Qdrat's local/privacy thesis.

Default rules:

- connections are disabled until explicitly configured;
- reads are preferred over writes;
- minimum scopes and service accounts are required;
- network destinations are allowlisted;
- credentials are encrypted and referenced, not duplicated through business tables;
- connector execution is attributable to a principal/service identity;
- sensitive fields can be masked or excluded before indexing/AI use;
- source-level and Qdrat-level authorization both apply where possible;
- bulk export and cross-source joins use additional controls;
- every write-through action is audited;
- AI access is a separate opt-in capability from ordinary application access;
- no connector may enable hidden telemetry or external model calls.

## Data lineage

Every derived record, analytical metric, search result, graph edge, and AI answer should be traceable back to its material sources when technically possible.

Lineage records:

- source system and resource;
- source key/version/cursor;
- extraction timestamp;
- connector version;
- mapping version;
- transformation steps;
- destination projection/index;
- freshness;
- permission context where relevant;
- model/runtime identity for inferred transformations.

Lineage is not optional metadata for AI-generated conclusions; it is part of the trust model.

## Failure and conflict model

Connectors are unreliable by definition. The platform must represent rather than hide this reality.

Required states include `HEALTHY`, `DEGRADED`, `OFFLINE`, `AUTH_FAILED`, `SCHEMA_CHANGED`, `RATE_LIMITED`, `SYNC_LAGGING`, and `CONFLICTED`.

Sync/write operations use durable checkpoints, idempotency keys, retry policies, dead-letter evidence, and operator-visible reconciliation queues. Schema drift must stop unsafe mappings instead of silently dropping or coercing data.

## Deployment freedom

Qdrat must support customer-selected deployment shapes:

- developer/laptop profile;
- single-node server;
- on-prem VM/bare metal;
- Docker/Podman-style deployment;
- private cloud VMs;
- Kubernetes/OpenShift-class cluster when scale justifies it;
- disconnected/air-gapped installation;
- multi-site deployment using bridges and replicated/projection data where explicitly designed.

Qdrat should not require the customer to use a Qdrat-hosted control plane.

## Product promise

The correct promise is not "Qdrat magically supports every database on day one." The correct architecture promise is:

> Qdrat owns a stable, governed connector and data-fabric contract so any database, server, storage system, application, or private service can be integrated without changing Qdrat's company model or compromising privacy. Qdrat ships and certifies high-value connectors incrementally, while customers and partners can build additional adapters through the same SDK.

This makes infrastructure choice a customer decision rather than a Qdrat constraint.