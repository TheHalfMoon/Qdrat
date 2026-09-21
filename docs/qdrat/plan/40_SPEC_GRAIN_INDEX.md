# SpecGrain index

96 SpecNode records use the actual upstream schema, stable SG IDs and revision-bound readiness declarations. `specgrain/nodes.json` is portable interchange, not a claim that it is the upstream durable store. G0-01 is REFINING; 95 successors are SHAPED. Implementation begins only after real readiness and a current work packet. No node is VERIFIED, MERGED or RELEASED.

Every task has a full record in [tasks/tasks.json](tasks/tasks.json); [the graph](EXECUTION_GRAPH.yaml) owns ordering. Chapters 41 and 43 define how to refine against repository truth.

| Task | SpecNode | State | Outcome |
|---|---|---|---|
| G0-01 | SG-000001 | REFINING | Freeze Linux amd64 Python 3.12 dependency artifacts |
| G0-02 | SG-000002 | SHAPED | Prove clean image and PostgreSQL bootstrap |
| G0-03 | SG-000003 | SHAPED | Qualify baseline tests and Qdrat CI triggers |
| G0-04 | SG-000004 | SHAPED | Capture baseline SBOM and source manifest |
| G0-05 | SG-000005 | SHAPED | Inventory legacy domains and execution surfaces |
| G0-06 | SG-000006 | SHAPED | Seal reproducible baseline evidence |
| G1-01 | SG-000007 | SHAPED | Create module boundaries and stable ObjectRef registry |
| G1-02 | SG-000008 | SHAPED | Map local users to Principal and Membership |
| G1-03 | SG-000009 | SHAPED | Implement policy decisions and field query scopes |
| G1-04 | SG-000010 | SHAPED | Add effective-dated Directory records |
| G1-05 | SG-000011 | SHAPED | Add transactional events and evidence records |
| G1-06 | SG-000012 | SHAPED | Bind files to owning objects |
| G1-07 | SG-000013 | SHAPED | Introduce protected secret references and local recovery keys |
| G1-08 | SG-000014 | SHAPED | Provide a local backup and restore foundation |
| G1-09 | SG-000015 | SHAPED | Create bilingual shell and protected directory page |
| G1-10 | SG-000016 | SHAPED | Add local MFA bootstrap and OIDC identity binding |
| G1-11 | SG-000017 | SHAPED | Add SCIM deprovision and expiring delegation |
| G2-01 | SG-000018 | SHAPED | Register connector manifests and data sources |
| G2-02 | SG-000019 | SHAPED | Preview spreadsheet and file imports |
| G2-03 | SG-000020 | SHAPED | Implement PostgreSQL read-only discovery and paging |
| G2-04 | SG-000021 | SHAPED | Implement canonical mapping and field authority |
| G2-05 | SG-000022 | SHAPED | Add HTTPS connector and webhook conformance kit |
| G2-06 | SG-000023 | SHAPED | Add write-through reconciliation journal |
| G2-07 | SG-000024 | SHAPED | Qualify snapshot plus PostgreSQL CDC |
| G2-08 | SG-000025 | SHAPED | Implement customer network bridge |
| G3-01 | SG-000026 | SHAPED | Implement ActionDefinition and operation API |
| G3-02 | SG-000027 | SHAPED | Implement leased step journal and timers |
| G3-03 | SG-000028 | SHAPED | Implement bound human approvals |
| G3-04 | SG-000029 | SHAPED | Implement budget reservation and cancellation |
| G3-05 | SG-000030 | SHAPED | Compile and validate typed Flow graphs |
| G3-06 | SG-000031 | SHAPED | Implement pure rules and decision tables |
| G3-07 | SG-000032 | SHAPED | Implement safe replay resume and compensation |
| G3-08 | SG-000033 | SHAPED | Migrate inherited scheduled jobs to durable ownership |
| G4-01 | SG-000034 | SHAPED | Add quarantined document ingestion and derivatives |
| G4-02 | SG-000035 | SHAPED | Add permission-aware full-text search and citations |
| G4-03 | SG-000036 | SHAPED | Build Company Twin adjacency projection |
| G4-04 | SG-000037 | SHAPED | Migrate core employment and contract journey |
| G4-05 | SG-000038 | SHAPED | Implement leave accrual and reservation ledger |
| G4-06 | SG-000039 | SHAPED | Implement time correction and shift assignment |
| G4-07 | SG-000040 | SHAPED | Implement onboarding and offboarding checklist |
| G4-08 | SG-000041 | SHAPED | Implement recruiting application and offer pipeline |
| G4-09 | SG-000042 | SHAPED | Implement performance goals and confidential feedback |
| G4-10 | SG-000043 | SHAPED | Implement compensation and benefit enrollment revisions |
| G4-11 | SG-000044 | SHAPED | Implement learning skills and headcount scenarios |
| G4-12 | SG-000045 | SHAPED | Validate People pilot migration and bilingual journeys |
| G5-01 | SG-000046 | SHAPED | Freeze Saudi rule and authority matrix |
| G5-02 | SG-000047 | SHAPED | Implement deterministic payroll shadow calculator |
| G5-03 | SG-000048 | SHAPED | Implement payroll approval release and WPS artifact |
| G5-04 | SG-000049 | SHAPED | Implement EOSB and employment amendment evidence |
| G5-05 | SG-000050 | SHAPED | Implement Saudi privacy and assisted authority integrations |
| G5-06 | SG-000051 | SHAPED | Certify parallel payroll and country pack release |
| G6-01 | SG-000052 | SHAPED | Implement WorkItem lifecycle and list-board views |
| G6-02 | SG-000053 | SHAPED | Implement work dependencies and planning calendars |
| G6-03 | SG-000054 | SHAPED | Implement goals portfolio and meeting decisions |
| G6-04 | SG-000055 | SHAPED | Implement Case and scoped portal |
| G6-05 | SG-000056 | SHAPED | Implement email and conversation channel adapter |
| G6-06 | SG-000057 | SHAPED | Implement SLA clocks and routing escalation |
| G6-07 | SG-000058 | SHAPED | Implement catalog incident problem and change records |
| G6-08 | SG-000059 | SHAPED | Qualify Jira Zendesk and ServiceNow migration mappings |
| G7-01 | SG-000060 | SHAPED | Implement account contact roles and identity merge preview |
| G7-02 | SG-000061 | SHAPED | Implement opportunity pipeline and activity links |
| G7-03 | SG-000062 | SHAPED | Implement generic enrichment waterfalls and signals |
| G7-04 | SG-000063 | SHAPED | Implement renewals customer onboarding and health |
| G7-05 | SG-000064 | SHAPED | Implement campaign consent and connector sends |
| G7-06 | SG-000065 | SHAPED | Implement expense receipts and budget reservations |
| G7-07 | SG-000066 | SHAPED | Implement purchase request order receipt matching |
| G7-08 | SG-000067 | SHAPED | Implement ledger proposal export and reconciliation |
| G7-09 | SG-000068 | SHAPED | Implement asset assignment and return lifecycle |
| G7-10 | SG-000069 | SHAPED | Implement CI inventory reconciliation and facility reservations |
| G8-01 | SG-000070 | SHAPED | Implement custom object schema publication |
| G8-02 | SG-000071 | SHAPED | Implement form grid and board authoring |
| G8-03 | SG-000072 | SHAPED | Implement pure formulas lifecycle and remaining views |
| G8-04 | SG-000073 | SHAPED | Implement signed extension export install upgrade |
| G8-05 | SG-000074 | SHAPED | Implement versioned metric definitions and dashboards |
| G8-06 | SG-000075 | SHAPED | Qualify BI semantic export and analytical snapshots |
| G8-07 | SG-000076 | SHAPED | Publish REST SDK webhook and optional MCP adapters |
| G9-01 | SG-000077 | SHAPED | Implement model registry and no-egress routing |
| G9-02 | SG-000078 | SHAPED | Implement context bundles scoped memory and hybrid retrieval |
| G9-03 | SG-000079 | SHAPED | Implement agent principals skills and proposed actions |
| G9-04 | SG-000080 | SHAPED | Implement isolated ExecutionRequest adapter |
| G9-05 | SG-000081 | SHAPED | Implement execution artifact custody and kill switch |
| G9-06 | SG-000082 | SHAPED | Qualify Arabic English grounded agent evaluations |
| G9-07 | SG-000083 | SHAPED | Implement foreground consented voice and local ASR |
| G9-08 | SG-000084 | SHAPED | Implement transcript drafts and command preview |
| G9-09 | SG-000085 | SHAPED | Qualify optional desktop and meeting adapters |
| G10-01 | SG-000086 | SHAPED | Implement qdratctl preflight install and bootstrap |
| G10-02 | SG-000087 | SHAPED | Implement offline application and model bundles |
| G10-03 | SG-000088 | SHAPED | Implement local observability diagnostics and runbooks |
| G10-04 | SG-000089 | SHAPED | Implement upgrade compatibility and rollback planner |
| G10-05 | SG-000090 | SHAPED | Qualify privacy retention deletion and recovery |
| G10-06 | SG-000091 | SHAPED | Seal People production release qualification |
| G11-01 | SG-000092 | SHAPED | Qualify multiworker fencing and database failover |
| G11-02 | SG-000093 | SHAPED | Qualify Kubernetes and supported platform matrix |
| G11-03 | SG-000094 | SHAPED | Measure workload budgets and optional engine triggers |
| G12-01 | SG-000095 | SHAPED | Qualify native ledger replacement specification |
| G12-02 | SG-000096 | SHAPED | Qualify industry and additional country packs |
