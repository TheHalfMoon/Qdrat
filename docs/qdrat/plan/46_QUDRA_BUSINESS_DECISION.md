# Qudra Business Decision

Status: **FOUNDER-DIRECTED PRODUCT ARCHITECTURE**

Qudra Business Decision is Qdrat's local business decision capability. It is not exposed to users as "PLD", "System One", a model family, or a probabilistic classifier. Those are implementation techniques that may sit behind the product contract.

Qudra Business Decision is the layer that turns incoming company work, questions, signals and exceptions into evidence-backed decisions and next actions.

## 1. Product promise

When something happens in the company, Qudra should help answer:

- What is this?
- Who or what is it related to?
- How urgent is it?
- Who owns it?
- What policy, contract, SLA, budget or history applies?
- What are the realistic options?
- What should happen next?
- What evidence supports that recommendation?
- What must a human approve?
- What can Qdrat execute safely now?
- What happened after the decision?

The product loop is:

```text
SENSE
  -> UNDERSTAND
  -> DECIDE
  -> PREVIEW
  -> APPROVE / ACT
  -> OBSERVE OUTCOME
  -> LEARN / CALIBRATE
```

Qudra is therefore not only a model endpoint. It is a product workflow spanning Qdrat events, Company Brain, Rules, Flow, permissions, budgets, approvals, actions and outcome evidence.

## 2. Local-only architecture

Qudra Business Decision is **local-only by architecture**.

Company decision context must not be sent to a remote inference, decision, reranking, OCR, agent or research provider.

Allowed runtime categories:

- Qdrat application services;
- customer-controlled PostgreSQL;
- locally packaged decision models;
- locally packaged LLMs;
- local embeddings/rerankers when enabled;
- local OCR/document models;
- local browser automation;
- local sandboxes;
- local filesystem/host adapters under explicit grants;
- customer-controlled on-prem or private-cluster compute.

External business systems may still be accessed through explicit Qdrat connectors when the company chooses to integrate them, but the Qudra reasoning/decision context remains inside the customer-controlled Qdrat environment.

There is no cloud fallback.

```text
QUDRA_INTELLIGENCE_EGRESS = DENY
REMOTE_MODEL_FALLBACK = FORBIDDEN
REMOTE_DECISION_PROVIDER = FORBIDDEN
REMOTE_RERANKER = FORBIDDEN
REMOTE_OCR = FORBIDDEN
REMOTE_AGENT_REASONING = FORBIDDEN
```

Remote projects such as Jev/TypeSafe or hosted TinyFish may be studied as references and benchmark targets. They are not Qudra runtime dependencies.

## 3. Core business object: DecisionCase

Every non-trivial Qudra decision should be representable as a durable Qdrat object.

```text
DecisionCase
  id
  tenant
  decision_type
  subject_object_refs[]
  trigger
  received_at
  owner
  participants[]
  urgency
  business_impact
  policy_class
  data_class
  context_revision
  evidence_refs[]
  facts[]
  uncertainties[]
  options[]
  recommendation
  confidence
  required_approvals[]
  executable_actions[]
  deadline
  sla
  budget
  status
  outcome
  feedback
  model_and_rule_evidence
  audit
```

A DecisionCase is not created for every trivial event. Qdrat may handle low-value routing inline. A durable case is required when the decision has meaningful business impact, uncertainty, approvals, financial consequence, customer consequence, employee consequence, compliance relevance, or future audit value.

## 4. Decision stack

Qudra must combine multiple local reasoning methods rather than forcing every problem through one model.

Preferred stack:

### Layer 1 — Deterministic facts

Use code and authoritative records for:

- permissions;
- balances;
- dates;
- SLA clocks;
- policy applicability;
- employment status;
- contract status;
- inventory;
- workflow state;
- hashes;
- test results;
- numerical calculations.

### Layer 2 — Deterministic rules

Use Qdrat Rules for:

- eligibility;
- routing constraints;
- thresholds;
- segregation of duties;
- compliance requirements;
- required approvals;
- escalation;
- prohibited actions.

### Layer 3 — Qudra local decision models

Use local typed decision models for bounded fuzzy tasks:

- intent classification;
- urgency;
- likely ownership;
- priority;
- duplicate/entity match suggestion;
- risk category;
- sentiment/tone;
- lead/account quality;
- review routing;
- exception classification;
- evidence-completeness triage.

Candidate implementation sources include Decider, SemIf and Bespoke Nimble, but Qudra owns the contract and benchmark.

### Layer 4 — Local Company Brain

Retrieve relevant:

- customer;
- employee;
- vendor;
- project;
- service;
- contract;
- ticket;
- conversation;
- invoice;
- policy;
- document;
- previous decision;
- similar historical outcome;
- Company Twin relationships.

### Layer 5 — Local reasoning model

A local LLM may synthesize complex context, compare options, explain trade-offs, draft responses and decompose work.

It may not create authority.

### Layer 6 — Simulation / what-if

Where useful, calculate scenarios using deterministic domain logic:

- budget impact;
- capacity impact;
- SLA consequence;
- revenue impact;
- renewal impact;
- staffing impact;
- inventory effect;
- schedule effect;
- cash-flow implication.

### Layer 7 — Policy and approval

Before action, Qdrat rechecks:

- actor;
- object;
- action;
- purpose;
- data class;
- policy revision;
- budget;
- approval;
- current object revision.

No model confidence can bypass this layer.

## 5. Qudra Action Card

The primary user experience is a Qudra Action Card inside Home, My Work, Inbox and domain pages.

Example:

```text
CLIENT ENQUIRY

Acme Ltd asked whether implementation can move to 15 October.

Qudra found:
- Contract start: 1 October
- Implementation project: 62% complete
- Two blocking tasks remain
- Assigned engineer is unavailable 12–16 October
- Contract allows one schedule revision without fee
- Customer health: At Risk
- Renewal value: SAR 420,000

Recommendation:
Offer 20 October and schedule an escalation call today.

Why:
1. 15 October conflicts with confirmed capacity.
2. 20 October is the first date with required staffing.
3. The account is high-value and currently at risk.

Confidence: 0.91

[Open evidence]
[Draft response]
[Create plan]
[Assign owner]
[Choose another option]
```

The recommendation is editable. The evidence is inspectable. The action is subject to normal Qdrat permissions.

## 6. Qudra Task Intake

Every task entering Qdrat may optionally pass through Qudra Task Intake.

Inputs can include:

- manual task creation;
- email;
- customer enquiry;
- form submission;
- ticket;
- meeting transcript;
- contract obligation;
- monitoring signal;
- workflow event;
- imported external-system task;
- agent-created proposal.

Qudra may locally propose:

- title normalization;
- intent/type;
- priority;
- owner/team;
- due date;
- SLA;
- related project/customer/service;
- dependencies;
- required skills;
- suggested subtasks;
- risk;
- expected effort band;
- next action.

Assignment should account for:

- permissions;
- workload;
- availability;
- skills;
- timezone/location when relevant;
- leave;
- conflicting deadlines;
- segregation of duties;
- domain ownership.

A probabilistic model may propose an assignee. Deterministic policy and current capacity decide whether assignment is allowed.

## 7. Qudra Client Enquiry

Qudra should turn incoming client communication into structured work.

For an enquiry, it may locally:

1. identify the customer/account/contact;
2. detect language and intent;
3. connect the message to the correct project, service, contract, invoice or opportunity;
4. determine urgency and SLA;
5. find unresolved related cases;
6. retrieve relevant knowledge and policy;
7. identify sentiment/risk;
8. determine the responsible team;
9. draft a grounded answer;
10. propose follow-up actions;
11. create/update the Case, WorkItem or Opportunity after approval/policy;
12. track the outcome.

Examples:

- "Where is my invoice?" -> Finance context + invoice status + draft response.
- "The service is down." -> Service incident + SLA + account impact + escalation.
- "Can we add 30 employees?" -> CRM opportunity + contract + capacity + pricing workflow.
- "We want to cancel." -> renewal/churn risk + account history + contract termination conditions + human escalation.
- "Can you send our data?" -> privacy/access workflow rather than a generic support response.

## 8. Qudra Business Inbox

Qdrat should expose one Business Inbox, not separate AI inboxes for each module.

Qudra groups work into:

- Needs Decision
- Needs Approval
- Needs Response
- At Risk
- Opportunity
- Exception
- Waiting
- Delegated
- Watching
- Completed

Cards may come from People, Work, Service, CRM, Finance, Procurement, Ops, Trust or Studio apps.

The user can filter by:

- company;
- team;
- domain;
- urgency;
- monetary impact;
- customer impact;
- employee impact;
- deadline;
- confidence;
- risk;
- owner.

## 9. Qudra Business Brief

Qudra should generate local daily/weekly briefings from company state.

Examples:

- top five customer risks;
- overdue high-impact work;
- approvals likely to block delivery;
- renewals due soon;
- contracts approaching expiry;
- invoices requiring attention;
- budget exceptions;
- staffing conflicts;
- project dependency risks;
- SLA risks;
- unresolved security/compliance actions;
- vendor issues;
- opportunities created by recent signals.

Every briefing item must link to evidence and the underlying Qdrat objects.

No "AI summary" may hide source state.

## 10. Qudra Signals

A BusinessSignal is an observed condition, not automatically a decision.

Examples:

- customer usage drops;
- support volume spikes;
- repeated task delay;
- invoice overdue;
- employee contract expiring;
- budget threshold approached;
- vendor certificate expiring;
- critical role has no backup;
- project milestone likely to slip;
- asset not returned after offboarding;
- account engages with a new product;
- unusual expense pattern;
- unresolved approval approaching SLA breach.

Signals can create or update DecisionCases.

Signal confidence, freshness and source lineage must be retained.

## 11. Qudra Exceptions

Qudra should focus human attention on exceptions instead of making users inspect every normal transaction.

Examples:

- payroll shadow difference;
- duplicate supplier invoice;
- unusual expense;
- customer escalation;
- contract-policy conflict;
- task with no eligible owner;
- impossible deadline;
- missing approval;
- conflicting schedules;
- stale customer data;
- inconsistent identity match.

Qudra explains:

- what is unusual;
- expected state;
- observed state;
- possible causes;
- available safe actions.

## 12. Qudra Decision Room

Complex decisions need more than one recommendation card.

A Decision Room should support:

- problem statement;
- participants;
- relevant objects;
- evidence;
- constraints;
- assumptions;
- options;
- scenario comparison;
- financial impact;
- capacity impact;
- timeline impact;
- risk;
- policy implications;
- recommendation;
- dissent/alternative;
- approval;
- final decision;
- outcome review.

Potential use cases:

- choose a vendor;
- prioritize projects;
- approve headcount;
- respond to a major customer escalation;
- decide whether to renew software;
- choose implementation timing;
- evaluate a commercial exception;
- select a hiring candidate after human-controlled process;
- decide whether to repair or replace an asset.

For consequential employment decisions, Qudra remains advisory and must follow applicable policy/human review requirements.

## 13. Qudra What-If

Users should be able to ask local scenario questions such as:

- What happens if this project moves two weeks?
- What if we hire three more people?
- What if this customer churns?
- What if we give a 10% discount?
- What if supplier lead time becomes 30 days?
- What if we approve all current leave requests?
- What if this vendor goes offline?
- What if we postpone this purchase?

Qudra should distinguish:

- deterministic calculated effects;
- assumptions;
- inferred/uncertain effects.

Scenario results never mutate production state until the user chooses an explicit action.

## 14. Qudra Follow-up and outcome learning

A recommendation without outcome tracking cannot improve.

For eligible decision classes, Qudra should record:

- selected option;
- rejected options;
- human modification;
- reason when supplied;
- downstream result;
- time to resolution;
- SLA outcome;
- financial outcome where measurable;
- customer/employee outcome where permitted;
- model confidence;
- whether confidence was calibrated.

This data forms a local Decision Learning Store.

It may improve:

- routing thresholds;
- model selection;
- calibration;
- similar-case retrieval;
- playbooks.

Do not train on sensitive records by default. Training/fine-tuning requires explicit local policy, purpose, dataset creation and provenance.

## 15. Qudra Playbooks

Repeated successful decision patterns can be promoted from fuzzy reasoning into governed playbooks.

Lifecycle:

```text
Observed decisions
 -> candidate pattern
 -> human review
 -> deterministic rules / Flow where possible
 -> simulation
 -> publish version
 -> monitor outcomes
```

This is strategically important: Qudra should gradually convert repeated company knowledge into reliable automation rather than permanently paying an AI reasoning cost for every repeated decision.

## 16. Qudra modes

Each DecisionCase should declare an autonomy mode.

### Observe
Qudra only detects and explains.

### Recommend
Qudra proposes an option but cannot create side effects.

### Prepare
Qudra may create drafts, previews, simulations and proposed actions.

### Execute bounded
Qudra may execute pre-authorized low-risk actions through normal Qdrat Action contracts.

### Human-controlled
High-impact actions always require explicit human approval.

The company can configure mode by domain, action, data class and risk.

## 17. Domain applications

### People
- onboarding/offboarding exception triage;
- leave routing;
- document expiry;
- staffing/capacity suggestions;
- policy-answer grounding;
- training suggestions;
- payroll exception explanation.

### Work
- task intake;
- priority;
- ownership;
- dependency risk;
- milestone forecast;
- meeting-to-work extraction;
- blocker escalation.

### Service
- enquiry triage;
- intent;
- SLA;
- case routing;
- incident correlation;
- response drafting;
- knowledge suggestion;
- escalation.

### CRM / Customer Success
- lead/account triage;
- opportunity signals;
- customer health explanations;
- renewal risk;
- next-best action;
- account brief;
- enquiry-to-opportunity conversion.

### Finance
- invoice query handling;
- expense exception triage;
- budget impact;
- collection priority;
- reconciliation exception explanation.

### Procurement
- vendor comparison;
- purchase-request triage;
- quote comparison;
- renewal/expiry signals;
- supply risk.

### Ops
- maintenance priority;
- asset exceptions;
- facility conflicts;
- service health impact.

### Trust
- access-review prioritization;
- control evidence triage;
- policy conflict;
- suspicious request routing.

## 18. Product surfaces

Qudra Business Decision should appear consistently in:

- Home;
- My Work;
- Business Inbox;
- object pages;
- customer/account pages;
- project pages;
- service/case pages;
- manager views;
- dashboards;
- command palette;
- Ask Qdrat.

Suggested reusable UI components:

- Qudra Action Card;
- Qudra Decision Case;
- Qudra Brief;
- Qudra Signal;
- Qudra Exception;
- Qudra Decision Room;
- Qudra What-If;
- Qudra Evidence Drawer;
- Qudra Outcome Review.

## 19. Explainability contract

Every material recommendation must answer:

- What do you recommend?
- Why?
- What evidence did you use?
- What assumptions did you make?
- What remains uncertain?
- What policy constrained the answer?
- What happens if I choose another option?
- Who must approve?
- What will Qdrat do if I click the action?

For high-impact decisions, the evidence and policy summary is mandatory.

## 20. Failure behavior

Qudra must abstain when:

- relevant evidence is missing;
- evidence conflicts materially;
- confidence is below the class threshold;
- no eligible action exists;
- policy is indeterminate;
- the local model needed by the configured profile is unavailable;
- the context exceeds qualified limits.

Correct output is then:

```text
NEEDS_REVIEW
INSUFFICIENT_EVIDENCE
CONFLICTING_EVIDENCE
NO_ELIGIBLE_ACTION
POLICY_INDETERMINATE
LOCAL_ENGINE_UNAVAILABLE
```

It must not silently call a cloud model.

## 21. Metrics

Measure Qudra by business usefulness, not model demos.

Core metrics:

- time to triage;
- time to decision;
- time to resolution;
- routing accuracy;
- recommendation acceptance;
- recommendation modification rate;
- abstention quality;
- calibration;
- reopened cases;
- missed SLA;
- prevented duplicate work;
- automated low-risk steps;
- decision outcome quality by domain;
- false escalation rate;
- user override rate;
- evidence citation correctness;
- permission leakage = zero on required corpus.

Never optimize recommendation acceptance alone; users may accept bad recommendations.

## 22. Execution-plan binding

The existing canonical DAG remains intact.

During future SpecGrain refinement:

- G3 Flow/Rules provides deterministic action/approval execution.
- G4-01/G4-02/G4-03 provide document evidence, search and Company Twin context.
- G6 Work/Service provides task and enquiry use cases.
- G7-03 provides business signals/enrichment.
- G8 Studio makes Qudra available to governed custom objects/apps.
- G9-01 becomes the local model + Qudra Business Decision engine registry.
- G9-02 provides Company Brain context bundles and retrieval.
- G9-03 provides local skills/capabilities and DecisionCase proposed actions.
- G9-04/G9-05 provide isolated local execution and evidence.
- G9-06 qualifies Qudra in Arabic/English with decision, retrieval and action-boundary evaluation.
- G10-02 packages all required Qudra models for offline install.
- G11-03 defines measured hardware/profile thresholds.

If these obligations make an existing SHAPED task too broad, split child SpecNodes during refinement. Do not pull implementation ahead of dependencies.

## 23. Naming rule

User-facing product name:

**Qudra Business Decision**

Preferred short name:

**Qudra**

Do not expose "PLD" as the product name.

Technical documentation may mention typed probabilistic decision techniques only when discussing model implementation, benchmarks or source provenance.

The product is the business capability, not the underlying model family.
