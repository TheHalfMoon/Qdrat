# Qudra Option Engine

Status: **FOUNDER-DIRECTED PRODUCT ARCHITECTURE**

Qudra must not collapse every business situation into one opaque "best answer." Its job is to give the customer the **best decision options available under the real company constraints**, show the trade-offs, and make the chosen option executable through Qdrat.

The supplied Jev + Treg workflow pattern reinforces a useful architecture split:

- the capability catalog discovers what can be done;
- local typed decision models score/rank bounded alternatives;
- Qudra generates and compares complete business options;
- Qdrat policy determines what is eligible;
- Flow/Actions execute the selected option;
- outcome evidence updates future calibration.

The user-facing product is **Qudra Option Engine**.

## 1. Core product promise

For every material business decision, Qudra should be able to answer:

- What are my realistic options?
- Which options are actually feasible now?
- Which option is best overall?
- Which is fastest?
- Which is cheapest?
- Which has the highest expected upside?
- Which has the lowest downside?
- Which is safest/compliance-friendliest?
- Which is easiest to reverse?
- Which preserves the most future flexibility?
- Which is best for the customer?
- Which is best for cash?
- Which is best for delivery capacity?
- Which option would I choose under a different priority?
- What happens if my assumptions are wrong?
- What is the cost of doing nothing?

Qudra should never hide a meaningful trade-off behind one score.

## 2. Decision Frontier

Qudra should generate a **Decision Frontier** rather than a single recommendation whenever multiple materially distinct options exist.

Typical frontier positions:

- **Best Overall**
- **Fastest**
- **Lowest Cost**
- **Lowest Risk**
- **Highest Upside**
- **Most Reversible**
- **Most Customer-Friendly**
- **Most Capacity-Efficient**
- **Most Compliant / Policy-Conservative**
- **Best Long-Term**
- **Best Short-Term**
- **Do Nothing / Wait**
- **Escalate for More Evidence**

Only show frontier positions that are genuinely distinct. If two labels resolve to the same option, collapse them rather than creating fake variety.

## 3. OptionSet contract

```text
OptionSet
  decision_case
  objective
  generated_at
  context_revision
  constraints_revision
  preference_profile
  assumptions[]
  uncertainties[]
  options[]
  frontier_labels[]
  dominated_options_hidden_count
  recommended_option
  alternative_if_assumption_changes
  no_action_option
  evidence_coverage
  sensitivity_summary
```

Each option:

```text
BusinessOption
  option_id
  title
  summary
  capability_plan
  eligibility
  hard_constraints[]
  expected_outcomes[]
  estimated_cost
  estimated_time
  expected_value
  downside
  risk
  reversibility
  customer_impact
  employee_impact
  compliance_impact
  capacity_impact
  cash_impact
  strategic_impact
  confidence
  uncertainty
  assumptions[]
  evidence_refs[]
  required_approvals[]
  execution_readiness
  rollback_or_exit_path
  score_breakdown
  rank_by_objective{}
```

## 4. Separate constraints from preferences

This is essential.

### Hard constraints

An option is not eligible when it violates:

- permission;
- law/regulatory policy;
- contractual obligation;
- approved budget ceiling;
- segregation of duties;
- required resource availability;
- mandatory SLA;
- technical dependency;
- data classification restriction;
- company policy.

Hard constraints are deterministic where possible.

### Preferences

Preferences may change ranking but do not create eligibility:

- minimize cost;
- maximize speed;
- maximize customer satisfaction;
- preserve margin;
- maximize strategic value;
- minimize operational burden;
- minimize uncertainty;
- prefer reversible actions;
- prefer internal resources;
- preserve optionality.

Qudra must never trade away a hard constraint merely because another option has a higher model score.

## 5. Multi-objective scoring

A single weighted score is useful but insufficient.

Qudra should use a local multi-objective process:

1. remove ineligible options;
2. calculate deterministic dimensions;
3. estimate uncertain dimensions locally;
4. identify Pareto-efficient options;
5. remove materially dominated options;
6. preserve diverse frontier options;
7. rank within each declared objective;
8. show sensitivity to preference changes.

A user should see when there is no universally best choice.

Example:

| Option | Time | Cost | Risk | Customer impact | Reversible |
|---|---:|---:|---:|---:|---:|
| A | 2 days | SAR 40k | Low | High | High |
| B | 1 day | SAR 85k | Medium | Very high | Medium |
| C | 5 days | SAR 10k | Very low | Medium | High |

Qudra should not compress this into "B = 87/100" without exposing the trade-off surface.

## 6. Local typed decision models

Local Jev-style engines are especially useful when ranking bounded options.

For each DecisionCase, Qudra may ask several typed questions over the **same local state**:

```text
best_overall:
  choice: A | B | C | NEED_MORE_EVIDENCE

lowest_execution_risk:
  choice: A | B | C

customer_outcome:
  score: poor | acceptable | good | excellent

delivery_confidence:
  score: very_low | low | medium | high | very_high

needs_human_escalation:
  boolean
```

The engine returns full distributions.

Qudra should preserve those distributions rather than flattening them immediately.

This supports:

- uncertainty-aware routing;
- human review thresholds;
- second-choice fallback;
- sensitivity analysis;
- disagreement detection.

The local decision engine is one input. It is not the authority.

## 7. Capability-aware option generation

The Capability Graph makes options executable rather than hypothetical.

When a user asks:

> "How can we save this customer?"

Qudra first discovers what the company can actually do:

- contract.discount.preview;
- pricing.exception.request;
- support.priority.raise;
- service.credit.propose;
- project.capacity.reallocate;
- executive.call.schedule;
- implementation.timeline.simulate;
- renewal.term.extend;
- knowledge.solution.search.

Then it can build complete options.

Example:

### Option A — Recover fast
- raise support priority;
- allocate senior engineer;
- executive call today;
- no commercial discount.

### Option B — Commercial recovery
- service credit;
- 12-month renewal extension;
- executive call;
- implementation recovery plan.

### Option C — Lowest cost
- specialist troubleshooting session;
- revised timeline;
- weekly success check-in.

Each option maps to a real CapabilityPlan.

## 8. Option generation pipeline

```text
DecisionCase
  -> Company Brain context
  -> hard constraints
  -> Capability Graph
  -> candidate capability plans
  -> local deterministic simulation
  -> local probabilistic scoring
  -> Pareto filtering
  -> diversity check
  -> Decision Frontier
  -> explanation/evidence
  -> preview
  -> approval/selection
  -> execution
  -> outcome
```

Candidate plans may be generated by:

- deterministic templates;
- domain playbooks;
- local planning LLM;
- combinations of existing capabilities;
- prior successful DecisionCases.

Do not generate unbounded arbitrary plans.

## 9. Option diversity

Qudra should not return five cosmetic variants of the same decision.

Require material diversity along one or more axes:

- cost;
- time;
- risk;
- aggressiveness;
- reversibility;
- internal vs external resource use;
- customer concession;
- staffing;
- cash timing;
- strategic horizon.

An OptionSet fails quality review if its alternatives are not meaningfully different.

## 10. Do-nothing and delay options

For many business decisions, "do nothing", "wait", or "collect more evidence" is legitimate.

Qudra should explicitly model:

- no action;
- defer until date/event;
- collect more evidence;
- escalate to specialist;
- run a small experiment first.

These options must include opportunity cost and deadline/SLA consequences.

## 11. Reversibility and real-options thinking

Qudra should explicitly value reversibility.

For uncertain situations, an option that preserves future choices may be better than a high-upside irreversible action.

Record:

- reversible without external effect;
- reversible with financial cost;
- reversible with customer impact;
- partially reversible;
- effectively irreversible.

Qudra may favor staged decisions:

```text
small test
 -> observe
 -> expand
```

instead of:

```text
full commitment now
```

when uncertainty is material.

## 12. Sensitivity analysis

Users should be able to ask:

- What if speed matters twice as much?
- What if the budget drops to SAR 50k?
- What if this customer is strategic?
- What if the engineer is unavailable?
- What if expected demand is 30% lower?
- What if we cannot use an external vendor?

Qudra recomputes the frontier from local state.

Show when the recommendation changes and **which assumption caused the change**.

## 13. Uncertainty and confidence

Every estimated dimension should distinguish:

- known fact;
- calculated value;
- forecast;
- model estimate;
- assumption;
- missing data.

An option with less evidence should not appear equally certain.

Use:

- confidence;
- interval/range where appropriate;
- evidence coverage;
- missing-input flags.

If uncertainty is too high:

```text
BEST_NEXT_ACTION = COLLECT_MORE_EVIDENCE
```

may be the correct recommendation.

## 14. Regret and worst-case analysis

For material decisions, Qudra should optionally show:

- best case;
- expected case;
- plausible worst case;
- maximum regret;
- failure recovery path.

This is especially useful for:

- hiring;
- procurement;
- projects;
- large customer concessions;
- financial commitments;
- vendor changes;
- capacity allocation.

## 15. Stakeholder views

The same option affects different stakeholders differently.

Qudra may show:

- Customer
- Employee
- Manager
- Finance
- Operations
- Compliance
- Executive
- Vendor

Example:

```text
Option B
Customer: +++
Finance: --
Delivery: +
Compliance: neutral
Reversibility: medium
```

Stakeholder scores must be explainable and source-backed where material.

## 16. Decision policies

A company should be able to configure option policies.

Examples:

- always show a no-action alternative;
- always show a low-risk option;
- never recommend a discount above 10% without CFO approval;
- prefer internal execution when delivery difference is under 2 days;
- prioritize customer retention for strategic-tier accounts;
- require reversible options when confidence < 0.70;
- require at least three materially distinct options for purchases above SAR 100k.

These policies belong in deterministic Qdrat Rules.

## 17. Option UX

The default UX should avoid overwhelming users.

### Quick view

Show the top three distinct choices:

1. **Recommended**
2. **Safest Alternative**
3. **Best Trade-off Alternative**

Then offer **See all options**.

### Compare view

Use a comparison matrix:

- outcome;
- cost;
- time;
- risk;
- confidence;
- reversibility;
- policy impact;
- customer impact;
- capacity impact.

### Evidence view

For every score, a **Why this?** action opens evidence and assumptions.

### What-if controls

Users can change priorities and immediately see the frontier recomputed locally.

## 18. Domain-specific examples

### Task arrives

Qudra may show:

**A — Assign to Ahmed now**
- fastest;
- medium workload risk.

**B — Assign to Sarah tomorrow**
- best skill match;
- lower delivery risk.

**C — Split into two tasks**
- best deadline confidence;
- higher coordination cost.

### Client enquiry

**A — Answer immediately from knowledge**
- fastest;
- high confidence.

**B — Open specialist case**
- safest;
- slower.

**C — Schedule customer call**
- best for ambiguous/high-value account.

### Sales opportunity

**A — Standard proposal**
- best margin.

**B — Pilot**
- most reversible.

**C — Discounted annual contract**
- highest close probability;
- lower margin.

### Procurement

**A — Lowest bid**
- cheapest;
- delivery risk higher.

**B — Preferred vendor**
- lowest operational risk.

**C — Split order**
- highest resilience;
- higher admin cost.

### Hiring

Qudra may compare candidates on job-relevant, policy-approved evidence but must remain advisory for consequential employment decisions and preserve human-controlled review.

### Service incident

**A — rollback**
- fastest recovery;
- loses latest change.

**B — forward fix**
- preserves change;
- slower.

**C — isolate affected service**
- limits blast radius;
- degraded functionality.

## 19. Qudra Choice Memory

Qudra should locally retain structured history:

- which options were shown;
- which was chosen;
- which was edited;
- rejected alternatives;
- why user changed the recommendation;
- actual outcome;
- actual cost/time;
- whether risk materialized.

This enables better local calibration and similar-case retrieval.

Do not optimize only for matching historical choices. Outcome quality matters more than imitation.

## 20. Option quality evaluation

Evaluate Qudra on:

- feasible-option recall;
- dominated-option rate;
- option diversity;
- recommendation calibration;
- evidence correctness;
- estimated vs actual cost/time;
- risk calibration;
- human override rate;
- outcome regret;
- policy violation rate = zero on required corpus;
- permission leakage = zero;
- percentage of decisions where "collect more evidence" was appropriately chosen.

## 21. Treg + local Jev-style synthesis

The public Jev + Treg pattern demonstrates a useful decomposition:

```text
Treg-like catalog -> state/data/capabilities
Local Jev-style model -> typed probabilities
Code/policy -> threshold and route
```

Qudra extends this substantially:

```text
Capability Graph
  + Company Brain
  + Rules
  + local typed decisions
  + local LLM planning where needed
  + deterministic simulation
  + Decision Frontier
  + approvals
  + Flow/Action execution
  + outcome learning
```

This makes Qudra a business option system rather than a tool router.

## 22. Local-only invariant

Every intelligence step in the Option Engine remains inside customer-controlled Qdrat infrastructure.

No option generation, scoring, reranking, explanation, OCR, retrieval or plan generation may silently leave the environment.

External systems may be called only as explicit business connectors/actions after the normal Qdrat policy checks.

## 23. Execution-plan binding

The current canonical DAG remains intact.

This document becomes a refinement input to:

- G3-06 deterministic Rules;
- G3-07 replay/compensation;
- G6 Work/Service use cases;
- G7-03 signals/enrichment;
- G7-04 customer health;
- G7-06/G7-07 finance/procurement choices;
- G8 Studio custom-domain DecisionCases;
- G9-01 Qudra local decision engine registry;
- G9-02 Company Brain context;
- G9-03 Capability Graph and CapabilityPlan;
- G9-04/G9-05 execution/evidence;
- G9-06 decision/option evaluation;
- G11-03 performance and model-selection qualification.

If refinement makes a parent task too broad, create child SpecNodes without weakening the parent acceptance criteria.
