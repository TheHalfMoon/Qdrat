# Competitor research and product lessons

Research date: 20–21 September 2026. These are primary documentation/API observations, not hands-on usability trials, purchase recommendations or independently verified vendor performance claims. “Strong reference” means the best-supported pattern for the specified job in this research set; it is not an absolute market ranking. Enterprise licensing, tenant configuration and API access must be qualified by each connector. The broad web discovery index includes navigation/candidate links and must not be represented as 636 deeply reviewed sources.

The tables record what was learned from each required competitor. Chapter 05 evaluates the jobs across ownership, privacy, UX, administration, API, extensibility and AI, and assigns Qdrat's response. Current endpoint documentation wins over remembered feature names. Versioned APIs and missing/forbidden-field semantics matter more than connector-logo counts.

## Work / project / product

| Product and primary evidence | Observed pattern | Consequence for Qdrat |
|---|---|---|
| [Jira import documentation](https://support.atlassian.com/jira-software-cloud/docs/import-data-into-jira/) | Imports require type, field and identity mappings | A migration is a reconciled job, not a CSV upload success message |
| [Linear API/webhooks](https://linear.app/docs/api-and-webhooks) | GraphQL and event integration support the work model | Fast triage/cycles are useful; one WorkItem identity across views and API |
| [Asana custom fields](https://help.asana.com/s/article/custom-fields?language=en_US) | Reusable and local field contexts | Global schema administration must not burden everyday project users |
| [ClickUp custom fields](https://developer.clickup.com/docs/customfields) | Typed custom-field integration | Preserve type/option IDs and missing values during migration |
| [Monday workflow blocks](https://developer.monday.com/apps/docs/monday-workflows) | Typed authoring blocks with inputs and outputs | Studio authors reusable typed actions; Automation executes them |
| [Notion developers](https://developers.notion.com/) | Pages/data sources, connections and permissions | Useful flexible surfaces, but a page is not an authoritative payroll record |
| [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) | Project views refer to issues and PRs, with custom fields/charts | Views should share records rather than copy tasks between products |
| [GitLab work items/issues](https://docs.gitlab.com/user/project/issues/) | Unified work-item direction extends issue tracking | Type-specific lifecycle over common work identity |
| [Azure Boards backlogs](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/backlogs-overview?view=azure-devops) | Team product, portfolio and sprint hierarchies | Distinguish parent rollups from dependency edges and capacity |
| [Smartsheet webhooks](https://developers.smartsheet.com/api/smartsheet/openapi/webhooks/createwebhook) | Sheet/row event integration | Spreadsheet UX needs stable row identity, types and event recovery |
| [Plane documentation](https://docs.plane.so/) and pinned source in 03 | Cycles, modules and issue views | Adopt focused work navigation, not another identity/runtime |
| [OpenProject work packages](https://www.openproject.org/docs/user-guide/work-packages/) | Typed work packages with stable IDs and alternative views | Gantt/list/board must operate on the same dependency-aware records |
| [Taiga API](https://docs.taiga.io/api.html) | Stories, sprints, backlog and kanban operations | Map agile concepts without forcing every business team into scrum |

## Support / customer service

| Product and primary evidence | Observed pattern | Consequence for Qdrat |
|---|---|---|
| [Zendesk Ticket API](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/) | Tickets have workflow fields, actors and conversation context | Preserve thread, actor, visibility and audit semantics in import; do not use retired chat APIs |
| [Intercom tickets](https://www.intercom.com/help/en/collections/3659257-tickets) | Customer, back-office and tracker ticket distinctions | Public conversation and internal fulfillment may link while retaining separate visibility |
| [Freshdesk API](https://developers.freshdesk.com/api/) | Versioned API, rate limits and retry guidance | Connector conformance includes 429/Retry-After, checkpoints and partial failures |
| [Gorgias ticket object](https://developers.gorgias.com/reference/the-ticket-object) | Ticket/conversation/channel information | Channels normalize into Conversation/Message without losing source IDs |
| [Help Scout Inbox API](https://developer.helpscout.com/mailbox-api/) | OAuth-based resource API | Mailbox/account scope must survive mapping and token refresh |
| [Zoho Desk API](https://desk.zoho.com/DeskAPIDocument) | OAuth-backed service records | Least-privilege scopes and tenant-qualified endpoint selection |
| [Salesforce omnichannel service](https://trailhead.salesforce.com/content/learn/modules/service-cloud-platform-quick-look/deliver-omnichannel-service) | Routing and flow-supported case work | Routing is a policy decision; fulfilling a case uses the shared journal |
| [Dynamics Customer Service](https://learn.microsoft.com/en-us/dynamics365/customer-service/implement/overview) | Customer-service implementation surface | Use as case/service breadth reference; no claim of hands-on configuration parity |
| [Chatwoot APIs](https://developers.chatwoot.com/introduction) | Application, platform and client API separation | Portal credentials cannot become administrative integration credentials |
| [Zammad documentation](https://docs.zammad.org/en/latest/) | Self-hosted ticket/service administration | Small-company service setup should have a short path to a working inbox |

## ITSM / ESM

| Product and primary evidence | Observed pattern | Consequence for Qdrat |
|---|---|---|
| [ServiceNow service catalog](https://www.servicenow.com/docs/r/servicenow-platform/service-catalog/request-cat-use-case.html) | Catalog and service model connect requests to fulfillment | Shared Service/Request/Approval/WorkItem with catalog schemas; avoid requiring full enterprise modeling to submit a request |
| [Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/what-is-jira-service-management/) | Service management atop work processes | Link case to work without making customer access equivalent to project membership |
| [Freshservice API](https://api.freshservice.com/) | Service records, journeys and approval integrations | Preserve chain/quorum semantics; API capability varies by account and edition |
| [BMC Helix ITSM 26.1](https://docs.bmc.com/xwiki/bin/view/Service-Management/IT-Service-Management/BMC-Helix-ITSM/itsm261/) | ITSM integration and process breadth | Incident/problem/change need distinct state machines, not arbitrary ticket labels |
| [ManageEngine service desk API](https://www.manageengine.com/products/service-desk/sdpod-v3-api/) | Requests, problems, changes and assets | Relate fulfillment to CI/Asset records while retaining authoritative source ownership |
| [HaloITSM integration guidance](https://usehalo.com/haloitsm/guides/1198/) | API/MCP integration surface | An exposed tool is still subject to current Qdrat action authorization |
| [GLPI navigation/modules](https://help.glpi-project.org/documentation/readme-1-1/navigation-modules) | Assets, assistance, management and administration | Progressive navigation can hide administration from requester UX |

## HCM

| Product and primary evidence | Observed pattern | Consequence for Qdrat |
|---|---|---|
| [Workday APIs](https://developer.workday.com/documentation/GUID-7b3b1dd7-e3b0-4a34-846b-6e37673226e1-enHYPHENus/WorkdayAPIs) | Multiple integration/API surfaces | Bulk synchronization and self-service transactions have different contracts |
| [SuccessFactors Compound Employee](https://help.sap.com/docs/successfactors-employee-central/integrating-sap-successfactors-employee-central-with-workforce-software/configurations-for-employee-central-compound-employee-api?locale=en-US&state=PRODUCTION&version=latest) | Employee Central integration requires explicit configuration | Effective dates and source authority must be mapped, not flattened |
| [Oracle HCM REST](https://docs.oracle.com/en/cloud/saas/human-resources/farws/index.html) | Extensive versioned human-resource resources | Broad HCM coverage requires typed subdomains and permission-aware migration |
| [Rippling permissions](https://www.rippling.com/platform/permissions) | Attribute-based groups connect scope and actions | Dynamic group membership is useful, but changes must invalidate cached authorization |
| [Deel global payroll](https://developer.deel.com/api/global-payroll/introduction) | Worker inputs and payroll-result integrations | Connect provider payroll through frozen snapshots and reconciliation |
| [BambooHR API](https://documentation.bamboohr.com/docs/getting-started) | Integration access follows user permissions | An omitted field may be forbidden, not blank; never delete the canonical value on omission |
| [Personio webhooks](https://developer.personio.de/reference/webhooks) | Event notification followed by authorized retrieval | Treat notification as a hint, not an authoritative complete record |
| [HiBob permissions](https://apidocs.hibob.com/reference/permissions) | Service-user/category permissions | Protect compensation and identity fields independently of profile visibility |
| [Factorial API](https://apidoc.factorialhr.com/docs/getting-started) | Developer integration surface | Candidate for connector qualification; docs review does not prove customer entitlement |
| [Zoho People API](https://www.zoho.com/people/api/overview.html) | Forms/employee API with scopes and limits | Flexible form mapping must preserve typed core employment semantics |

## CRM / sales

| Product and primary evidence | Observed pattern | Consequence for Qdrat |
|---|---|---|
| [Salesforce Composite API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_composite_post.htm) | Composite calls bind dependent operations with explicit failure semantics | A local transaction does not imply remote multi-system atomicity |
| [HubSpot object schemas](https://developers.hubspot.com/docs/api-reference/latest/crm/objects/schemas/guide) | Objects, properties and associations; edition/scope restrictions | Native parties/relationships plus namespaced custom objects; map account entitlements |
| [Dynamics Sales](https://learn.microsoft.com/en-us/dynamics365/sales/overview) | Dataverse/model-driven sales integration | Avoid duplicating contacts across customer, vendor and employee roles |
| [Zoho CRM API v8](https://www.zoho.com/crm/developer/docs/api/v8/) | Metadata, bulk, notification and query interfaces | Discover schema before sync and use bulk limits/checkpoints explicitly |
| [Pipedrive deals](https://developers.pipedrive.com/docs/api/v1/Deals) | Stages, values and custom fields across API versions | Pipeline configuration is versioned; stage changes must preserve history |
| [Attio deal records](https://docs.attio.com/rest-api/endpoint-reference/standard-objects/deals/list-deal-records) | Scoped record query and timestamped values | Value provenance and time belong in the shared object model |
| [Clay waterfalls](https://university.clay.com/lessons/enrich-companies-waterfalls-clay-101) | Ordered provider attempts stop on usable data | Generic budgeted waterfall with freshness, validation, privacy and unknown-cost settlement |

## ERP / finance

| Product and primary evidence | Observed pattern | Consequence for Qdrat |
|---|---|---|
| [SAP S/4HANA purchase order API](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/f5d3e1005efd4e86acf9a65abf428082/c89eec80ec2043d980cb7b8c89e0a00a.html) | Versioned procurement interfaces | Purchase intent/approval can be native while ERP owns posting and settlement |
| [Oracle Financials payables](https://docs.oracle.com/en/cloud/saas/financials/26b/farfa/Query_Payables_Invoices.html) | Query and invoice resources under financial permissions | Never infer AP authority from a generic integration administrator |
| [NetSuite SuiteTalk REST](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_1540391670.html) | Account-specific integration service | Endpoint/account identity belongs in the credential grant and idempotency domain |
| [Dynamics Finance ledger](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-ledger) | Legal entities, dimensions, currencies and period close | LegalEntity is distinct from tenant; closed-period corrections append adjustments |
| [Odoo 19 accounting](https://www.odoo.com/documentation/19.0/applications/finance/accounting.html) | Double-entry and multicompany breadth | Useful coverage benchmark; do not embed a second ERP runtime |
| [ERPNext immutable ledger](https://docs.frappe.io/erpnext/immutable-ledger-in-erpnext) | Reversal/correction rather than rewriting ledger history | Financial authority requires immutable posting and reconciliation evidence |
| [QuickBooks developer portal](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/change-data-capture) | Public portal is dynamically rendered; this fetch did not expose CDC details | API capability remains unqualified. Use authorized export/import initially; no invented webhook/CDC guarantee |
| [Xero invoices](https://developer.xero.com/documentation/api/accounting/invoices) | Invoice state constrains editing/voiding and delivery | Model posted/paid/cancelled states distinctly and reconcile external sends |

## Automation

| Product and primary evidence | Observed pattern | Consequence for Qdrat |
|---|---|---|
| [n8n source](https://github.com/n8n-io/n8n) pinned in 03 | Broad connector/workflow authoring | Adopt typed connector ergonomics; no second executor. A legacy queue-mode documentation URL returned 404 during refresh |
| [Zapier polling contract](https://docs.zapier.com/platform/build/error-array-expected) | Trigger polling expects structured items in a defined form/order | Explicit stable IDs, ordering and deduplication in trigger conformance |
| [Make error handling](https://help.make.com/overview-of-error-handling) | Failed/incomplete execution recovery | Expose resumable state and operator decisions; never relabel unknown effects as retryable |
| [Workato error handling](https://docs.workato.com/recipes/best-practices-error-handling) | Structured failures and recipe recovery | Classify errors at the connector boundary rather than string matching in every flow |
| [Activepieces human input](https://www.activepieces.com/pieces/forms) and source | Typed pieces and form-driven waits | Human approval/input is persisted journal state, not a blocked worker process |
| [Refly](https://github.com/refly-ai/refly), [Flow-Like](https://github.com/Rheosoph/flow-like), [LiveContext](https://github.com/livecontext-ai/livecontext-ce) pinned in 03 | Skills, typed canvas flows and chat/app authoring convergence | Authoring surfaces compile to one versioned Flow and shared actions |
| [Clay workflows](https://university.clay.com/docs/workflow-faqs), Bricks/Altclay in 03 | Record-level enrichment, previews and provider selection | Reuse DataSource, Action, Signal, Run and budgets across all suites |
| Eigent/AnythingLLM sources in 03 | Local/private agent tooling | Local model placement does not itself establish isolation or least privilege |

## Collaboration / knowledge

| Product and primary evidence | Observed pattern | Consequence for Qdrat |
|---|---|---|
| [Slack token types](https://docs.slack.dev/authentication/tokens/) | Bot, user and workflow tokens have distinct authority | Preserve original actor and credential class; no silent delegation expansion |
| [Teams content export](https://learn.microsoft.com/en-us/microsoftteams/export-teams-content) | Export has protected access/licensing and pagination | Export capability is not assumed from chat membership; preserve retention and permissions |
| [Google Workspace document authorization](https://developers.google.com/workspace/docs/api/auth) | File-scoped access options | Prefer explicitly selected file scopes over whole-drive access |
| [Confluence operations API](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-operation/) | Permitted operations depend on resource context | Source ACLs and current Qdrat policy both constrain indexed material |
| Notion developer source above | Flexible pages/data sources | Document blocks and operational objects can share links without sharing all permissions |
| [SharePoint site discovery](https://learn.microsoft.com/en-us/graph/api/site-list?view=graph-rest-1.0) | Site discovery is permission-dependent | A connector listing is not proof that every file is readable |
| [Outline collections](https://docs.getoutline.com/s/guide/doc/collections-l9o3LD22sV) | Collection-level knowledge organization | Familiar library UX with object/field policy and current revocation |
| AFFiNE/AppFlowy pinned in 03; [AppFlowy self-hosting integration](https://docs.appflowy.io/docs/documentation/appflowy/debugging-with-appflowy-cloud) | Local blocks/canvas and self-hosted document apps | Reuse editing patterns, retain one original/derivative/file identity |
| [Mattermost plugins](https://developers.mattermost.com/contribute/more-info/server/plugins/) | Server/plugin and client bundle architecture | Extension manifests and process boundaries; avoid untrusted in-process hooks |
| [Element migration guidance](https://docs.element.io/latest/element-cloud-documentation/element-matrix-services/migrate-from-ems-to-self-hosted/) | Provider migration/exit is an operational concern | Preserve conversation IDs/exportability and make encrypted-search tradeoffs explicit |
| [Zulip permissions](https://zulip.com/help/manage-permissions) | Topic/channel organization with granular administration | Shared conversations need discoverability without uncontrolled channel sprawl |

## AI / enterprise agents

| Product and primary evidence | Observed pattern | Consequence for Qdrat |
|---|---|---|
| [Microsoft Copilot sharing](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-manage-content-sharing) | Sharing an answer differs from source access | A generated answer is itself a classified artifact with authorized recipients |
| [Salesforce Agentforce trust](https://developer.salesforce.com/docs/ai/agentforce/guide/trust.html) | Grounding, masking and provider data commitments | Useful controls; provider contractual retention is different from no egress |
| [ServiceNow approval assistance](https://www.servicenow.com/docs/r/intelligent-experiences/plat-approval-assistance-ai-agent.html) | Current record data assists a human approval | Suggestions cannot grant approval or waive separation of duties |
| [Rovo agent actions](https://support.atlassian.com/rovo/docs/agent-actions/) | Tools/actions have permission and capability boundaries | Every tool invocation reaches the same Action API as human commands |
| [Zendesk AI escalation](https://support.zendesk.com/hc/en-us/articles/8357756604186-Configuring-escalation-strategies-and-flows-for-AI-agents) | Escalation differs by channel and flow | Human handoff must retain transcript, evidence and unresolved intent |
| [Intercom data connectors](https://www.intercom.com/help/en/articles/9916497-how-to-set-up-data-connectors) | Inputs and preview before live connection | Dry-run/previews must be explicit about whether providers are called |
| [Glean action access](https://docs.glean.com/administration/actions/managing-actions/managing-role-based-access-actions) | Action configuration and end-user execution are different powers | Separate author, installer, operator and invoker capabilities |
| [Moveworks Agent Studio roles](https://help.moveworks.com/agent-studio/access-control/roles-and-permissions) | Workspace/asset roles distinguish editing and runtime access | Studio publication does not mint execution credentials |
| Onyx, AnythingLLM, Eigent, OpenRAG in 03; founder Kernux/Kodac/Morize in 02 | Private retrieval, tools, memory and authority patterns | Shared policy-filtered context, explicit agent principals, bounded effects and inspectable citations |

## Cross-category conclusion

The valuable differentiator is the join between systems: an approved hire can create employment, provision scoped access, assign an asset, open onboarding work and retain one evidence trail. A support escalation can connect an account, service CI, incident, project and contract while preserving each object's authority. Neither requires copying every competitor screen. Qdrat first connects existing authorities, then replaces selected jobs only after migration and recovery are proved.

Unverified details are connector qualification work, not permission to guess. QuickBooks dynamic documentation, paid API entitlements, real-world usability and vendor performance remain explicitly unmeasured; the architecture has export/import and manual-assisted paths that do not depend on those claims.
