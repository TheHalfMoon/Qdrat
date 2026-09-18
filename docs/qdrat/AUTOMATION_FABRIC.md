# Qdrat — Automation Fabric

## Purpose

Qdrat must not embed separate automation engines for HR, CRM, Service, Work, Finance, Ops, AI and custom Studio apps. The **Qdrat Automation Fabric** is the shared execution substrate that turns company data, policies, humans, agents and external systems into governed repeatable work.

The goal is not to clone n8n, Zapier, Make, Clay or any single workflow product. Qdrat should combine their strongest jobs with Qdrat-native identity, permissions, Data Fabric, Company Digital Twin, Flow, Rules, Studio, My Work, audit and local AI.

## Product principle

A company should be able to describe, draw, script, schedule or trigger a business process once and then expose it as any appropriate surface:

- background automation;
- API or webhook;
- scheduled job;
- approval workflow;
- agent skill/tool;
- chat command;
- form;
- mini-app;
- table/enrichment recipe;
- service request;
- reusable Studio capability.

One logical process should not be copied into separate automation, agent and app-builder systems.

## Canonical layers

### 1. Action graph

Every executable unit is a typed graph with versioned nodes, ports, contracts and policy metadata.

Node families include:

- deterministic functions;
- connector actions;
- data queries and writes;
- transforms and formulas;
- conditions and branching;
- loops/maps;
- timers and waits;
- human tasks and approvals;
- Rules decisions;
- AI/model calls;
- agent/skill calls;
- browser/research actions;
- document operations;
- subflows;
- notifications;
- compensation/rollback actions.

The visual canvas and any text/DSL representation must edit the same canonical model rather than drift into separate implementations.

### 2. Connector and capability layer

Connector actions are typed capabilities backed by Data Fabric credentials and scopes.

A capability declares:

- input/output schema;
- read/write effects;
- required scopes;
- data classifications touched;
- idempotency;
- retry safety;
- dry-run support;
- timeout/resource expectations;
- network requirements;
- approval/risk tier;
- compensation semantics;
- provenance/version.

Activepieces' type-safe Pieces model, n8n's broad node ecosystem, Refly skills and Flow-Like capability declarations are important references.

### 3. Run ledger

Every execution creates a durable Run with:

- immutable run identity;
- workflow/skill version;
- trigger and principal;
- node-by-node state;
- inputs/outputs with redaction policy;
- retries;
- timing;
- cost/token/provider usage;
- external request identifiers;
- approvals;
- artifacts;
- errors;
- compensation;
- final outcome;
- audit correlation.

Runs must be inspectable, replayable where safe, resumable where designed, and attributable to humans or agents.

### 4. Human-in-the-loop

Human intervention is a native execution state, not an exception.

Support:

- approve/reject;
- provide missing information;
- edit proposed changes;
- choose among alternatives;
- sign/acknowledge;
- resolve a conflict;
- override with reason;
- pause/resume;
- reassign.

Human tasks appear in the same Qdrat `My Work` surface as other actionable work.

### 5. Agent skills

A Skill is a versioned, typed, permission-scoped capability that an agent can invoke.

Skills may be created from:

- native Qdrat operations;
- connectors;
- deterministic code;
- Flow graphs;
- Rules;
- browser/research operations;
- composed subskills.

Refly's governed skill registry and export model, Eigent's workforce model, Buzz and Munder Difflin's agent-principal patterns, and OpenSandbox's governed execution boundary should inform the design.

### 6. Enrichment and research plane

Qdrat Data and Qdrat Sales/CRM should support Clay-class enrichment without making GTM the only use case.

A table, dataset, object collection or query result can be enriched with:

- deterministic lookups;
- company/internal data;
- approved external providers;
- web research;
- browser agents;
- model reasoning;
- formulas;
- classification;
- validation;
- deduplication;
- confidence scoring.

The same mechanism can enrich leads, vendors, candidates, assets, incidents, contracts, research datasets or any governed Studio object.

### 7. Provider waterfalls

A Waterfall is a reusable ordered/fan-out provider strategy with:

- provider sequence;
- stop conditions;
- confidence thresholds;
- field-level provenance;
- per-provider cost budget;
- rate limits;
- retry/cooldown;
- fallback;
- data-use policy;
- freshness;
- quality metrics.

Clay's provider waterfalls and Bricks' provider failover are key references. Qdrat must preserve which provider produced each accepted value.

### 8. Signals and watches

Any governed change can become a Signal:

- new database row;
- field change;
- webhook;
- scheduled query;
- external event;
- hiring/funding/news change;
- service health event;
- policy or contract date;
- customer usage change;
- workflow event.

Signals should feed Rules/Flow rather than create a second event system.

### 9. App surfaces

Automation can expose small operational interfaces: forms, review screens, dashboards, chat surfaces, tables and approval views.

LiveContext and Flow-Like show why app + workflow + execution evidence should stay close. Qdrat Studio owns the canonical UI extension model.

## Enrichment governance

Qdrat must make data acquisition governable.

Every external-data action should support:

- source URL/provider;
- retrieval timestamp;
- contractual/data-use classification;
- lawful-purpose metadata where required;
- suppression/consent state for outreach contexts;
- retention rule;
- confidence;
- verification status;
- cost;
- lineage into downstream fields and decisions.

Do not design around covert scraping or mass unsolicited outreach. Browser automation is a governed connector capability subject to policy, site/API terms, customer configuration and applicable law.

## Build-vs-borrow direction

Evaluate the founder-authorized sources as follows, subject to Astro's deeper qualification:

- **Activepieces** — strongest permissive candidate for connector/Piece SDK patterns and potentially selected Community Edition components.
- **n8n** — high-value reference for ecosystem scale, authoring UX, production execution and AI automation; public license boundaries plus founder grant require explicit intake evidence.
- **Refly** — high-value reference/donor for versioned skills, intervenable execution and SOP-to-skill compilation.
- **Flow-Like** — high-value typed graph/DSL/runtime/reference for canvas-text duality, run evidence and local/remote capability analysis.
- **LiveContext** — high-value reference/donor for chat-to-workflow-to-app convergence, scoped agents, budgets and built-in operational tables.
- **Bricks** — high-value local enrichment/browser/provider-waterfall donor; harden security and policy before adopting patterns.
- **Clay** — benchmark for table-centric enrichment, provider marketplace/waterfalls, signals, AI research and sequencing. Qdrat should not depend on a proprietary provider marketplace.
- **OpenClay (Altclay)** — privacy-first browser-local enrichment and stateless API reference.
- **Eigent** — local multi-agent workforce, skills/MCP, scheduled automation and model/tool portability.

## Architecture rule

Qdrat Flow remains the business-process authoring layer. Qdrat Rules remains deterministic decision logic. Qdrat Data Fabric owns source/connector authority. Qdrat Studio owns extension and app UI. Qdrat AI owns models/agents. **Automation Fabric is the shared execution contract binding these systems together, not a competing sixth system.**

## Competitive target

Qdrat should eventually let an authorized user say:

> Watch our connected systems for companies matching this criterion, enrich the records using approved sources, research missing facts, score them with an inspectable rule, route uncertain cases to me, update the CRM, create follow-up work, and keep the entire process private and auditable.

The same substrate should also handle employee onboarding, invoice approvals, incident response, vendor review, recruiting, compliance checks and custom business operations.

That cross-domain reuse is the advantage over specialized automation products.
