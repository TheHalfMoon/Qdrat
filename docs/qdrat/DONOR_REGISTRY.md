# Qdrat — Donor and Dependency Registry

`SOURCE_LANDSCAPE.md` is the broad research/intake map. This registry is stricter: it records sources that are already the inherited base or are serious candidates for code import/runtime dependency. Being present here is not authorization to copy arbitrary files.

## Rules

Every external source is classified before code is copied. Classification options are `BASE`, `DIRECT_DONOR`, `SELECTIVE_DONOR`, `DEPENDENCY`, `REFERENCE_ONLY`, or `REJECTED`.

For every copied file/component record the exact repository, commit/tag, original path, license/SPDX posture, copyright/notice requirements, local modifications and destination path. Repository-level permission or licensing does not erase third-party notices, bundled dependency terms, contributor rights or trademarks.

Reciprocal/restricted source code is not copied into Qdrat core unless the project deliberately accepts the resulting obligations after explicit review. Where useful, such projects can remain references or isolated services with their own source/notice obligations.

## Current base and high-priority candidates

| Source | Role | Observed license posture | Current intended use |
|---|---|---|---|
| `horilla/horilla-hr` | BASE | LGPL-2.1 | Full inherited Git history and HR functional baseline; preserve notices/upstream provenance. |
| `Graphify-Labs/graphify` | DIRECT_DONOR candidate | Apache-2.0 | Deterministic local graph extraction, explained-edge/provenance patterns. |
| `vitali87/code-graph-rag` | DIRECT_DONOR candidate | MIT | AST/graph-RAG and graph traversal/retrieval patterns. |
| `baserow/baserow` | SELECTIVE_DONOR candidate | MIT OSE with premium/enterprise exceptions | Studio/custom-object/view/app-builder patterns; only qualified OSE files. |
| `gristlabs/grist-core` | DIRECT_DONOR candidate | Apache-2.0 | Relational spreadsheet, forms, formulas and view UX. |
| `cortezaproject/corteza` | DIRECT_DONOR candidate | Apache-2.0 | Low-code object/process/privacy/RBAC implementation patterns. |
| `gorules/zen` | DIRECT_DONOR candidate | MIT | Deterministic rules execution. |
| `gorules/jdm-editor` | DIRECT_DONOR candidate | MIT | Visual decision graph/table editor. |
| `apache/superset` | DEPENDENCY candidate | Apache-2.0 | Isolated advanced BI/embedded analytics profile. |
| `Mintplex-Labs/anything-llm` | DIRECT_DONOR candidate | MIT | Local-agent UX, tool-selection and agent-flow patterns. |
| `onyx-dot-app/onyx` | SELECTIVE_DONOR candidate | MIT core + enterprise directories | Connectors, enterprise search, agentic RAG; exclude enterprise files. |
| `langflow-ai/openrag` | DEPENDENCY/REFERENCE candidate | Apache-2.0 | RAG ingestion/orchestration patterns; avoid making it mandatory runtime. |
| `getnao/nao` | SELECTIVE_DONOR candidate | Apache-2.0 majority + enterprise-marked files | Analytics-agent context/evaluation patterns. |
| `PostHog/posthog` | SELECTIVE_DONOR candidate | MIT core + enterprise directory | Event/analytics/experimentation implementation patterns. |
| `Flagsmith/flagsmith` | DIRECT_DONOR/DEPENDENCY candidate | BSD-3-Clause | Feature rollout/configuration patterns. |
| `Infisical/infisical` | SELECTIVE_DONOR/DEPENDENCY candidate | MIT core + enterprise directories | Integration-secret lifecycle patterns; no enterprise import. |
| `strapi/strapi` | SELECTIVE_DONOR candidate | MIT community + enterprise directories | Plugin/admin/generated-API patterns. |
| `calcom/cal.diy` | DIRECT_DONOR candidate | MIT | Scheduling/availability/calendar capabilities. |
| `ErugoOSS/Erugo` | DIRECT_DONOR candidate | MIT | Secure file-sharing patterns. |
| `papercups-io/papercups` | DIRECT_DONOR candidate | MIT | Conversation/support chat patterns. |
| `yuzutech/kroki` | DEPENDENCY candidate | MIT | Local diagram rendering. |
| `gotenberg/gotenberg` | DEPENDENCY candidate | MIT | Local document-to-PDF conversion. |
| `Stirling-Tools/Stirling-PDF` | SELECTIVE_DONOR/DEPENDENCY candidate | MIT majority + excluded subtrees | PDF processing after path-level license qualification. |
| `umami-software/umami` | DIRECT_DONOR candidate | MIT | Privacy-first analytics patterns. |
| `louislam/uptime-kuma` | DIRECT_DONOR/DEPENDENCY candidate | MIT | Health/monitoring UX and checks. |
| `qdrant/qdrant` | DEPENDENCY candidate | Apache-2.0 | Optional semantic/vector retrieval profile, not mandatory baseline. |
| `keycloak/keycloak` | DEPENDENCY candidate | Apache-2.0 | Optional enterprise identity federation. |
| `openfga/openfga` | DEPENDENCY candidate | Apache-2.0 | Optional relationship-based authorization if native policies reach a proven boundary. |
| `ollama/ollama` | DEPENDENCY candidate | MIT | Local model runtime and development ergonomics. |
| `ggml-org/llama.cpp` | DEPENDENCY candidate | MIT | Local/edge inference runtime option. |
| `temporalio/temporal` | DEPENDENCY candidate | MIT | Optional durable orchestration only after native Qdrat Flow proves insufficient. |
| `block/buzz` | DIRECT_DONOR/REFERENCE candidate | Apache-2.0 + founder standing authorization | Human/agent principal symmetry, event/audit patterns, agent-first CLI, workflow/collaboration/project-memory concepts; do not adopt Nostr automatically. |
| `chatwoot/chatwoot` | SELECTIVE_DONOR candidate | MIT core + separately licensed enterprise directory | Omnichannel/shared-inbox/conversation/widget patterns from qualified core paths. |
| `LiveHelperChat/livehelperchat` | DIRECT_DONOR/REFERENCE candidate | Apache-2.0 | Real-time support, messaging, voice/video/screenshare and channel adapter patterns. |
| `netbox-community/netbox` | DIRECT_DONOR/REFERENCE candidate | Apache-2.0 | Typed infrastructure source-of-truth, topology, plugin/API and reconciliation patterns for Qdrat Ops/Digital Twin. |
| `backstage/backstage` | DIRECT_DONOR/REFERENCE candidate | Apache-2.0 | Catalog, plugin architecture, developer portal and self-service template patterns. |
| `apache/camel` | DEPENDENCY/REFERENCE candidate | Apache-2.0 | Integration-pattern and connector breadth; investigate selected components/sidecar use, not wholesale framework adoption. |
| `debezium/debezium` | DEPENDENCY candidate | Apache-2.0 | Optional CDC engine for certified `SYNCED` Data Fabric connectors. |
| `flowable/flowable-engine` | REFERENCE/DEPENDENCY candidate | Apache-2.0 | BPMN/human-task/process semantics; Qdrat Flow remains canonical. |
| `activepieces/activepieces` | SELECTIVE_DONOR/REFERENCE candidate | MIT core + separately licensed EE paths | Connector/piece SDK, workflow builder and MCP/agent integration patterns from qualified core paths. |
| `open-policy-agent/opa` | DEPENDENCY/REFERENCE candidate | Apache-2.0 | General policy-as-code evaluation; optional engine behind Qdrat policy vocabulary. |
| `open-telemetry/opentelemetry-collector` | DEPENDENCY candidate | Apache-2.0 | Optional local telemetry collection/export profile under customer-controlled egress policy. |
| `prometheus/prometheus` | DEPENDENCY/REFERENCE candidate | Apache-2.0 | Optional local metrics/alerting integration profile. |
| `docling-project/docling` | DEPENDENCY candidate | MIT | Local document parsing/extraction. |

## Reference-only examples under current policy

Frappe HRMS, OrangeHRM, Odoo, ZITADEL, Huly, EspoCRM, Listmonk, Documenso, Plane, Paperless-ngx, Mautic, HumHub, Outline, BigCapital, Pretix, Mattermost, Snipe-IT, AppFlowy, Element and other reciprocal/restricted/mixed-license projects in `SOURCE_LANDSCAPE.md` remain architecture/domain/UX references or explicitly isolated-service candidates until a narrower review changes their status.

## Supply-chain and adoption gate

Before adopting a dependency or importing donor code, record:

- exact repository URL and commit/tag;
- exact source paths and destination paths;
- license and notice/attribution obligations;
- dependency tree and transitive-license impact;
- security posture and maintenance status;
- network/data-egress behavior;
- runtime resource cost;
- air-gap behavior;
- migration/removal strategy;
- why a Qdrat-owned implementation or smaller library is not preferable.

Generate SBOMs and provenance manifests for releases. Fail release gates on unknown/forbidden source provenance rather than allowing undocumented code intake.
