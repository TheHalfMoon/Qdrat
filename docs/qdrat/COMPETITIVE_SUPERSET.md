# Qdrat — Competitive Superset Target

## Objective

Qdrat is not complete when it contains a ticket screen, a kanban board, and an AI chat box. The target is to become a **simpler, private, integrated functional superset** of the categories that companies currently buy separately: Jira/Jira Service Management, Zendesk/Intercom-class support, ServiceNow-class service operations, modern work management, knowledge, collaboration, internal tools, analytics, AI automation and eventually CRM/finance/procurement.

"Superset" does **not** mean reproducing every legacy configuration knob. It means covering the valuable jobs-to-be-done while removing fragmentation, duplicated identity, duplicated automation, duplicated search, duplicated audit, and administration tax.

## The competitive thesis

Traditional enterprise suites usually win through breadth but become expensive to configure, integrate and govern. Best-of-breed SaaS products often win through UX but fragment company data and permissions. Qdrat should combine:

- the breadth of enterprise platforms;
- the speed and focus of modern work tools;
- the channel depth of modern customer-support platforms;
- the extensibility of low-code platforms;
- the context of a company digital twin;
- the leverage of governed agents;
- the sovereignty of local/private infrastructure.

The primary moat is **shared context**: a person, customer, asset, service, project, policy, case, document, approval, vendor, database and agent can participate in one governed object/relationship model and one evidence trail.

## Current competitor baseline — verified 2026-09-11

The target must move with the market. The following current product surfaces are the minimum benchmark Astro must preserve in its plan.

### Jira
Official Jira material currently emphasizes planning and assignment, goals, boards/lists/timeline/calendar views, dependencies, forms/request intake, customizable workflows, no-code automation, reporting, capacity/performance insight, Rovo AI and thousands of marketplace integrations.

Official reference: https://www.atlassian.com/software/jira/features

### Jira Service Management
Current JSM material covers request, incident, problem, change, asset and configuration management, including service queues, major-incident escalation, CI/CD-linked change risk and a flexible asset/CI relationship model.

Official references:
- https://www.atlassian.com/software/jira/service-management/features
- https://support.atlassian.com/jira-service-management-cloud/docs/get-to-know-the-main-jira-service-management-features/

### Zendesk
Zendesk's 2026 Resolution Platform direction explicitly unifies AI agents, copilots, knowledge, workflows/actions, integrations, governance and insights across omnichannel customer/employee service. Its current AI layer includes autonomous agents, agent assistance, intelligent triage, search/knowledge and routing.

Official references:
- https://www.zendesk.com/blog/zendesk-insights/innovation/relate-2025-resolution-platform-ai-agents/
- https://www.zendesk.com/newsroom/articles/relate-2026/
- https://support.zendesk.com/hc/en-us/articles/10018448457498-Overview-of-Zendesk-AI-offerings

### ServiceNow
Current ServiceNow ITSM unifies incident, change, problem and request management with CMDB/service context, omnichannel self-service, AI specialists, shared data/workflow foundations and cross-enterprise workflows.

Official references:
- https://www.servicenow.com/products/itsm.html
- https://www.servicenow.com/docs/r/it-service-management/r_ITServiceManagement.html

These capabilities are the baseline, not the Qdrat differentiation. Qdrat must add private/local deployment, infrastructure/data freedom, a shared company graph across more domains, agent principals, open connector contracts, simpler administration and evidence-first automation.

## The universal work model

Qdrat should avoid separate engines for Jira issues, Zendesk tickets, HR requests and ServiceNow cases. Use shared primitives with typed domain profiles.

### `WorkItem`
A work item can represent task, issue, bug, story, epic, objective, milestone, request, case, incident action, change task, onboarding task, procurement action, audit finding or custom Studio work.

Core capabilities:
- stable typed identity;
- title/description/state/priority/severity;
- requester/reporter/owner/assignee/team;
- watchers/subscribers;
- hierarchy and arbitrary typed relationships;
- dependencies/blockers;
- due dates, schedules and effective dates;
- estimates, time/capacity and costs where relevant;
- SLA/OLA clocks;
- forms/custom typed fields;
- labels/tags only for lightweight classification, not core semantics;
- comments/conversation references;
- files/knowledge references;
- workflow/rules attachment;
- audit/event timeline;
- external-source mapping;
- agent/tool visibility and action policy.

Domain modules add constraints and behaviors; they do not fork the engine.

### `Conversation`
Conversation is a channel-independent thread of communication linked to company objects and participants. Email, web chat, messaging, comments, voice transcripts, portal replies and agent messages can normalize into this layer while retaining original-channel evidence.

### `Case`
A case groups work, communication, evidence, affected objects, policies, SLAs and outcomes. Customer support, HR employee relations, compliance investigations, IT service, vendor disputes and other domains reuse the case substrate with different access rules.

### `Request`
A request is structured intake with requester, requested outcome, catalog/form schema, approvals, fulfillment plan, SLA and resolution. It can create one or many WorkItems/Cases/Changes.

### `Service`
A service represents a business or technical capability with owner, dependencies, customers, health, SLAs/SLOs, related assets/systems, knowledge, incidents and changes.

This model is what lets Qdrat beat products that must be integrated after purchase.

## Better than Jira / Jira Service Management

Qdrat Work must eventually cover the valuable Jira-family jobs while reducing configuration friction.

### Work planning
- list, table, board, calendar, timeline, Gantt, tree, workload and graph views over the same items;
- backlog, cycles/sprints, epics/initiatives, milestones, releases and roadmaps;
- dependency and critical-path views;
- cross-project portfolios and goals/outcomes;
- capacity, allocation, time and cost views where enabled;
- saved filters, advanced query language and natural-language query compilation with inspectable output;
- templates without schema forks;
- bulk operations with preview and undo/compensation where possible.

### Intake and workflow
- forms and service catalog entries;
- email/API/webhook/portal/chat/event intake;
- configurable status models and transitions;
- Flow automation, deterministic Rules and approval gates;
- SLA/OLA clocks, escalation and calendars;
- custom fields through typed Studio metadata;
- versioned workflow publishing, simulation and migration of in-flight work.

### Developer/product workflow
- source-control and CI/CD links;
- commit/branch/release/deployment evidence;
- incident/change links;
- optional branch/project-room patterns inspired by Buzz;
- agent reviewers/triage principals with explicit scopes;
- product discovery/ideas/evidence linked directly to delivery objects.

### Why it should be better
Jira often becomes an island of project configuration. Qdrat Work can know the actual people, skills, capacity, assets, services, customers, budgets, policies and approvals because those objects already exist in the same Company OS. A work item should not need custom synchronization just to know who a person is or which service/customer it affects.

## Better than Zendesk / Intercom-class support

Qdrat Service must eventually provide a complete omnichannel resolution workspace while keeping support data private and connected to company systems.

### Omnichannel conversation
- email;
- web chat/widget;
- customer portal;
- SMS/approved messaging networks through adapters;
- social/messenger adapters where customers configure them;
- voice/call records/transcripts through adapters;
- API/webhook/system-generated conversations;
- one conversation history that preserves channel provenance.

### Ticket/case resolution
- tickets/cases/requests with forms and typed fields;
- queues/views, assignment, ownership and swarming;
- skill, team, workload, language, customer, severity and policy-aware routing;
- priority and impact/urgency matrices;
- SLA/OLA, business calendars, escalation and breach prediction;
- macros/playbooks and reusable response/action bundles;
- parent/child, merge/link and problem-pattern relationships;
- customer/account/contact context from Qdrat CRM or connected external systems;
- entitlement/contract/support-plan logic;
- approvals and cross-department fulfillment.

### Knowledge and self-service
- permission-aware help center and knowledge bases;
- public/private/audience-specific articles;
- community/discussion capability when needed;
- article lifecycle, ownership, review and expiry;
- search analytics and content-gap detection;
- AI answers with inspectable citations;
- feedback that creates knowledge improvement work.

### AI resolution layer
- autonomous read/recommend/triage agents within policy;
- draft replies and suggested actions;
- tool execution against CRM, billing, orders, inventory and internal systems through Data Fabric;
- resolution plans spanning multiple systems;
- human approval for high-risk writes;
- QA/evaluation of both human and agent interactions;
- reason codes, citations and complete action traces;
- local models by default with administrator-approved remote providers optional.

### Workforce and quality
- forecasting inputs;
- schedules/capacity handoff to People/Workforce where appropriate;
- conversation quality scorecards;
- policy/compliance checks;
- coaching findings linked to skills/learning without exporting employee data into a separate SaaS system.

### Why it should be better
Zendesk must integrate with HR, assets, project work, finance, product delivery and internal knowledge to get full company context. Qdrat can resolve a customer case directly through native or connected company objects and workflows. A customer issue can become a product bug, incident, refund approval, vendor case and knowledge update without five separate integration products.

## Better than ServiceNow-class enterprise service management

Qdrat must eventually cover the high-value enterprise-service patterns without requiring ServiceNow-scale platform administration.

### ITSM/service operations
- incidents, major incidents and swarming;
- service requests and catalogs;
- problems/root causes/known errors;
- changes, risk, approvals, calendars and deployment evidence;
- on-call/assignment/escalation integration;
- service ownership and service portfolio;
- SLA/SLO/OLA contracts;
- post-incident reviews and action tracking;
- status/public communication adapters.

### CMDB and digital twin
- assets/configuration items/services/applications/databases/integrations/endpoints;
- typed relationships and dependency graphs;
- ownership and lifecycle;
- discovery/import/connector evidence;
- reconciliation rules and authoritative-source markers;
- impact analysis;
- history and effective dating;
- link to people, vendors, contracts, costs, risks, incidents and changes.

Qdrat should call this broader capability the **Company Digital Twin**, with CMDB/service graph as one governed subset.

### Enterprise workflows beyond IT
- employee/HR services;
- customer service;
- vendor/procurement operations;
- security/privacy/compliance cases;
- facilities/asset requests;
- finance approvals;
- legal/policy workflows;
- custom Studio applications.

### Why it should be better
The competitive advantage is a smaller default runtime, local-first deployment, normal software-engineering extension paths, clearer typed contracts, and a UX that exposes complexity progressively rather than forcing every customer to become a platform administrator.

## Better than Slack/Teams-style collaboration

Qdrat should not recreate an unlimited-chat product just because chat is popular. Collaboration exists to move company work forward.

Target behaviors:
- object-linked discussions and rooms;
- threads/topics that preserve context;
- DMs/group discussions where justified;
- voice/meeting integrations or optional local service;
- shared canvases/docs;
- agent participants with real identities/scopes;
- action extraction into WorkItems/decisions/approvals;
- searchable institutional memory;
- notification defaults that prioritize actions and mentions over noise;
- retention/legal-hold/privacy controls.

Buzz and Zulip are particularly valuable references here.

## Better than Confluence/Notion-style knowledge

- wiki/pages and policy objects;
- structured docs and collaborative blocks where useful;
- records/document attachments;
- ownership/review/expiry/acknowledgment;
- public/internal/restricted audience policies;
- cross-link to any company object;
- full-text, semantic and graph search;
- citations/provenance;
- document parsing/OCR;
- content quality and gap detection;
- offline/private storage;
- templates plus Studio structured data when a document should become a real business object.

## Better than fragmented CRM/helpdesk/project stacks

A shared account/contact/customer model can connect sales, implementation, support, projects, invoices, contracts, usage, product feedback and renewal work. Qdrat does not need to build Salesforce immediately to create this advantage; Data Fabric can link an external CRM first, then native Sales/CRM can replace it later where valuable.

## Private voice and governed execution advantage

Qdrat should exceed cloud-first work/support suites by making voice and agent execution first-class **private platform capabilities** rather than external add-ons.

### Local Voice Plane
- dictate into any Qdrat field or composer;
- issue voice commands to permission-scoped agents;
- record/transcribe meetings with explicit consent indicators and retention policy;
- local multilingual ASR with downloadable/offline model packs;
- optional diarization and speaker recognition under administrator policy;
- convert transcripts into linked notes, decisions, tasks, cases and knowledge with provenance;
- redact or classify sensitive transcript segments before downstream AI use;
- support cloud ASR only as an explicit customer-selected provider profile.

Primary authorized source studies: `OpenWhispr/openwhispr` and `Starmel/OpenSuperWhisper`.

### Governed Agent Execution Plane
- code, browser, GUI, file and tool execution must run in an explicit sandbox boundary when risk requires it;
- per-run CPU/memory/time/disk limits;
- deny-by-default or policy-scoped network egress;
- credential brokering without exposing raw secrets to agent workloads where possible;
- strong-isolation profiles for sensitive workloads;
- artifact capture, command/file traces and correlation to Qdrat audit events;
- human approval and kill/circuit-breaker controls;
- portable sandbox contract so Docker, Kubernetes, gVisor/Kata/Firecracker-class substrates can evolve independently.

Primary authorized source study: `opensandbox-group/OpenSandbox`. Multi-agent supervisor/mailbox/memory/autonomy patterns should also be evaluated from `chaitanyagiri/munder-difflin`, while `jaredrhod/fullstack-agent` contributes memory/voice/interaction/self-repair patterns and `langflow-ai/openrag` remains an authorized retrieval/orchestration source.

This is a Qdrat advantage over SaaS tools that require company content or agent actions to transit vendor-controlled execution infrastructure.


## Better than Zapier / Make / n8n / Clay-class automation

Qdrat should not compete by counting nodes. It should remove the boundary between automation and the company model.

Target capabilities:

- visual typed flows plus code/DSL escape hatches;
- schedules, webhooks, events, forms, chat and data-change triggers;
- retries, branches, loops, waits, subflows and compensation;
- human approvals and editable proposed changes;
- reusable versioned skills/actions;
- first-class MCP/tool exposure where appropriate;
- connector SDK and private connectors;
- one execution/run ledger with provenance and cost;
- provider waterfalls and confidence thresholds;
- table/object enrichment with deterministic and AI columns;
- web/browser research under explicit policy;
- signals/watches that trigger reusable plays;
- agent steps with real principal/scopes/budgets;
- mini-app/form/dashboard surfaces generated around workflows;
- local/offline execution profiles.

Clay's current benchmark includes provider waterfalls, AI web research, scheduled/real-time enrichment, signals, CRM enrichment and sequencing. Qdrat should generalize these capabilities beyond GTM: the same enrichment and signal substrate must work for vendors, candidates, contracts, assets, incidents, research and arbitrary Studio objects.

The competitive advantage is that Qdrat automation already understands the same people, customers, services, permissions, policies and audit model as the rest of the Company OS. A workflow does not need a third-party automation service merely to reconnect Qdrat to itself.

See `AUTOMATION_FABRIC.md`.

## Agent-native Company OS

The strongest long-term differentiator should be that agents are **governed operational principals**.

Each human or agent principal has:
- identity;
- role/relation/membership;
- scopes and object permissions;
- purpose and risk limits;
- model/runtime/tool policy for agents;
- delegation source and expiry;
- presence/activity state where relevant;
- immutable action evidence;
- budget/rate/resource limits;
- ability to request elevated approval rather than silently bypass policy.

Agents can participate in Work, Service, Knowledge, People, Ops, Data and future Finance/CRM without creating a second security model.

## One Inbox / My Work

A major UX advantage should be one action surface for:
- assigned work;
- approvals;
- service cases;
- mentions/replies;
- workflow human steps;
- review requests;
- signatures/acknowledgements;
- incidents/on-call actions;
- agent requests for approval;
- policy/compliance tasks.

Users should not need to open seven modules to discover what requires attention.

## One search and command layer

Global search/command palette should span permitted:
- people and teams;
- work/projects;
- cases/conversations/customers;
- services/assets/systems;
- documents/knowledge;
- workflows/rules;
- vendors/contracts;
- reports/metrics;
- external linked objects;
- agent traces/actions.

Search results must preserve source authority and permissions. `Ask Qdrat` should sit on the same retrieval contract rather than own a hidden index.

## Administration without administration tax

To beat enterprise platforms, Qdrat needs progressive complexity:

### Do
Normal users see focused workflows and clear defaults.

### Understand
Power users can inspect relationships, history, rules, permissions and automation evidence.

### Design
Authorized builders use Studio, Flow, Rules, connector management, schemas and policy controls.

Advanced capability should not make basic workflows feel like platform development.

## Competitive quality gates

A Qdrat feature should not be called a replacement for a competitor category until it proves:

1. **Job completeness** — the key end-to-end jobs work, not only CRUD screens.
2. **Migration/import** — existing data/config can enter with mapping, validation and reconciliation.
3. **Integration** — external systems can remain connected during migration.
4. **Performance** — common actions remain fast at representative scale.
5. **Permissions** — row/object/field/action access behaves correctly across UI/API/search/AI.
6. **Auditability** — sensitive actions and automation have inspectable evidence.
7. **Offline/private operation** — enabled features do not silently require public SaaS.
8. **Accessibility/i18n** — Arabic/English, RTL/LTR and accessibility are tested.
9. **Agent safety** — agents respect the same object permissions plus risk/approval controls.
10. **Upgrade safety** — configuration and data survive supported upgrades/rollback paths.
11. **Supportability** — administrators can diagnose health and export evidence locally.
12. **UX benchmark** — common tasks require fewer or clearer steps than the target competitor, not merely equal feature names.

## Anti-goals

Do not:
- clone Jira's schema/configuration complexity;
- clone Zendesk as a separate support silo;
- clone ServiceNow's full platform topology;
- make chat the system of record;
- make AI the only way to operate the product;
- introduce separate identity/permission engines per suite;
- copy every donor application into a monorepo;
- promise every external connector as day-one certified;
- require customers to replicate all data into Qdrat;
- require Qdrat cloud for licensing, telemetry, AI or administration.

## Definition of competitive success

Qdrat wins when a company can deploy it privately, connect the systems it already owns, gradually centralize work and service operations, and eventually remove multiple SaaS products **without losing capability or control**.

The desired outcome is not "Qdrat has a Jira module and a Zendesk module." It is:

> Qdrat makes the boundary between project work, service work, company operations, knowledge, data and AI disappear where the business benefits from that unification — while preserving strong domain semantics, permissions and evidence underneath.
