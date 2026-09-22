# Qudra Optimization, Simulation and Process Intelligence

Status: FOUNDER-DIRECTED TECHNICAL PLAN

Qudra needs more than generative reasoning. Many best-option problems are constraint, optimization, process or causal questions that should be solved with deterministic or analytical local methods.

## 1. Three complementary engines

### Local judgement
Typed local decision models classify, score and rank bounded fuzzy choices.

### Local optimization
Mathematical and constraint solvers find feasible or optimal assignments, schedules, routes, allocations and portfolios.

### Local process intelligence
Event evidence reconstructs how work actually flows, where it deviates, and which bottlenecks or repeated exceptions deserve improvement.

A local LLM may explain, generate candidate structures or translate user intent, but it does not replace these engines.

## 2. Optimization contract

~~~text
OptimizationProblem
  problem_type
  subject_refs[]
  decision_variables[]
  hard_constraints[]
  soft_constraints[]
  objectives[]
  preference_profile
  current_state_revision
  scenario_inputs
  time_limit
  solution_limit
  solver_profile
  evidence_refs[]

OptimizationResult
  status
  feasible
  solutions[]
  objective_values
  constraint_slacks
  infeasibility_explanation
  runtime
  solver
  solver_version
  deterministic_seed
  evidence
~~~

Supported problem families should include:
- assignment;
- workforce scheduling;
- task/resource scheduling;
- capacity allocation;
- project portfolio selection;
- procurement allocation;
- facility/resource reservation;
- routing where Qdrat has an approved use case;
- budget allocation;
- inventory/maintenance planning.

google/or-tools is a strong Apache-2.0 candidate for a local solver adapter, especially CP-SAT, assignment, routing and scheduling. Qdrat must keep the solver contract replaceable.

## 3. Infeasibility is a product feature

If constraints make a problem impossible, Qudra must not fabricate a schedule or silently break a rule.

Return:
- which constraints conflict;
- minimal or bounded relaxation candidates where possible;
- business impact of each relaxation;
- who may approve a policy exception, if any;
- collect-more-evidence option where the conflict may be data quality.

## 4. Scenario engine

~~~text
Scenario
  baseline_revision
  variables{}
  assumptions[]
  deterministic_changes[]
  uncertain_inputs[]
  horizon
  comparison_metrics[]
  result
  sensitivity
  evidence
~~~

Support:
- deterministic what-if;
- bounded ranges;
- local Monte Carlo where justified;
- best, expected and plausible-worst cases;
- sensitivity/tornado analysis;
- break-even analysis.

Do not present model-generated numeric forecasts as deterministic calculations.

## 5. Forecasts

Forecasting is optional and local. Every forecast must expose:
- training/data window;
- freshness;
- target;
- horizon;
- error metrics;
- confidence interval where appropriate;
- model version;
- major known limitations.

Forecasts may support options but may not silently become facts.

## 6. Process Event Backbone

Qdrat already has events, Runs, WorkItems, Cases, approvals and audit. Build process intelligence from those authoritative records rather than a second event warehouse by default.

~~~text
ProcessEvent
  process_type
  case_ref
  activity
  timestamp
  actor_or_principal
  object_refs[]
  source_event_ref
  state_before_ref
  state_after_ref
  duration_or_wait
  outcome
  policy_revision
~~~

Process projections are derived and rebuildable.

## 7. Qudra Process Doctor

Local process intelligence should answer:
- how does this process actually run;
- where do cases wait;
- where do they loop;
- which handoffs fail;
- which approvals create delay;
- where rework occurs;
- which variants correlate with better outcomes;
- which policies are frequently overridden;
- which automation candidates repeat.

Outputs:
- process map;
- variant distribution;
- bottlenecks;
- conformance deviations;
- rework/loop hotspots;
- SLA delay contributors;
- automation/playbook candidates;
- evidence-linked affected cases.

Celonis-style process-intelligence ideas are useful benchmarks. PM4Py is a public AGPL-3.0 reference candidate and should remain reference or isolated unless exact license/grant posture justifies deeper reuse.

## 8. Conformance

A published Flow or Playbook can define the expected process. Qudra compares observed ProcessEvents against that model and classifies:
- conformant;
- allowed variant;
- missing step;
- unexpected step;
- order violation;
- repeated/rework;
- policy override;
- stalled.

Conformance never retroactively changes history.

## 9. Improvement loop

~~~text
Observed process
  -> bottleneck/deviation
  -> opportunity
  -> DecisionCase
  -> options
  -> simulate/optimize
  -> human approval
  -> Flow/Rule/Playbook version
  -> shadow measurement
  -> publish
  -> monitor outcome
~~~

This is how Qdrat becomes more organized over time.

## 10. Causal caution

Historical correlation is not proof that an intervention caused an outcome.

For claims such as:
- discount caused renewal;
- extra engineer reduced delay;
- this workflow improves retention;

Qudra must label observational associations as such.

Optional local causal-analysis adapters may help when the data and assumptions support them. py-why/dowhy is an MIT public reference/dependency candidate. Any causal estimate must record the causal question, graph and assumptions, treatment/outcome, identification method and sensitivity/refutation evidence.

No causal method should be exposed as magic certainty.

## 11. Experiments and shadow mode

Qudra should support local controlled experiments where appropriate:
- shadow recommendation vs actual human decision;
- A/B process variant;
- canary playbook;
- staged rollout;
- holdout where ethically and operationally appropriate.

Protected or high-impact employment decisions, safety, legal entitlement, security access and similar domains require stricter controls and may forbid automated experimentation.

## 12. Decision economics

For each material option, Qudra may model:
- implementation cost;
- recurring cost;
- opportunity cost;
- expected benefit;
- downside;
- switching cost;
- reversibility;
- time to value;
- evidence confidence.

Do not use expected value alone when tail risk, hard constraints or irreversibility dominate.

## 13. Robustness

For uncertain decisions, test whether the recommendation survives plausible changes to:
- demand;
- capacity;
- cost;
- timeline;
- failure probability;
- customer value;
- supplier lead time;
- forecast error.

Prefer robust options when the nominal optimum is fragile and the business priority favors resilience.

## 14. Source posture

- google/or-tools — DISCOVERED_PUBLIC_SOURCE; Apache-2.0; strong local solver dependency candidate.
- process-intelligence-solutions/pm4py — DISCOVERED_PUBLIC_SOURCE; AGPL-3.0; reference or isolated evaluation by default.
- py-why/dowhy — DISCOVERED_PUBLIC_SOURCE; MIT; optional local causal-analysis candidate.

No source becomes a default merely because this plan names it.
