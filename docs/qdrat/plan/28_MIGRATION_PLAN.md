# Migration is a product

Owner: qdrat/data migration coordinator under C10. Initial imports: Horilla database, spreadsheets, files and generic APIs. Later certified mappings cover Jira/Zendesk/ServiceNow/CRM/ERP/HR systems. No adapter promises full fidelity before its mapping tests.

Migration phases: discover schema/rights → snapshot → map with field authority → dry-run → validate → staged import → reconcile → freeze source writes or capture tail → switch bounded authority → observe → retire. A job pins source revision, mapping version, source ACL, checksum, cursor and target schema. Import source IDs are immutable and namespaced. Invalid rows go to a downloadable permission-safe error ledger.

Reconciliation compares source/target row and key sets, attachment hashes, relationship integrity, effective-date histories, permission samples and financial/payroll totals. A matching count alone is insufficient. Duplicate people/customers are merge candidates with reversible mappings and approval; never fuzzy-merge silently.

Horilla migration preserves stable mapping from every legacy table/PK, password/auth compatibility where appropriate, signed/original file custody and business history. Backfill is chunked and idempotent; schema expansion precedes code switch; removal follows a measured compatibility window. Legacy and new code cannot both own the same field.

Cutover obtains a write fence, records final source watermark, drains/reconciles in-flight external actions, verifies backup and switches one owner. Abort keeps old authority. After irreversible effects or new-schema writes, rollback may require forward repair or point-in-time restore plus external reconciliation; a Git revert is not a data rollback.

Customer UX supports preview of transformations, estimated downtime/space, sample diffs, resume, cancellation and exceptional rows. Export includes open documented schemas, relationships, attachments, source IDs, retention constraints and audit manifests so customers can leave Qdrat.

Tests: crash after partial batch, duplicate pages, schema drift, revoked credentials/ACL, attachment loss, absent fields, restart with changed mapping, counterparty changes during cutover and restoration before re-enabling outbox dispatch.
