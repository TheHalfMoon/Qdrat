# Qudra Expansion Gap Review — DBX, Paperclip and Synaplan

Status: **PLAN HARDENING REVIEW**

This review attacks the 2026-09-29 expansion before implementation.

## 1. Data Workbench becomes a second database authority
Risk: connection state, permissions or schema ownership diverge from Data Fabric.

Resolution:
- DataSource registry remains canonical;
- Workbench reads/acts through Data Fabric adapters;
- no separate credential store;
- schema snapshots are projections;
- writes compile to governed Action/Run semantics.

## 2. Natural-language query becomes unrestricted SQL
Risk: Qudra produces a destructive or data-exfiltrating query.

Resolution:
- model produces `DataQueryPlan`, not execution authority;
- parser/adapter effect classification;
- row/time/result/network bounds;
- write/DDL/admin policy and approval;
- read-only credentials preferred;
- explicit preview/explain.

## 3. Query classification error
Risk: a write is misclassified as read-only.

Resolution:
- adapter/database parser is authoritative where available;
- unknown/ambiguous statement fails closed;
- transaction/read-only session controls used when supported;
- regression corpus per backend/dialect;
- no model confidence can downgrade effect class.

## 4. Data export becomes exfiltration
Risk: large or sensitive data leaves through export/transfer.

Resolution:
- export is an Action/Run;
- field/object/purpose policy;
- data-classification limits;
- destination allowlist;
- approval for sensitive/bulk export;
- artifact custody/retention/audit.

## 5. Cross-engine transfer corrupts semantics
Risk: type conversion or collation/timezone differences silently change data.

Resolution:
- explicit mapping/conversion plan;
- staging/preview;
- rejected-row ledger;
- source/destination counts/checksums/samples;
- post-transfer reconciliation;
- incompatible mappings block apply.

## 6. Schema drift invalidates saved plans
Risk: saved query/transfer/lineage plans use stale schema.

Resolution:
- bind source schema snapshot digest;
- preflight live schema revision;
- stale plan state;
- regenerate/reapprove sensitive operations.

## 7. Inferred lineage presented as fact
Risk: weak lineage inference affects compliance or decisions.

Resolution:
- DECLARED/PARSED/OBSERVED/INFERRED provenance classes;
- confidence/evidence retained;
- inferred edges never silently promoted;
- review/promotion workflow.

## 8. Database credentials reach models
Risk: connection strings, passwords or tunnel keys leak into prompts/traces.

Resolution:
- secret references only;
- execution-boundary resolution;
- redaction tests;
- model context receives normalized metadata/results only.

## 9. Agent role becomes legal employee identity
Risk: AI agents appear in HR/payroll/employment records as workers.

Resolution:
- AgentProfile extends Principal only;
- separate AgentAssignment;
- no Employment record unless it refers to a real person;
- UX avoids legal employment terminology for agents.

## 10. Goal ancestry grants authority
Risk: “important company goal” is treated as permission.

Resolution:
- goals are context only;
- authorization remains Principal + policy + delegation;
- tests prove goal linkage cannot widen scopes.

## 11. Goal gaming
Risk: agent maximizes a local goal metric while harming broader outcomes.

Resolution:
- hard policy/guardrails first;
- multi-objective outcome metrics;
- side-effect review;
- Decision Frontier and business constraints;
- human-controlled promotion of routines/playbooks.

## 12. Duplicate agents perform the same work
Risk: heartbeat/routine races cause duplicate customer or financial effects.

Resolution:
- atomic WorkLease;
- generation fencing;
- Flow idempotency still required;
- external UNKNOWN_OUTCOME reconciliation;
- concurrency fixtures.

## 13. Heartbeat storm
Risk: many agents wake simultaneously and overload local hardware/database.

Resolution:
- wakeup coalescing;
- per-tenant/host concurrency budget;
- jitter and queue;
- priority/fairness;
- backpressure and pause.

## 14. Budget enforcement arrives after cost
Risk: runaway local compute already consumed resources before hard stop.

Resolution:
- preflight budget;
- per-node/run reservation where useful;
- continuous accounting;
- hard stop/cancel;
- stale-worker fencing;
- budget reconciliation after crash.

## 15. Supervisor privilege escalation
Risk: supervisor agent delegates capabilities it does not possess.

Resolution:
- delegation is intersection of supervisor authority, subordinate grants and task policy;
- no transitive scope expansion;
- explicit delegation receipt/expiry;
- denial corpus.

## 16. Skill supply-chain compromise
Risk: imported skill carries hidden instructions/tools.

Resolution:
- signed/versioned skill packs;
- source provenance;
- capability manifest;
- evaluation fixtures;
- review before publish;
- no ambient secret/network access.

## 17. Performance metric rewards unsafe agent
Risk: fastest agent is selected despite poor evidence/safety.

Resolution:
- outcome/safety/evidence metrics dominate throughput;
- policy violation and unknown-effect penalties;
- minimum quality gates;
- no automatic promotion.

## 18. Portable team pack leaks secrets or tenant data
Risk: export contains credentials, IDs or business records.

Resolution:
- structural export schema;
- secret scrubbing;
- tenant reference remapping;
- preview;
- collision handling;
- fixture proving no secret material.

## 19. Reasoning Graph becomes second workflow engine
Risk: planners implement waits, approvals and side effects in the DAG.

Resolution:
- ReasoningGraph nodes are analytical only;
- no side-effect node type;
- business effect compiles to CapabilityPlan and Flow/Action;
- graph lifetime bounded to Run/DecisionCase analysis;
- explicit architecture tests.

## 20. Planner invents graph capabilities
Risk: local LLM references unknown node/capability types.

Resolution:
- closed node schema;
- Capability Graph lookup;
- typed validation;
- unknown node/capability rejects plan;
- no best-effort execution.

## 21. Model router chooses fastest but worse engine
Risk: cost/latency optimization degrades decision quality.

Resolution:
- quality threshold is a hard eligibility criterion;
- only qualified engines participate;
- task-specific benchmark profile;
- shadow comparison before default change;
- routing evidence retained.

## 22. Model readiness cache lies
Risk: model is marked READY after artifact/runtime changes.

Resolution:
- readiness binds artifact/runtime digests and hardware profile;
- invalidation on install/update/remove;
- lightweight health probe before use where needed;
- stale readiness expires.

## 23. Context capacity truncates decisive evidence
Risk: router selects a model that cannot fit required context.

Resolution:
- preflight context capacity;
- explicit ContextBuildResult omissions;
- retrieval/compaction policy;
- choose larger qualified local model or NEED_MORE_EVIDENCE;
- no silent truncation.

## 24. Optional sidecar becomes hidden mandatory dependency
Risk: a disabled vector/OCR/browser service breaks unrelated product paths.

Resolution:
- capability registration is health-driven;
- disabled capability is absent, not fake-enabled;
- core baseline tests run with all optional sidecars off;
- dependencies declared by feature.

## 25. Air-gap install is incomplete
Risk: model/plugin/image fetch occurs at runtime.

Resolution:
- complete offline manifest;
- digest/license inventory;
- network-disabled install/start/readiness qualification;
- missing artifact fails before feature activation.

## 26. Sidecar upgrade silently changes behavior
Risk: updated OCR/reranker/model changes outputs with no qualification.

Resolution:
- version pinning;
- compatibility/evaluation pack;
- shadow qualification;
- rollback/recovery;
- old DecisionCase retains original provider evidence.

## 27. Progressive reasoning UI implies action already happened
Risk: users confuse “analysis complete” with “business effect complete.”

Resolution:
- separate visual states for ANALYSIS, PROPOSAL, APPROVAL, EXECUTION, RECONCILIATION;
- effect receipts shown only after Action/Flow evidence.

## 28. Local resource accounting leaks private workload detail
Risk: per-agent metrics expose sensitive employee/customer activity.

Resolution:
- tenant/role permissions;
- aggregation by default;
- purpose-limited traces;
- retention and redaction.

## 29. Data Workbench encourages production tinkering
Risk: convenient UI bypasses change management.

Resolution:
- environment classification;
- production write policy stricter than dev/test;
- approval/change window hooks;
- query history and evidence;
- read-only default.

## 30. Source donor drift
Risk: future upstream code differs from researched revision.

Resolution:
- research revisions pinned in authorization amendment;
- imported paths bind exact commit/tag;
- later upstream updates require new intake/qualification;
- no floating wholesale copy.

## 31. Final readiness check

This expansion is implementation-ready only when:
- source authorization amendment is normative;
- DBX concepts map to Data Fabric rather than replace it;
- Paperclip concepts map to Principal/Work/Flow rather than duplicate them;
- Synaplan ReasoningGraph is explicitly non-side-effecting;
- all nine QD-F17..QD-F25 packages have dependencies, outputs, acceptance and risk;
- air-gap/local-only rules remain intact;
- data, agent and reasoning failure states are explicit;
- security, deletion, backup, upgrade and rollback responsibilities are preserved.

Exact donor files, runtime winners and implementation paths are intentionally deferred to SpecGrain refinement at the accepted parent head; they are evidence-gated implementation choices, not architecture gaps.
