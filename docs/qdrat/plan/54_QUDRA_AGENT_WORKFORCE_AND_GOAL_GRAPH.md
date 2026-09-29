# Qudra Agent Workforce and Goal Graph

Status: **FOUNDER-DIRECTED IMPLEMENTATION PLAN**

Source inspiration: `paperclipai/paperclip` at `24beb005755465f71a19ec92a85da0958d1b9740` (MIT + founder authorization).

Qdrat already models agents as principals. This plan adds the missing **governed agent workforce operating model** without inventing a second organization, task manager, budget system or workflow engine.

## 1. Product decision

Add a shared **Agent Workforce** experience inside Qdrat.

Agents are:
- `Principal`s;
- assigned explicit business roles and scopes;
- linked to Teams/Projects/Services/DecisionTypes through governed assignments;
- budgeted and observable;
- pausable/revocable;
- evaluated on evidence-backed outcomes.

An agent assignment is **not** legal employment and must not be represented as employee status.

## 2. Goal Graph

Every material agent task should answer **why this work exists**.

Canonical lineage:

```text
Company Goal
  -> Team Objective
  -> Initiative / Program
  -> Project / Service / Account / Control
  -> WorkItem / Case / DecisionCase
  -> CapabilityPlan / AgentRun
  -> Action / Outcome
```

The Goal Graph is a projection over existing Qdrat business objects, not a new goal database.

Required properties:
- versioned goal/object references;
- owner;
- target/outcome metric;
- status;
- time horizon;
- mandatory vs discretionary;
- evidence links;
- contribution relationship type;
- no model-created authority.

## 3. Goal-aware execution

Before an agent executes a task, its local context may include:
- task objective;
- parent goal chain;
- business constraints;
- relevant DecisionCase;
- allowed capabilities;
- current budget;
- acceptance/evidence requirements.

Goal ancestry is context, not permission.

## 4. AgentProfile

```text
AgentProfile
  principal_ref
  display_name
  purpose
  role_assignments[]
  supervisor_ref
  capability_grants[]
  runtime_profile
  skill_versions[]
  resource_budget
  autonomy_mode
  duty_cycle
  evaluation_profile
  pause_state
  expiry
```

The canonical security identity remains Qdrat Principal.

## 5. Atomic work claiming

Paperclip's atomic checkout pattern solves a real Qdrat problem: multiple agents must not unknowingly perform the same side-effecting work.

Add a `WorkLease`:

```text
WorkLease
  work_ref
  principal_ref
  lease_id
  acquired_at
  expires_at
  heartbeat_at
  generation
  purpose
  status
```

Rules:
- claim is atomic;
- lease expires;
- renewal is explicit;
- takeover increments generation;
- stale worker cannot commit after lease loss;
- read-only collaboration can coexist without exclusive lease;
- side-effecting execution binds the active lease generation.

## 6. Duty cycles and heartbeats

Agents may be scheduled to wake, inspect eligible work and propose/execute only what current policy permits.

Duty-cycle triggers:
- schedule;
- event;
- WorkItem assignment;
- DecisionCase state;
- signal;
- explicit human request.

A heartbeat does not grant new capabilities.

Every wakeup must respect:
- concurrency limit;
- resource budget;
- pause/kill state;
- work lease;
- current policy revision;
- local runtime health.

## 7. Agent budgets

Because Qudra intelligence is local, budget is broader than token cost.

Track and enforce:
- wall-clock time;
- CPU time;
- GPU/ANE time where measurable;
- memory/VRAM class;
- model invocations;
- token/context use where available;
- disk/artifact bytes;
- network bytes for explicitly authorized business connectors;
- concurrent Runs;
- monetary connector/API cost if an explicit external business system charges per use.

Budgets can warn, throttle, pause or require approval.

## 8. Skill Studio

A skill is a versioned composition over Qdrat capabilities, not arbitrary prompt text.

```text
AgentSkill
  skill_id
  version
  purpose
  input_schema
  output_schema
  required_capabilities[]
  prompt_or_policy_assets[]
  evaluation_pack
  risk_ceiling
  supported_runtime_profiles[]
  provenance
```

Promotion lifecycle:

```text
DRAFT -> TESTED -> QUALIFIED -> PUBLISHED -> DEPRECATED -> RETIRED
```

## 9. Agent evaluation and performance

Evaluate agents/skills using business and safety evidence:
- task success;
- acceptance criteria;
- evidence completeness;
- rework/reopen rate;
- human override;
- policy violations;
- failed/unknown external effects;
- latency/resource use;
- outcome quality;
- calibration/abstention where relevant.

Do not optimize only for task throughput or agreement with humans.

## 10. Agent supervisor patterns

A supervisor may be human or another agent, but delegation authority remains explicit.

A supervisor agent may:
- decompose work;
- assign eligible sub-work;
- request evidence;
- consolidate outcomes;
- escalate blockers.

It may not:
- expand a subordinate's grants;
- approve actions outside its own delegated authority;
- create secrets;
- alter governance policy merely because it is the supervisor.

## 11. Routines

Recurring agent work must compile to existing Qdrat Flow/Automation semantics.

Examples:
- daily account-risk review;
- nightly data-quality check;
- weekly procurement watch;
- SLA watch;
- contract-expiry review;
- executive brief preparation.

Each routine creates/updates governed WorkItems/DecisionCases and produces normal Run evidence.

## 12. Persistent run state

Agent work must survive restart without pretending unfinished effects succeeded.

Persist:
- accepted input/event;
- current plan revision;
- active work lease;
- completed steps;
- pending approvals;
- operation outcomes;
- context/evidence refs;
- model/runtime versions;
- budget consumption;
- next safe resume point.

`UNKNOWN_OUTCOME` blocks blind replay.

## 13. Workspaces

Where code/files/tools need isolated state, map workspaces to the existing Execution Plane:
- sandbox workspace;
- project/repository workspace;
- temporary artifact workspace;
- explicit trusted-host workspace.

Workspace access is capability-scoped and does not imply broad filesystem access.

## 14. Agent Inbox and management UX

Managers should see:
- active agents;
- current assignment;
- goal ancestry;
- work lease;
- run status;
- resource budget;
- recent outcomes;
- incidents/retries;
- pending approval;
- skill/runtime version;
- pause/terminate controls.

Avoid anthropomorphic HR fields that imply legal employment.

## 15. Portable team packs

Qdrat may package reusable local templates:
- role assignments;
- skills;
- routines;
- DecisionTypes;
- capabilities;
- evaluation packs;
- budget defaults.

Exports must scrub secrets and tenant-specific identifiers.

## 16. Source adoption boundaries

Selectively adapt Paperclip patterns for:
- goal ancestry;
- atomic task claiming;
- persistent run/session semantics;
- heartbeats/routines;
- resource budgets and hard stops;
- governance/approval UX;
- skill/evaluation concepts;
- portable templates;
- multi-organization isolation lessons.

Do not import:
- a second org chart;
- separate identity/RBAC authority;
- separate ticket/work system;
- cloud/model-provider assumptions incompatible with Qudra local-only intelligence;
- autonomous agent hiring/termination semantics mapped to legal People records.

## 17. Parent-plan binding

Implementation work is pre-shaped as QD-F19 through QD-F22 in the extension plan and remains dependency-bound to Principal, Work, Flow, Capability Fabric, Execution Plane and Qudra evaluation parents.
