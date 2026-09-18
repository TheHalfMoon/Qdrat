# Qdrat Source Landscape

Initially verified against the listed public GitHub repositories on 2026-09-11; source expansion was re-verified for the newly added automation/enrichment sources on 2026-09-18. This document is an engineering intake register, not legal advice. Repository-level licenses can hide directory-level exceptions; file-level provenance remains mandatory before copying code.

## Expansion note — 2026-09-11

The founder subsequently added `https://github.com/block/buzz` under standing source authorization. Additional public-source research for Work/Jira, Service/Zendesk, ITSM/CMDB, workflow, Data Fabric, authorization, observability, knowledge and collaboration is maintained in `SOURCE_EXPANSION.md`. `COMPETITIVE_SUPERSET.md` defines the capability target those sources support.

`block/buzz` is Apache-2.0 at the currently researched `main` state and is especially relevant for human/agent principal symmetry, event/audit patterns, agent-first CLI surfaces, collaboration/workflow integration and project memory. Qdrat should adapt these patterns behind Qdrat contracts rather than automatically adopting Nostr as its canonical protocol.

The founder later added `chaitanyagiri/munder-difflin`, `jaredrhod/fullstack-agent`, `opensandbox-group/OpenSandbox`, `OpenWhispr/openwhispr` and `Starmel/OpenSuperWhisper`, and re-confirmed `langflow-ai/openrag`, all under standing source authorization. These additions materially strengthen Qdrat's multi-agent orchestration, secure execution sandbox and local/private voice/transcription design space; see `SOURCE_EXPANSION.md` and `DONOR_REGISTRY.md` for intake posture.

## Expansion note — 2026-09-18

The founder added Bricks, Clay, n8n, Activepieces, Refly, Flow-Like, LiveContext, OpenClay and the Eigent Clay-alternative reference under standing authorization. OpenClay's supplied site resolves to `raghav3600/Altclay`; the Eigent reference resolves to the official `eigent-ai/eigent` repository. `clay.com` is a commercial/source reference with founder-stated source permission, but the supplied public URL does not identify an authorized source-code repository, so exact source-package provenance remains required before code intake.

These additions establish `AUTOMATION_FABRIC.md` as a new canonical architecture document. They strengthen typed workflow execution, connector ecosystems, agent skills, human-in-loop execution, data enrichment, provider waterfalls, signals, browser/web research, mini-app surfaces and local multi-agent automation. Qdrat must synthesize these capabilities behind shared contracts rather than embed separate n8n/Clay-style products.

## Intake rules

- `DIRECT_DONOR`: permissive source may be copied selectively after file-level provenance/security review.
- `SELECTIVE_DONOR`: only identified permissive directories/packages are eligible; other areas have different terms.
- `DEPENDENCY`: prefer running or linking the project behind a stable interface rather than importing its source.
- `REFERENCE`: study product, domain, architecture, workflows, and UX without importing source under the current Qdrat licensing policy.
- `REJECT`: do not adopt as a foundation because maintenance, licensing, fit, or deployment cost is poor.
- Private permission does not erase third-party notices, dependency licenses, contributor rights, or trademark obligations. Preserve provenance for every imported file.

## Highest-value sources

| Source | Observed license posture | Qdrat role | Capability to extract |
|---|---|---|---|
| `horilla/horilla-hr` | LGPL-2.1 inherited base | BASE | HR/payroll/attendance/recruiting functional bootstrap |
| `Graphify-Labs/graphify` | Apache-2.0 | DIRECT_DONOR | Deterministic local graph extraction, explained edges, graph query UX |
| `vitali87/code-graph-rag` | MIT | DIRECT_DONOR | AST graph, graph-RAG, structured retrieval/editing patterns |
| `baserow/baserow` | MIT OSE + premium/enterprise exceptions | SELECTIVE_DONOR | Custom objects, tables, app/automation builder, API-first extensibility |
| `apache/superset` | Apache-2.0 | DEPENDENCY/DIRECT_DONOR | Advanced BI, dashboards, SQL analytics, embedded analytics |
| `cortezaproject/corteza` | Apache-2.0 | DIRECT_DONOR | Low-code object/process patterns, privacy and RBAC concepts |
| `gristlabs/grist-core` | Apache-2.0 | DIRECT_DONOR | Relational spreadsheet UX, formulas, forms, records and views |
| `gorules/zen` | MIT | DIRECT_DONOR | Deterministic rules engine, versioned decision execution |
| `gorules/jdm-editor` | MIT | DIRECT_DONOR | Visual decision graph/table editor |
| `Mintplex-Labs/anything-llm` | MIT | DIRECT_DONOR | Local agent UX, agent flows, tool selection, multi-user AI patterns |
| `langflow-ai/openrag` | Apache-2.0 | DEPENDENCY/REFERENCE | Agentic RAG pipelines, ingestion, workflow composition |
| `onyx-dot-app/onyx` | MIT core + enterprise directories | SELECTIVE_DONOR | Enterprise search, connectors, agentic RAG, actions/MCP |
| `getnao/nao` | Apache-2.0 majority + enterprise-marked files | SELECTIVE_DONOR | Analytics-agent context, evaluation, provenance and feedback loops |
| `PostHog/posthog` | MIT core + enterprise directory | SELECTIVE_DONOR | Event model, analytics, experimentation, session/event thinking |
| `Flagsmith/flagsmith` | BSD-3-Clause | DIRECT_DONOR/DEPENDENCY | Feature flags, staged rollout and environment configuration |
| `Infisical/infisical` | MIT core + enterprise directories | SELECTIVE_DONOR/DEPENDENCY | Secrets lifecycle, integration credentials, PKI/PAM concepts |
| `strapi/strapi` | MIT community + enterprise directories | SELECTIVE_DONOR | Plugin architecture, generated APIs, extensible admin patterns |
| `calcom/cal.diy` | MIT | DIRECT_DONOR | Scheduling, availability, booking and calendar orchestration |
| `ErugoOSS/Erugo` | MIT | DIRECT_DONOR | Secure local file transfer and sharing |
| `papercups-io/papercups` | MIT | DIRECT_DONOR | Embedded chat/support conversation patterns |
| `yuzutech/kroki` | MIT | DEPENDENCY | Diagram rendering from text for org/process/system diagrams |
| `louislam/uptime-kuma` | MIT | DIRECT_DONOR/DEPENDENCY | Simple self-hosted monitoring UX and health checks |
| `umami-software/umami` | MIT | DIRECT_DONOR | Privacy-first analytics UX and event aggregation |
| `gotenberg/gotenberg` | MIT | DEPENDENCY | Reliable document-to-PDF conversion API |
| `Stirling-Tools/Stirling-PDF` | MIT majority + proprietary/other subtrees | SELECTIVE_DONOR/DEPENDENCY | PDF edit/OCR/redact/convert/workflow capabilities |
| `toeverything/AFFiNE` | MIT majority + backend/native exceptions | SELECTIVE_DONOR/REFERENCE | Local-first collaboration, blocks, canvas and realtime UX |
| `flarum/framework` | MIT | DIRECT_DONOR/REFERENCE | Extension architecture, discussions and community patterns |
| `localstack/localstack` | Apache-2.0 repository; currently archived | REFERENCE | Offline emulation/test philosophy; do not make it a core runtime dependency |

## Strong references or isolated-service candidates

| Source | Observed license posture | Qdrat role | Capability to study |
|---|---|---|---|
| `odoo/odoo` | LGPL-3.0 with third-party notices | REFERENCE | ERP module model, views, workflows, CRM, finance, inventory, HR breadth |
| `hcengineering/platform` | EPL-2.0 | REFERENCE | Unified work platform, transaction/event architecture, realtime collaboration |
| `zitadel/zitadel` | AGPL-3.0 | REFERENCE/ISOLATED | Multi-tenant identity, OIDC/OAuth/MFA, audit/event model |
| `espocrm/espocrm` | AGPL-3.0 | REFERENCE | CRM object model, activities, customer portal |
| `knadh/listmonk` | AGPL-3.0 | REFERENCE/ISOLATED | High-volume campaigns, mailing lists and segmentation |
| `documenso/documenso` | AGPL-3.0 | REFERENCE/ISOLATED | E-sign flows, templates, signing lifecycle |
| `postgis/postgis` | GPL-2.0 | DEPENDENCY | Geospatial/geofencing/location queries inside PostgreSQL |
| `HumanSignal/label-studio` | Apache-2.0 | DEPENDENCY/REFERENCE | Human labeling and AI evaluation workflows |
| `lukevella/rallly` | AGPL-3.0 | REFERENCE | Poll-based scheduling and group availability |
| `makeplane/plane` | AGPL-3.0 | REFERENCE | Projects, cycles, issue views, triage and product UX |
| `formbricks/formbricks` | AGPL core; selected SDK packages MIT | SELECTIVE_DONOR/REFERENCE | Surveys, feedback, targeting and experience analytics |
| `paperless-ngx/paperless-ngx` | GPL-3.0 | REFERENCE/ISOLATED | OCR, document archive, indexing, tagging and retention |
| `Attendize/Attendize` | Attribution Assurance License | REFERENCE | Events, registration, ticket lifecycle |
| `mautic/mautic` | GPL-3.0-or-later | REFERENCE | Marketing automation, segments, campaigns and journeys |
| `chaskiq/chaskiq` | AGPL + Commons Clause | REJECT_AS_DONOR | Support/marketing UX only; source terms are unsuitable for Qdrat core |
| `humhub/humhub` | AGPL-3.0-or-later or proprietary | REFERENCE | Enterprise social/community spaces |
| `taigaio/taiga-back` | MPL-2.0; frontend AGPL | REFERENCE | Agile project management and event patterns |
| `outline/outline` | BSL-1.1 with use restriction/change date | REFERENCE | Knowledge base UX, collections and permissions |
| `bigcapitalhq/bigcapital` | AGPL-3.0 | REFERENCE | Double-entry accounting and financial reporting |
| `pretix/pretix` | AGPL-3.0 with additional terms | REFERENCE | Events, capacity, orders, check-in and registration |
| `miroslavpejic85/mirotalk` | AGPL-3.0 | REFERENCE/ISOLATED | Private WebRTC meetings, whiteboard and recording |
| `siglens/siglens` | Apache-2.0; archived | REFERENCE | Log search/observability architecture; avoid new dependency on archived repo |
| `mattermost/mattermost` | AGPL source + Apache areas + commercial option | REFERENCE/ISOLATED | Enterprise chat, plugins, webhooks, collaboration |
| `frappe/hrms` | GPL-3.0 | REFERENCE | HR/payroll domain breadth and workflows |
| `grokability/snipe-it` | AGPL-3.0 | REFERENCE | IT asset/license assignment lifecycle |
| `teableio/teable` | AGPL core; packages MIT | SELECTIVE_DONOR/REFERENCE | Database/spreadsheet/internal-tool UX |
| `bluewave-labs/Checkmate` | AGPL-3.0 | REFERENCE | Server/incident monitoring UX |
| `AppFlowy-IO/AppFlowy` | AGPL-3.0 | REFERENCE | Local-first docs/projects/wiki collaboration |
| `akaunting/akaunting` | BSL with user/company/service restrictions | REFERENCE | Accounting UX and workflows only |
| `element-hq/element-web` / `element-hq/synapse` | AGPL-3.0 | REFERENCE/ISOLATED | Matrix messaging, federation, realtime communication |
| `uvdesk/community-skeleton` | OSL-3.0 | REFERENCE | Helpdesk, ticket workflows, extension framework |

## Organization URLs resolved

The supplied organization-only links resolve for this research as follows: `calcom` → `calcom/cal.diy`; `flarum` → `flarum/framework`; `mautic` → `mautic/mautic`; `hasura` → `hasura/graphql-engine`; `taigaio` → `taigaio/taiga-back` plus frontend references; `gorules` → `gorules/zen` and `gorules/jdm-editor`; `element-hq` → `element-hq/element-web` and `element-hq/synapse`; `uvdesk` → `uvdesk/community-skeleton`. The supplied `Geta` organization is primarily Optimizely/EPiServer utilities and does not currently map to a meaningful Qdrat company-OS donor, so it is rejected unless a specific repository is named.

## Strategic conclusion

Do not assemble Qdrat by merging entire donor repositories. Extract capabilities behind Qdrat-owned contracts. Prefer permissive components for in-process code, keep reciprocal or restricted projects behind service boundaries when used at all, and reproduce useful product ideas independently when licensing or architecture makes direct reuse expensive.
