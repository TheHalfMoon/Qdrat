# Unified Work

Owner: qdrat/work. WorkItem has type, project, title, permitted rich text, status revision, assignee Principal, requester, priority, estimates, dates and links. Issue/bug/story/task/epic are configurable typed work categories; Request/Case retains separate Service obligations. Project defines workflow, permissions and planning policy.

A shared lifecycle publishes transitions, required fields, validators and approval references. Every transition invokes an action with expected revision. Dependencies are typed blocks/relates/duplicates/parent; blocking edges reject cycles, related edges may be cyclic. Parent/child rollups are computed with declared semantics, not forced percentages.

Initial list/board supports triage, assignment, filters, labels, comments, attachments and bulk preview. Then cycles/milestones, timeline/Gantt, roadmaps, goals, portfolio, workload and capacity. Capacity joins authorized employment calendars and leave availability without exposing leave reason or salary. Missing source freshness makes capacity unknown. Meetings attach agenda/decisions/tasks to work rather than create a second task store.

GitHub/GitLab/Azure/Jira integrations retain foreign IDs and source authority. Imported issue states map explicitly; unknown states quarantine rather than become “done”. Commit/PR references are evidence links, not proof that business acceptance is met. SpecGrain-derived agent tasks can be WorkItems but governance state remains an evidence-backed execution adapter.

UX borrows Linear's focused triage, GitHub's direct issue/PR references, Plane cycles, Asana/Monday flexible views and OpenProject planning depth. Simplicity is a hypothesis tested by employee/admin journeys, not a claim that competitors lack capability.

Acceptance: concurrent move conflict, dependency cycle detection, bulk selection drift, restricted comments/attachments, undo as a new authorized transition, large-list keyboard navigation, Arabic mixed identifiers, calendar boundaries and import reconciliation. No source hosting, CI runner fleet or arbitrary project scripting in the first Work gate.
