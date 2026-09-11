# Qdrat People — Master Product Plan

## Product thesis

Qdrat People is a private, local-first People Operating System for the AI era. It must combine the breadth of a modern HRIS/HCM suite with a position-and-skills-centric workforce model, durable workflow automation, explainable local AI agents, and enterprise-grade privacy controls. Cloud connectivity is optional and disabled by default.

Qdrat People is not a reskin of Horilla. Horilla is the functional bootstrap and upstream source base; Qdrat becomes a distinct product through a new canonical data model, permission model, workflow layer, AI plane, design system, country/compliance packs, and integration architecture.

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
10. Start as a modular monolith. Split services only where isolation, scale, or deployment boundaries justify it.

## Product surfaces

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
Asset inventory, device assignment, software/access requests, lifecycle triggers from HR changes, LDAP/Active Directory/Keycloak connectors, SCIM, SSO, joiner-mover-leaver workflows, entitlement review, and access recertification.

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
- Builder Agent: creates forms, reports, automations, policies, and workflow drafts from natural language; changes require preview/diff/approval before activation.

## Differentiators

Qdrat wins by combining capabilities normally split across HRIS, talent, workforce planning, IT lifecycle, service delivery, and AI platforms while keeping customer data under customer control. The product should provide a local AI control plane, position-centric workforce digital twin, skills graph, permission-aware RAG, country packs, programmable workflows, time-travel data, and inspectable automation evidence in one system.

## Saudi Arabia first-class pack

The first country pack should support Saudi employment structures and configurable rules for labor-law working time and leave, end-of-service calculations, Qiwa contract workflows/adapters, Nitaqat-oriented workforce views, Mudad/Wage Protection exports or approved integrations, GOSI-related payroll data, Hijri/Gregorian dates, Arabic documents, Saudi holidays, and PDPL privacy controls. Integrations that require external credentials remain disabled until configured by the customer.

## Definition of "best"

The product is not considered best because it has the longest feature list. It should measurably reduce HR administrative effort, support trustworthy decisions, provide faster employee self-service, shorten recruiting/onboarding cycles, reduce payroll/compliance errors, expose skills and workforce gaps, survive disconnected deployments, and make every sensitive action explainable and auditable.
