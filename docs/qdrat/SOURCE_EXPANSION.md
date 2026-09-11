# Qdrat — Source Expansion Landscape

## Purpose

This document extends the founder-supplied source landscape with additional public projects discovered specifically to close capability gaps in Qdrat's goal of becoming the best private Company Operating System.

The founder-supplied sources remain governed by `SOURCE_AUTHORIZATIONS.md`. Sources discovered by Qdrat research are **not** silently labeled with private founder authorization; they are recorded as `DISCOVERED_PUBLIC_SOURCE` and enter Qdrat only through their observed public license and normal provenance review unless a separate authorization record is later added.

## Intake vocabulary

Every source should eventually receive one primary intake decision:

- `COPY_COMPONENT` — copy a bounded implementation behind a Qdrat-owned contract.
- `ADAPT_PATTERN` — learn from architecture/UX/protocol patterns without copying the implementation.
- `RUN_AS_SERVICE` — integrate an isolated service behind a stable adapter.
- `DEPENDENCY` — consume the project as a normal dependency/component.
- `REFERENCE_ONLY` — use for requirements, behavior, tests, and design comparison.
- `REJECT` — do not use because the cost, license, security, maintenance, or architecture fit is poor.

No whole repository becomes Qdrat architecture merely because its code is available.

## Founder-supplied addition — Block Buzz

| Source | Authority | Observed license | Qdrat value | Initial posture |
|---|---|---|---|---|
| `block/buzz` | `FOUNDER_STANDING_AUTHORIZATION` | Apache-2.0 | Humans and agents as first-class principals; one event/audit substrate; agent-first CLI; workflows; channels/threads/canvases; signed events; hash-chain audit; project memory; branch-as-room concepts | `ADAPT_PATTERN` + selective `COPY_COMPONENT` after path-level qualification |

### Buzz concepts Qdrat should absorb

1. **Agents are principals, not omnipotent bots.** Every agent gets a stable identity, memberships, scopes, audit history, lifecycle, and explicit delegation.
2. **Conversation and work share evidence.** A ticket, project, incident, workflow, decision, approval, and agent action should be linkable in one timeline instead of scattered across products.
3. **Agent-first interfaces matter.** CLI/tool APIs should be deterministic, structured, and usable without a GUI.
4. **The event trail is a product feature.** Work should retain why a decision happened, not merely its current state.
5. **Zero-noise defaults are valuable.** Qdrat Home/My Work should prioritize actionable items rather than recreate notification overload.
6. **Do not inherit Nostr automatically.** Qdrat already has a PostgreSQL/domain-event direction; Buzz's protocol is a pattern candidate, not a mandated substrate.

## Founder-supplied additions — agent runtime, sandbox and private voice

The founder subsequently supplied the following sources under the same standing authorization. They must be evaluated as a coherent extension of Qdrat AI/Trust rather than as unrelated utilities.

| Source | Authority | Observed public license posture | Qdrat value | Initial posture |
|---|---|---|---|---|
| `chaitanyagiri/munder-difflin` | `FOUNDER_STANDING_AUTHORIZATION` | MIT in current README | Multi-agent supervisor, local terminal-agent processes, shared memory, mailboxes, task ledger, approvals, circuit breakers, BYO provider/local model | `ADAPT_PATTERN` + selective `COPY_COMPONENT` after exact-path qualification |
| `jaredrhod/fullstack-agent` | `FOUNDER_STANDING_AUTHORIZATION` | AGPL-3.0-or-later in current README; founder separately states copy permission | Persistent memory, voice, visual presence, optional embodied input, conversational installer and self-repair UX | `ADAPT_PATTERN`; selective copy only with exact provenance/grant evidence recorded |
| `opensandbox-group/OpenSandbox` | `FOUNDER_STANDING_AUTHORIZATION` | Apache-2.0 | General-purpose agent sandbox, SDK/CLI/MCP, Docker/Kubernetes runtimes, egress policy, credential vault, gVisor/Kata/Firecracker isolation | Strong `DEPENDENCY`/`RUN_AS_SERVICE` candidate for Qdrat Agent Execution Plane |
| `OpenWhispr/openwhispr` | `FOUNDER_STANDING_AUTHORIZATION` | MIT | Cross-platform local dictation, Whisper/Parakeet-class ASR, meeting transcription/diarization, notes, local/cloud model routing, enterprise controls, MCP/API | `ADAPT_PATTERN` + selective `COPY_COMPONENT` for Qdrat Voice Plane |
| `Starmel/OpenSuperWhisper` | `FOUNDER_STANDING_AUTHORIZATION` | MIT | Lightweight native macOS transcription, hotkey/hold-to-record UX, local Whisper/Parakeet execution | `ADAPT_PATTERN` + selective native-client donor study |
| `langflow-ai/openrag` | Existing `FOUNDER_STANDING_AUTHORIZATION`, re-confirmed | Apache-2.0 in existing qualification | RAG ingestion/orchestration and retrieval pipeline patterns | Existing `DEPENDENCY`/`REFERENCE` candidate; authorization re-confirmed |

### Qdrat Agent Execution Plane requirements derived from these sources

Agents that can execute code, browse, manipulate files, call tools or operate external systems must run through a governed execution boundary. The plan should define sandbox lifecycle, image/runtime profiles, CPU/memory/time budgets, filesystem mounts, network ingress/egress policy, secret injection without secret disclosure, provenance, artifact capture, trace correlation, approval gates, kill/circuit-breaker behavior and local/offline operation. OpenSandbox is the leading evaluated substrate candidate; Qdrat contracts must remain substrate-independent.

### Qdrat Voice Plane requirements derived from these sources

Voice is a first-class local interaction mode, not a cloud-only convenience. Plan for push-to-talk and hands-free modes, dictation into Qdrat fields, multilingual transcription, meeting capture, diarization, optional voice fingerprinting where appropriate, transcript-to-knowledge ingestion, voice commands to agents, local ASR/model packs, explicit recording consent indicators, retention controls, redaction, searchable provenance and complete offline operation. OpenWhispr and OpenSuperWhisper are donor/reference candidates; the Qdrat Voice contract must remain cross-platform and model-agnostic.

### Multi-agent orchestration requirements derived from these sources

Munder Difflin reinforces the need for a supervisor/dispatcher pattern, per-agent identities, durable task ledger, agent mailbox/event routing, shared-but-governed memory, provider abstraction, autonomy levels, approval queues, loop/cost circuit breakers and live observability. Qdrat should implement these semantics through its own principal, Flow, audit and policy contracts rather than copying a desktop-office metaphor as the canonical UX.

## Discovered public sources — Work, project and portfolio management

| Source | Status / observed license | Gap covered | Initial Qdrat posture |
|---|---|---|---|
| `kanboard/kanboard` | Active; MIT | Minimal fast kanban, task movement, automation simplicity | `ADAPT_PATTERN`; possible selective component study |
| `opf/openproject` | Active; GPL-3.0 | Portfolio/project planning, work packages, Gantt, roadmaps, time tracking, agile depth | `REFERENCE_ONLY` by default |
| `makeplane/plane` | Founder-supplied; AGPL-3.0 current repo metadata | Modern Jira/Linear-style UX, cycles, modules, triage, docs | Governed by founder authorization + donor intake review; do not make its model canonical |
| `block/buzz` | Founder-supplied; Apache-2.0 | Human-agent collaborative workspaces, workflows, project memory | See Buzz section above |

Qdrat Work should combine the interaction speed of modern issue trackers with enterprise planning depth, but use the same company identity, approvals, files, knowledge, graph, service and AI layers as every other Qdrat suite.

## Discovered public sources — Customer support and omnichannel service

| Source | Status / observed license | Gap covered | Initial Qdrat posture |
|---|---|---|---|
| `chatwoot/chatwoot` | Active; MIT outside separately licensed `enterprise/` paths | Shared inbox, live chat, email/support conversations, customer contact UX, widget/channel patterns | `COPY_COMPONENT` or `ADAPT_PATTERN` only from qualified MIT paths |
| `LiveHelperChat/livehelperchat` | Active; Apache-2.0 | Live support, voice/video/screenshare, Telegram/WhatsApp/Facebook patterns, bots | `ADAPT_PATTERN`; selective donor candidate |
| `zammad/zammad` | Active; AGPL-3.0 | Mature helpdesk: ticket lifecycle, channels, SLA/escalation, macros, knowledge/support operations | `REFERENCE_ONLY` by default |
| `frappe/helpdesk` | Active; AGPL-3.0 | Modern customer-service UX and ticketing patterns | `REFERENCE_ONLY` by default |
| `papercups-io/papercups` | Founder-supplied; MIT | Lightweight live customer chat/helpdesk patterns | Existing qualified donor candidate |
| `uvdesk/*` | Founder-supplied | Helpdesk/service patterns | Existing authorized landscape; path/license qualification required |

Qdrat Service must not be a separate Zendesk clone. External customer support, employee service, IT service, HR cases, vendor cases, incidents and requests should reuse one case/request/workflow substrate with domain-specific policies and views.

## Discovered public sources — ITSM, CMDB, infrastructure and service graph

| Source | Status / observed license | Gap covered | Initial Qdrat posture |
|---|---|---|---|
| `glpi-project/glpi` | Active; GPL-3.0 | ITIL service desk, CMDB, assets, licenses, inventory, data-center operations | `REFERENCE_ONLY` by default |
| `netbox-community/netbox` | Active; Apache-2.0 | Infrastructure source-of-truth, DCIM/IPAM, typed topology, plugin/API discipline | `ADAPT_PATTERN`; selective donor/dependency candidate |
| `grokability/snipe-it` | Founder-supplied; AGPL-3.0 | Asset/device assignment and lifecycle | Existing reference candidate |
| `backstage/backstage` | Active; Apache-2.0 | Developer portal, catalog, plugin architecture, self-service templates | `ADAPT_PATTERN`; selective dependency/component study |

Qdrat's Company Digital Twin should generalize beyond people: services, software, devices, facilities, vendors, endpoints, integrations, databases, documents, customers, projects and risks can participate in the same typed graph without collapsing their domain schemas.

## Discovered public sources — Workflow, BPM and durable execution

| Source | Status / observed license | Gap covered | Initial Qdrat posture |
|---|---|---|---|
| `temporalio/temporal` | Active; MIT | Durable execution, retries, long-running workflows, timers, failure recovery | Optional `RUN_AS_SERVICE` only when native Qdrat Flow proves insufficient |
| `flowable/flowable-engine` | Active; Apache-2.0 | BPMN/process semantics, human tasks, formal process management | `ADAPT_PATTERN`; possible isolated service study |
| `activepieces/activepieces` | Active; MIT core with separately licensed EE paths | Integration pieces, workflow builder, MCP/agent tool catalog | Selective `ADAPT_PATTERN`/`COPY_COMPONENT` from qualified core paths |
| `gorules/zen` + `gorules/jdm-editor` | Founder-supplied; MIT | Deterministic decision execution and rule editor | Existing leading Rules candidate |

Qdrat Flow remains Qdrat-owned. External engines are implementation options, not the business-process source of truth.

## Discovered public sources — Data Fabric and integration

| Source | Status / observed license | Gap covered | Initial Qdrat posture |
|---|---|---|---|
| `apache/camel` | Active; Apache-2.0 | Enterprise integration patterns and hundreds of protocol/component adapters | `ADAPT_PATTERN`; investigate selected components/sidecar use rather than importing the framework wholesale |
| `debezium/debezium` | Active; Apache-2.0 | CDC for multiple databases and durable incremental synchronization | Optional `DEPENDENCY`/`RUN_AS_SERVICE` for certified `SYNCED` connectors |
| `hasura/graphql-engine` | Founder-supplied; Apache-2.0 | Data/API access patterns | Existing source landscape |
| `postgis/postgis` | Founder-supplied | Geospatial operations/geofencing | Existing dependency candidate |

The Data Fabric should expose one Qdrat connector contract while allowing protocol-specific implementations. It should not reimplement mature CDC or integration protocols without a clear reason.

## Discovered public sources — Identity, authorization and policy

| Source | Status / observed license | Gap covered | Initial Qdrat posture |
|---|---|---|---|
| `keycloak/keycloak` | Active; Apache-2.0 | OIDC/SAML identity federation, enterprise IdP behavior | Optional `RUN_AS_SERVICE`; standards reference, never mandatory kernel dependency |
| `openfga/openfga` | Active; Apache-2.0 | Zanzibar-style relationship-based/fine-grained authorization | `ADAPT_PATTERN`; evaluate optional policy service at scale boundaries |
| `open-policy-agent/opa` | Active; Apache-2.0 | General policy-as-code decisions and compliance policy evaluation | `ADAPT_PATTERN`; possible optional policy evaluator |
| `infisical/infisical` | Founder-supplied; MIT core / EE boundary | Secrets and privileged credential patterns | Existing selective donor/dependency candidate |

Qdrat authorization needs a stable native vocabulary first: subject/principal, relation, object, action, purpose, data class, organization scope, delegation and time. Engines may execute policy, but must not define Qdrat's domain semantics.

## Discovered public sources — Knowledge, search and collaboration

| Source | Status / observed license | Gap covered | Initial Qdrat posture |
|---|---|---|---|
| `zulip/zulip` | Active; Apache-2.0 | High-signal topic/thread collaboration and notification discipline | `ADAPT_PATTERN`; selective donor study |
| `BookStackApp/BookStack` | GitHub mirror now points to Codeberg; MIT | Structured wiki/document UX | `REFERENCE_ONLY` unless current Codeberg upstream is qualified |
| `meilisearch/meilisearch` | Active; mixed MIT + BUSL-1.1 enterprise portions | Fast typo-tolerant/hybrid search | Optional `RUN_AS_SERVICE`/dependency only after path/edition qualification |
| `outline/outline` | Founder-supplied; restricted source license | Modern knowledge UX | Existing reference candidate |
| `toeverything/affine` | Founder-supplied; mixed | Local-first collaborative blocks/canvas | Existing selective donor/reference candidate |
| `hcengineering/platform` | Founder-supplied; EPL-2.0 | Integrated collaboration/work patterns | Existing architecture reference |

Search remains a Qdrat contract. PostgreSQL FTS is the baseline; external search becomes an optional scale/capability profile.

## Discovered public sources — Observability and operational evidence

| Source | Status / observed license | Gap covered | Initial Qdrat posture |
|---|---|---|---|
| `open-telemetry/opentelemetry-collector` | Active; Apache-2.0 | Standard collection/export pipeline for traces, metrics and logs | `DEPENDENCY`/optional local service profile |
| `prometheus/prometheus` | Active; Apache-2.0 | Metrics, alerting inputs, operational telemetry | Optional `RUN_AS_SERVICE`/integration profile |
| `louislam/uptime-kuma` | Founder-supplied; MIT | Human-friendly service monitoring UX | Existing donor/reference candidate |
| `bluewave-labs/checkmate` | Founder-supplied | Monitoring patterns | Existing reference candidate |

Qdrat must observe both itself and company services without forcing telemetry to leave customer-controlled infrastructure.

## Discovered public sources — Platform / low-code / application framework

| Source | Status / observed license | Gap covered | Initial Qdrat posture |
|---|---|---|---|
| `frappe/frappe` | Active; MIT | Metadata-driven application framework, forms, hooks, multitenancy, APIs | `ADAPT_PATTERN`; selective donor study for Studio/app architecture |
| `backstage/backstage` | Active; Apache-2.0 | Plugin/catalog/self-service extension model | `ADAPT_PATTERN` |
| `cortezaproject/corteza` | Founder-supplied; Apache-2.0 | Low-code structured apps/workflows | Existing strong Studio donor |
| `baserow/baserow` | Founder-supplied; mixed with permissive OSE paths | App/database/view builder | Existing selective Studio donor |
| `gristlabs/grist-core` | Founder-supplied; Apache-2.0 | Relational spreadsheet/formula/views | Existing Studio/Data donor |

## Capability gaps this expansion closes

The combined source portfolio now gives Qdrat serious references or donor candidates for:

- project, issue, product and portfolio management;
- internal and external service delivery;
- omnichannel customer support;
- ITSM, CMDB, assets and service topology;
- human-agent collaboration;
- durable workflows, BPM and decision rules;
- broad integration and CDC;
- fine-grained authorization and policy evaluation;
- knowledge, chat and search;
- observability and operational evidence;
- low-code custom application building;
- identity federation and enterprise interoperability.

The remaining problem is no longer finding one application for every category. It is designing **one Qdrat semantic and interaction model** so these capabilities reinforce each other instead of recreating a fragmented suite inside a single repository.

## Reverification rule

Repository licenses, editions, default branches and product boundaries can change. Before any code intake, reverify the exact source commit and path-level license at that time. This document records research truth, not a permanent license guarantee.
