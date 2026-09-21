# Automation Fabric

Automation Fabric is the shared contract and durable execution substrate (C05/C06), not an additional user-facing builder. Flow compiles orchestration; Rules evaluates pure decisions; Studio supplies forms/views; Data provides connector actions; AI produces proposals or agent steps; Execution Plane runs isolated tools. All produce the same ActionDefinition/Run/StepAttempt evidence.

Use PostgreSQL run, step, lease, timer, approval, inbox and outbox tables first. A worker is separate from the web process. At-least-once delivery plus idempotent handlers is the guarantee. Human approval, connector side effect and workflow state may span transactions; never claim distributed atomicity. Broker/cache loss cannot erase a committed run.

Trigger types: domain event, signed webhook, schedule, manual invocation, form submission and permitted signal. Dedupe by trigger source/event ID. Webhooks validate signature over original bytes, time window, subscription identity and payload size before enqueue. A webhook only proposes the configured trigger; payload text cannot select arbitrary actions.

WaterfallStep is generic: ordered provider candidates, eligibility/data-classification checks, validator version, cost ceiling, stop predicate, provenance and failure policy. It applies to enrichment or document extraction, not only sales. Each provider call is a child step with its own credential, egress decision and budget reservation. Prefer existing fresh permitted evidence before purchase/call. A changed provider does not silently send data to a new country.

Research steps accept explicit sources and allowed browsing purposes. Pages and document content are untrusted evidence. Proposed actions return to policy/approval; browser sessions never inherit the user's full desktop credentials.

Flow/agent tools expose the same typed registry over REST/CLI and optional MCP. MCP is an interface, not a source of authority. Tool names, schemas and annotations never replace runtime authorization.

Run UI shows current state, owner, pending human action, cost, evidence, retry/reconcile options and cancellation consequences. Signals debounce/coalesce with effective time, evidence, confidence and expiry; they do not create grants. Operational alerts route into the shared Inbox.

Adoption decision: study n8n/Activepieces connector ergonomics, Refly skills, Flow-Like typed plans, LiveContext app/flow integration, Clay waterfalls and Eigent bounded delegation. Do not embed their independent identities, databases or schedulers. DBOS/Restate/Temporal are reference/qualification candidates; adoption requires workload evidence and an ADR replacing the native adapter, not creating parallel truth.
