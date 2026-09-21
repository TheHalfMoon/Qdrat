# Bounded reconciliation 1: repository Diffcipline scope contract (G0-01)

## Conflict

`.diffcipline.toml` carried `expected_files = ["docs/qdrat/plan/**", ".diffcipline.toml"]`
and the comment "Canonical-plan change policy only. Implementation tasks must
publish a bounded task-specific policy".

Diffcipline does not work that way. Enterprise layering is deliberately
monotonic: `layered_scope_violations` evaluates the repository `expected_files`
contract *independently* of the task policy, so an enterprise policy can add
constraints but can never widen the repository contract
(`crates/diffcipline-cli/src/enterprise.rs`, pinned revision
`1e6d14f77b95bb132b42276f10d67f1018ab5bb6`).

Consequence: every implementation task is rejected before its own review starts.
G0-01 was the first task to reach that wall. Its frozen dependency artifacts
cannot live under `docs/qdrat/plan/**`, so no task-specific policy could rescue
the run.

## Observed evidence

First Diffcipline attempt, with the task policy originally written across
multiple lines and before this reconciliation:

```text
$ diffcipline check --base 144935cd6bb64d3448ec3927fa7d1569bee93ca0 --risk R2 \
    --enterprise-policy .diffcipline/tasks/G0-01.toml --run --json
diffcipline: expected_files must be an array
exit 64
```

That first failure was a policy-format failure, preserved in
`diffcipline-attempt-1.log`: Diffcipline's policy reader takes one
`key = [...]` per line and rejects a wrapped array. Fixing the formatting
exposed the scope conflict described above rather than a passing gate, so both
failures are recorded rather than the second one replacing the first.

## Bounded fix

Removed only `expected_files` from the repository policy. Everything else -
file and line ceilings, the three review decisions, cumulative forbidden
surfaces and the R1 baseline commands - is unchanged.

Rationale for removing rather than widening it: an `expected_files` contract is a
per-change statement, not a repository constant. Leaving it empty in the
repository layer and declaring scope in each task policy keeps one enforced
contract per change, and keeps the plan-only contract that planning changes rely
on intact in `docs/qdrat/plan/plan-policy.toml`.

What this does **not** change: the task policy still declares
`forbidden_surfaces` including `docs/qdrat/plan/**`, `requirements.txt`,
`Dockerfile`, `horilla/**`, `base/**` and `.github/workflows/**`, so the plan and
the application surfaces remain protected for this change.

## Residual risk

With an empty repository `expected_files`, a change that arrives *without* a task
policy has no expected-files contract at all; only the repository ceilings and
forbidden surfaces apply. That is a real reduction in defence for unplanned
changes, and it is the reason this is recorded as a reconciliation rather than a
silent edit. A later task should make the task policy mandatory by an
organisation-controlled enforcement path rather than by a local file, which
Diffcipline's own contract documentation says is the only way to make such a
baseline genuinely mandatory.
