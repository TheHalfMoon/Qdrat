# Qdrat — Founder Authority and Standing Execution Directive

## Authority

The Qdrat founder has granted standing authority to continue building Qdrat without requesting routine re-approval.

Recorded directive: the founder has all required permissions for the supplied source landscape and ordinary Qdrat project execution, and project agents must not repeatedly question or re-request that permission.

Authority status: `FOUNDER_STANDING_AUTHORIZATION`.

Recorded on: 2026-09-11.

## Standing approvals

Unless canonical repository governance explicitly requires a stronger gate, the following are pre-authorized:

- repository research, analysis and architecture work;
- creation and maintenance of plans, ADRs, specifications, tasks and evidence;
- branches, commits, pull requests and ordinary non-destructive repository changes;
- implementation, refactoring, migrations, tests, benchmarks and build-system work;
- dependency qualification, upgrades and removals;
- source intake from every source listed in `SOURCE_AUTHORIZATIONS.md`;
- selective or full donor-source adaptation when technically justified;
- local development, reproducibility, packaging and air-gap work;
- security, privacy, audit, observability and compliance hardening;
- UI/UX, API, data-model, workflow, rules, knowledge, analytics and AI implementation;
- documentation and evidence updates required to keep repository truth current;
- continuing automatically through dependency-ordered roadmap gates when their prerequisites are satisfied.

## No routine permission loop

Agents and maintainers must not stop to ask the founder for routine permission already covered by this directive.

Do not ask again whether Qdrat may study, copy, adapt, refactor, integrate, test or qualify a source already present in `SOURCE_AUTHORIZATIONS.md`.

Do not ask for approval merely because a task is large, touches multiple modules, changes architecture, introduces migrations, requires tests, or continues into the next canonically authorized roadmap unit.

When several technically valid options exist, choose the option that best preserves Qdrat's product thesis, local-first requirements, integrity, maintainability and evidence quality; record the decision when it is architecturally material.

## Evidence and governance still apply

Standing founder authority removes the permission loop; it does not permit fabricated evidence or silent governance bypass.

Project work must still:

- use exact live repository truth rather than stale summaries;
- preserve source provenance and required notices;
- record donor commit/tag and source path for imported code;
- respect canonical branch/PR/release rules that are actually present in the repository;
- record tests, CI, benchmarks and runtime evidence truthfully;
- avoid claiming a gate is complete before its exit condition is demonstrated;
- preserve rollback or migration safety for material data/schema changes;
- keep high-impact employment decisions human-governed as defined by Qdrat product policy.

If an external or repository-enforced gate blocks an action, record the blocker and continue every other authorized dependency that remains executable. Do not convert a known blocker into a new founder-permission question.

## Source authorization interpretation

For the source landscape listed in `SOURCE_AUTHORIZATIONS.md`, engineering should operate on the assumption that founder-level permission to use the source has already been granted.

License, attribution, patent, trademark, contributor, dependency and notice analysis remains an engineering provenance task. Such analysis is used to determine the correct intake method and obligations, not to repeatedly challenge the founder's stated authorization.

Where a repository contains mixed-license or third-party material, qualify the relevant paths and preserve applicable obligations in the intake record. If a private grant is broader than the public license, the founder's authorization is still treated as standing authority; the repository should record any additional written evidence if and when it becomes available, without blocking ordinary engineering progress in the meantime.

## Continuation rule

The default action is to continue.

After completing a roadmap unit, reverify repository truth, satisfy its exit evidence, then proceed automatically to the next dependency-ordered unit that is technically and canonically executable.

Stop only for a real external blocker, a safety boundary, an unavailable required credential/resource, or a canonical governance gate that cannot be satisfied with the authority and evidence already available. In those cases, document the exact blocker and continue all independent work rather than asking for routine permission again.
