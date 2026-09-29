# Source Intake — DBX, Paperclip and Synaplan

Status: **RESEARCH / INTAKE RECORD**

Research date: 2026-09-29.

The founder has standing authorization to use/copy/adapt these sources. This record fixes the researched upstream revisions and architecture disposition; actual copied paths must still be recorded exactly when intake occurs.

## 1. t8y2/dbx

Research revision: `4269a61e2cf6c19afdcaba41fed1e57d6e5e3512`

Observed public license: Apache-2.0.

Observed high-value capabilities/patterns:
- broad heterogeneous database support;
- source-specific workspaces rather than one generic SQL box;
- query editor and object/source tooling;
- database/schema search;
- ER diagrams;
- schema diff;
- field lineage;
- CSV/Excel/SQL import/export and cross-engine transfer;
- connection/tunnel patterns;
- AI assistant and MCP exposure;
- plugin connection actions.

Qdrat destination:
- Data Fabric workbench;
- DataSchemaSnapshot;
- governed DataQueryPlan;
- schema/field lineage;
- DataSource capability matrix;
- import/export/transfer Runs;
- SDK/MCP data capabilities.

Do not inherit:
- a separate DataSource/credential authority;
- unrestricted DB admin actions;
- DBX app state as Qdrat truth;
- ambient database access for agents.

Initial code-intake posture: **STRONG_SELECTIVE_DONOR / REFERENCE**.

## 2. paperclipai/paperclip

Research revision: `24beb005755465f71a19ec92a85da0958d1b9740`

Observed public license: MIT.

Observed high-value capabilities/patterns:
- agent task management tied to organizational goals;
- mixed human/agent organizational roles;
- atomic task checkout/locking;
- persistent agent state;
- scheduled heartbeats/routines;
- budget and cost hard stops;
- approval/governance controls;
- skill studio/evaluations;
- sandbox/runtime integrations;
- scoped secrets;
- activity/audit and work products;
- portable company/team templates;
- multi-organization isolation.

Qdrat destination:
- AgentProfile over Principal;
- Goal Graph projection;
- WorkLease;
- DutyCycle;
- local AgentResourceBudget;
- AgentSkill lifecycle and evaluation packs;
- Agent Workforce management UX;
- portable team packs;
- persistent Run recovery semantics.

Do not inherit:
- a separate org chart, ticket system, identity system or workflow authority;
- legal-employment semantics for agents;
- provider/cloud assumptions incompatible with Qudra local-only intelligence;
- automatic supervisor privilege expansion.

Initial code-intake posture: **STRONG_SELECTIVE_DONOR / REFERENCE**.

## 3. metadist/synaplan

Research revision: `e81eb3431deb3e242c3a114e8cbf08e2fbfd1e88`

Observed public license: Apache-2.0.

Observed high-value capabilities/patterns:
- self-hosted and air-gapped AI platform design;
- DAG task decomposition/routing;
- per-task model choice;
- local model via Ollama and provider abstraction;
- local RAG/document processing/transcription/speech;
- progressive task cards;
- model/provider setup and readiness;
- optional building blocks/sidecars;
- plugin system;
- OpenAPI;
- MCP server and client;
- deployment/update/rollback discipline;
- local model availability/readiness refresh.

Qdrat destination:
- non-side-effecting ReasoningGraph;
- ReasoningNode;
- Local Engine Router;
- LocalEngineProfile/readiness inventory;
- optional LocalServiceCapability sidecars;
- progressive intelligence UX;
- complete air-gap capability bundle;
- unified local engine lifecycle for LLM/decision/OCR/RAG/voice.

Do not inherit:
- remote-provider fallback for Qudra;
- a second durable workflow/action authority;
- Synaplan tenant/data model as Qdrat authority;
- separate plugin permissions outside Capability Fabric.

Initial code-intake posture: **STRONG_SELECTIVE_DONOR / REFERENCE**.

## 4. Combined architecture synthesis

The strongest combined design is:

```text
Data Fabric / Data Workbench
        |
        v
Company Brain + Goal Graph
        |
        v
Qudra DecisionCase
        |
        v
Reasoning Graph (local, analytical, no side effects)
        |
        +--> Fast Classification / Typed Decisions
        +--> Retrieval / Data Query
        +--> Optimization / Simulation
        +--> Stronger Local Reasoning
        |
        v
Decision Frontier / CapabilityPlan
        |
        v
Principal + Policy + Approval
        |
        v
Flow / Action / WorkLease
        |
        v
Agent Workforce / Execution Plane
        |
        v
Evidence + Outcome + Evaluation
        |
        v
Playbook / Rule promotion after review
```

This composition preserves one business authority while adding better data access, better agent management and better local reasoning efficiency.

## 5. Intake gate for copied code

For every copied component from these repositories, persist:
- upstream repository and exact commit/tag;
- original path;
- destination path;
- license/notice;
- modifications;
- transitive dependencies;
- security review;
- data/network behavior;
- relevant tests/evaluation;
- update/removal strategy;
- exact Qdrat revision that qualified it.
