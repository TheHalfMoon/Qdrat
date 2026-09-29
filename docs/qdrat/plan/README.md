# Qdrat canonical implementation plan

Plan version: **1.0.0**, researched 20–21 September 2026. This directory is the proposed successor to the foundation roadmap. It describes target behavior, not shipped capability. Gate 0 is open; no implementation gate is certified by this planning change.

## Post-seal Intelligence Fabric amendment candidate

The sealed 1.0.0 plan remains the immutable parent snapshot. Founder-directed post-seal planning amendments are carried in:

- [44_INTELLIGENCE_FABRIC_AMENDMENT.md](44_INTELLIGENCE_FABRIC_AMENDMENT.md)
- [45_INTELLIGENCE_SOURCE_INTAKE.md](45_INTELLIGENCE_SOURCE_INTAKE.md)
- [46_QUDRA_BUSINESS_DECISION.md](46_QUDRA_BUSINESS_DECISION.md)
- [47_QUDRA_OPTION_ENGINE.md](47_QUDRA_OPTION_ENGINE.md)
- [48_QUDRA_DOMAIN_EXPERIENCES.md](48_QUDRA_DOMAIN_EXPERIENCES.md)
- [49_QUDRA_OPTIMIZATION_PROCESS_INTELLIGENCE.md](49_QUDRA_OPTIMIZATION_PROCESS_INTELLIGENCE.md)
- [50_QUDRA_IMPLEMENTATION_PLAN.md](50_QUDRA_IMPLEMENTATION_PLAN.md)
- [QUDRA_EXECUTION_EXTENSION.yaml](QUDRA_EXECUTION_EXTENSION.yaml)
- [51_QUDRA_GAP_REVIEW.md](51_QUDRA_GAP_REVIEW.md)
- [52_QUDRA_FAST_LOCAL_INTELLIGENCE.md](52_QUDRA_FAST_LOCAL_INTELLIGENCE.md)
- [53_QDRAT_DATA_WORKBENCH.md](53_QDRAT_DATA_WORKBENCH.md)
- [54_QUDRA_AGENT_WORKFORCE_AND_GOAL_GRAPH.md](54_QUDRA_AGENT_WORKFORCE_AND_GOAL_GRAPH.md)
- [55_QUDRA_LOCAL_REASONING_GRAPH.md](55_QUDRA_LOCAL_REASONING_GRAPH.md)
- [56_QUDRA_IMPLEMENTATION_EXTENSION_2.md](56_QUDRA_IMPLEMENTATION_EXTENSION_2.md)
- [QUDRA_EXECUTION_EXTENSION_2.yaml](QUDRA_EXECUTION_EXTENSION_2.yaml)
- [57_QUDRA_EXPANSION_GAP_REVIEW.md](57_QUDRA_EXPANSION_GAP_REVIEW.md)

Source authority for the 2026-09-29 expansion is recorded in `../SOURCE_AUTHORIZATIONS_2026-09-29_AMENDMENT.md` as effective entries 89–91 for `t8y2/dbx`, `paperclipai/paperclip`, and `metadist/synaplan` until folded into the main register.

The amendment family adds engine-independent Document Intelligence, Company Brain/RAG, **Qudra Business Decision**, a multi-objective **Qudra Option Engine**, Capability Fabric, **Qudra Fast Triage / local Classification Fabric**, local semantic filtering, hardware-specific edge decision profiles, durable agent-operation boundaries, local research/execution, domain decision packs, local optimization/simulation/process intelligence, a governed **Data Workbench**, **Goal Graph + Agent Workforce**, and an explicitly non-side-effecting **Local Reasoning Graph + Local Engine Router**.

It **does not change Gate 0 ordering or invalidate active G0 evidence**. Its obligations are inputs to future SpecGrain refinement of the existing G2/G3/G4/G6/G7/G8/G9/G10/G11 contracts; any task that becomes too broad must split into child SpecNodes without weakening parent acceptance.

Read 00 (truth), 07–08 (product and architecture), CONTRACTS (normative interfaces), 39–42 (gates and execution), then 43 (Muse handoff). Research registers and source amendments support decisions; they never grant runtime authority. Historical documents remain evidence and standing founder authority remains effective.

Order of authority: explicit founder directives → live repository and immutable evidence → accepted architecture decisions in 08/CONTRACTS → gate and execution graph → task record → explanatory chapter. A contradiction stops only the affected task and produces a bounded reconciliation change. Repository behavior wins factual disputes; it does not silently change the target design.

The default product is a customer-operated Django/PostgreSQL modular monolith with one durable worker contract. React/TypeScript progressively replaces inherited screens. AI, vector search, OCR, voice, remote connections, agent execution, database workbench features, and advanced analytics are optional profiles. Local operation without those profiles must pass release tests.

Files in evidence/ are research and verification manifests. tasks/tasks.json contains 96 sealed parent work definitions; the Qudra execution-extension YAML files contain prospective child-work candidates only. SpecGrain nodes and execution graphs are planning state, never fabricated completion evidence. Every future path is explicitly prospective until created by its task. [DOMAIN_SCHEMAS.md](DOMAIN_SCHEMAS.md) fixes logical schemas and lifecycle invariants. [REVIEW_LOG.md](REVIEW_LOG.md) records ten planning review passes and the final challenge.

This plan supersedes incompatible intake labels and speculative completeness claims in earlier planning docs only after review and acceptance. It does not authorize a production deployment or certify Saudi regulatory compliance.