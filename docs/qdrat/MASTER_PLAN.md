# Qdrat — Master Product Plan

## Product thesis

Qdrat is a private, local-first Company Operating System for the AI era. `Qdrat People` is the first complete suite and the first product-quality proof of the shared platform. The long-term platform must combine people, work, service, knowledge, data, operations and trust capabilities through one coherent object model, identity/permission system, workflow/rules engine, audit trail, search/knowledge plane and governed AI runtime.

Qdrat People must combine the breadth of a modern HRIS/HCM suite with a position-and-skills-centric workforce model, durable workflow automation, explainable local AI agents, and enterprise-grade privacy controls. Cloud connectivity is optional and disabled by default.

Qdrat is not a reskin of Horilla and must not become a pile of copied applications. Horilla is the functional HR bootstrap and upstream source base. Qdrat becomes a distinct platform through a canonical company/people model, Qdrat Studio, permission model, workflow/rules layer, AI plane, design system, country/compliance packs, extension SDK and integration architecture.

See `COMPANY_OS_STRATEGY.md`, `CAPABILITY_ARCHITECTURE.md`, `SOURCE_LANDSCAPE.md` and `EXECUTION_ROADMAP.md` for the broader company-OS design and donor qualification.

## Non-negotiable principles

1. Local-first and deployable without public cloud dependencies.
2. No telemetry, model calls, or data egress unless an administrator explicitly enables them.
3. PostgreSQL is the production system of record; SQLite remains development-only where useful.
4. Human authorization remains mandatory for high-impact employment decisions.
5. Every AI answer that relies on company knowledge should provide inspectable provenance.
6. Every AI action is permission-scoped, dry-runnable, reviewable, and auditable.
7. Effective-dated data and point-in-time history are first-class concepts.
8. Job, position, worker, person, legal entity, and organizational unit are separate canonical objects.
9. Arabic and English, including first-class RTL UX, are product requirements rather than translation afterthoughts.
10. Start as a modular monolith. Split services only where isolation, scale, runtime or deployment boundaries justify it.
11. Core regulated objects remain strongly typed; customer extensions use governed metadata rather than unrestricted EAV.
12. A capability may not create a parallel identity, permission, workflow, audit, file or AI-governance system without an explicit ADR.
13. Donor code is imported only behind Qdrat-owned contracts with exact provenance and license boundaries.
14. Qdrat People reaches product excellence before additional suites are allowed to dilute execution focus.

## Qdrat Platform surfaces

### Qdrat Studio
Custom objects, typed fields, relationships, formulas, forms, tables, kanban, calendars, timelines, graph views, permissions, workflows, reports, dashboards and extension manifests. Studio lets customers model business processes without source forks while core regulated objects remain relational and strongly typed.

### Qdrat Flow and Rules
Durable workflows coordinate triggers, approvals, human tasks, timers, SLAs, integrations and agent-assisted steps. Deterministic decision rules are versioned, tested and simulated separately from workflow orchestration.

### Qdrat Graph
Typed relationship projections connect people, positions, teams, skills, projects, documents, assets, policies, access, customers and other business objects. Edges carry provenance (`SYSTEM`, `EXTRACTED`, `INFERRED`) so graph-assisted AI remains inspectable.

### Qdrat Knowledge
Permission-aware documents, policies, wiki/pages, records, OCR/parsing, full-text search, semantic retrieval, graph traversal, citations, retention and legal holds.

### Qdrat Data
Custom data, operational dashboards, metrics, reports, cohorts, surveys, event analytics, advanced BI and natural-language analytics under the same permission model.

### Qdrat AI
A local-first model/tool/agent runtime shared by every suite. Agents are governed views over platform capabilities, not separate chatbots with duplicate permissions or memory.

## Qdrat People product surfaces

### People Core
Employee and worker records, legal entities, organizational units, positions, jobs, contracts, lifecycle changes, documents, dependents, emergency contacts, custom fields, employee and manager self-service, org charts, directories, announcements, and acknowledgements.

### Workforce Structure and Planning
Position management, headcount plans, vacancies, cost centers, budget ownership, headcount requests, scenario planning, workforce cost simulation, skills supply/demand, succession risk, spans and layers, and historical/future-dated organization views.

### Recruiting and Talent Acquisition
Requisitions, career pages, candidate portal, sourcing/import, referrals, talent pools, screening, interview plans, scorecards, scheduling, offers, approvals, background-check adapters, recruiting analytics, and controlled AI assistance.

### Journeys
Onboarding, crossboarding, internal transfer, promotion, leave-of-absence return, and offboarding. Journeys coordinate tasks, documents, training, access, assets, equipment, knowledge transfer, 30/60/90-day goals, approvals, and reminders.

### Time and Workforce Management
Attendance, shifts, scheduling, time clocks, kiosks, QR/biometric adapters, geofencing rules, overtime, time banks, breaks, project/cost-center time, leave, holidays, absence policies, approvals, and exception handling.

### Payroll and Total Rewards
Payroll rules, earnings/deductions, variable pay, loans, allowances, benefits, payroll simulation, pre-payroll validation, payslips, payment/WPS exports, GL exports, retroactivity, country packs, compensation bands, salary-review cycles, budgets, pay-equity analysis, and total-reward statements.

### Performance, Growth, and Skills
Goals and OKRs, 1:1s, continuous feedback, review cycles, 360 feedback, calibration, competencies, 9-box, career paths, succession, learning plans, certifications, expiry tracking, skills profiles, proficiency evidence, gap analysis, internal opportunities, mentorship, and talent marketplaces.

### Learning
Course catalog, assignments, learning paths, compliance learning, certifications, assessments, evidence, manager assignment, completion analytics, and future SCORM/xAPI interoperability.

### Employee Experience
Pulse surveys, eNPS, wellbeing, recognition, kudos, communities, employee voice, action plans, workplace announcements, events, and configurable experience journeys.

### Employee Relations and Service Delivery
HR helpdesk, cases, confidential cases, grievances, whistleblowing, investigations, knowledge base, SLAs, escalations, templates, service catalog, and evidence packs.

### Assets, Identity, and Access Lifecycle
Asset inventory, device assignment, software/access requests, lifecycle triggers from HR changes, LDAP/Active Directory/identity-provider connectors, SCIM, SSO, joiner-mover-leaver workflows, entitlement review, and access recertification.

### Analytics and People Intelligence
Operational dashboards, custom reports, metric definitions, cohorts, funnels, headcount/turnover, compensation, recruiting, performance, learning, time, payroll, workforce-planning analytics, natural-language analytics, and privacy-preserving aggregate insights.

### Compliance and Governance
Policy management, acknowledgements, records retention, legal holds, privacy requests, data minimization, audit evidence, configurable country packs, compliance calendars, risk registers, AI governance, export controls, and segregation of duties.

## Qdrat AI plane

Qdrat AI is local by default and is a capability framework, not a single chatbot.

- Employee Agent: policy Q&A, leave and time actions, onboarding guidance, payslip explanations, learning and career support.
- Manager Agent: team briefs, approvals, staffing requests, performance preparation, skills gaps, and workload views.
- HR Agent: employee cases, lifecycle actions, policy assistance, workflows, analytics, and compliance preparation.
- Recruiter Agent: job-description assistance, candidate summarization, interview-plan drafting, scheduling, and evidence-grounded comparison. Autonomous rejection is disabled by default.
- Payroll Agent: anomaly detection, missing-data checks, payroll simulation review, and variance explanations.
- Compliance Agent: rule checks, deadlines, evidence collection, policy drift, and audit preparation.
- People Analytics Agent: permission-aware natural-language analytics with aggregate/privacy controls.
- Career Coach: skill-gap analysis, career-path exploration, mentorship, and learning recommendations.
- Service Agent: case triage, knowledge-grounded drafts, SLA awareness and approved service actions.
- Builder Agent: creates forms, objects, reports, automations, policies, rules and workflow drafts from natural language; changes require preview/diff/approval before activation.

## Differentiators

Qdrat wins by combining capabilities normally split across HRIS, talent, workforce planning, low-code/internal tools, IT lifecycle, service delivery, knowledge, analytics and AI platforms while keeping customer data under customer control.

The defensible moat is not feature count alone. It is the unified company graph, local AI control plane, position-centric workforce digital twin, skills graph, permission-aware retrieval, Qdrat Studio, versioned Flow/Rules, country packs, time-travel data and inspectable automation evidence in one system.

## Saudi Arabia first-class pack

The first country pack should support Saudi employment structures and configurable rules for labor-law working time and leave, end-of-service calculations, Qiwa contract workflows/adapters, Nitaqat-oriented workforce views, Mudad/Wage Protection exports or approved integrations, GOSI-related payroll data, Hijri/Gregorian dates, Arabic documents, Saudi holidays, and PDPL privacy controls. Integrations that require external credentials remain disabled until configured by the customer.

## Definition of "best"

The product is not considered best because it has the longest feature list. It should measurably reduce administrative work, integration friction and SaaS fragmentation; support trustworthy decisions; provide faster employee and manager self-service; shorten recruiting/onboarding cycles; reduce payroll/compliance errors; expose skills and workforce gaps; survive disconnected deployments; let customers extend the platform safely; and make every sensitive action explainable and auditable.
