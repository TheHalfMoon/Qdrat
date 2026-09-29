# Qdrat canonical implementation plan

Plan version: **1.0.0**, researched 20–21 September 2026. This directory is the proposed successor to the foundation roadmap. It describes target behavior, not shipped capability. Gate 0 is open; no implementation gate is certified by this planning change.

## Post-seal Qudra planning amendment

The sealed 1.0.0 plan remains the immutable parent snapshot. Founder-directed post-seal planning amendments are carried in:

- [44_INTELLIGENCE_FABRIC_AMENDMENT.md](44_INTELLIGENCE_FABRIC_AMENDMENT.md)
- [45_INTELLIGENCE_SOURCE_INTAKE.md](45_INTELLIGENCE_SOURCE_INTAKE.md)
- [46_QUDRA_BUSINESS_DECISION.md](46_QUDRA_BUSINESS_DECISION.md)
- [47_QUDRA_OPTION_ENGINE.md](47_QUDRA_OPTION_ENGINE.md)
- [48_QUDRA_DOMAIN_EXPERIENCES.md](48_QUDRA_DOMAIN_EXPERIENCES.md)
- [49_QUDRA_OPTIMIZATION_PROCESS_INTELLIGENCE.md](49_QUDRA_OPTIMIZATION_PROCESS_INTELLIGENCE.md)
- [50_QUDRA_IMPLEMENTATION_PLAN.md](50_QUDRA_IMPLEMENTATION_PLAN.md)
- [51_QUDRA_GAP_REVIEW.md](51_QUDRA_GAP_REVIEW.md)
- [52_QUDRA_FAST_LOCAL_INTELLIGENCE.md](52_QUDRA_FAST_LOCAL_INTELLIGENCE.md)
- [53_QDRAT_DATA_WORKBENCH.md](53_QDRAT_DATA_WORKBENCH.md)
- [54_QUDRA_AGENT_WORKFORCE_AND_GOAL_GRAPH.md](54_QUDRA_AGENT_WORKFORCE_AND_GOAL_GRAPH.md)
- [55_QUDRA_LOCAL_REASONING_GRAPH.md](55_QUDRA_LOCAL_REASONING_GRAPH.md)
- [56_QUDRA_IMPLEMENTATION_EXTENSION_2.md](56_QUDRA_IMPLEMENTATION_EXTENSION_2.md)
- [57_QUDRA_EXPANSION_GAP_REVIEW.md](57_QUDRA_EXPANSION_GAP_REVIEW.md)
- [58_SOURCE_INTAKE_DBX_PAPERCLIP_SYNAPLAN.md](58_SOURCE_INTAKE_DBX_PAPERCLIP_SYNAPLAN.md)
- [59_IMPLEMENTATION_READINESS.md](59_IMPLEMENTATION_READINESS.md)

### Authoritative Qudra execution graph

**[QUDRA_EXECUTION_GRAPH.yaml](QUDRA_EXECUTION_GRAPH.yaml) is the single authoritative machine-readable Qudra child-work graph.**

It contains 39 unique prospective package/rollout IDs:

- QD-F01..QD-F25;
- QD-D01..QD-D09;
- QD-L01..QD-L05.

`QUDRA_EXECUTION_EXTENSION.yaml` and `QUDRA_EXECUTION_EXTENSION_2.yaml` are retained only as historical construction inputs. They do not override `QUDRA_EXECUTION_GRAPH.yaml`.

Source authority for the 2026-09-29 expansion is recorded in `../SOURCE_AUTHORIZATIONS_2026-09-29_AMENDMENT.md` as effective entries 89–91 for `t8y2/dbx`, `paperclipai/paperclip`, and `metadist/synaplan` until folded into the main register.

The amendment family adds engine-independent Document Intelligence, Company Brain/RAG, **Qudra Business Decision**, a multi-objective **Qudra Option Engine**, Capability Fabric, **Qudra Fast Triage / local Classification Fabric**, local semantic filtering, hardware-specific edge decision profiles, durable agent-operation boundaries, local research/execution, domain decision packs, local optimization/simulation/process intelligence, a governed **Data Workbench**, **Goal Graph + Agent Workforce**, and an explicitly non-side-effecting **Local Reasoning Graph + Local Engine Router**.

It **does not change Gate 0 ordering or invalidate active G0 evidence**. Its obligations are inputs to future SpecGrain refinement of the existing G1/G2/G3/G4/G5/G6/G7/G8/G9/G10/G11 tasks; any task that becomes too broad must split into child SpecNodes without weakening parent acceptance.

## Planning readiness

The complete planning-readiness declaration is in [59_IMPLEMENTATION_READINESS.md](59_IMPLEMENTATION_READINESS.md).

Current planning marker:

```text
QUDRA_PLAN_IMPLEMENTATION_READY=YES
PLANNING_BLOCKERS=NONE
RUNTIME_COMPLETION_CLAIM=NO
```

This means the plan is ready to be implemented through the canonical dependency graph. It does **not** mean Qdrat/Qudra is implemented or that a blocked parent may be bypassed.

Read 00 (truth), 07–08 (product and architecture), CONTRACTS (normative interfaces), 39–42 (gates and execution), then 43 (Muse handoff), then the Qudra amendment family and `QUDRA_EXECUTION_GRAPH.yaml`. Research registers and source amendments support decisions; they never grant runtime authority. Historical documents remain evidence and standing founder authority remains effective.

Order of authority: explicit founder directives → live repository and immutable evidence → accepted architecture decisions in 08/CONTRACTS → canonical gate/execution graph → `QUDRA_EXECUTION_GRAPH.yaml` for Qudra child-work dependencies → task/SpecGrain record → explanatory chapter. A contradiction stops only the affected task and produces a bounded reconciliation change. Repository behavior wins factual disputes; it does not silently change the target design.

The default product is a customer-operated Django/PostgreSQL modular monolith with one durable worker contract. React/TypeScript progressively replaces inherited screens. AI, vector search, OCR, voice, remote connections, agent execution, database workbench features, and advanced analytics are optional profiles. Local operation without optional profiles must pass release tests.

Files in evidence/ are research and verification manifests. `tasks/tasks.json` contains 96 sealed parent work definitions; `QUDRA_EXECUTION_GRAPH.yaml` contains prospective Qudra child-work candidates only. SpecGrain nodes and execution graphs are planning state, never fabricated completion evidence. Every future path is explicitly prospective until created/refined by its task. [DOMAIN_SCHEMAS.md](DOMAIN_SCHEMAS.md) fixes logical schemas and lifecycle invariants. [REVIEW_LOG.md](REVIEW_LOG.md) records the canonical planning review passes and final challenge.

The Qudra planning amendment supersedes incompatible post-seal intake labels or split execution-extension interpretations only after review/acceptance. It does not authorize production deployment, certify Saudi regulatory compliance, or convert planning evidence into runtime proof.