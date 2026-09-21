# Trust, identity and authorization

Owner: qdrat/trust. C02/C06 define the shared authorization vocabulary. Principal types: human, service, agent and external portal. Person and user account are distinct. Group/role membership is tenant-scoped and effective-dated. Grant names action/object/field/purpose scope. Deny wins; missing context is indeterminate and fails closed.

Local login and bootstrap work offline with customer-controlled secrets, password policy, recovery and MFA. Add OIDC federation first, SAML through a qualified adapter later, SCIM provisioning/deprovisioning with immutable external identity mapping. IdP group mapping cannot create owner/admin roles without configured policy. Break-glass identities are local, limited, monitored and never used for routine agents.

ReBAC relations (member, manager, owner, participant) and ABAC attributes (legal entity, classification, purpose, employment status) compile into a Qdrat-owned decision interface. Native policy evaluation and query scopes come first; OpenFGA/SpiceDB/Cedar/OPA are references or scale adapters, not four simultaneous engines. No arbitrary customer executable policy in the web process.

Enforcement points: HTTP/session/JWT, query services, field serialization, exports, file download, search/graph/BI, worker dispatch, connector credential broker and extension/sandbox boundary. Service tokens bind tenant/audience/allowed actions and expire; background jobs cannot reuse a global administrator. Current source restrictions are intersected with Qdrat grants.

SecretReference contains encrypted value/key version, owner, scope, expiry and rotation status. Master encryption keys live outside application blobs/database backups and have a recovery escrow procedure. Local encrypted store is baseline; OpenBao/Infisical integration optional. Secret values never enter workflow definitions, logs, evidence manifests or model context.

Privacy requires classification, processing purpose/lawful basis, retention, export/deletion requests, legal holds and transfer controls. “Local” does not mean every local employee may see every record. No hidden telemetry, remote model calls or error-reporting endpoint. Administrator egress configuration is explicit and audited.

Qualification matrix tests same-tenant cross-company, cross-tenant, field masking, list/count/export leakage, delegation narrowing, revoke-during-wait, SCIM termination, stale source ACL and break-glass recovery. A default-allow UI or inherited superuser shortcut cannot satisfy this contract.
