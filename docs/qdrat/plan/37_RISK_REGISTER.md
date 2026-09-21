# Risk register

| ID | Material risk | Mitigation/owner | Evidence gate |
|---|---|---|---|
| R01 | Breadth overwhelms first market wedge | People-first vertical journey; explicit phase non-goals | G4/G5 |
| R02 | Inherited build/CI assumed healthy | Exact lock/build/tests; fix branch targeting | G0 |
| R03 | Generic file access exceeds business scope | Owner-aware file registry and policy migration | G1 |
| R04 | Backup code mistaken for recoverability | Replace/repair contract; independent restore to another host | G1/G10 |
| R05 | Duplicate source authority | FieldAuthority single-owner intervals and cutover fences | G2 |
| R06 | Duplicate external effects | Idempotency plus UNKNOWN_OUTCOME reconciliation | G3 |
| R07 | Multiple execution engines | One journal/action contract; adapter ADR only | G3/G9 |
| R08 | Saudi payroll/legal errors | Official effective-dated matrix, specialist acceptance, parallel pay | G5 |
| R09 | Derived search/AI leaks | Query-time/source ACL enforcement and revocation tests | G4/G9 |
| R10 | Donor license/maintenance debt | Exact intake manifest, contract boundary, no blanket copying | Every intake |
| R11 | Hidden SaaS/egress | Denied-network no-AI/offline profile tests and egress inventory | G10 |
| R12 | HA without fencing | Multiworker/failover tests; singleton inherited jobs until replaced | G11 |
| R13 | Arabic/accessibility bolted on | Shared shell and bilingual journeys from G1 | Every UI task |
| R14 | Future tasks falsely marked ready | SHAPED records; actual SpecGrain readiness at frontier | Every task |
| R15 | Compliance promises exceed evidence | Qualified profile/pack labels and blocked live payroll | G5/G10 |
| R16 | Public plan exposes private donor content | Record hashes/path-level conclusions, no credentials/raw private source | Plan review |
| R17 | Review tool/agent unavailable | Explicit NOT_RUN and sequential source review; no fake independent approval | R3 gate |
| R18 | Regulatory or API source changes | Revalidate exact source/entitlement before implementation; versioned adapters | G2/G5 |

Implementation blockers and material planning gaps are tracked separately in REVIEW_LOG.md. A risk with an explicit qualification gate is not evidence that the qualification passed. Founder decisions currently required: none for the architecture. Commercial packaging, specialist availability and pilot customers must be settled before a public release; they do not justify pausing baseline engineering.
