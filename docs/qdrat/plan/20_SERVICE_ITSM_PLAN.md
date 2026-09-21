# Service and ITSM

Owner: qdrat/service. Case is an accountable service obligation; Conversation contains channel messages; Request applies a ServiceOffering; Incident restores service; Problem tracks underlying cause; Change controls a planned alteration. They share links, work, approvals and evidence, not one untyped ticket with hundreds of optional columns.

Message identity is tenant/channel/account/remote message ID. Inbound mail/web chat is normalized, deduplicated, scanned and associated by authorized identity. Email display names are not authenticated employee identity. Public/private/internal notes have explicit audience; replies preview recipients and attachments. Outbound sends use C04/C05 unknown-result handling. Customer portals use scoped external Principals without employee permissions.

Queue routing uses Rules with capacity and skills. SLA/OLA clocks pin policy, calendar/timezone, priority, start/pause/resume/stop events and breach evidence. Reopening creates defined new/resumed obligations; edits do not erase prior breach. Escalation is a Flow; timer correctness survives restarts and calendar changes. Business calendars do not assume Saturday/Sunday weekends.

Initial channels: portal and explicitly configured email. Third-party chat/voice/WhatsApp/social channels connect through declared provider credentials/terms and remain unavailable in air-gap. No synthetic promise of offline external delivery. Knowledge suggestions use C07 and human-reviewed publication.

ITSM adds catalog request forms, incident/problem/change lifecycle, major-incident collaboration and CI/service relationships from the shared twin. Change has standard/normal/emergency policy, risk/impact, deployment window, conflict checking, approval and backout evidence. Do not implement autonomous network discovery or device control by default; connect trusted inventory feeds first.

AI triage drafts category/priority/reply with cited context; AI resolution requires action-level authority and escalation to human. QA samples/redacts interactions with explicit retention and staff/customer policy.

Measure first response/resolution, reopen, transfer, breach and customer satisfaction with denominators and excluded periods defined. Test channel duplicates, lost sends, audience leaks, SLA pause races, external-principal isolation, restricted HR cases, incident links, emergency approvals and portal RTL. ServiceNow depth is added only when the common model can support it without separate platform administration.
