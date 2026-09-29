# Qudra Local Reasoning Graph

Status: **FOUNDER-DIRECTED IMPLEMENTATION PLAN**

Source inspiration: `metadist/synaplan` at `e81eb3431deb3e242c3a114e8cbf08e2fbfd1e88` (Apache-2.0 + founder authorization).

Qudra needs a way to decompose complex local intelligence work into a directed graph without creating a second durable workflow engine. This document defines that boundary.

## 1. Architecture law

```text
Business Flow != Reasoning Graph
```

- **Qdrat Flow** owns durable business process, waits, approvals, side effects, retries and compensation.
- **Qudra Reasoning Graph** is an ephemeral/local analytical plan inside a DecisionCase, Run step or agent task.
- A Reasoning Graph cannot directly create external side effects.
- Any side effect must compile to a typed `CapabilityPlan` and pass normal Qdrat Action/Flow authorization.

## 2. ReasoningGraph contract

```text
ReasoningGraph
  graph_id
  objective
  context_revision
  nodes[]
  edges[]
  resource_budget
  deadline
  runtime_profile
  evidence_requirements[]
  status
  result_refs[]
```

Node types may include:
- retrieve;
- classify;
- extract;
- calculate;
- compare;
- decide;
- optimize;
- simulate;
- draft;
- verify;
- aggregate;
- ask_human.

No node type implies permission to execute a business effect.

## 3. Node contract

```text
ReasoningNode
  node_id
  node_type
  input_refs[]
  output_schema
  required_capabilities[]
  engine_requirements
  quality_threshold
  max_context
  time_budget
  resource_budget
  cache_policy
  evidence_policy
  state
```

## 4. Local model/router

Synaplan's task-specific model routing is useful, but Qudra is local-only. Add a **Local Engine Router** that chooses the smallest qualified local engine capable of satisfying each node.

Selection factors:
- task/node type;
- Arabic/English support;
- context capacity;
- structured-output support;
- calibration requirement;
- installed model/runtime;
- hardware profile;
- measured quality;
- latency budget;
- memory/VRAM/ANE budget;
- energy/thermal profile where relevant;
- current health/readiness.

No remote fallback is allowed.

## 5. Model Capability Inventory

```text
LocalEngineProfile
  engine_id
  engine_type
  model_digest
  runtime_digest
  platform
  hardware_requirements
  languages[]
  context_capacity
  supported_node_types[]
  structured_output
  calibration_profile
  benchmark_profile
  memory_budget
  readiness
  health
  last_qualified_at
```

Readiness states:
- NOT_INSTALLED;
- INSTALLED;
- VERIFYING;
- READY;
- DEGRADED;
- UNAVAILABLE;
- INCOMPATIBLE.

## 6. Readiness before routing

A model appearing in configuration is not proof it can run.

Before selection Qudra verifies:
- model artifact exists;
- digest matches;
- runtime exists;
- hardware requirement fits;
- tokenizer/adapter assets exist;
- health probe passes;
- required context capacity fits;
- DecisionType qualification allows the engine.

## 7. DAG execution semantics

Reasoning nodes execute only when dependencies are satisfied.

Required behaviors:
- bounded parallelism;
- cancellation;
- node timeout;
- deterministic cache key where safe;
- failure propagation;
- explicit partial results;
- node-level provenance;
- progressive UI updates;
- resource accounting;
- no hidden retry of uncertain external work because external work is not executed here.

## 8. Progressive intelligence UX

For complex decisions, users may see live task cards such as:

```text
✓ Gather account context
✓ Check contract terms
✓ Calculate delivery capacity
● Compare recovery options
○ Verify policy constraints
○ Build Decision Frontier
```

The UI must distinguish analysis progress from business action progress.

## 9. Local resource accounting

Every graph/node may record:
- wall time;
- CPU/GPU/ANE time where measurable;
- peak memory/VRAM class;
- token/context count;
- model calls;
- cache hits;
- artifact bytes.

This supports routing and capacity planning even when monetary model cost is zero.

## 10. Optional sidecars

Synaplan demonstrates a useful pattern: optional capabilities should remain genuinely optional.

Examples in Qdrat:
- local vector service;
- OCR/document parser;
- office conversion;
- local speech/ASR/TTS;
- browser runner;
- sandbox service;
- graph engine;
- optimization service.

A disabled/unhealthy sidecar must:
- not render controls that imply it works;
- not cause unrelated core features to fail;
- publish capability health;
- have explicit fallback/degraded behavior;
- be independently upgradeable where architecture permits.

## 11. Sidecar contract

```text
LocalServiceCapability
  service_id
  version
  capabilities[]
  endpoint_ref
  required_network_scope
  artifact_digests[]
  health_probe
  readiness
  resource_requirements
  data_classes
  retention_behavior
  backup_behavior
```

## 12. Air-gap deployment

Qudra local intelligence must have a complete offline profile:
- pinned images/packages;
- model/tokenizer/runtime bundles;
- OCR/embedding/reranker/decision artifacts;
- solver artifacts;
- plugin/capability packs;
- license/notice inventory;
- checksums/signatures;
- network-disabled install/start test;
- model readiness verification without downloads.

## 13. MCP/OpenAPI/plugin surfaces

Synaplan validates the value of OpenAPI, MCP server/client and non-invasive plugins. Qdrat already has Capability Fabric and SDK/API plans; therefore:
- MCP server/client are adapters to Capability Fabric;
- plugins register capabilities/UI contributions under policy;
- OpenAPI remains generated from Qdrat-owned contracts;
- no plugin gets ambient database/filesystem/network authority.

## 14. Local RAG/document/speech convergence

Qudra should use the same local engine inventory/readiness model for:
- embeddings/rerankers;
- OCR/document understanding;
- ASR/TTS;
- decision models;
- local LLMs.

This prevents each feature from inventing its own model lifecycle.

## 15. Routing quality

A smaller/faster engine is preferred only when it meets the node quality threshold.

Qualification metrics include:
- task accuracy;
- calibration;
- citation correctness;
- Arabic/English quality;
- structured-output validity;
- latency;
- resource use;
- stability.

Router decisions must be explainable and reproducible from the recorded profile/revision.

## 16. Failure states

Explicit states include:
- NO_QUALIFIED_LOCAL_ENGINE;
- ENGINE_NOT_READY;
- CONTEXT_TOO_LARGE;
- NODE_TIMEOUT;
- NODE_FAILED;
- PARTIAL_GRAPH_RESULT;
- REQUIRED_SIDECAR_UNAVAILABLE;
- BUDGET_EXHAUSTED;
- HUMAN_INPUT_REQUIRED.

No state silently invokes a cloud engine.

## 17. Source adoption boundaries

Selectively adapt Synaplan patterns for:
- DAG task decomposition;
- per-task model choice;
- model inventory/readiness;
- progressive execution UX;
- self-hosted/air-gap lifecycle;
- optional sidecar behavior;
- plugin/OpenAPI/MCP patterns;
- local RAG/document/speech integration lessons.

Do not import:
- remote-provider fallback into Qudra intelligence;
- a second workflow/action authority;
- Synaplan-specific tenant/data model as Qdrat authority;
- provider secrets into model context.

## 18. Parent-plan binding

Implementation work is pre-shaped as QD-F23 through QD-F25 in the extension plan and remains dependency-bound to Qudra engine registry, Fast Triage, Capability Fabric, Execution Plane, offline bundles and performance qualification.
