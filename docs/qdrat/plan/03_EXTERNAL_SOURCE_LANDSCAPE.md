# External source landscape and intake decisions

The 76 entries in the founder authorization register were reconciled with live upstream metadata and content. The grant is accepted; it is not repeatedly re-requested. Repository-level license metadata is recorded as observed, including mixed/NOASSERTION cases, and is not a substitute for notices and file-level provenance. Geta is an organization catalog; Clay is product documentation, not a located source package. Neither is counted as a cloned code repository.

Exact branches, commit IDs, README blobs, license paths and manifest paths are in [authorized sources](evidence/authorized-sources.json). The following decisions apply to each entry. No production donor component is copied by this planning change. Optional candidates remain REFERENCE_ONLY until a specific adapter earns its cost and passes conformance.

| Source | Decision | Useful job/pattern | Qdrat boundary / reason |
|---|---|---|---|
| [horilla/horilla-hr](https://github.com/horilla/horilla-hr/tree/d5cb062d5e2d33beb367f524760593592a16c58e) | ADAPT_PATTERN | People functional bootstrap | Inherited base remains; qualify existing source before expansion |
| [vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag/tree/94120a67df5124bd721654c00452dbe935a496a7) | ADAPT_PATTERN | Explained code/graph retrieval | Company semantics and permission model remain Qdrat-owned |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify/tree/20a20d30d8e7eef77675651f0199d87f913bd3e7) | ADAPT_PATTERN | Local extraction and provenance edges | No new graph authority or mandatory graph database |
| [odoo/odoo](https://github.com/odoo/odoo/tree/6bae1e2f5eed5aae790944492e3d89d50bab5954) | REFERENCE_ONLY | ERP module and accounting breadth | Connect ledger; avoid whole ERP/runtime replacement |
| [baserow/baserow](https://github.com/baserow/baserow/tree/81e094a1f4b3a62625c218d78fe319ba44098617) | ADAPT_PATTERN | Typed custom fields and app views | Mixed paths; reuse UX contract not independent identity/database |
| [zitadel/zitadel](https://github.com/zitadel/zitadel/tree/3ff4fbc7e4f22cd6eee49d3de951350c5ed855cd) | REFERENCE_ONLY | OIDC SAML SCIM MFA identity | Customer federation optional; no second mandatory identity service |
| [apache/superset](https://github.com/apache/superset/tree/4511c1381930ec53cd74c1e25c3ad4397768e2b4) | REFERENCE_ONLY | Advanced analytics embedding | Optional adapter qualification; permission-aware read views required |
| [espocrm/espocrm](https://github.com/espocrm/espocrm/tree/8499172c1b631e6fff57093445e11e2440788d6f) | ADAPT_PATTERN | CRM activities and portal | Native shared organization/person model |
| [getnao/nao](https://github.com/getnao/nao/tree/9952ec789ca3993778750baefff0caece3977a13) | ADAPT_PATTERN | Analytics context and evaluation | Metric definitions shared with BI and AI |
| [ErugoOSS/Erugo](https://github.com/ErugoOSS/Erugo/tree/922c00c2beafa5b6136ff551333d52387270be49) | ADAPT_PATTERN | Local sharing lifecycle | Shared FileObject owner/expiry policy |
| [hcengineering/platform](https://github.com/hcengineering/platform/tree/9aa7da386c8eb79a8ed2a7905ea0606ef567a0d0) | ADAPT_PATTERN | Unified work/collaboration | Hosted service discontinued per README; no hosted dependency |
| [papercups-io/papercups](https://github.com/papercups-io/papercups/tree/6a6f5adc7f0cef5813b2c2f1c0659922defaf976) | REFERENCE_ONLY | Conversation widget | Maintenance mode; no new runtime foundation |
| [knadh/listmonk](https://github.com/knadh/listmonk/tree/594b74056dd8a0d3a7621a32898ee38bfbe10e96) | ADAPT_PATTERN | Campaign segmentation and suppression | Generic governed sends; separate channel service only if qualified |
| [yuzutech/kroki](https://github.com/yuzutech/kroki/tree/f23aee4be7e3dea656240ba64e7c65e78978909a) | REFERENCE_ONLY | Diagram conversion interface | Optional local render adapter; no hosted endpoint default |
| [langflow-ai/openrag](https://github.com/langflow-ai/openrag/tree/dbb6f9e442fe90b2a60414bf2eb6d4c83d1dd30d) | ADAPT_PATTERN | RAG ingestion orchestration | Do not add another workflow/search authority |
| [documenso/documenso](https://github.com/documenso/documenso/tree/e658cc581878f52c03b3e6a8f7ffd613aead4e69) | ADAPT_PATTERN | Signing lifecycle | Legal signature qualification separate from UI |
| [postgis/postgis](https://github.com/postgis/postgis/tree/84890ccbe53549130de8a2b75a72ab3a54b570d1) | REFERENCE_ONLY | Spatial query primitives | Optional DB extension only when geospatial workload requires |
| [HumanSignal/label-studio](https://github.com/HumanSignal/label-studio/tree/f45d81328316d559db0b8cde340b13b5a6e8ce03) | ADAPT_PATTERN | Annotation and evaluation review | Use rights-cleared evaluation corpus; optional isolated review service |
| [onyx-dot-app/onyx](https://github.com/onyx-dot-app/onyx/tree/711a0479f1630dcce38f8f58212a63080702b753) | ADAPT_PATTERN | Enterprise search/connectors | Source ACL freshness and shared retrieval contract |
| [Peppermint-Lab/peppermint](https://github.com/Peppermint-Lab/peppermint/tree/ba6e2179f9409db76abeb9a3007a262160e24628) | REFERENCE_ONLY | Helpdesk simplicity | Archived; not a maintained runtime candidate |
| [lukevella/rallly](https://github.com/lukevella/rallly/tree/5185e3c134eb4fac4f897f27a220e1fbf29fe385) | ADAPT_PATTERN | Availability polls | Shared Calendar/Conversation rather than another scheduler |
| [calcom/cal.diy](https://github.com/calcom/cal.diy/tree/54343aa685ae8f33159d2f485ec4a57bad5c574a) | REFERENCE_ONLY | Booking UX | Upstream recommends personal non-production use |
| [makeplane/plane](https://github.com/makeplane/plane/tree/01064a756221921a1ce3e7941ae4d439f298029a) | ADAPT_PATTERN | Cycles triage work views | WorkItem shared model |
| [posthog/posthog](https://github.com/posthog/posthog/tree/5517c962c8bdeab523fc97c500389080e6334084) | ADAPT_PATTERN | Event analytics | No hidden product telemetry/session recording |
| [formbricks/formbricks](https://github.com/formbricks/formbricks/tree/79977e0c4bfa70db250d65d09c0b0ff545cf22cb) | ADAPT_PATTERN | Survey design | Minimum cohort and response confidentiality |
| [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx/tree/87d157096e14198fa600793951524cd9340c3172) | ADAPT_PATTERN | Document archive OCR lifecycle | Single original/derivative/permission plane |
| [attendize/attendize](https://github.com/attendize/attendize/tree/9289acbab1583898fd85aeee66c7b613d8971deb) | REFERENCE_ONLY | Event registration | Later industry extension; no ticket-sales system now |
| [flarum/framework](https://github.com/flarum/framework/tree/b91ac1c2045bfcdd7c0392101fb377f616d46491) | ADAPT_PATTERN | Extension/discussion patterns | No separate forum identity by default |
| [mautic/mautic](https://github.com/mautic/mautic/tree/7912edbd7ede249ddbb2721abd6def94bee52f3e) | ADAPT_PATTERN | Marketing journeys | Consent/suppression and shared Automation |
| [infisical/infisical](https://github.com/infisical/infisical/tree/bd2179cf211874925e2313664e22dae2501fe30a) | ADAPT_PATTERN | Secret lifecycle | Optional service; encrypted local secret references first |
| [strapi/strapi](https://github.com/strapi/strapi/tree/d83af0410bf31b034b01757729f2231862ee5e87) | ADAPT_PATTERN | Schema/plugin administration | Do not replace Django or expose arbitrary core models |
| [flagsmith/flagsmith](https://github.com/flagsmith/flagsmith/tree/190c645d83d11f627a241cd4e5540d0a26ad73ba) | ADAPT_PATTERN | Flag rollout | Small local versioned feature config first |
| [chaskiq/chaskiq](https://github.com/chaskiq/chaskiq/tree/46dfdd11c63c6849ecde16a0dcc54d388e2613a3) | REFERENCE_ONLY | Support messaging UX | Restricted/mixed source and extra runtime; no core code copy |
| [hasura/graphql-engine](https://github.com/hasura/graphql-engine/tree/9d4df1586326d31937935837fa155b5a5d16eb0a) | REFERENCE_ONLY | Database API policies | No auto-exposure of raw company database |
| [humhub/humhub](https://github.com/humhub/humhub/tree/cf51cf811d36d5c1ab59e2fd1e098d67786121ab) | ADAPT_PATTERN | Company community | Shared conversation/profile/permission primitives |
| [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma/tree/e62702d868a0b072c6e1870e5278762319637f04) | ADAPT_PATTERN | Health UX | Operational health is not audit or security proof |
| [taigaio/taiga-back](https://github.com/taigaio/taiga-back/tree/eb0803da0150523c990e46a4e47e7447f402b4aa) | ADAPT_PATTERN | Agile workflows | Back/frontend licenses differ; no whole app import |
| [outline/outline](https://github.com/outline/outline/tree/4ed1665728921a94ce40e924e5da407a52c65e0b) | ADAPT_PATTERN | Knowledge collections | Collection UX with object-level current authorization |
| [bigcapitalhq/bigcapital](https://github.com/bigcapitalhq/bigcapital/tree/1efc788a6cd427672650db0a8d8a34fd7cc2004a) | REFERENCE_ONLY | Double-entry domains | Native ledger remains separately certified |
| [cortezaproject/corteza](https://github.com/cortezaproject/corteza/tree/3835dfc4ac8bd89381753f09042ad147a4502576) | ADAPT_PATTERN | Low-code schema/process | One custom-object and Flow contract |
| [pretix/pretix](https://github.com/pretix/pretix/tree/aa14505d2cca8fd446294af38a20afff102a53ea) | REFERENCE_ONLY | Capacity/check-in/events | Later pack; source terms/path review needed |
| [miroslavpejic85/mirotalk](https://github.com/miroslavpejic85/mirotalk/tree/10a68742fd48acb87202d50533a67e7acb1cc746) | REFERENCE_ONLY | Private WebRTC meetings | Optional provider; TURN/network/recording burden |
| [siglens/siglens](https://github.com/siglens/siglens/tree/e7245091af780ee5a592076278e5e3364b41b580) | REFERENCE_ONLY | Log analysis | Archived; use standard local observability contracts |
| [Stirling-Tools/stirling-pdf](https://github.com/Stirling-Tools/stirling-pdf/tree/d6784b3962c18bde49e533c763a14724fc9c6396) | REFERENCE_ONLY | PDF operations | Mixed edition/path; isolated qualified conversion only |
| [mattermost/mattermost](https://github.com/mattermost/mattermost/tree/80a0d4da72887d2e1b54ba1947d5cbc74f89b894) | ADAPT_PATTERN | Enterprise messaging/plugins | Connect existing server first; no duplicate identity |
| [frappe/hrms](https://github.com/frappe/hrms/tree/d222ced551c2d9de2ac67edb89fde121eb39a9af) | REFERENCE_ONLY | HCM/payroll domain breadth | Do not treat another country's rules as Saudi payroll |
| [grokability/snipe-it](https://github.com/grokability/snipe-it/tree/4b16384c9289b0c4f1df0235bf6f1b58e08d3f0f) | ADAPT_PATTERN | Asset assignment lifecycle | Shared Asset/Person/Service links |
| [mintplex-labs/anything-llm](https://github.com/mintplex-labs/anything-llm/tree/da6685510ce691b2e1be417f739c7dffee3cfc49) | ADAPT_PATTERN | Local agent UI/tool choice | Model availability not authority; no duplicate memory |
| [teableio/teable](https://github.com/teableio/teable/tree/5ef2238883cad7c3980084de9a9031135fb9734f) | ADAPT_PATTERN | Relational spreadsheet views | Core regulated models remain typed |
| [gorules/zen](https://github.com/gorules/zen/tree/adf7cdf44aa4381967a5bef1908b3b02789c3180) | ADAPT_PATTERN | Deterministic rules engine | Candidate engine after decimal/unknown/budget conformance |
| [bluewave-labs/checkmate](https://github.com/bluewave-labs/checkmate/tree/da8b230ceccade54fd6e8dc6f64f283381b63576) | ADAPT_PATTERN | Incident/health UX | No obligatory monitoring server |
| [umami-software/umami](https://github.com/umami-software/umami/tree/ec0ff50388c264ed8ce46f00967e92f7e71476ae) | ADAPT_PATTERN | Privacy-aware aggregates | Customer-local opt-in analytics only |
| [appflowy-io/appflowy](https://github.com/appflowy-io/appflowy/tree/5cf3a365dec0d59f64bad1ee4bb1050471a39b93) | ADAPT_PATTERN | Local documents/projects | CRDT collaboration not access authority |
| [gotenberg/gotenberg](https://github.com/gotenberg/gotenberg/tree/39e43205b17a21f48af75e13b6f0bd5597c50e9f) | REFERENCE_ONLY | Local PDF conversion API | Strong optional candidate; offline/fonts/sandbox qualification required |
| [akaunting/akaunting](https://github.com/akaunting/akaunting/tree/f2d049ed92a6b968e7163f6e02c549b2f5468daa) | REFERENCE_ONLY | Small-business finance UX | Restricted source posture; no accounting copy |
| [toeverything/affine](https://github.com/toeverything/affine/tree/d897bb3d84099e54a6b3c0bd5f4265f8aa87d190) | ADAPT_PATTERN | Blocks/canvas local-first UX | Mixed source; shared document identity and policy |
| [gristlabs/grist-core](https://github.com/gristlabs/grist-core/tree/87eeb6ab43d6aa04a0bbfe1525f336e2223b3160) | ADAPT_PATTERN | Relational spreadsheet/forms | No embedded unrestricted Python formulas |
| [element-hq/element-web](https://github.com/element-hq/element-web/tree/359a8b7345f8e5d00959f689972486c285a8eab4) | REFERENCE_ONLY | Matrix messaging clients | Existing provider integration; encryption/search tradeoffs explicit |
| [localstack/localstack](https://github.com/localstack/localstack/tree/8b9a79f05846835cf4dff63ab7eefdde9df83783) | REFERENCE_ONLY | Offline test emulation | Archived public repo; no runtime dependence |
| [uvdesk/community-skeleton](https://github.com/uvdesk/community-skeleton/tree/6f35040f447f7fe1dcd254e259e7b7e0a9f7a79f) | REFERENCE_ONLY | Helpdesk extension model | Extra PHP/Symfony runtime not justified |
| [block/buzz](https://github.com/block/buzz/tree/ef2aa1ae38fadcc0bc22b8bf6ed96b35933146be) | ADAPT_PATTERN | Human/agent principals and evidence | Do not inherit Nostr substrate |
| [chaitanyagiri/munder-difflin](https://github.com/chaitanyagiri/munder-difflin/tree/c7c8921f4491104d342861e32fa214e486442304) | ADAPT_PATTERN | Bounded supervisor/mailbox | CLI subscription wrapper not provider-neutral Company OS foundation |
| [jaredrhod/fullstack-agent](https://github.com/jaredrhod/fullstack-agent/tree/5bb159f47dbd6fa8f108651d0532a43aef16346b) | REFERENCE_ONLY | Memory/voice setup UX | README requires Claude Code; not offline/provider-agnostic baseline |
| [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox/tree/07e95cccd294b92f81bb715d22af6da2b619227d) | ADAPT_PATTERN | Sandbox SDK/runtime abstraction | Candidate execution adapter; must prove confinement on supported host |
| [OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr/tree/6d56d75e7e13ec47009e573e9ff4cded0d0ccc61) | ADAPT_PATTERN | Local dictation/voice UX | No ambient microphone or provider fallback |
| [Starmel/OpenSuperWhisper](https://github.com/Starmel/OpenSuperWhisper/tree/c8e6fe79d6851078940f459ab7dbc8ee39e2a97d) | ADAPT_PATTERN | macOS capture/hotkeys | Platform-specific optional adapter |
| [BraaMohammed/bricks](https://github.com/BraaMohammed/bricks/tree/586186e0d71d49a1a2fb762b66f65ad4f33d44f6) | ADAPT_PATTERN | Enrichment preview/provider cost | No root public license; grant acknowledged; BYOK calls still egress |
| [n8n-io/n8n](https://github.com/n8n-io/n8n/tree/0b2ff221c1e3b8acf46c9ab9faf2e82bd2e757db) | ADAPT_PATTERN | Workflow and connector ergonomics | Restricted/mixed source; no second execution engine |
| [activepieces/activepieces](https://github.com/activepieces/activepieces/tree/cdc72d3194cfc313f136754b121c37fe90eaed62) | ADAPT_PATTERN | Typed pieces and human input | Qualify selected SDK patterns; do not import enterprise paths blindly |
| [refly-ai/refly](https://github.com/refly-ai/refly/tree/71f8b875c8751e881776749d8ed7a74383b65fb0) | ADAPT_PATTERN | Skills and intervenable workflows | Skill version is not runtime authorization |
| [Rheosoph/flow-like](https://github.com/Rheosoph/flow-like/tree/71e45a42bb920d38b6eed6c1669f14e9286eacfb) | ADAPT_PATTERN | Typed flows/canvas/run evidence | Runtime replaceable; no new canonical app/data model |
| [livecontext-ai/livecontext-ce](https://github.com/livecontext-ai/livecontext-ce/tree/354d4fb41bf74de4901c805af49ff5cfff9f0452) | ADAPT_PATTERN | Chat/flow/app convergence | Separate authoring from runtime grants and budget enforcement |
| [raghav3600/Altclay](https://github.com/raghav3600/Altclay/tree/874d0ed8ef0a279b12c4ec01e87d42a5a7130b0d) | ADAPT_PATTERN | Small-batch enrichment and cost preview | No README; CLAUDE/package inspected: remote BYOK and Vercel analytics, not air-gapped |
| [eigent-ai/eigent](https://github.com/eigent-ai/eigent/tree/0035d94213b29f98309c1854b68233de6697822b) | ADAPT_PATTERN | Local multi-agent workforce | Narrow delegation/action contracts rather than desktop OS embedding |
| [Geta](https://github.com/Geta) | REJECT | Optimizely/.NET utilities | No material baseline fit from organization catalog |
| [clay.com](https://university.clay.com/docs/workflow-faqs) | REFERENCE_ONLY | Waterfalls/record workflows/enrichment | Product docs only; exact authorized source package not identified |

## Findings that change earlier assumptions

Cal.diy explicitly cautions against production use; Papercups is in maintenance mode; Huly’s README reports its hosted service discontinued. Peppermint, SigLens and the public LocalStack repository were archived at inspection. Fullstack-agent requires Claude Code. Altclay has no root README or LICENSE in the inspected tree; its CLAUDE.md/package.json show remote BYOK providers and a Vercel analytics dependency. None qualifies as the offline baseline merely because its repository is public.

OpenSandbox is a particularly useful execution reference, but its fast-sandbox profile shares a host/network domain and central control plane. Its policy/traffic/vault design describes deny-first binding, reset/replay after restart, fastlet-only dispatch and in-memory credential revisions. These are design/source observations, not confinement tests. Qdrat must select and qualify a concrete profile and cannot infer VM-level isolation from the SDK. See [the pinned policy design](https://github.com/opensandbox-group/OpenSandbox/blob/07e95cccd294b92f81bb715d22af6da2b619227d/components/egress/docs/policy-traffic-vault-flow.md).

## Independent discovery

36 additional repositories were inspected through live metadata, root manifests and documentation. Heads are research snapshots, not automatically preferred release versions. These are outside the founder-specific grant and require their own ordinary license/provenance qualification for actual intake.

| New source | Decision | Contribution and cost decision |
|---|---|---|
| [frappe/erpnext](https://github.com/frappe/erpnext/tree/db6e0891099ab27f571b7b9697ba90f6573430f5) | REFERENCE_ONLY | Immutable ledger/reversal and procurement semantics; connect financial authority first, no second ERP. |
| [twentyhq/twenty](https://github.com/twentyhq/twenty/tree/84b446a29ae79fc24b9407638a85bb1920f555d0) | ADAPT_PATTERN | Flexible CRM objects and activity UX; shared Person/Organization and Qdrat policy replace separate CRM authority. |
| [dbos-inc/dbos-transact-py](https://github.com/dbos-inc/dbos-transact-py/tree/a041d4d5d1e69a3b5ce1b044c6ec2033850e7c59) | ADAPT_PATTERN | PostgreSQL durable-workflow recovery; study persistence invariants, do not add another scheduler. |
| [restatedev/restate](https://github.com/restatedev/restate/tree/d5425f5bfae4024f4d26bab447bc8e6c6db08bfa) | REFERENCE_ONLY | Durable execution/service journal alternative if measured needs exceed current journal; extra server is not baseline. |
| [windmill-labs/windmill](https://github.com/windmill-labs/windmill/tree/6186a0645d3f3e92e06b666a6b5774b8af2b488f) | ADAPT_PATTERN | Typed internal-tool actions and isolated jobs; no second app/identity engine. |
| [dlt-hub/dlt](https://github.com/dlt-hub/dlt/tree/3ec3cfcaa6312bf2136f6750494d7cc3075ebf37) | ADAPT_PATTERN | Incremental extraction/schema evolution; Qdrat owns cursors, ACL, mapping and secrets. |
| [meltano/meltano](https://github.com/meltano/meltano/tree/f91d2e4f0d93065d7ca50ff775124382f4db2d0e) | REFERENCE_ONLY | Connector ecosystem; adapter qualification before adding Python/CLI orchestration stack. |
| [cube-js/cube](https://github.com/cube-js/cube/tree/d5fed3d9d72aa94be1862e74da05232f07b14fbe) | ADAPT_PATTERN | Versioned semantic measures, dimensions and access context; no separate mandatory semantic service. |
| [tobymao/sqlglot](https://github.com/tobymao/sqlglot/tree/8b6ff9386ddf4f6f8e3120a21f1991a384e60abd) | REFERENCE_ONLY | Candidate SQL dialect parser; parsing is not authorization or sandboxing. |
| [duckdb/duckdb](https://github.com/duckdb/duckdb/tree/bdd42afc245c278198fa94cddec7087e77acf7c0) | REFERENCE_ONLY | Optional bounded local analytical snapshot engine; canonical writes stay PostgreSQL. |
| [OpenLineage/OpenLineage](https://github.com/OpenLineage/OpenLineage/tree/e248b98e3146ff4437df76fcb07c83913d41f727) | ADAPT_PATTERN | Lineage facets and event vocabulary; adapt into shared evidence envelope. |
| [pgvector/pgvector](https://github.com/pgvector/pgvector/tree/efa08fda9ec485d80292d0487a77939c087dedcc) | REFERENCE_ONLY | First optional vector candidate after FTS benchmark; DB extension version/recall/ACL qualification required. |
| [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp/tree/5670d5c0bbcb148feabef84400a07cfca9aa3b30) | REFERENCE_ONLY | Local ASR candidate for CPU/desktop; separate model rights, Arabic quality and memory benchmarks. |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper/tree/ed9a06cd89a93e47838f564998a6c09b655d7f43) | REFERENCE_ONLY | Alternative local ASR throughput candidate; GPU/runtime burden must earn inclusion. |
| [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx/tree/1d04ac4d666430e911f526d9ae55a26a859159cd) | REFERENCE_ONLY | Offline streaming ASR/diarization candidate; choose via rights-cleared bilingual evaluation. |
| [ocrmypdf/OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF/tree/64d999aea85a672b51d83747f0b567907d7b38bd) | REFERENCE_ONLY | Isolated local OCR pipeline candidate; PDF parser/toolchain and resource limits required. |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract/tree/8ae68101439b3f7df123499a784e8896c805179d) | REFERENCE_ONLY | Offline Arabic/English OCR candidate; preserve original and measure extraction quality. |
| [yjs/yjs](https://github.com/yjs/yjs/tree/96c96e1fcb1ef6ce866d5264b3f97f7f77b11f64) | REFERENCE_ONLY | Collaborative document CRDT candidate; authorization, deletion and reconnect invariants remain server-owned. |
| [ueberdosis/tiptap](https://github.com/ueberdosis/tiptap/tree/8623fbe8478132aa0af7c8448a18b9a6ad080d8c) | REFERENCE_ONLY | Schema-based editor candidate; qualify extension license paths and offline assets before dependency. |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri/tree/f45ec0dcf83c139c8fdde5e61923a0e82836f756) | REFERENCE_ONLY | Optional desktop shell; signing/update/OS permissions burden deferred until browser gaps measured. |
| [microsoft/playwright](https://github.com/microsoft/playwright/tree/07f1a6154795f055f341b8972086533e8e48b36f) | REFERENCE_ONLY | Browser regression and optional controlled execution candidate; never inherit ambient user sessions. |
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core/tree/c54d1aa2decef1657e0430aec7768a3c7c103801) | REFERENCE_ONLY | Automated accessibility candidate; human keyboard/Arabic review remains required. |
| [unicode-org/cldr](https://github.com/unicode-org/cldr/tree/8c9471b37f0ac7353b5be2de6c22a04f50e9b477) | REFERENCE_ONLY | Locale/calendar reference; observed main includes prerelease data, pin a qualified release for shipping. |
| [sigstore/cosign](https://github.com/sigstore/cosign/tree/0c66ecdff337f647bbcb0259efe61a81e33a76e8) | REFERENCE_ONLY | Signing/verification candidate; offline trust-root flow cannot depend on public OIDC/Rekor at install. |
| [theupdateframework/python-tuf](https://github.com/theupdateframework/python-tuf/tree/cc8a376f5f27e94e1c3927dd148aa85b410e1ddc) | ADAPT_PATTERN | Offline update metadata, delegation and expiry/rotation; explicit trusted recovery for disconnected customers. |
| [anchore/syft](https://github.com/anchore/syft/tree/b49f0172f636fca01282eb12a411de6b0e26e633) | REFERENCE_ONLY | SBOM generation candidate; artifact inventory is not vulnerability clearance. |
| [cloudevents/spec](https://github.com/cloudevents/spec/tree/2ed3806b4ad8fda35813263cfefb2d73098b7655) | ADAPT_PATTERN | Portable event metadata vocabulary aligned to C03; domain revision and authority remain explicit. |
| [asyncapi/spec](https://github.com/asyncapi/spec/tree/1dd65fd2c1ed13f06365c1e870c61cdc82d8a981) | ADAPT_PATTERN | Event interface documentation; avoid a second runtime transport or queue requirement. |
| [cel-expr/cel-spec](https://github.com/cel-expr/cel-spec/tree/40a3c9007a9305d1f2638d5f538a4e011732cace) | ADAPT_PATTERN | Pure bounded expression semantics; deterministic decimal/missing/unknown behavior must pass Qdrat corpus. |
| [openbao/openbao](https://github.com/openbao/openbao/tree/dddb7c9577574b82585c5e685548ec3a83a4a322) | REFERENCE_ONLY | Customer secret service adapter for larger deployments; encrypted local secret store first. |
| [cedar-policy/cedar](https://github.com/cedar-policy/cedar/tree/9502ae02564a23028c732f8c1f2311635394c34f) | ADAPT_PATTERN | Typed authorization policy validation; no policy engine swap without identical deny semantics. |
| [authzed/spicedb](https://github.com/authzed/spicedb/tree/f7620a59fb61d4b523b02d5c98d7f13dc1f19dce) | REFERENCE_ONLY | Optional ReBAC engine if measured graph policy warrants service cost; Qdrat policy adapter remains authority. |
| [google/gvisor](https://github.com/google/gvisor/tree/26f3455a4cb9a377354c33aeac049080a077c79c) | REFERENCE_ONLY | Optional Linux sandbox isolation candidate; kernel/profile compatibility and limits need qualification. |
| [langfuse/langfuse](https://github.com/langfuse/langfuse/tree/816e69d4e21fdab9c32aa3872e1583aa03050297) | ADAPT_PATTERN | Local trace/evaluation review patterns; one evidence plane and no prompt/secret telemetry by default. |
| [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy/tree/40a6e168914a7b81a78b1a081d93f26de18c8d0d) | REFERENCE_ONLY | Offline prompt/program evaluation reference; optimizers cannot change production policy or model routing. |
| [novuhq/novu](https://github.com/novuhq/novu/tree/36c5c0cefa400e8edc6ec8b18ac4574288eabd03) | ADAPT_PATTERN | Channel notification/preferences patterns; shared Inbox and delivery journal remain canonical. |

## Coverage of discovery gaps

| Gap family | Evidence used | Decision |
|---|---|---|
| ERP, finance, procurement, payroll/HCM/recruiting | ERPNext, Odoo, Frappe HRMS, official Saudi authorities, HCM API research | Native shared approvals and employment; connect accounting/benefit/ATS authorities until qualified |
| CRM, customer success, support, work, ITSM/CMDB | Twenty, EspoCRM, Plane, Chatwoot/Zammad, ServiceNow/GLPI references | Shared parties, WorkItem, Case, Service and CI; no donor application federation |
| Durable execution, integration, CDC, reverse ETL | DBOS, Restate, dlt, Meltano, existing Debezium/Temporal references | One journal, checkpoint contract, source-owned writes and reconciliation; no exactly-once claim across remote APIs |
| Internal tools, grids, semantic BI | Windmill, Grist, Baserow, Cube, DuckDB, SQLGlot | Shared custom schema, policy-filtered metrics and optional analytical adapter |
| Search, RAG, graphs, memory/evaluation | Onyx, OpenRAG, Graphify, code-graph-rag, Morize/Flake, Langfuse/DSPy | Rebuildable projections and exact source citations, never second authority |
| Documents, OCR/PDF, signing | Paperless, OCRmyPDF, Tesseract, Gotenberg, Signthos/Documenso | Local derivative pipeline; legal signature assurance separately certified |
| Communications/meetings/voice | Matrix/Element, Mattermost, Zulip references, Novu, whisper.cpp/sherpa/faster-whisper | Connect existing channels; optional local capture/transcription; no hidden recording |
| Agents, browser, secure execution, waterfalls/signals | OpenSandbox, gVisor, Playwright, Kernux/Kodac, Bricks/Clay | Scoped execution and generic budgeted enrichment under shared Action API |
| IAM/ABAC/ReBAC, secrets, supply chain, offline update | Cedar, SpiceDB, OpenBao, Cosign, TUF, Syft | Adapter boundaries; small baseline; pinned complete offline release |
| Extensions/mobile/desktop/accessibility/Arabic | Yjs/Tiptap, Tauri, axe-core, CLDR, W3C WCAG/Arabic layout | Responsive browser first, qualified optional desktop; keyboard and bidirectional proof |

## Implementation intake template

For an actual copy/dependency/service, create a SourceIntake record with repository, immutable commit/tag, file paths and hashes, destination, intended interface, founder-grant or license basis, notices, transitive artifact list, modifications, threat review, contract tests, version owner, upgrade diff procedure and replacement/fallback. ADAPT_PATTERN alone requires attribution of the idea and independent Qdrat tests; it must be reclassified before copied source enters the tree. No template field may say merely “latest” or “MIT” when only repository metadata was checked.

The only tools executed for this planning work are recorded in methodology evidence. Optional production dependencies above have not been installed, imported or certified.
