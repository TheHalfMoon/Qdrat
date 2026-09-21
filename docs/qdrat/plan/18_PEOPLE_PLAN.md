# People: first full market wedge

People owns employment, not identity. Person can be candidate, contractor, employee and customer contact simultaneously; Employment is legal-entity-specific and effective-dated. Horilla is a bootstrap adapter whose routes/models are inventoried before replacement.

| Slice | Data/behavior | Required proof |
|---|---|---|
| Core HR | Person/Employment/Assignment, status history, documents, manager and position | Concurrent edits, future/retroactive changes, field permissions, export fidelity |
| Contracts | Template revision, employment terms, effective interval, signed original and acceptance | No overlapping active contract authority; amendment preserves old version |
| Time/attendance | Raw punch evidence, corrected TimeEntry, source/device, timezone, schedule, approver | Overnight shifts, duplicate punches, DST, missing entries, audit correction |
| Scheduling | Shift template, assignment, availability, overtime/coverage warnings | Conflict detection and legal-pack limits; manager override evidence |
| Leave | LeavePolicyRevision, accrual ledger, reservation, approval, cancellation | No negative entitlement without explicit policy; concurrent reservation and reversal |
| Payroll | PayRun input snapshot, calculation revision, line evidence, review, release, reconciliation | Exact decimal totals, retro adjustments, shadow comparison, no duplicate bank export |
| Recruiting | Requisition, CandidateApplication, consent, stage, interview, offer | Separate candidate privacy; human decision; deletion and offer revision |
| On/offboarding | Versioned checklist of People/Trust/Ops/Work actions | Partial failure, access revocation, asset return and accountable outstanding items |
| Performance | Goal, feedback, review cycle, calibration access, acknowledgments | Confidentiality, appeal/correction, human accountability |
| Compensation/benefits | Effective-dated package/enrollment, budget approvals, eligibility | Segregation, pro-rata/retro changes, restricted sensitive fields |
| Learning/skills/succession | Skill evidence, course assignment/completion, development plans | No unsupported competency inference; versioned assessment and consent |
| Workforce planning | Headcount scenario, position budget, capacity and aggregate analytics | Scenario isolation; no automatic employment changes |
| Employee experience | Self-service requests, service cases, surveys, policy acknowledgment | Arabic/mobile/accessibility, anonymization thresholds and grievance privacy |

PayRun lifecycle: DRAFT → INPUT_FROZEN → CALCULATED → REVIEWED → APPROVED → EXPORTED → RECONCILING → CLOSED. Rejection returns to a new draft revision; input changes invalidate approval. A payment export is a signed artifact with checksum and beneficiary/count totals, not proof of bank settlement. Corrections append adjustments/reversals; closed results are never silently edited. Payroll-to-ledger creates balanced JournalProposal and reconciles acceptance by the authoritative finance system.

Initial native journey: directory → contract/assignment → leave request → manager approval → evidence/document view. Payroll remains shadow-only until Saudi pack, dual-control, golden fixtures and independent payroll acceptance pass. Benefits/learning/ATS providers connect first where local breadth is not yet qualified. Every suite reuses Inbox, Work, Service, files and Automation.

Do not preserve Horilla table boundaries merely for familiarity. Preserve imported IDs/provenance and migration reversibility. Attendance geolocation is optional, purpose-bound and minimized; it is not a general employee surveillance feature.
