# Qdrat — UX North Star

## Goal

Qdrat should expose enterprise breadth without enterprise-software cognitive load. Users should not need to understand product module boundaries to complete work.

The experience is organized around people, objects, work and decisions—not around a sidebar containing every feature the company purchased.

## Universal surfaces

### Home
Home is role-aware and configurable. It answers: what changed, what needs my attention, what is at risk, and what should I do next?

Examples:
- employee: schedule, leave, payslip, tasks, required acknowledgements, learning and requests;
- manager: approvals, team changes, staffing, attendance exceptions, goals and risks;
- HR: lifecycle events, cases, hiring, payroll readiness, compliance and workforce signals;
- executive: workforce/cost/skills/operations metrics and material exceptions;
- service/ops: queue, incidents, assets, requests and SLA risks.

### My Work
One work queue contains approvals, tasks, reviews, interviews, document signatures, cases, workflow human steps and assigned follow-ups across every suite.

Each item shows why it is assigned, deadline/SLA, relevant evidence, required decision and downstream effect. Users never need to hunt through modules for pending work.

### Global search
One permission-aware search covers people, positions, teams, projects, tickets, policies, documents, assets, customers, custom objects and actions.

Results support direct navigation and actions. Search may combine structured lookup, lexical search, semantic retrieval and graph relationships while preserving source permissions.

### Command palette
A keyboard-first palette supports navigation and safe actions: create request, find employee, start workflow, open report, add candidate, issue asset, run rule simulation, open Studio, invoke an approved agent tool.

### Ask Qdrat
The AI entry point exists globally but remains contextual. It sees the current object/page, user role, allowed data and relevant company knowledge.

It answers with sources when evidence is used, previews writes before execution and routes high-risk actions through approval workflows.

### Inbox and notifications
One inbox combines actionable notifications from every suite. Notifications are grouped by object/workflow and support digesting to reduce noise.

### Object page
Every major object follows a consistent shell:
- identity/header and status;
- key fields;
- relationships;
- activity timeline;
- documents/files;
- comments/mentions;
- tasks/workflows;
- permissions-sensitive analytics;
- AI/context actions;
- audit/history for authorized roles.

A Person, Position, Project, Ticket, Asset, Policy or custom object should feel related even though domain-specific panels differ.

## Core view system

Qdrat uses the same view grammar across modules:
- table/grid;
- cards;
- kanban;
- calendar;
- timeline/Gantt;
- hierarchy/tree;
- relationship graph;
- map where location matters;
- dashboard/chart;
- form/detail.

Views are configurations over objects, not isolated implementations. Qdrat Studio lets authorized users save, share and govern them.

## Progressive complexity

Default screens prioritize the most common task. Advanced configuration lives behind explicit builder/admin modes.

The product should work at three depths:
1. `Do`: complete the task with minimal fields and guidance.
2. `Understand`: inspect context, history, relationships and metrics.
3. `Design`: configure schema, rules, workflows, permissions and reports.

This prevents powerful features from making ordinary employee and manager experiences intimidating.

## Explainability as UX

Qdrat should answer `why` directly in the interface:
- why this approval came to me;
- why this leave balance changed;
- why this payroll validation failed;
- why this person has access;
- why this rule produced the result;
- why an AI answer or recommendation was produced;
- which data/source/version was used.

Rules, workflows and AI traces should expose human-readable explanations, not only developer logs.

## Safe action design

Sensitive actions show:
- what will change;
- affected objects/people;
- validation warnings;
- permission/policy checks;
- downstream workflows/integrations;
- whether the operation is reversible;
- required approvals.

Bulk actions and AI actions use the same preview/diff pattern.

## Arabic and bilingual design

Arabic/English support is structural:
- first-class RTL/LTR layout tests;
- mixed-direction names, IDs and numeric content;
- localized search aliases;
- Hijri/Gregorian display options where applicable;
- Arabic-friendly document templates and PDF output;
- mirrored navigation/icon behavior where semantically required;
- terminology packs per country/customer.

Do not bolt RTL onto a completed English design.

## Mobile and field use

The PWA/mobile experience prioritizes employee and manager actions, attendance, leave, approvals, tasks, documents, asset handoffs, field work and notifications.

Local/private does not mean LAN-only UX. Customers may expose their own secure endpoint/VPN; Qdrat should not require a vendor cloud relay.

## Migration experience

Making Qdrat the default company platform requires exceptional onboarding.

Build guided import/migration flows for:
- employee/organization data;
- payroll opening balances;
- leave balances;
- candidates;
- assets;
- documents;
- projects/tasks;
- tickets;
- custom tables;
- identity mappings.

Every import supports mapping, validation, dry run, error export, reconciliation report and rollback/compensation where feasible.

## Administrator experience

Admins get one control center for:
- modules/features;
- identity/federation;
- permissions/delegations;
- Studio schemas;
- Flow/Rules;
- integrations/credentials;
- country packs;
- AI models/tools/policies;
- data retention/privacy;
- backup/restore;
- system health;
- upgrade readiness;
- license/SBOM/provenance evidence;
- egress policy.

## Performance target philosophy

The shell, search, employee self-service and approval flows must feel immediate on a normal private-network deployment. Advanced AI or analytics may take longer, but the interface should stream progress and never make deterministic business actions depend on an LLM response.

## Design test

A feature is not integrated merely because it appears in the navigation. It is integrated only when it reuses Qdrat identity, object relationships, permissions, My Work, search, audit, notifications and design grammar.
