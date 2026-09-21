# G0-02 execution evidence - SG-000002

Task: `G0-02 - Prove clean image and PostgreSQL bootstrap`.
`docs/qdrat/plan/tasks/tasks.json` requires `scope-and-base`, `contract-tests`,
`recovery-proof`, `diffcipline-proof`, `independent-review` and `accepted-head`.
This directory holds the machine evidence for the first four; review and
acceptance are addressed at the end, and neither is claimed.

Base: `a5834978ea87c14f658adc5f9061526055894012` (the G0-01 acceptance branch,
which carries the accepted head `b4531988f`). Head at proof time:
`da6f808bb7a2646a5d851afc696bba62ea8b4b53`.

| File | Proves |
| --- | --- |
| `refinement.json`, `specgrain-readiness.json`, `workpacket.json` | The real SpecGrain refinement of SG-000002, its Grain readiness, and the WorkPacket it was executed against. |
| `build-no-cache.log`, `build-no-cache-full.log` | The clean `--no-cache` build: exit 0, the builder installs the frozen lock through `docker/lock-requirements.py`, the direct spaCy wheel comes from the recorded URL, and the export names the image digest. |
| `compose-config-dev.log`, `compose-config-prod.log` | `docker compose config` for both stacks, exit 0, with the digest-pinned service images and the scheduler's release-task opt-out visible. |
| `manage-check.log` | `manage.py check` inside the running container: 0 issues. |
| `race-before-serialisation-1.log`, `-2.log` | **Negative evidence.** Two containers STARTED TOGETHER against an empty database: one exited 0, the other exited 1 with a `UniqueViolation` on `pg_type_typname_nsp_index` while creating `django_migrations`. |
| `race-after-serialisation-1.log`, `-2.log`, `-3.log` | Three containers started together against an empty database on the fixed image: all exit 0, one applies 250 migrations while the other two wait 298.9s and 317.9s for the release lock and then find nothing to apply. |
| `bootstrap-2-repeat.log` | The repeated bootstrap: lock acquired immediately, "No migrations to apply.", `Listening at http://0.0.0.0:8000` 3m47s later (collectstatic on a bind-mounted Windows host). |
| `os-packages.txt` | OS package inventory of the built image: 157 Debian packages with exact versions. |
| `bootstrap-proof.json` | The acceptance mapping: every criterion, its command, its observed result, the artifact digests, and every finding including the ones that are not fixed. |

## What the task actually required, and what it took

The five acceptance criteria are a clean build, a valid compose configuration, a
passing `manage.py check`, a repeated bootstrap with no migration race, and logs
that bind the image digest. Three of those are mechanical. Two were not.

`Dockerfile` used to install `requirements.txt`, whose ranges let pip resolve a
different set on every build. G0-01 froze the exact set and explicitly deferred
wiring it in. Doing that needs one thing the lock cannot do on its own: the
spaCy model is a GitHub release asset, not an index distribution, so a plain
`pip install --require-hashes -r <lock>` cannot resolve it. `docker/lock-requirements.py`
renders the lock and the artifact inventory into one file where that single
artifact becomes `name @ url#sha256=...`, with the URL taken from the inventory
rather than repeated in the Dockerfile.

"Repeated bootstrap has no migration race" was measured rather than assumed, and
the measurement found a race that the plan's wording only hinted at: two
containers starting together both create `django_migrations`, and one of them
dies. That is preserved in `race-before-serialisation-*.log` and fixed by
`docker/release_tasks.py`, which takes a PostgreSQL advisory lock around
`migrate` and `collectstatic`. The fix was then re-probed, and the re-probe
immediately found a second defect of its own - the runner could not import the
application when executed as `python docker/release_tasks.py`, because that puts
`docker/` rather than the project root on `sys.path`. Both are recorded.

## What is not claimed

* **No independent review.** Open Code Review v1.12.8 is present, its
  deterministic preview runs, and its review cannot: no LLM endpoint credential
  exists in this environment (`OCR_LLM_URL`/`OCR_LLM_TOKEN`/`OCR_LLM_MODEL` or a
  config file are all absent), and the only model credential available serves
  Jev decision models rather than diff review. Under chapter 41 that is
  ABSTAIN/UNAVAILABLE, which is not approval.
* **No accepted-head record for G0-02.** It cannot be produced honestly before
  the revision is accepted.
* **No CI.** The inherited workflows still trigger only on `dev/v2.0` and `2.0`.
  The G0 exit requires CI on the actual PR base; that is a successor task.
* **No merge, no release, no gate closure.** `evidence/gates/G0.json` does not
  exist.
* **The healthcheck budget is not fixed.** On this host a legitimate first
  bootstrap takes 8m51s and a repeat takes 3m47s, while the compose healthcheck
  budget is 150s, so `docker compose up --wait` reports unhealthy while the
  bootstrap is progressing normally. The numbers are recorded and the decision
  is named as `QDRAT-DEV-HEALTHCHECK-BUDGET` rather than made silently here.
* **The measured timings are this host's.** They include the cost of the Windows
  bind mount, and they are not a claim about other hardware.
