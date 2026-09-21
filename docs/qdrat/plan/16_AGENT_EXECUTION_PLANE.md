# Replaceable agent execution plane

Owner: qdrat/automation execution adapters plus Trust. This plane executes authorized tool requests; it never decides business permission. Baseline disables arbitrary shell, GUI and browser agents.

ExecutionRequest binds run/step/action digest, principal/delegation, profile, image digest, command/tool schema, read-only input artifacts, allowed output types, egress destinations, secret handles, resource limits, deadline and cancellation token. ExecutionResult returns outcome, exit/status, artifact digests, sanitized trace, measured usage and confinement evidence. C05 handles unknown completion.

Profiles separate document conversion, analytics, browser research and code/shell. Untrusted code requires a qualified strong isolation boundary (e.g. gVisor/microVM) on supported Linux; ordinary containers alone do not qualify the enterprise untrusted-code profile. OpenSandbox is the leading adapter candidate, not an assurance certificate. If the host cannot provide the required confinement, deny the tool and preserve ordinary application operation.

No host Docker socket, home directory, SSH agent, cloud metadata endpoint or broad network mount. Inputs are immutable per-run artifacts. Credentials are short-lived, target-bound broker handles injected only into the intended operation; outputs/logs are scanned/redacted before publication. Network rules are enforced outside the guest with destination resolution/revalidation; the guest cannot grant itself egress.

A separate customer-controlled execution worker identity has no direct production database write credential. All company changes return through action APIs. Remote systems use connectors with account-bound grants. Browser sessions begin with isolated profiles and explicitly authorized accounts, never ambient employee cookies. GUI support is later and has visible session/target binding, preview and action approval.

Kill switch revokes dispatch and credentials, terminates workers, records incomplete/irreversible actions, and fences stale completion. Circuit breakers cap repeated failures/cost. Cleanup destroys ephemeral disks and expires artifacts according to policy; compliance evidence is retained separately.

Qualification uses benign isolation and conformance checks, resource saturation limits, denied egress destinations, cancellation, crash recovery, artifact custody and secret redaction. Do not implement offensive autonomous testing or bypass mechanisms as part of this plane.
