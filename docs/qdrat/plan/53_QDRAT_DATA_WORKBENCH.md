# Qdrat Data Workbench

Status: **FOUNDER-DIRECTED IMPLEMENTATION PLAN**

Source inspiration: `t8y2/dbx` at `4269a61e2cf6c19afdcaba41fed1e57d6e5e3512` (Apache-2.0 + founder authorization).

Qdrat already has a Data Fabric. This plan adds the missing operator/user experience for inspecting, querying, understanding and moving data **without creating a second data authority**.

## 1. Product decision

Add a shared **Qdrat Data Workbench** for administrators, analysts, engineers and governed Qudra capabilities.

It must reuse:
- DataSource registry and authority modes;
- Qdrat identity/authorization;
- secret references and network policy;
- audit/evidence;
- Company Twin lineage/provenance;
- Action/Flow for effects.

It must not become an independent database-management authority.

## 2. Core surfaces

### Connection Catalog
One governed view over SQL, document, search, vector, graph, file/object and other Data Fabric sources.

Each source exposes a capability matrix rather than pretending every backend supports SQL.

### Source Workspace
The workspace depends on source family:
- relational: schemas/tables/views/routines/query;
- Mongo/document: collections/documents/indexes/aggregation;
- search: indexes/mappings/query;
- vector: collections/namespaces/metadata/search;
- graph: labels/types/relationships/traversal;
- files/object: folders/objects/metadata/preview;
- event systems: topics/streams/consumer metadata.

### Query Studio
A governed query/command interface with explicit effect class.

### Schema Explorer
Tables/fields/types/indexes/constraints/relationships, or equivalent metadata for non-relational sources.

### Data Search
Find schemas, tables, fields, indexes, collections and other objects across permitted DataSources.

### ER / Relationship View
Visualize database relationships and map them to Company Twin object types where configured.

### Schema Diff
Compare source snapshots/revisions and produce bounded migration/reconciliation proposals.

### Field Lineage
Track column/field origin, transformations, downstream materializations and linked Qdrat objects where lineage is known.

### Import / Export / Transfer
Governed CSV/Excel/SQL/object export and cross-source transfer jobs with checksums, row counts and reconciliation.

## 3. Query safety model

Every query or command declares a class:

```text
READ_ONLY
EXPLAIN_ONLY
TRANSACTION_PREVIEW
BOUNDED_WRITE
BULK_WRITE
DDL
MIGRATION
ADMINISTRATIVE
```

`READ_ONLY` is not inferred from natural-language intent; it is determined by the adapter/parser/driver contract where possible.

Sensitive classes require normal Qdrat policy/approval.

## 4. DataQueryPlan

```text
DataQueryPlan
  datasource_ref
  source_revision
  language_or_protocol
  statement_or_command
  parameters
  query_class
  expected_objects
  row_limit
  timeout
  transaction_mode
  network_path
  credential_ref
  explain_plan
  estimated_effects
  approval_requirement
  evidence_contract
```

A model may propose a DataQueryPlan. It may not bypass validation or execute raw database writes directly.

## 5. Qudra + data

Qudra can use the Workbench through typed capabilities such as:
- `data.schema.search`
- `data.query.read`
- `data.query.explain`
- `data.lineage.trace`
- `data.schema.diff`
- `data.transfer.preview`

Qudra must receive normalized typed results and provenance, not ambient database credentials.

## 6. Connection security

Required:
- credential references only;
- TLS policy;
- SSH/tunnel profile as a separate governed capability where required;
- allowed hosts/ports;
- read-only credentials preferred for read capabilities;
- connection test evidence;
- no secret in prompts/logs;
- connection health and last-qualified driver/version.

## 7. Schema snapshots

Capture a rebuildable `DataSchemaSnapshot`:

```text
DataSchemaSnapshot
  datasource_ref
  captured_at
  adapter_version
  objects[]
  relationships[]
  indexes[]
  capabilities[]
  digest
  warnings[]
```

Snapshots support search, diff, lineage, migration planning and Company Twin mapping.

## 8. Lineage

Field lineage must distinguish:
- declared lineage;
- parsed deterministic lineage;
- observed runtime lineage;
- inferred lineage.

Every inferred edge retains confidence and provenance and is never silently promoted to fact.

## 9. Transfers and migrations

A cross-source transfer is a Run, not a UI copy action.

Required evidence:
- source/destination revisions;
- mapping;
- type conversions;
- row/object counts;
- checksums/samples;
- rejected rows;
- idempotency key;
- resume cursor;
- final reconciliation.

## 10. MCP and API

DBX demonstrates the value of exposing data operations to agents. Qdrat may expose Workbench capabilities through existing SDK/MCP surfaces, but:
- MCP is an adapter, not authority;
- permission is evaluated by Qdrat;
- raw unrestricted SQL tools are not the default;
- every effect maps to a Qdrat capability/action class.

## 11. Performance and scale

Plan for:
- metadata pagination;
- lazy schema loading;
- bounded result sets;
- streaming export;
- cancellation;
- per-source timeouts;
- query history retention policy;
- large-schema search index as a rebuildable projection.

## 12. UX requirements

- source-family-specific workspace instead of one generic query box;
- clear read/write badge;
- current DataSource authority mode visible;
- explain/preview before sensitive writes;
- Arabic/English and RTL/LTR;
- keyboard-first query/editor workflows;
- saved views/queries contain no secrets.

## 13. Failure states

Explicit states include:
- SOURCE_UNREACHABLE
- AUTH_FAILED
- DRIVER_UNAVAILABLE
- UNSUPPORTED_OPERATION
- QUERY_REJECTED_BY_POLICY
- QUERY_TIMEOUT
- RESULT_TRUNCATED
- WRITE_APPROVAL_REQUIRED
- TRANSFER_PARTIAL
- RECONCILIATION_FAILED
- SCHEMA_CHANGED

## 14. Adoption boundaries

From DBX, selectively study/adapt:
- adapter/connection abstractions;
- source-specific workspaces;
- query/editor ergonomics;
- schema/database search;
- ER/schema diff/field-lineage patterns;
- import/export/transfer;
- tunnel/connection patterns;
- MCP/AI tool exposure patterns.

Do not import:
- a competing connection/permission authority;
- unrestricted host/global credentials;
- write operations that bypass Qdrat Action/approval;
- DBX-specific application state as canonical Qdrat Data Fabric state.

## 15. Parent-plan binding

Implementation work is pre-shaped as QD-F17 and QD-F18 in the extension plan. It remains dependency-bound to Data Fabric, Trust, API/SDK and Company Twin parents.
