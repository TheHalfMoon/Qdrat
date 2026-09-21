# Data Fabric

Owner: qdrat/data. Normative contracts C01–C04/C07. Data Fabric discovers, maps and reconciles systems; it never owns a second workflow engine or relaxes source permissions.

DataSource identifies one customer-controlled endpoint/account. ConnectorBinding pins package and configuration revisions, mode, credential reference and network policy. ExternalIdentity is unique on tenant/source/type/foreign key. FieldAuthority stores canonical field, source, effective interval and allowed command path; overlapping authoritative intervals are rejected. Observations retain competing values with confidence and provenance without overwriting the owner.

| Mode | Semantics | Failure behavior |
|---|---|---|
| NATIVE | Qdrat owns domain writes | Transactional consistency |
| LINKED_READ | Fetch external records on demand | Show unavailable/stale explicitly |
| SYNCED | Maintain an authorized projection from source | Source wins owned fields; local edits become proposals |
| MATERIALIZED | Versioned analytical snapshot | Expose snapshot freshness and delete propagation |
| WRITE_THROUGH | Send bound intent to authoritative source | Reconcile unknown result before retry |

Initial connectors: CSV/XLSX staged import, PostgreSQL read-only schema/rows, generic HTTPS/OpenAPI read adapter and protected file import. Customer SQL credentials cannot create schema, invoke unsafe functions or write arbitrary tables. Query templates are parameterized, allowlisted and timeout/row-limited. PostgreSQL CDC is a later certified adapter: publication/table scope, snapshot watermark, replication-slot growth and resnapshot policy must be explicit. Debezium remains optional, not a mandatory Kafka stack.

qdrat-bridge uses outbound mutually authenticated connections from a customer network to that customer's Qdrat deployment. It runs allowlisted connector operations, has per-binding credentials, encrypted bounded spool, certificate rotation, replay protection and kill switch. It is not a general reverse shell. Disconnection preserves checkpoints and reports stale data; queue quotas stop acquisition before exhausting disk.

Connector certification requires deterministic fake-provider tests for duplicate/out-of-order pages, 429/Retry-After, expired credentials, absent fields, deleted rows, changed keys, lost response, ACL revocation, incompatible schema and partial batches. Record source API version and granted scopes. Write certification additionally proves idempotency or operation lookup; otherwise write-through is unavailable.

Admin UX: inspect endpoint/account, discover without writing, classify fields, preview mapping and permissions, show query/egress costs, activate read mode, reconcile, separately activate writes. Health exposes last success, watermark lag, rejected rows, drift, credential expiry and reconciliation queue. Removal exports mappings/checkpoints and stops schedules before credentials are revoked.
