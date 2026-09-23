# Qudra Implementation Plan

Status: IMPLEMENTATION-READY AMENDMENT PLAN

This plan turns the Qudra product architecture into bounded work packages. It does not modify or bypass the sealed 96-node canonical DAG. Each package below is a pre-shaped child-work candidate that must be converted into real SpecGrain child nodes when its parent dependencies are satisfied.

## 1. Canonical contracts

The implementation must converge on the following Qdrat-owned contracts:

- DecisionType
- DecisionCase
- DecisionFact
- DecisionUncertainty
- ObjectiveProfile
- ConstraintSet
- BusinessOption
- OptionSet / Decision Frontier
- BusinessCapability
- CapabilityPlan
- Scenario
- OptimizationProblem / OptimizationResult
- ProcessEvent / ProcessProjection
- BusinessSignal
- DecisionOutcome
- DecisionPolicy
- DecisionEvaluationPack

These contracts must use existing Qdrat principal, object, event, action, policy, approval, audit and evidence vocabulary.

## 2. Foundation work packages

### QD-F01 — Decision contracts and storage
Parents: G3-06, G4-03, G8-01.

Deliver:
- versioned DecisionType and DecisionCase schema;
- facts/uncertainties/evidence references;
- status machine;
- ObjectiveProfile and ConstraintSet;
- deletion/retention behavior;
- event/audit emissions.

Acceptance:
- migrations use expand-contract and have rollback/recovery notes;
- tenant and permission isolation tests pass;
- context revisions bind to exact object revisions;
- no model field creates authority;
- Arabic/English labels supported;
- stale DecisionCases cannot silently execute.

### QD-F02 — Capability Graph
Parents: G8-07, G9-03.

Deliver:
- BusinessCapability registry;
- structural and semantic local search;
- provider health;
- local credential references;
- policy eligibility;
- capability packs;
- signed install/update/remove metadata.

Acceptance:
- discovery cannot widen scopes;
- unhealthy or disabled capability is excluded;
- raw secrets never enter model context;
- provider swap preserves capability contract;
- every capability declares side effects, risk, idempotency and evidence contract.

### QD-F03 — Local Qudra decision-engine adapters
Parent: G9-01.

Deliver:
- common typed local decision interface;
- Decider adapter candidate;
- SemIf adapter candidate;
- Bespoke Nimble adapter candidate where hardware/profile qualifies;
- abstention and calibration contract;
- profile-specific model packaging metadata.

Acceptance:
- fully offline fixture execution;
- deterministic input/output schema validation;
- option-order and paraphrase robustness pack;
- Arabic/English benchmark;
- engine failure never invokes remote fallback;
- every output records engine/model digest.

### QD-F04 — Option Engine core
Parents: QD-F01, QD-F02, QD-F03.

Deliver:
- hard-constraint filter;
- preference/objective model;
- candidate option normalization;
- Pareto filtering;
- dominated-option detection;
- diversity checks;
- frontier labels;
- evidence coverage;
- uncertainty model;
- no-action and collect-evidence options.

Acceptance:
- ineligible options can never rank;
- duplicate/cosmetic alternatives collapse;
- hard constraints and preferences are structurally distinct;
- score decomposition is reproducible;
- model judgement remains separable from deterministic calculations;
- stale context invalidates the option set before action.

### QD-F05 — Scenario engine
Parent: QD-F04.

Deliver:
- baseline/scenario revisions;
- deterministic what-if;
- bounded uncertain inputs;
- sensitivity;
- best/expected/plausible-worst reporting;
- break-even support;
- zero production mutation.

Acceptance:
- scenario cannot commit Actions;
- facts, assumptions, forecasts and model estimates are structurally distinct;
- same scenario revision is replayable;
- changed assumptions identify which recommendation changed and why.

### QD-F06 — Optimization adapter
Parents: G6-02, G7-07, QD-F04.

Deliver:
- OptimizationProblem / OptimizationResult;
- local solver adapter;
- assignment/scheduling/resource-allocation baseline;
- infeasibility explanation;
- multiple feasible frontier solutions where relevant.

Leading candidate: Google OR-Tools after source qualification.

Acceptance:
- hard constraints never silently relax;
- infeasible is a first-class result;
- solver version, seed, runtime and objective values captured;
- deterministic fixture suite;
- timeout returns bounded partial/no-solution state rather than fabricated optimum;
- human/alternative plan remains valid fallback.

### QD-F07 — Process Intelligence
Parents: G3-07, G6-07, QD-F01.

Deliver:
- ProcessEvent projection;
- process variants;
- wait/rework/loop analysis;
- conformance;
- bottleneck/opportunity records;
- process-to-DecisionCase link.

Acceptance:
- projection rebuildable from authoritative evidence;
- source-event links complete;
- process-mining output cannot mutate source records;
- permission-aware views;
- conformance distinguishes published process revision.

### QD-F08 — Outcome and calibration store
Parent: QD-F04.

Deliver:
- selected/rejected options;
- user override reason;
- actual cost/time/outcome;
- confidence/calibration;
- model and policy revisions;
- local comparison by DecisionType.

Acceptance:
- outcome collection is purpose-controlled;
- no sensitive training by default;
- deletion/retention propagates;
- historical outcomes never silently change policy;
- outcome and human choice are distinct.

### QD-F09 — Decision Studio
Parents: G8-04, QD-F01, QD-F02, QD-F04.

Deliver:
- DecisionType editor;
- context-source selection;
- hard constraints;
- objectives;
- option generators;
- allowed capabilities;
- rubrics;
- local model profile;
- scenario variables;
- approval/autonomy mode;
- outcome metrics;
- evaluation fixtures;
- version publishing.

Acceptance:
- draft/simulate/publish lifecycle;
- incompatible changes detected;
- rollback to prior published version;
- unavailable scopes/capabilities block publication;
- every published DecisionType has an evaluation pack.

### QD-F10 — Shared Qudra UX
Parents: G6-04, QD-F04.

Deliver reusable:
- Action Card;
- Decision Frontier;
- Compare Options;
- Evidence Drawer;
- What-If;
- Decision Room;
- Approval;
- Outcome Review;
- Business Inbox projections.

Acceptance:
- Arabic/English and RTL/LTR parity;
- keyboard/accessibility;
- evidence and uncertainty visible;
- user can choose a non-recommended eligible option;
- destructive/high-impact actions have preview;
- recommendation labels never hide hard constraints.

### QD-F11 — Local Decision-to-Action compiler
Parents: QD-F02, QD-F04, G3-05.

Deliver:
- natural business intent to structured objective;
- eligible capability-set resolution;
- bounded local plan generation;
- typed CapabilityPlan validation;
- preview and approval handoff to Flow/Actions.

Acceptance:
- generated plan cannot bypass capability eligibility;
- every step re-authorized at execution time;
- unknown/unhealthy capability blocks or triggers explicit alternative planning;
- external writes use idempotency/reconciliation semantics.

### QD-F12 — Decision learning and playbook promotion
Parents: QD-F07, QD-F08, G3-06.

Deliver:
- repeated-pattern detection;
- candidate playbook;
- human review;
- deterministic Rule/Flow conversion;
- shadow validation;
- promotion/versioning;
- rollback.

Acceptance:
- no self-modifying production policy;
- promotion requires fixtures and accepted evidence;
- degraded outcomes can disable/revert the playbook;
- original decision history preserved.

### QD-F13 — Local Classification Fabric
Parent: G9-01.
Depends on: QD-F03.

Deliver:
- ClassificationRequest / ClassificationResult;
- single-label and multi-label local classification;
- batching;
- calibrated confidence / abstention;
- local Confidence Ladder;
- REST/SDK/MCP/CLI adapters through Qdrat API conventions;
- evaluation and feedback receipts.

Acceptance:
- fully offline execution;
- stable input ordering;
- per-DecisionType thresholds;
- Arabic/English qualification;
- no request-text persistence by default;
- low confidence escalates only to more local context/model or human review;
- no cloud fallback.

### QD-F14 — Semantic Filter and Evidence Triage
Parents: G4-02, G9-02.
Depends on: QD-F13.

Deliver:
- permission-aware candidate enumeration;
- deterministic/lexical first-pass priority;
- provenance-bound chunking;
- local parallel classification;
- keep-when-uncertain policy;
- rejected-candidate audit sampling;
- search/backlog/log/document filtering adapters.

Acceptance:
- permission checks occur before content evaluation;
- false-negative benchmark and recall target;
- protected source classes cannot be silently pruned;
- uncertain evidence retained for high-impact decisions;
- no arbitrary host scan;
- every retained result cites source/object span.

### QD-F15 — Edge Decision Runtime Profiles
Parents: G9-01, G10-02, G11-03.
Depends on: QD-F03.

Deliver:
- replaceable local runtime profile contract;
- optional Core ML / Apple Neural Engine provider;
- CPU/GPU local provider compatibility;
- offline model bundle metadata;
- capacity/error contract;
- calibration and conversion-fidelity evidence.

Acceptance:
- Apple-specific acceleration is optional;
- runtime profile chosen from measured qualified hardware;
- model/tokenizer/runtime digests bound;
- over-capacity requests fail explicitly rather than silently truncate;
- calibration safeguards tested;
- no on-demand network model download in offline profiles.

### QD-F16 — Durable Agent Operation Boundary
Parents: G3-02, G9-04, G9-05.
Depends on: QD-F02.

Deliver:
- stable input deduplication identity;
- pure tool-call translator contract;
- serializable/versioned Operation proposal;
- mapping into Qdrat Run / StepAttempt;
- context omission/truncation record;
- recovery/fork/replay rules;
- model-facing result formatter.

Acceptance:
- redelivered external input is idempotent;
- translation performs no hidden I/O;
- operation state is distinct from tool-translation state;
- UNKNOWN_OUTCOME never becomes blind retry;
- omitted/truncated context is inspectable;
- no second workflow/session authority is created.

## 3. Domain packs

### QD-D01 — Work Decision Pack
Parents: G6-03, QD-F06, QD-F10.
Includes Task Intake, Scheduler, Resource Optimizer, Project Rescue, Portfolio Optimizer, Meeting-to-Decision.

### QD-D02 — Service Decision Pack
Parents: G6-07, QD-F10.
Includes Client Enquiry, Case Router, Response Options, SLA Rescue, Incident Commander, Problem Finder.

### QD-D03 — Customer/CRM Decision Pack
Parents: G7-04, QD-F10.
Includes Account Brief, Customer Rescue, Renewal Advisor, Deal Desk, Pricing Options, Next Best Action.

### QD-D04 — Finance Decision Pack
Parents: G7-08, QD-F05, QD-F10.
Includes Cash Priority, Collections, Expense Exception, Reconciliation Exception, Budget Reallocator, Cashflow Scenario.

### QD-D05 — Procurement Decision Pack
Parents: G7-07, QD-F06, QD-F10.
Includes Purchase Advisor, Vendor Compare, Vendor Negotiator, Supplier Risk, Renew/Replace.

### QD-D06 — People Decision Pack
Parents: G4-12, QD-F06, QD-F10.
Includes Workforce Planner, Shift Scheduler, Onboarding Rescue, Offboarding Assurance, Skills Gap, Leave Impact, Hiring Support.

Hard rule: consequential employment decisions remain human-controlled and cannot be promoted to autonomous execution.

### QD-D07 — Ops Decision Pack
Parents: G7-10, QD-F06, QD-F10.
Includes Maintenance Advisor, Asset Advisor, Facility Scheduler, Service Impact, Capacity Planner.

### QD-D08 — Trust Decision Pack
Parents: G5-06, QD-F10.
Includes Access Review, Policy Impact, Compliance Evidence, Security Triage, Change Risk.

### QD-D09 — Executive Decision Pack
Parents: QD-D01 through QD-D08, QD-F07.
Includes Operating Brief, Executive Decision Room, Strategic Portfolio, Business Pulse.

## 4. Rollout packages

### QD-L01 — Observe and Shadow
Run Qudra locally without affecting business workflows. Compare recommendations with human decisions and actual outcomes.

### QD-L02 — Recommend
Expose options and evidence; no side effects.

### QD-L03 — Prepare
Allow drafts, previews, simulations and proposed CapabilityPlans.

### QD-L04 — Execute Bounded
Only for explicitly qualified low-risk actions with normal Qdrat authorization, idempotency, approval, kill/revocation and exact evidence.

### QD-L05 — Playbook Promotion
Turn repeated proven patterns into versioned deterministic Rules/Flow after human review and simulation.

No domain skips directly to QD-L04.

## 5. Representative API/service capabilities

Exact REST paths remain subordinate to G8-07 conventions, but the service contract must support:
- create/read/list DecisionCase;
- build/rebuild context;
- generate OptionSet;
- compare/recompute under an ObjectiveProfile;
- create Scenario;
- solve OptimizationProblem;
- preview CapabilityPlan;
- approve/select BusinessOption;
- execute selected plan through Action/Flow;
- submit OutcomeReview;
- query ProcessProjection;
- simulate/publish DecisionType.

## 6. Explicit failure states

Use explicit states such as:
- INSUFFICIENT_EVIDENCE;
- CONFLICTING_EVIDENCE;
- NO_FEASIBLE_OPTION;
- POLICY_INDETERMINATE;
- LOCAL_ENGINE_UNAVAILABLE;
- SOLVER_INFEASIBLE;
- SOLVER_TIMEOUT;
- CAPABILITY_UNHEALTHY;
- APPROVAL_REQUIRED;
- STALE_CONTEXT;
- STALE_OPTION_SET;
- EXECUTION_UNKNOWN_OUTCOME;
- OUTCOME_NOT_OBSERVED.

Never map these to a confident recommendation.

## 7. Version binding

Bind every OptionSet and CapabilityPlan to:
- DecisionType revision;
- policy revision;
- source object/context revisions;
- model/engine versions;
- capability versions;
- objective profile;
- solver version;
- retrieval/index generation where relevant.

Before execution, revalidate stale bindings.

## 8. Security and privacy

Mandatory:
- local-only Qudra intelligence;
- permission enforcement before retrieval;
- no prompt-visible raw secrets;
- side-effect classification;
- approval and purpose checks;
- policy recheck at action time;
- untrusted-content/prompt-injection treatment;
- sandbox vs host separation;
- immutable evidence links;
- retention/deletion propagation;
- no protected-trait inference;
- no model confidence as authorization.

## 9. Evaluation matrix

### Decision quality
- feasible-option recall;
- hard-constraint violation rate = 0;
- dominated-option rate;
- option diversity;
- recommendation calibration;
- abstention quality.

### Retrieval/evidence
- citation correctness;
- evidence coverage;
- permission leakage = 0;
- stale/deleted-source behavior.

### Optimization
- feasibility correctness;
- objective correctness;
- runtime by problem size;
- infeasibility explanation quality.

### Process intelligence
- event linkage completeness;
- bottleneck validity;
- conformance correctness;
- false automation-opportunity rate.

### Business outcome
- time to decision;
- time to resolution;
- override rate;
- reopened work;
- SLA outcomes;
- estimated vs actual cost/time;
- regret/outcome quality.

### UX
- comprehension of trade-offs;
- successful alternative selection;
- accessibility;
- Arabic/RTL parity.

## 10. Operational readiness

Before a Decision Pack is production-enabled:
- offline model/solver bundle exists;
- local health diagnostics exist;
- resource budget is measured;
- backup/restore covers DecisionCase and outcome evidence;
- derived indexes/projections are rebuildable;
- upgrade compatibility defined;
- failure-mode runbook exists;
- shadow/recommend evidence accepted;
- security review bound to exact revision.

## 11. Parent-plan integration rule

These QD work packages are not independently authorized around current dependencies. When the named parents become accepted, refine each package into real SpecGrain child nodes against the then-live repository state.

If a canonical parent task already contains the same scope, merge the obligations rather than duplicating runtime systems.
