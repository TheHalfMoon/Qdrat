# Gap analysis and closure decisions

“Closed in design” means the architecture has an owner, contract, task and acceptance condition. It does not mean the feature is implemented or certified. The inherited runtime remains the baseline recorded in chapter 00. Uncertainty in external entitlement, legal qualification and measured performance is handled by explicit gated work and conservative fallback, not an unmade architecture choice.

| Material gap challenged | Resolution | Owning work / proof |
|---|---|---|
| Foundation docs mistaken for merged implementation | Exact main, foundation head and PR state kept separate; no gate marked complete | 00; G0-01–G0-06 |
| Build/install not reproducible | Hash locks and offline wheel inventory before feature work | G0-01; two independent resolutions and offline install |
| Unclear People vs identity ownership | Person/Employment/Principal separate; one authorization vocabulary | C01/C02, 07; G1-01–G1-04 |
| Tenant and company selector conflated | Explicit tenant boundary plus legal-entity policy; workers carry checked context | G1-02, G1-03; negative cross-scope corpus |
| Two sources both write payroll/customer fields | Exclusive FieldAuthority by interval; fenced cutover with reconciliation | C04, 09, 28; G2-04, G2-06 |
| Flow, Rules, agents and donor tools each execute | Single C05 journal; pure Rules and compiled Flow; adapters cannot create a second authority | G3-01–G3-08; crash/replay/unknown-outcome tests |
| Graph, BI and memory become competing facts | Rebuildable projections of versioned source data with current policy | G4-02, G4-03, G8-05, G9-02 |
| Approval changes while an agent waits | Approval binds exact input/revision; resume revalidates current grants and policy | C02/C06; G3-03, G9-03 |
| Remote timeout duplicated payment/email | UNKNOWN_OUTCOME blocks retry until lookup/idempotency reconciliation | C04/C05; G2-06, G3-02 |
| Source ACL revocation leaks in search, counts or citations | Fail closed on stale confidential ACL; query-time filtering plus invalidation | C07; G4-02 |
| Media and derivatives escape owner permissions | FileObject quarantine/owner checks; originals immutable; previews share deletion/hold | C08; G1-06, G4-01 |
| Studio overrides a regulated field or executes Python | Typed core plus namespaced JSONB; pure bounded expressions; publication/migration review | C09; G8-01–G8-04 |
| “Local” assumes a hidden model/download/analytics call | No-AI/no-egress release profile; offline fonts/models/artifacts; no remote fallback | G9-01, G10-02; packet-capture/DNS-denied installation proof |
| Laptop promise confused with disconnected writes | Local server remains authority; disconnected client only eligible drafts, no payroll/approval cache | 27/30; G1-09, G10-01 |
| Single process jobs duplicated in HA | Inventory scheduler; persisted timers, fencing, idempotency and restore reconciliation | G0-05, G3-02, G3-08, G11-01 |
| Sandbox design assumed secure on every host | Required profile qualification; deny unsupported tools; external policy enforcement | 16; G9-04/G9-05 |
| Saudi rates/calendars/API availability guessed | Versioned rule source matrix and cohort fixtures; assisted channel fallback; shadow-only payroll | 26; G5-01–G5-06 |
| Finance scope turns into a premature ERP rewrite | Native intent/approval; external ledger authority; separate replacement admission task | 22; G7-08, G12-01 |
| Privileged extensions undermine upgrades | Signed manifest, constrained API, out-of-process code, compatibility and restore | C09/C10; G8-04, G10-04 |
| “Backup succeeded” omits keys/blobs/checkpoints | Full manifest restore on another host; outbound effects paused until reconciliation | C10; G1-08, G10-05 |
| Research labels conflict with intake evidence | Reconciled 36/76/36 machine inventories and deliberate classifications; no copied donor runtime | 02/03/35; validator |
| Future tasks claim READY against nonexistent code | SHAPED targets, exact-head refinement at frontier, real SpecGrain readiness, per-task evidence | 40–43; no fabricated implementation receipts |
| Large future tasks invite architecture improvisation | Domain schemas and lifecycle rules fixed; work-packet bounds and deterministic child-split rule | DOMAIN_SCHEMAS, 41; fail readiness if packet exceeds budget |
| No measurable gate exits | Gate-specific criteria added to graph as well as chapter 39 | 39; validator verifies agreement |
| Broad source grant causes accidental private-code publication | Public plan contains conclusions and identifiers only; private source text stays out | 02/35; source intake review |

The remaining uncertainties are delivery measurements: exact dependency resolution, resource ceilings, production country-pack validation, supported-provider capabilities, customer migrations and hands-on usability. They have named gates and failure behavior. They are not evidence of current success and cannot be waived by this plan. Any new contradiction is entered as a bounded reconciliation issue with affected nodes blocked; unaffected accepted work can continue.

The final adversarial question is recorded in REVIEW_LOG.md. Completion of planning means the next work is specified and the architecture has no known unresolved material choice; production readiness remains conditional on the gate receipts.
