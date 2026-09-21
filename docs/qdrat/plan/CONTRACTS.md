# Normative cross-cutting contracts, version 1

These contracts define the implementation target. Task records reference contract IDs. JSON uses UTF-8; money is an integer minor-unit amount plus ISO currency and declared rounding policy, never float. Quantities/ratios use fixed-precision decimal strings. Timestamps are RFC3339 UTC; local date, IANA timezone and country calendar are separate fields. IDs are UUIDs; source IDs remain opaque strings.

## C01 — Object identity and command

ObjectRef = {tenant_id, object_type, object_id}. Revision is a monotonically increasing integer per object. A command contains request_id, tenant_id, principal_id, effective_principal_id, delegation_id?, purpose, action_type, action_version, target, expected_revision, arguments, idempotency_key, trace_id. Idempotency uniqueness is (tenant_id, principal_id, action_type, idempotency_key). Reuse with a different canonical arguments/target digest is a conflict. POST /api/v1/actions/{type}:invoke returns operation_id, state and permitted result projection. GET /api/v1/operations/{id} reauthorizes reads.

Expected revision is mandatory for updates and approvals; mismatch returns 409 without an effect. Invalid schema returns 422; unauthenticated 401; unauthorized resource lookup returns policy-consistent 404 or 403 without hidden field names. Error objects contain stable code, safe message, correlation_id and retry classification. There is no generic write-any-table API.

## C02 — Authority

Decision input = principal, delegation chain, tenant, legal entities, action, object, field set, purpose, classification, source ACL/freshness, time, policy revision. Decision = ALLOW/DENY/INDETERMINATE, allowed_fields, obligations, reason_codes, policy_revision, decision_id, expires_at. INDETERMINATE denies effects. List queries, counts, filters, exports, aggregations, links and search snippets must enforce equivalent policy; hiding a UI column is insufficient.

Delegation is the intersection of issuer's current authority, explicit grant, agent/service permission, resource scope, purpose, expiry and budget. Revocation increments a tenant policy epoch, invalidates decision caches and stops queued execution. No principal can approve its own privilege elevation. Creator permission, editor permission and runtime execution permission are separate. Admin support impersonation requires a short-lived audited support session and never bypasses payroll segregation.

## C03 — Domain event and evidence

Event = CloudEvents-compatible {specversion, id, source, type, subject, time, datacontenttype, data, qdrat_tenant, aggregate_revision, schema_version, trace_id, causation_id}. The producer writes an outbox row in the domain transaction. Delivery is at least once; consumer inbox uniqueness is (tenant, consumer, event_id). Checkpoints advance only with durable effects. Ordering is per aggregate, not globally. Events carry IDs/minimal safe fields; protected data is fetched under recipient authority.

EvidenceRecord records subject/action/input digest, policy/approval IDs, before/after revisions, outcome, source revisions, artifact digests, actor and time. Operational logs are not audit truth. Tamper evidence uses per-tenant sequence/hash chaining and customer-controlled signed checkpoints outside the mutable database; a hash chain alone does not defeat a database administrator. Secret values and full model prompts are excluded by default.

## C04 — Data connector

ConnectorManifest contains identifier/version/digest, supported modes, capabilities, configuration schema, credential scopes, allowed endpoint templates, egress hosts/ports, data classes, rate/query limits and runtime/isolation requirements. Operations: discover_schema, read_page, read_change_batch, fetch_acl, prepare_write, execute_write, lookup_operation, health, export_checkpoint. No operation gets an unrestricted database connection by default.

ReadBatch = source_revision, schema_revision, records, tombstones, next_cursor, high_water_mark, observed_at, ACL_revision, completeness(full/partial/unknown), warnings. A missing/forbidden field is not a deletion. MappingRevision binds source key, canonical type/field, transform version, authority owner, effective interval and conflict rule. Unknown schema additions quarantine; destructive/incompatible drift stops writes. Cursor commits occur after canonical transaction and inbox commit. Bootstrap snapshot plus CDC watermark must prove no gap; lost source history requires a new reconciliation snapshot.

WriteIntent binds source/account/resource, exact payload digest, expected remote version, credential grant reference, approval and idempotency key. Result is COMMITTED/REJECTED/FAILED_RETRYABLE/FAILED_FINAL/UNKNOWN_OUTCOME. Unknown results enter reconciliation; retry is permitted only after remote idempotency/lookup proves safety. Read-only and write-through credentials are separate.

## C05 — Run journal

Run binds workflow_revision, inputs digest, principal/delegation, trigger, budget and policy epoch. StepAttempt binds step version, attempt number, execution lease/fencing token, action digest and artifacts. States: CREATED → VALIDATING → READY → RUNNING → SUCCEEDED; RUNNING may enter WAITING_APPROVAL, WAITING_SIGNAL, RETRY_WAIT, RECONCILING, COMPENSATING, FAILED or CANCELLED. Waiting returns through VALIDATING. SUCCEEDED is immutable; correction creates a linked run.

The worker claims a lease by transactional compare-and-swap. A fencing token prevents a stale worker from committing a step. External idempotency/reconciliation remains necessary because database fencing alone cannot undo a remote effect. Bounded retries use classified failures, exponential delay/jitter and persisted next_attempt_at. Cancellation revokes future work, sends a kill request and records any irreversible effects still outstanding. Compensation is a new authorized forward action, not time travel.

Durable timers live in PostgreSQL. Schedules specify timezone, DST policy, catch-up limit and coalescing. Every loop has a max iteration bound; parallel fan-out has concurrency and aggregate budget limits. A global pause blocks dispatch and revokes active capabilities. Pure replay uses recorded inputs and stubs all effects; resume uses recorded completed steps and revalidates future effects. Re-run creates a new run and approval context.

## C06 — Approval and budgets

Approval binds target revision, action/input digest, approver eligibility policy, required quorum, expiry, separation-of-duties rules and evidence digest. Edits invalidate approval. Decision is PENDING/APPROVED/REJECTED/EXPIRED/REVOKED; approved is consumed once by its exact intent. A human approving a workflow does not grant every future unbounded action.

Budget reserves atomically before dispatch across the run/delegation/tenant hierarchy: wall time, CPU, memory, disk, network bytes, token count, external cost, rows and tool calls. Release unused reservation on settlement; keep unknown external costs reserved until reconciled or explicitly estimated by policy. Prices and currency conversions are versioned estimates, not authoritative bills.

## C07 — Query/search

QueryRequest binds principal, tenant, purpose, permitted sources, filters, page size, deadline, row/scan budget, freshness and consistency requirement. Results contain source/canonical revision, observed time, citation span and permitted fields. Full-text, vector and graph adapters cannot broaden the authorized candidate set. If source ACL is stale beyond its connector-specific TTL, fail closed for confidential material. Revocation invalidates caches and indexes; query-time checks remain mandatory during reindex.

Derived answer citations point to immutable source revision+span; absent evidence returns UNKNOWN, not a fabricated answer. Counts, facets and timing-sensitive high-cardinality probes must not disclose hidden records. SQL tools use a read-only role against authorized views with statement timeout, row limit and no extension/file/network operations; SQL parsing alone is not a security boundary.

## C08 — File/document

FileObject owns blob digest, tenant, owner object, MIME detected from content, size, quarantine state, encryption-key reference, retention/hold, revision and ACL policy. Upload → QUARANTINED → SCANNED → AVAILABLE or REJECTED. Download authenticates and authorizes the owning object every time; signed download grants are short-lived and resource-bound. No raw path access.

Derivative binds original digest, tool/model/version, configuration and extraction evidence. OCR/rendered previews never replace signed/original bytes. Conversion executes offline with resource limits. Expired links, removed membership and delete/hold policy apply to previews, transcripts, vector chunks and exports. Legal hold blocks destruction and records the conflict with deletion requests.

## C09 — Extension and schema publication

Extension manifest binds publisher, package digest, API range, object namespaces, requested permissions/egress, dependencies, migration plan, rollback and supported profiles. Declarative objects/forms/rules are the default. Arbitrary extension code runs out of process under the execution plane. UI extensions use a constrained message API, CSP and sandboxed frames where needed. No extension imports raw Django models or obtains an administrator credential.

Schema publication performs validation, dependency analysis, dry-run migration, permission review and revision pinning. Removing a referenced field or changing type creates a new version and a migration; it never silently coerces existing values. Formula dependency cycles fail publication; formulas are pure, budgeted and cannot call network/filesystem.

## C10 — Pack/release/migration

Release manifest binds exact application commit, image and wheel digests, SBOM, notices, schemas, migration graph, extension compatibility, model/font/locale assets and verification evidence. Offline installation verifies all content locally with a provisioned trust root; no public transparency/OIDC endpoint is required. Key rotation and metadata expiry are explicit, with an offline administrative recovery procedure.

MigrationJob = source snapshot, mapping revision, dry-run digest, counts/totals, resumable cursor, error ledger, cutover owner, write fence and rollback point. Cutover requires count/key/financial-total reconciliation plus sampled record fidelity, permission and attachment checks. Backfill cannot silently drop unknown fields. Restore includes database, blobs, encryption keys, configuration, source checkpoints and release manifest, with outbound effects paused until reconciliation.
