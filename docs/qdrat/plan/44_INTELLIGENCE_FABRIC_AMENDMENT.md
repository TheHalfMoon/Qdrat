# Qdrat Intelligence Fabric amendment

Status: **PLANNING AMENDMENT CANDIDATE**

Parent plan: Qdrat canonical implementation plan **1.0.0** at `144935cd6bb64d3448ec3927fa7d1569bee93ca0`.

This amendment strengthens the existing plan without changing the current Gate 0 execution frontier. It does not rewrite the 96-node execution graph, reopen completed evidence, or authorize implementation ahead of dependencies. The requirements below become binding inputs when the affected SHAPED tasks are refined through SpecGrain.

## 1. Product decision

Qdrat remains a private, local-first Company Operating System. AI is not a separate product and no model, retrieval engine, browser, tool registry, or execution substrate becomes a second authority.

Add one shared optional **Qdrat Intelligence Fabric** with six replaceable planes:

1. **Document Intelligence** — parse/OCR/layout/table/form/image understanding into provenance-bearing document artifacts.
2. **Company Brain / Retrieval** — structured lookup, Company Twin graph, lexical search, optional semantic retrieval, reranking, temporal/event memory, and exact citations.
3. **Qudra Business Decision** — local evidence-backed business triage, recommendation, multi-option Decision Frontiers, simulation and bounded action across Qdrat domains.
4. **Capability Fabric** — one Qdrat-owned catalog for Actions, tools, skills, CLIs, MCP adapters and provider capabilities.
5. **Research / Browser Plane** — governed local-first web research, structured extraction, dataset construction and refresh.
6. **Execution Plane** — isolated agent execution by default, with separately authorized host-machine and cluster backends.

Every plane is optional. Qdrat must retain a supported no-AI/no-vector/no-browser/no-computer-control baseline.

## 2. Non-negotiable architecture laws

```text
MODEL != AUTHORITY
QUDRA_RECOMMENDATION != AUTHORIZATION
RAG_RESULT != TRUTH
TOOL_DISCOVERY != TOOL_PERMISSION
BROWSER_ACCESS != EGRESS_PERMISSION
HOST_ACCESS != SANDBOX
REMOTE_PROVIDER != SILENT_FALLBACK
VECTOR_INDEX != SOURCE_OF_TRUTH
GRAPH_PROJECTION != TRANSACTIONAL_AUTHORITY
AGENT_COMPLETION != TRUSTED_COMPLETION
```

PostgreSQL and Qdrat domain contracts remain authoritative. Graph, vector, Qudra recommendations, OCR, browser and agent outputs are evidence-bearing derived/proposal artifacts unless an existing Qdrat command/action contract explicitly commits them.

## 3. Local intelligence profiles and user choice

All Qdrat intelligence features are customer-controlled and local by architecture. The user can enable or disable Document Intelligence, Company Brain semantic retrieval, Qudra Business Decision, local browser research, local agents and explicit host capabilities independently.

Required local profiles:

| Profile | Intelligence egress | OCR | Retrieval | Qudra | Browser/research | Host computer |
|---|---|---|---|---|---|---|
| Air-gapped | DENY | local only | local only | local only | local/off | explicit local grants only |
| Local Core | DENY | optional local | structured/FTS | deterministic + small local decision engine | off | off |
| Local Standard | DENY | local | local hybrid | local decision + local LLM | local | ask/scoped |
| Local Pro | DENY | local best-qualified | local hybrid + reranker | local decision + local reasoning/simulation | local parallel research | scoped |
| Custom Local | DENY | explicit local provider | explicit local provider | explicit local provider | explicit local provider | explicit local grants |

There is no remote-model or remote-decision fallback in Qudra Business Decision.

External business APIs/connectors may still be used when a company explicitly configures them for normal business integration, but Qudra decision context, OCR, retrieval, reranking and reasoning stay inside customer-controlled Qdrat infrastructure.

Every local provider invocation should record, as appropriate:

- provider and exact engine/model version or digest;
- hardware/runtime profile;
- data classes used;
- latency/resource budget;
- evidence/provenance reference;
- whether the result is deterministic, probabilistic or generative.

See `46_QUDRA_BUSINESS_DECISION.md` for the complete product contract and `47_QUDRA_OPTION_ENGINE.md` for multi-objective option generation, Pareto filtering, sensitivity, reversibility and trade-off UX.

## 4. Document Intelligence

### 4.1 Contract

Extend the intent of G4-01 from generic extraction into a normalized document-understanding contract without changing its dependency position.

A derived document should be representable as:

```text
DocumentArtifact
  source_file_object
  source_digest
  parser_or_ocr_provider
  provider_version_or_digest
  language
  pages[]
  blocks[]
    block_type
    text
    bounding_box
    reading_order
    confidence
    source_span
  tables[]
  forms[]
  figures[]
  images[]
  markdown_or_text_projection
  warnings[]
  provenance
```

The original file remains immutable custody evidence. OCR/layout output is derivative and rebuildable.

### 4.2 Required behavior

- native text extraction before OCR when safe and sufficient;
- hostile/corrupt/oversize inputs remain quarantined;
- no parser/OCR network egress in local profiles;
- Arabic and English are first-class qualification languages;
- preserve page, region, table and form provenance where available;
- confidence is retained, not flattened into asserted truth;
- failed extraction never publishes a successful searchable revision;
- deletion/retention propagates to every derivative.

Cohere Parse and DeepSeek-class document understanding are **capability benchmarks**, not mandatory providers. The Qdrat contract must remain engine-independent.

## 5. Company Brain and RAG

G9-02 must implement **layered retrieval**, not a vector-database product.

Preferred retrieval order:

1. typed transactional/object lookup;
2. deterministic Company Twin / relationship traversal;
3. permission-aware PostgreSQL FTS / lexical search;
4. analytics/metric lookup where the question is numerical;
5. optional semantic/vector retrieval;
6. fusion/reranking;
7. bounded inference only after evidence retrieval.

Laya contributes useful patterns for cross-source context association, Coherence-style entity timelines, temporal summaries, hybrid lexical+semantic retrieval and user-correctable grouping. Qdrat must absorb those patterns into Qdrat-owned records rather than adopting Laya storage as a second authority.

Required retrieval evidence:

- source object and revision;
- source span/page/row where applicable;
- retrieval route;
- score/rank;
- freshness;
- access-policy decision;
- projection/index generation;
- conflict/uncertainty labels.

Embedding indexes remain rebuildable projections. Qdrat must work without pgvector or another vector service.

## 6. Qudra Business Decision

Add Qudra Business Decision as the Qdrat-owned local business decision capability under G9-01/G9-03, using typed probabilistic models only as one implementation technique.

```text
DecisionRequest
  decision_type
  state_reference_or_bounded_payload
  questions[]
  option_schema
  criteria
  confidence_policy
  data_class
  resource_budget

DecisionResult
  selected_option_or_score
  probabilities
  confidence
  calibration_metadata
  abstained
  engine
  engine_version_or_digest
  latency
  evidence_refs
```

Qudra may use local typed decision models for fuzzy, bounded business triage such as:

- routing and triage;
- priority/classification;
- entity-match suggestions;
- evidence-completeness triage;
- risk/review routing;
- enrichment-provider selection;
- lead/account scoring;
- support/work-item classification;
- low-cost guardrails before expensive agents.

Qudra's probabilistic engines must **not** decide deterministic facts such as hashes, balances, test pass/fail, schema validity, permissions, or whether a payment/payroll/employment action is authorized.

Candidate providers to benchmark behind the same contract:

- `Mapika/decider`;
- `TheoLeeCJ/SemIf`;
- `bespokelabs/Bespoke-Nimble-9B`;
- Jev/TypeSafe as a development/research benchmark reference only; it is not a Qudra runtime provider.

Do not hard-code a winner before G9-06/G11-03 measurements. Compare accuracy, calibration, abstention, Arabic/English behavior, latency, RAM/VRAM, startup cost and offline packaging. Runtime candidates must pass fully local qualification.

## 7. Capability Fabric

G9-03 and G8-07 must converge on one capability vocabulary rather than separate tool/MCP/plugin registries.

Adopt the strongest pattern from Treg: **ask for the capability, not the vendor**, while retaining Qdrat authority.

A capability descriptor should include:

```text
CapabilityDescriptor
  capability_id
  provider_id
  version
  input_schema
  output_schema
  read_write_class
  side_effect_class
  data_classes
  required_scopes
  execution_location
  offline_supported
  egress_destinations
  credentials_ref
  resource_budget
  monetary_cost_model
  replay_semantics
  idempotency_support
  approval_policy
  health
```

Provider selection can consider policy, data class, offline requirement, cost, latency, quality and health, but the selected provider may never widen the caller's grants.

Treg is a high-value donor/reference for:

- endpoint/CLI/skill catalog semantics;
- server-side credential injection;
- capability discovery;
- cost visibility;
- audit history;
- MCP exposure;
- local/self-hosted registry concepts.

Because Treg's public license has additional hosted-service restrictions, any copied path must bind the founder's separate authorization/grant evidence plus exact source provenance and notices.

## 8. Research and Browser Plane

G7-03 and G9-03 must support a local-first research path.

TinyFish/AgentQL/BigSet patterns are useful for:

- natural-language structured extraction;
- resilient semantic page targeting;
- multi-entity research fan-out;
- schema inference;
- evidence verification;
- deduplication;
- refresh cadence;
- structured dataset output.

Qdrat must not depend on TinyFish cloud for core local operation.

Required routing:

```text
native integration/API
  -> structured web protocol/selector
  -> local semantic browser
  -> visual interaction
  -> raw input only when explicitly allowed
```

Hosted TinyFish services are research references only for Qudra's intelligence runtime. Qdrat must implement or qualify a customer-controlled local research/browser path.

A research dataset row must retain source URLs/references, capture time, evidence spans/artifacts, confidence/verification state and refresh lineage.

## 9. Execution Plane

G9-04 remains Qdrat-owned and substrate-independent.

Provider classes:

| Provider | Intended role |
|---|---|
| OpenSandbox or smaller qualified sandbox | default isolated code/browser/file/tool execution |
| local container/process sandbox | lightweight single-server profile |
| Google AX | optional cluster/enterprise high-throughput agent workload backend |
| Desktop Commander local MCP patterns | explicit trusted-host capability adapter, not a sandbox |
| remote desktop relay | reference only; not a Qudra local intelligence runtime |

Google AX contributes Task/Workspace/Gateway/Model, egress fencing, resource quotas and suspend/resume patterns. It must not make Kubernetes mandatory for normal Qdrat installations.

Desktop Commander contributes mature filesystem/terminal/process/session patterns, bounded output, long-running process control and local audit. Its own documentation explicitly distinguishes guardrails from a sandbox; therefore Qdrat must never present a Desktop Commander-style host adapter as confinement.

Host capabilities require an explicit lease:

```text
HostCapabilityLease
  principal
  device
  allowed_roots
  allowed_commands_or_capabilities
  read_write_scope
  network_scope
  expiry
  purpose
  approval
  revocation_generation
```

No ambient shell, host socket, SSH key directory, browser profile, environment-secret access or unrestricted filesystem authority is granted by merely enabling an agent.

## 10. Intelligence UX

Laya's best product lesson is not its storage stack; it is the reduction of context switching.

Qdrat should extend existing Home / My Work / Inbox / object pages with an **Intelligence Inbox**:

- action cards that join company context before asking the user to act;
- daily/period briefings;
- entity timelines across Work, Service, People, CRM, Finance and Ops;
- related-context groups with manual merge/split correction;
- explanation of why an item is urgent or related;
- one-click open, investigate, draft, delegate or dismiss actions;
- agent session timeline and artifacts;
- cost/resource visibility;
- exact provider/egress badge when AI is used.

Do not create a second notification product. Intelligence cards are projections over existing Qdrat objects, events and permissions.

## 11. Source-specific adoption decisions

| Source | Qdrat role | Initial posture |
|---|---|---|
| `google/ax` | cluster agent execution and isolation/control-plane patterns | REFERENCE + optional execution backend; no mandatory Kubernetes |
| `superdesigndev/treg` | local capability/tool/CLI/skill registry and credential broker patterns | SELECTIVE_DONOR; founder grant evidence mandatory for copied hosted-service-restricted paths |
| `aayushch/laya` | Intelligence Inbox, Coherence/context association, hybrid search, agent workspace, budget UX | SELECTIVE_DONOR/REFERENCE |
| `TheoLeeCJ/SemIf` | local typed probability decisions | Qudra decision-engine provider/reference |
| `Mapika/decider` | trained local decision models and Jev-compatible System-One API pattern | Qudra decision-engine provider/dependency candidate |
| `bespokelabs/Bespoke-Nimble-9B` | local structured/evidence-grounded decision model candidate | Qudra local decision-model candidate |
| `tinyfish-io/*` | local web extraction/research patterns, AgentQL, live dataset workflows | SELECTIVE_DONOR/REFERENCE; remote services optional only |
| `wonderwhy-er/DesktopCommanderMCP` | local host filesystem/terminal/process capability patterns | SELECTIVE_DONOR/REFERENCE; never treated as sandbox |

## 12. Existing execution graph mapping

This amendment deliberately does not renumber the 96-task DAG.

| Existing task | Additional refinement obligation |
|---|---|
| G4-01 | normalized DocumentArtifact, OCR/layout/table/form derivatives and provenance |
| G4-02 | hybrid lexical/citation baseline remains first-class |
| G4-03 | Company Twin relationships become a retrieval route, never retrieval-only truth |
| G7-03 | capability-based enrichment waterfalls, TinyFish-style research datasets, cost/egress/verification |
| G8-07 | shared capability descriptors across SDK/webhook/MCP exposure |
| G9-01 | local model and **Qudra Business Decision** engine registry; no remote intelligence fallback |
| G9-02 | Company Brain layered retrieval, context association, temporal memory and citations |
| G9-03 | Treg-style capability catalog, skills/tools/CLI/MCP providers and bounded proposals |
| G9-04 | provider-neutral ExecutionRequest: OpenSandbox/local/AX/explicit host adapter |
| G9-05 | artifact custody, host/sandbox evidence, provider usage, kill/revocation |
| G9-06 | Arabic/English local LLM + Qudra decision + retrieval evaluation and calibration |
| G10-02 | offline OCR/embedding/reranker/Qudra decision/model packs with digests |
| G11-03 | measured provider-selection triggers and resource envelopes |

During refinement, any task that becomes too broad must split into child SpecNodes while preserving the parent acceptance requirements. No implementation should be pulled forward merely because this amendment exists.

## 13. Benchmark and promotion gates

Before a provider becomes a default, measure it on Qdrat-owned, rights-cleared workloads.

### Document intelligence
- Arabic/English OCR quality;
- reading order;
- tables/forms;
- layout grounding;
- scanned/rotated/noisy documents;
- latency and peak memory;
- offline package size.

### Retrieval
- Recall@k / MRR or task-appropriate retrieval metrics;
- citation correctness;
- permission leakage = zero on required corpus;
- stale/deleted source behavior;
- Arabic/English exact and semantic search;
- graph-vs-lexical-vs-vector ablations.

### Qudra Business Decision engines
- task accuracy/balanced accuracy as appropriate;
- calibration/ECE;
- abstention quality;
- Arabic/English;
- latency;
- RAM/VRAM;
- cold-start;
- model size;
- stability under option order and paraphrase perturbation.

### Tools/research/execution
- capability discovery precision;
- schema conformance;
- secret non-disclosure;
- egress policy;
- unknown-outcome handling;
- replay/idempotency;
- confinement;
- kill/revocation;
- crash/restart recovery.

A faster or larger model is not automatically preferred. Defaults are selected by measured profile-specific utility.

## 14. Security and privacy requirements

All retrieved/browser/document/tool/model output is untrusted data by default.

Required defenses include:

- prompt-injection and fake-policy corpora;
- data classification before model/tool egress;
- credential brokering rather than prompt-visible secrets;
- explicit local/remote provider identity;
- no remote provider in air-gapped mode;
- no implicit browser authentication reuse outside the selected profile;
- no tool output creating grants;
- bounded context and artifact retention;
- deletion propagation;
- audit of provider/model/tool version and effects;
- UNKNOWN_OUTCOME reconciliation for external writes;
- revocation/kill behavior that fences stale workers.

## 15. What this amendment intentionally rejects

- mandatory cloud AI;
- mandatory vector database;
- mandatory Kubernetes;
- a second workflow engine for agents;
- a second identity system for agents;
- vendor-specific domain models;
- unrestricted Desktop Commander-style host access;
- remote intelligence/decision fallback;
- replacing deterministic rules with probabilistic models;
- treating Qudra confidence as permission;
- treating OCR text or RAG passages as authoritative business facts;
- wholesale import of any donor.

## 16. Completion condition for this amendment

This amendment is planning-complete when:

1. source authorization/provenance entries exist;
2. donor/source roles are recorded;
3. future G4/G7/G8/G9/G10/G11 refinements explicitly incorporate these obligations;
4. no current Gate 0 implementation dependency is changed;
5. no source is declared selected without benchmark/qualification evidence.

Implementation remains governed by the canonical execution graph, SpecGrain, Diffcipline, exact-head evidence and independent review.
