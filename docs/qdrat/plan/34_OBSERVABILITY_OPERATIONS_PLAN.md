# Operations and observability

Local structured logs, metrics and traces share trace_id/run_id/operation_id but not raw secret/customer content. Telemetry is local by default. Remote export is an explicit customer-configured destination with classification and retention. OpenTelemetry integration is optional transport; no mandatory vendor account.

Core signals: request error/latency, DB pool/locks, outbox age, worker leases, oldest runnable/waiting/reconciling steps, failed approvals, connector lag/drift, credential expiry, file quarantine age, index generation lag, backup age/restore test age, disk saturation and egress denials. Separate liveness from readiness and degraded optional capabilities.

Operations UI links a failure to safe evidence and bounded actions: pause, retry when safe, reconcile unknown effect, cancel, rotate credentials, resnapshot source, rebuild projection and restore. Each action is authorized/audited. A “retry all” button must exclude non-idempotent or unknown-result operations.

Runbooks specify symptoms, read-only diagnosis, owner, impact, preservation of evidence, reversible action, escalation and recovery proof. Priority incidents: database unavailable, disk full, credential compromise, source ACL stale, payroll export uncertain, leaked file share, failed upgrade and missing backup keys.

Proposed SLOs: 99.5% monthly essential API availability for qualified single-server deployments excluding declared maintenance; HA target 99.9% only after G11 proof. Customer host/network choices bound these claims. Alert on burn rate, stale backups and stuck financial actions; do not overwhelm users with every retry.

Backup/recovery proof is a user-visible operational status. Diagnostics bundle lists included data and redaction findings before export. Support can receive it only through an explicitly authorized sharing action; no hidden telemetry/support tunnel.
