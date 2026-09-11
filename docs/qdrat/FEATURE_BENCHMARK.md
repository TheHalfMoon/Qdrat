# Qdrat People — Competitive Feature Benchmark

## Benchmark intent

This document is a requirements inventory, not a mandate to imitate competitor UI or proprietary implementation. Competitor behavior is used to identify user needs; Qdrat implements original workflows and code.

## Baseline inherited from Horilla

The imported Horilla base already provides employee management, recruitment, onboarding/offboarding, attendance, leave, payroll, performance, assets, helpdesk, projects, reporting, API surfaces, audit capabilities, automation, biometrics, LDAP, meetings, backup, and additional supporting modules. Qdrat should preserve useful functionality while replacing weak domain boundaries and UX incrementally.

## Commercial benchmark coverage

### BambooHR
Benchmark against core HR data/reporting, recruiting, onboarding, time and attendance, leave, payroll, benefits, compensation, performance, recognition, employee experience, compliance, global employment, mobile self-service, dashboards, workflows, and embedded AI assistance.

### Zoho People
Benchmark against employee records, attendance, shifts, leave, performance, cases, automation, custom forms, reports, mobile experiences, integrations, and Zia-style conversational navigation/actions while implementing Qdrat AI locally and with stronger execution governance.

### Workday and Oracle HCM
Benchmark the enterprise model: unified workforce data, positions, skills intelligence, workforce planning, talent, recruiting, learning, payroll/workforce management, employee journeys, analytics, and governed AI/digital agents.

### SAP SuccessFactors
Benchmark global core HR/payroll, talent, learning, succession, compensation, onboarding/crossboarding/offboarding, workforce planning, employee experience, and AI-assisted work.

### Rippling
Benchmark the joiner-mover-leaver bridge between HR, identity, application access, devices, software, policy automation, workflow automation, recruiting, time, payroll, benefits, learning, and analytics.

### Deel
Benchmark multi-worker/global worker models, contractor/EOR abstractions, workforce planning, compensation, recruiting, learning, reviews, surveys, workflows, role/permission governance, global payroll concepts, and agentic HR operations.

### Personio, HiBob, and Factorial
Benchmark modern mid-market UX for workflows, self-service, documents/e-signatures, employee experience, communities, performance, surveys, compensation, learning, time, expenses/assets, reporting, and service delivery.

## Capabilities Qdrat must add beyond the inherited baseline

1. Position management and effective-dated organizational history.
2. Workforce planning with headcount and cost scenarios.
3. Skills graph with ESCO-based seed ontology and customer-defined extensions.
4. Internal talent marketplace, career paths, succession, and mentorship.
5. Rich compensation planning, salary bands, cycle budgets, pay-equity analysis, and total rewards.
6. Learning paths, certifications, compliance learning, and evidence tracking.
7. Employee listening, recognition, communities, and action planning.
8. Visual workflow builder with durable execution evidence.
9. Enterprise identity/access and IT lifecycle orchestration.
10. Policy/knowledge management with permission-aware local RAG.
11. Country/compliance-pack framework, beginning with Saudi Arabia.
12. Local AI agents with capability security, approval gates, provenance, and evaluations.
13. Point-in-time analytics and natural-language analytics over authorized data.
14. Privacy operations: retention, deletion/anonymization, legal hold, subject-request workflows, and export controls.
15. Extensible integration/plugin SDK with versioned API/event contracts.

## Reference standards

Use HR Open Standards where useful for interoperable HR data exchange. Seed the skills/occupation model from ESCO where license and attribution requirements are satisfied, with optional O*NET mappings for additional occupational detail. Support SCIM for identity lifecycle interoperability and OIDC/SAML/LDAP for authentication/federation.
