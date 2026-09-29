# Qudra Fast Local Intelligence

Status: FOUNDER-DIRECTED TECHNICAL PLAN

Qudra should not send every item through the heaviest local reasoning path. Large business queues need a fast local sensory layer that cheaply narrows, labels, prioritizes and routes information before deeper analysis.

## 1. Fast-path architecture

```text
Authorized candidates
  -> deterministic / lexical prefilter
  -> local batch classifier
  -> confidence + uncertainty
  -> one of:
       ACCEPT FAST RESULT
       RETRIEVE MORE CONTEXT
       ESCALATE TO STRONGER LOCAL MODEL
       HUMAN REVIEW
```

There is no cloud escalation.

## 2. Qudra Classification Fabric

Canonical contracts:

```text
ClassificationRequest
  decision_type
  inputs[]
  labels[]
  instructions
  multi_label
  max_labels
  context_refs[]
  confidence_policy
  model_profile

ClassificationResult
  input_id
  labels[]
  probabilities{}
  confidence
  abstained
  engine
  engine_digest
  context_revision
  evidence_refs[]
```

Requirements:
- single-label and multi-label;
- stable input ordering;
- batching;
- calibrated confidence where supported;
- explicit abstention;
- local-only execution;
- no request-text persistence by default;
- Arabic and English qualification;
- deterministic schema validation;
- benchmarked thresholds per DecisionType, not one global threshold.

Useful Qudra applications include task routing, enquiry intent, case triage, search-result filtering, document classification, signal triage, duplicate-candidate filtering, review routing and evidence-worthiness.

## 3. Confidence Ladder

Qudra must treat confidence as routing evidence, not authority.

Example local ladder:

```text
FAST_LOCAL
  if confident -> return bounded classification
  else -> RETRIEVE_CONTEXT

RETRIEVE_CONTEXT
  rebuild local state/evidence
  -> FAST_LOCAL or DEEP_LOCAL

DEEP_LOCAL
  stronger local typed model / local LLM
  if still uncertain -> HUMAN_REVIEW
```

The ladder must be configurable by DecisionType, risk and business impact.

## 4. Semantic Filter

The jev_search pattern is useful when the candidate set is large.

Qudra adaptation:

1. enumerate only permission-authorized candidates;
2. use cheap deterministic/lexical scoring to prioritize;
3. chunk with provenance;
4. classify chunks locally in parallel;
5. keep high-confidence matches;
6. keep uncertain items when false negatives are costly;
7. preserve file/object/source references;
8. send only survivors to expensive local reasoning.

Never scan arbitrary host files merely because a model requests it. Candidate roots and object scopes come from Qdrat permissions/capability grants.

## 5. False-negative control

Filtering can be more dangerous than ranking because discarded evidence disappears.

Every filter profile must define:
- recall target;
- keep-when-uncertain behavior;
- maximum pruning ratio;
- protected source classes that cannot be pruned;
- audit sample of rejected candidates;
- benchmark corpus;
- rollback threshold.

For high-impact decisions, filtering should bias toward recall over precision.

## 6. Apple Silicon edge profile

laya-coreml demonstrates a useful optional runtime shape:
- Core ML packaging;
- Apple Neural Engine execution;
- offline model bundles;
- multilingual typed decisions;
- capacity errors instead of silent truncation;
- calibration-temperature safeguards;
- conversion-fidelity fixtures;
- measured latency and energy.

Qdrat should implement an optional CoreMLDecisionProvider behind the same local typed-decision contract used by CPU/GPU providers.

Core ML is not the canonical decision contract and must not make Apple hardware mandatory.

## 7. Runtime profile selection

Local runtime selection may consider:
- OS/architecture;
- CPU/GPU/ANE availability;
- RAM/VRAM;
- model size;
- context capacity;
- measured latency;
- measured calibration;
- energy/thermal budget where relevant.

Selection remains deterministic/policy-driven from qualified profiles. It does not silently download a model.

## 8. Durable agent operation boundary

Unreal Agent contributes a strong separation between model-produced tool requests and asynchronous execution.

Qdrat adaptation:

```text
Model / planner
  -> typed tool request
  -> pure translator / validator
  -> serializable Operation proposal
  -> Qdrat Action / Flow authorization
  -> Run / StepAttempt execution
  -> durable result
  -> model-facing formatted result
```

Required invariants:
- caller input has stable idempotency identity;
- accepted inputs are durably recorded;
- tool translation performs no hidden I/O;
- operations are versioned and serializable;
- execution state is separate from translation state;
- context builder records omitted/truncated/compacted material;
- recovery never assumes an operation completed when outcome is unknown;
- fork/replay uses Qdrat evidence and does not create a second source of truth.

## 9. Context omission record

Local models have finite context windows. Qudra must not hide truncation.

```text
ContextBuildResult
  included_refs[]
  omitted_refs[]
  truncated_refs[]
  compacted_refs[]
  token_or_capacity_budget
  reason_by_ref{}
  builder_version
```

Material decisions must expose insufficient-context conditions when omitted evidence could change the outcome.

## 10. Local batch surfaces

The classifier.dev product shape is useful as a UX/API benchmark.

Qdrat may expose the same local classification capability through:
- internal service API;
- REST/SDK;
- optional MCP;
- CLI;
- Studio formula/action;
- Flow step.

All surfaces call the same Qdrat-owned local Classification Fabric and permission model.

## 11. Feedback and eval loop

Borrow the useful idea of structured feedback/receipts:
- bad classification;
- missed evidence;
- wrong route;
- overconfident result;
- model/runtime fault;
- latency regression.

Feedback becomes local evaluation evidence, not automatic model/policy mutation.

## 12. Implementation binding

Add four child-work candidates:

- QD-F13 — Local Classification Fabric
- QD-F14 — Semantic Filter and Evidence Triage
- QD-F15 — Edge Decision Runtime Profiles
- QD-F16 — Durable Agent Operation Boundary

They are defined in 50_QUDRA_IMPLEMENTATION_PLAN.md and QUDRA_EXECUTION_EXTENSION.yaml.

## 13. Acceptance principles

- local intelligence only;
- no remote fallback;
- false-negative behavior measured;
- confidence calibrated/qualified per use case;
- no hidden context truncation;
- input redelivery idempotent;
- operations versioned and recoverable;
- Apple-specific acceleration optional;
- every fast-path result remains subordinate to Qdrat policy and evidence.
