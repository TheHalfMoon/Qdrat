# Studio and company extensions

Owner: qdrat/studio. C09 is mandatory. Studio provides configurable objects, forms and views on the same policy/API/action substrate. It does not generate unmanaged application servers or bypass typed core tables.

ObjectDefinition pins namespace, owner, schema revision, field definitions, classification, relationships, validation, retention and lifecycle. CustomRecord uses tenant/type/revision with validated JSONB. Promote high-volume query fields through declared indexes; quotas prevent arbitrary index creation. Monetary/payroll/identity/ledger records remain typed domain models. Custom fields on core objects live in an extension table with explicit allowed field types and policy inheritance.

ViewDefinition supports grid/table, cards, board, calendar, timeline/Gantt, tree, graph, map and dashboard as projections of a permitted query. Kanban moves invoke a lifecycle action; they do not update status columns directly. Form submission creates a command and supports idempotent retry. Bulk changes preview the exact selected set and reauthorize each record at execution.

Formula dependencies are versioned and acyclic; deterministic chapter 11 expression semantics in 11 apply. No arbitrary SQL or code in a standard formula. Calendar and date fields store locale-independent values; bilingual labels and RTL layouts are versioned presentation metadata.

Publication: draft → validate → preview migration on representative synthetic data → review permission/cost diff → publish immutable revision. References from workflows, APIs and reports block incompatible deletion. Export packages contain manifests, definitions, fixtures and migration metadata, never credentials/customer records by default.

Initial authoring surface is limited to a custom request object, form, table and approval-backed Flow. Later views reuse the same query/action contract. Industry packs are extension packages with namespaces and compatibility ranges; they may not redefine Principal, FileObject or Run.

Evidence includes schema upgrade and rollback, index quota enforcement, formula limits, field masking through every view/export, keyboard-only creation, Arabic labels and mobile form completion. Empty/error/offline states must remain understandable without exposing schema internals to ordinary employees.
