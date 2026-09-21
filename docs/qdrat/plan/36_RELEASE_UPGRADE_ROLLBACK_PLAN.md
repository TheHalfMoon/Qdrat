# Release, upgrade and rollback

Release unit: application image(s), database migration graph, frontend bundle, configuration schema, extension/API compatibility, static locale/font assets and optional profile manifests, all pinned by digest. Product version does not substitute exact component identity.

Channel progression: developer → internal synthetic → qualified pilot → general release. Promotions reuse the same built artifact; no rebuild between review and deployment. Release gates include source provenance, required tests, restore rehearsal, upgrade compatibility, Arabic/no-AI/offline checks and unresolved-risk review. Signed manifests expose support end date and minimum compatible database version.

Upgrade plan records installed/current target digests, required free space, migrations, downtime/rolling constraints, extension compatibility, backup/restore point, source connector versions and pending external operations. Preflight rejects unsupported jumps. Pause effect dispatch; drain or snapshot runs; expand schema; migrate/backfill; verify; switch app; resume with reconciliation.

Expand/contract schema changes keep current and previous supported application version compatible through the declared window. Destructive migration waits until old code/extension retirement and proven recovery. A downgrade that cannot read the new schema is refused. Rollback plan selects application rollback, forward repair or full state restore explicitly.

Restore recovers database, blobs, secrets/key references, manifests, deletion/hold journals, checkpoints and pending runs. Outbound effects remain paused until remote-state reconciliation; otherwise restoring old state can repeat payments/messages. Restore to a separate host is mandatory evidence.

Air-gap updates are signed importable bundles; trust-root rotation is customer-controlled and can be performed without internet. Bundles include revoked/expired artifact metadata and a documented emergency trust recovery path. No automatic update that changes schema or data egress without a reviewed plan.

A release status page identifies qualified profiles and known limits; laptop success cannot certify HA/Kubernetes or remote providers. Customer extension incompatibility blocks only the affected profile/upgrade with an actionable migration path.
