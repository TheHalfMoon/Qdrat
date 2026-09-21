# Target architecture and accepted design decisions

These decisions are normative targets. Existing behavior is catalogued in 00 and 31; no target control is asserted to exist already.

| ADR | Decision | Reason and rejected alternative |
|---|---|---|
| A01 | Django modular monolith, explicit qdrat/ modules and service contracts | Reuse inherited domain knowledge; avoid a multi-language service per donor |
| A02 | PostgreSQL owns transactional state, outbox, durable runs and source mappings | Avoid dual authorities and mandatory Kafka/graph/Temporal |
| A03 | Native local authentication plus standard external federation; one Principal and policy vocabulary | No separate AI/Studio/Service users |
| A04 | One durable Automation execution journal; Flow/Rules/AI are definitions or step implementations | Prevent three retry/approval systems |
| A05 | Source authority is per field and effective interval, with exactly one write owner | “Synced” never means silent last-write-wins between payroll sources |
| A06 | Graph/vector/FTS/BI are replaceable projections | Projection deletion or rebuild cannot erase source records or create authority |
| A07 | React/TypeScript PWA adopted route-by-route through typed APIs | Avoid a full Horilla rewrite before evidence and customer value |
| A08 | Baseline has no AI, no external egress, no public cloud control plane | Optional integrations must declare their loss of function offline |
| A09 | High-impact employment, payroll release, identity elevation and payments require human accountability | Agent proposals cannot bootstrap grants or approve themselves |
| A10 | External effects have UNKNOWN_OUTCOME and reconciliation, not “exactly once” claims | A lost response cannot prove a remote action did not happen |
| A11 | Deployment instance is the first customer isolation unit; tenant_id still explicit | Multi-company is not cross-customer SaaS isolation |
| A12 | Narrow rules AST first; qualify GoRules/CEL behind the same contract later | Never run user formulas as Python/JS inside the web process |
| A13 | Local FTS first, optional pgvector in the same database before another vector service | Qdrant justified only by measured scale/capability need |
| A14 | Untrusted tools/documents run in isolated workers; OpenSandbox is a candidate adapter | A container is not proof of a security boundary |
| A15 | Native ledger, public-cloud fleet and autonomous high-impact decisions remain gated | Connect established authorities before replacing regulated depth |

## Boundaries and placement

Prospective packages: qdrat/kernel (object references, transactions, events); qdrat/trust; qdrat/directory; qdrat/data; qdrat/automation; qdrat/knowledge; qdrat/studio; qdrat/people; qdrat/work; qdrat/service; qdrat/relationships; qdrat/finance; qdrat/ops; qdrat/analytics; qdrat/ai; qdrat/voice; qdrat/country/sa. frontend/ owns the shell/design system; connectors/ and extensions/ contain signed, qualified packages, not arbitrary code loaded into Django.

A module may read another module through a query service and command it through a typed action. Cross-module mutation is forbidden outside an explicitly owned transaction coordinator. Read-model SQL views are versioned contracts. Schema migrations belong to the owning module. Boundary checks in CI forbid imports of another module's write internals.

A request authenticates a principal, resolves tenant/company scope, validates input, authorizes action/fields/purpose, checks expected revision, commits domain state plus outbox/evidence intent atomically, and returns an operation ID. Workers carry a signed/bound principal context and recheck current permission before an effect. Long waits never retain an authorization decision indefinitely.

Baseline runtime: web, PostgreSQL, one or more lease-based workers, customer TLS entry point. Preserve inherited Redis until a measured dependency inventory permits removal; target correctness must not depend on Redis persistence. Existing singleton scheduler remains singleton until all jobs use durable lease/idempotency contracts. Optional profiles contain OCR/conversion, model inference, sandbox, S3-compatible storage, metrics export and enterprise federation.

## Strangler sequencing

Inventory each inherited route/model/job and assign owner. Add stable IDs/mappings without destructive renames. Put protected APIs around one People journey. Route a new screen to the new service while legacy screens continue against the same owner. Backfill in resumable batches, compare counts/checksums/business totals, switch reads, then writes, then retire legacy paths after a compatibility window and restored-backup rehearsal.

No dual independent payroll engines. During transition, legacy calculation is an explicitly versioned adapter; new calculations run in shadow mode and cannot release payment. A schema change that invalidates rollback requires a forward-repair or full restore plan before deployment.
