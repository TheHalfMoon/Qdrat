# Qudra Adversarial Gap Review

Status: PLAN HARDENING REVIEW

Purpose: attack the Qudra plan before implementation and record how each material failure mode is prevented.

## 1. Architecture duplication
Risk: Qudra could accidentally create a second workflow, identity, audit, policy, search or data authority.

Resolution:
- Flow remains the only durable business orchestration model.
- Rules remains deterministic decision policy.
- existing Principal/authorization remains authority.
- PostgreSQL/domain objects remain transactional truth.
- Company Twin/vector/process projections remain derived.
- Qudra creates DecisionCases, OptionSets and CapabilityPlans, not a parallel application platform.

## 2. "AI decides everything"
Risk: local models become de facto policy.

Resolution:
- hard constraints evaluated before ranking;
- model confidence never grants permission;
- deterministic facts/calculations separated from judgement;
- reauthorization occurs at execution time;
- high-impact domains use HUMAN_CONTROLLED mode.

## 3. Bad options presented as choice
Risk: Qudra gives several cosmetic variants and calls them alternatives.

Resolution:
- Option Engine requires material diversity;
- Pareto/dominance checks;
- no-action and collect-more-evidence options;
- feasible-option recall and option-diversity evaluation.

## 4. Impossible optimum
Risk: optimizer violates policy/resource constraints to produce an attractive plan.

Resolution:
- hard constraints cannot relax silently;
- infeasible is a valid result;
- relaxation candidates are explicit proposals;
- solver version, objective and constraint evidence retained.

## 5. Stale decisions
Risk: user approves an option built from old price, capacity, policy, contract or permissions.

Resolution:
- OptionSet/CapabilityPlan bind exact revisions;
- stale context is explicit;
- policy/object revision rechecked before every side effect;
- changed context forces recompute or explicit reconfirmation.

## 6. Local-only drift
Risk: a provider silently sends decision context to cloud.

Resolution:
- Qudra intelligence egress deny by architecture;
- no remote model/decision/reranker/OCR fallback;
- provider descriptors declare execution location;
- offline tests and network-deny qualification;
- external systems only through explicit business connectors/actions.

## 7. Hidden secret exposure
Risk: model or tool prompt receives credentials.

Resolution:
- secret references only;
- execution-boundary credential resolution;
- destination/purpose scoping;
- redacted evidence;
- tests for prompt/tool-context secret leakage.

## 8. Prompt injection / hostile evidence
Risk: documents, web pages or customer text alter Qudra policy.

Resolution:
- retrieved content is untrusted evidence;
- tool/model instructions remain separate from data;
- fake-policy and prompt-injection evaluation packs;
- no retrieved text creates scopes or approvals.

## 9. Ambiguous customer enquiry
Risk: Qudra confidently routes mixed or unclear messages.

Resolution:
- multi-label evidence and uncertainty retained;
- NEED_MORE_EVIDENCE / request clarification;
- human escalation thresholds;
- similar-case retrieval is advisory.

## 10. Decision feedback becomes self-fulfilling
Risk: Qudra learns to imitate historical human choices even when outcomes were poor or biased.

Resolution:
- choice and outcome stored separately;
- optimize outcome quality, not agreement rate;
- protected-trait prohibition;
- calibration and regret measures;
- no automatic training on sensitive decision history.

## 11. Correlation presented as cause
Risk: Qudra claims a workflow, discount or staffing change caused an outcome.

Resolution:
- observational vs causal labels;
- optional explicit causal-analysis contract;
- assumptions/refutations recorded;
- experiments only where policy/ethics permit.

## 12. Process mining surveillance
Risk: Process Intelligence becomes employee surveillance.

Resolution:
- purpose-limited process views;
- aggregate/process metrics preferred;
- permissions and retention;
- no protected-trait inference;
- People-domain uses require governance and human review.

## 13. Employment high-impact automation
Risk: Qudra autonomously hires, fires, ranks or penalizes workers.

Resolution:
- consequential employment decisions HUMAN_CONTROLLED;
- Qudra may organize job-relevant evidence and scenarios only;
- no protected-trait inference;
- decision evidence and human rationale retained where required.

## 14. Financial autonomy
Risk: a recommendation becomes an unauthorized payment/posting.

Resolution:
- payments/journals remain existing Finance actions;
- approvals/budget/SoD enforced deterministically;
- Qudra may propose, preview and reconcile;
- external effect UNKNOWN_OUTCOME never blindly retries.

## 15. Negotiation overreach
Risk: Qudra offers terms outside authority.

Resolution:
- negotiation envelope defined by deterministic limits;
- concession ladder and walk-away boundary;
- final external send/commit policy;
- high-value exceptions require approval.

## 16. Resource unfairness
Risk: Scheduler repeatedly overloads the same people because they are "efficient."

Resolution:
- workload/fairness constraints;
- leave/working-time policy;
- configurable balancing objective;
- explain assignment rationale;
- human override and outcome monitoring.

## 17. Optimization latency
Risk: complex solver problems block user workflow.

Resolution:
- problem-size thresholds;
- time limits;
- incumbent/partial result policy;
- asynchronous run for large jobs;
- safe timeout state;
- benchmark-based hardware profiles.

## 18. Local model resource explosion
Risk: every feature needs a different large model.

Resolution:
- common local model registry;
- small typed decision engines for bounded judgement;
- optional shared local LLM;
- profile-specific packs;
- benchmark promotion;
- G10-02 offline bundle inventory.

## 19. Model/version drift
Risk: same DecisionCase changes unpredictably after upgrade.

Resolution:
- model digests/version binding;
- frozen evaluation packs;
- shadow comparison before default promotion;
- old DecisionCases retain original engine evidence.

## 20. RAG/vector lock-in
Risk: Qudra fails if vector service is unavailable.

Resolution:
- structured lookup + graph + PostgreSQL FTS baseline;
- vector retrieval optional;
- vector indexes rebuildable;
- citation/evidence contract independent of index engine.

## 21. Process-intelligence lock-in
Risk: PM4Py/Celonis-like implementation dictates Qdrat data model.

Resolution:
- Qdrat ProcessEvent/Projection contracts owned internally;
- third-party engine is adapter/reference only;
- authoritative events remain Qdrat-owned.

## 22. Solver lock-in
Risk: OR-Tools becomes domain authority.

Resolution:
- OptimizationProblem/Result owned by Qdrat;
- solver adapter replaceable;
- problem semantics tested independently of solver.

## 23. Capability explosion
Risk: thousands of tools make selection noisy or unsafe.

Resolution:
- typed Capability Graph;
- domain/intents;
- health;
- eligibility before ranking;
- capability packs;
- search/ranking benchmarks;
- disabled/unhealthy exclusion.

## 24. Tool side-effect ambiguity
Risk: model chooses a read-like tool that actually writes.

Resolution:
- explicit side-effect class;
- preview/dry-run/idempotency metadata;
- policy and approval;
- Action contract wraps external writes.

## 25. Agent plan hallucination
Risk: local planner invents capabilities or invalid parameters.

Resolution:
- CapabilityPlan validates IDs/schema/preconditions;
- no unknown capability execution;
- parameters type-checked;
- plan proposal is not authority.

## 26. No rollback for real-world effects
Risk: Git rollback is treated as business rollback.

Resolution:
- compensation/exit path attached to options;
- external writes require reconciliation;
- irreversible actions flagged;
- reversibility shown in Decision Frontier.

## 27. Outcome not observable
Risk: Qudra cannot learn whether a recommendation worked.

Resolution:
- OUTCOME_NOT_OBSERVED explicit;
- each DecisionType declares measurable outcome fields;
- avoid fake learning when outcome is missing.

## 28. Gaming metrics
Risk: teams optimize "recommendation acceptance" rather than real results.

Resolution:
- acceptance is secondary;
- outcome quality/regret/SLA/reopen/actual cost-time tracked;
- manual override is not treated as failure.

## 29. Data retention/deletion gaps
Risk: source is deleted but decision memory/vector/process projection keeps it.

Resolution:
- derivative lineage;
- deletion journal;
- retention/hold rules;
- rebuild/remove tests across OptionSet, context, embeddings, process projections and outcome stores.

## 30. Backup/restore inconsistency
Risk: DecisionCase restored without matching policy/model/capability versions.

Resolution:
- version references preserved;
- restore validation;
- missing model/capability shown as unavailable;
- no silent re-execution after restore.

## 31. Upgrade incompatibility
Risk: DecisionType or capability upgrade invalidates in-flight cases.

Resolution:
- immutable published revisions;
- compatibility declarations;
- in-flight pinning or reviewed migration;
- upgrade preview and rollback.

## 32. Studio misuse
Risk: admins create unsafe custom decision types.

Resolution:
- publish validation;
- scope/capability checks;
- mandatory evaluation pack;
- simulation;
- risk/autonomy ceiling;
- review for high-impact DecisionTypes.

## 33. Arabic/RTL gap
Risk: intelligence quality works only in English.

Resolution:
- Arabic/English model and retrieval qualification;
- RTL UX acceptance;
- Arabic document/OCR benchmarks;
- bilingual evaluation fixtures;
- language-specific normalization evidence.

## 34. Accessibility gap
Risk: complex option matrix unusable with keyboard/screen reader.

Resolution:
- semantic tables/cards;
- keyboard comparison controls;
- accessible chart alternatives;
- no color-only risk communication;
- WCAG-oriented acceptance in shared Qudra UX.

## 35. Mobile/low-resource gap
Risk: local intelligence unusable away from workstation.

Resolution:
- server-local intelligence for web/mobile clients;
- Local Core profile;
- queue/defer heavy analysis;
- progressive results;
- no requirement that phone run the model itself.

## 36. Air-gap package incompleteness
Risk: Qudra claims local but model/tokenizer/solver wheel must be downloaded.

Resolution:
- G10-02 complete signed offline bundle;
- model/tokenizer/runtime/solver digests;
- license/notices inventory;
- network-disabled install test.

## 37. Performance unpredictability
Risk: user waits minutes without feedback.

Resolution:
- operation budgets;
- progressive state;
- asynchronous Run for heavy optimization/research;
- cancellation;
- workload benchmarks in G11-03;
- UX shows analysis stage and freshness.

## 38. No observability
Risk: admins cannot diagnose bad decisions.

Resolution:
- local structured traces;
- DecisionCase/Run correlation;
- engine/solver/capability version;
- redacted debug export;
- model distribution and deterministic decision evidence.

## 39. Bias from missing data
Risk: missing records are interpreted as negative evidence.

Resolution:
- missingness represented explicitly;
- evidence coverage;
- no default-to-negative;
- collect-more-evidence path;
- data-quality signal linked to DecisionCase.

## 40. Conflicting sources
Risk: CRM, contract and finance data disagree.

Resolution:
- source-authority mode and lineage;
- conflict visible in DecisionCase;
- no silent overwrite;
- reconciliation or human review before affected action.

## 41. Excessive notifications
Risk: Business Inbox becomes another noisy feed.

Resolution:
- decision-worthiness threshold;
- grouping/deduplication;
- urgency and impact;
- digest/brief mode;
- user/team tuning;
- outcome metric includes ignored/noisy cards.

## 42. "Everything in one" becomes complexity
Risk: Qudra adds a different mini-app for every use case.

Resolution:
- common primitives and shared UX;
- domain packs are configurations/experience templates;
- Decision Studio for extension;
- reuse Company Brain, Capability Graph, Option Engine, Flow and Rules.

## 43. No realistic adoption path
Risk: Qudra requires full Company OS migration first.

Resolution:
- connect-first model;
- can operate over linked/synced sources;
- shadow/recommend modes before native replacement;
- decisions cite external authority sources through Data Fabric.

## 44. Unsafe self-improvement
Risk: outcome learning changes policies or prompts automatically.

Resolution:
- learning produces proposals/metrics;
- model/policy/playbook promotion is versioned and reviewed;
- no production self-modification.

## 45. No exit/fallback
Risk: customer becomes dependent on Qudra model artifacts.

Resolution:
- domain records remain normal Qdrat objects;
- deterministic/manual workflows remain supported;
- provider/solver contracts replaceable;
- export of DecisionCase/OptionSet/evidence;
- disabling Qudra never deletes business state.

## 46. Final plan readiness check

The Qudra amendment is implementation-ready only if:
- all canonical contracts have clear ownership;
- every domain experience maps to shared primitives;
- each side effect ends in existing Action/Flow authority;
- all local engines have replaceable adapters;
- rollout begins Shadow/Recommend before bounded execution;
- high-impact human-control rules are explicit;
- failure states are modeled;
- versioning, deletion, restore, upgrade and observability are covered;
- Arabic/English/accessibility are acceptance criteria;
- execution packages are dependency-bound and SpecGrain-ready when parents unlock.

Remaining unknowns such as exact model/solver winners are intentionally evidence-gated implementation decisions, not planning gaps.
