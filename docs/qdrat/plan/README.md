# Qdrat canonical implementation plan

Plan version: **1.0.0**, researched 20–21 September 2026. This directory is the proposed successor to the foundation roadmap. It describes target behavior, not shipped capability. Gate 0 is open; no implementation gate is certified by this planning change.

## Post-seal Intelligence Fabric amendment candidate

The sealed 1.0.0 plan remains the immutable parent snapshot. A later founder-directed planning amendment is carried in:

- [44_INTELLIGENCE_FABRIC_AMENDMENT.md](44_INTELLIGENCE_FABRIC_AMENDMENT.md)
- [45_INTELLIGENCE_SOURCE_INTAKE.md](45_INTELLIGENCE_SOURCE_INTAKE.md)

The amendment adds engine-independent Document Intelligence, Company Brain/RAG, **Qudra Business Decision**, Capability Fabric, local-first browser/research and additional execution backends using the newly authorized source set. It **does not change Gate 0 ordering or invalidate active G0 evidence**. Its obligations are inputs to future SpecGrain refinement of the existing G4/G7/G8/G9/G10/G11 nodes; any task that becomes too broad must split into child SpecNodes without weakening parent acceptance.

Read 00 (truth), 07–08 (product and architecture), CONTRACTS (normative interfaces), 39–42 (gates and execution), then 43 (Muse handoff). Research registers support decisions; they never grant runtime authority. Historical documents remain evidence and standing founder authority remains effective.

Order of authority: explicit founder directives → live repository and immutable evidence → accepted architecture decisions in 08/CONTRACTS → gate and execution graph → task record → explanatory chapter. A contradiction stops only the affected task and produces a bounded reconciliation change. Repository behavior wins factual disputes; it does not silently change the target design.

The default product is a customer-operated Django/PostgreSQL modular monolith with one durable worker contract. React/TypeScript progressively replaces inherited screens. AI, vector search, OCR, voice, remote connections, and advanced analytics are optional profiles. Local operation without those profiles must pass release tests.

Files in evidence/ are research and verification manifests. tasks/tasks.json contains 96 work definitions; SpecGrain nodes and the execution graph are planning state, never fabricated completion evidence. Every future path is explicitly prospective until created by its task. [DOMAIN_SCHEMAS.md](DOMAIN_SCHEMAS.md) fixes logical schemas and lifecycle invariants. [REVIEW_LOG.md](REVIEW_LOG.md) records ten planning review passes and the final challenge.

This plan supersedes incompatible intake labels and speculative completeness claims in earlier planning docs only after review and acceptance. It does not authorize a production deployment or certify Saudi regulatory compliance.
