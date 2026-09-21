# API, SDK and extension platform

REST /api/v1 with OpenAPI is the first external contract; internal services use the same typed semantics. Add webhook/event AsyncAPI definitions and optional MCP/CLI adapters over Action/Query registries. Do not add GraphQL until measured consumer need justifies another authorization/query surface.

API conventions: cursor pagination, stable ObjectRef, ETag/expected revision, bounded bulk operations, request idempotency, typed safe errors, trace IDs, versioned schemas and explicit deprecation. Cursor binds query/scope/version, not just row offset. API tokens carry audience, scopes, tenant and expiry; browser sessions retain CSRF protections. Public portal and administrative APIs have distinct audiences.

SDKs initially Python and TypeScript generated from a pinned schema with contract tests. Generation artifacts never substitute server authorization. Webhooks are signed, deduplicated and retried with bounded dead-letter retention and administration UI. Endpoint configuration cannot bypass egress/SSRF controls.

Extension tiers: declarative package; isolated action/connector service; explicitly installed UI extension. Install preview shows publisher/digest, capabilities, egress, data classes, schema changes, compatibility and removal consequences. Approval is an administrative product action, not permission for an agent to widen itself. Trust revocation disables future calls and quarantines queued effects.

Extension upgrade pins old/new manifests, migrates in shadow where possible, runs compatibility fixtures and publishes atomically. Uninstall preserves exportable customer records under retention policy and shows dependent workflows/views. No source forks needed for custom company forms, objects, rules and workflows.

Acceptance covers SDK/server version skew, unknown fields, pagination under change, callback replay, extension capability denial, stale permission caches, signed package tampering and offline installation. Backward compatibility covers the current and immediately previous supported API minor through a documented window; removal requires telemetry from customer-local diagnostics and an explicit migration guide, not hidden phone-home metrics.
