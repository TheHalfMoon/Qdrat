# Product model

Qdrat sells a coherent way to operate a company. People is the first market wedge. Its advantage is a permission-preserving connection from a person and employment agreement to work, services, assets, evidence and governed actions. Functional breadth is a long-term program, not a claim that the inherited HR application already replaces enterprise suites.

## Object ownership

| Owner | Authoritative types | Shared links |
|---|---|---|
| Trust | Principal, Membership, Grant, Delegation, PolicyRevision, Approval | Person is optional; a service/agent is not an employee |
| Directory | Person, Organization, LegalEntity, Team, Position, Location | Customer/Vendor are organization roles, not duplicate identities |
| People | Employment, EmploymentContract, Assignment, TimeEntry, LeaveLedger, PayRun, CandidateApplication | Person may have several employments across legal entities |
| Work | Project, WorkItem, Goal, Cycle, Milestone, Dependency | Cases and opportunities link work; they do not inherit all issue fields |
| Service | Case, Request, Incident, Problem, Change, ServiceOffering, SLAClock | WorkItem supplies work execution; Case supplies service obligations |
| Relationships | AccountRole, ContactRole, Lead, Opportunity, Renewal, HealthAssessment | AccountRole points to Organization |
| Finance | Expense, BudgetReservation, PurchaseRequest, PurchaseOrder, InvoiceReference, JournalProposal | External ledger remains authoritative until a certified ledger exists |
| Ops | Asset, AssetAssignment, ConfigurationItem, Service, Facility, Reservation | Physical asset and observed CI are distinct linked records |
| Knowledge | FileObject, Document, DocumentRevision, KnowledgeArticle, RecordPolicy | Derived OCR, vectors and transcripts keep original revision identity |
| Data | DataSource, ConnectorBinding, ExternalIdentity, MappingRevision, SyncCheckpoint | Foreign IDs are namespaced by source/tenant/object kind |
| Automation | ActionDefinition, WorkflowRevision, RuleRevision, Trigger, Run, StepAttempt, Signal | Every producer dispatches through the same action boundary |
| AI | AgentDefinition, ModelProfile, PromptRevision, ContextBundle, MemoryRecord, Evaluation | Runs/approvals/audit belong to shared Automation/Trust |
| Platform | Event, EvidenceRecord, Notification, ViewDefinition, ExtensionPackage | No suite-private substitute identity/search/workflow engines |

Every registered object has a tenant-scoped UUID, type, schema version, owning module, revision, classification, timestamps and deletion state. Typed core tables enforce accounting, employment and lifecycle constraints. A small ObjectRef registry indexes links; it is not a giant EAV database. Studio custom records use validated versioned JSONB with typed promoted indexes and quotas; core constraints cannot be overridden by metadata.

LegalEntity is not a tenant. A deployment hosts one customer organization by default; multi-company scope within it is explicit. Tenant is an isolation domain. Separate customer installations are the default; hosted multitenancy is not an initial business dependency. No session selector alone enforces row access.

Company Digital Twin is a governed projection of these objects and sourced relationships, including uncertain observations. It can answer “who owns this service and which staff depend on it?” without granting permission to view salaries, customer secrets or hidden projects.

## Product progression

CONNECT: register authoritative external systems and preview imports. UNDERSTAND: map identities, freshness and permitted relationships. GOVERN: establish ownership, retention, approvals and evidence. AUTOMATE: execute authorized typed actions with recovery. REPLACE WHERE VALUABLE: switch a bounded field/domain authority only after reconciliation and a reversible cutover.

Success measures: fewer repeated data entries, shorter request resolution, fewer orphaned entitlements, payroll reconciliation correctness, successful restore/upgrade, Arabic/English task success and measured administrative effort. Do not optimize for the count of modules or AI messages.
