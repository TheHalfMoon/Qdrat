# Live repository truth

Observed 2026-09-20 and reverified 2026-09-21 through the connected GitHub account and a clean local checkout:

| Item | Verified value |
|---|---|
| Repository | TheHalfMoon/Qdrat, public |
| Default branch | main |
| Main/import base | e2d288940aab52af881786678b2fc86dfa5c272a |
| Foundation branch | foundation/qdrat-people-blueprint |
| Foundation head | 933f9c1070c151876c1e198d6141413f33e4b6d3 |
| Existing PR | [#1](https://github.com/TheHalfMoon/Qdrat/pull/1), open, non-draft, unmerged |
| Planning branch | codex/qdrat-canonical-plan |
| Runtime baseline | Horilla 2.0-derived Django application, not the target platform |
| Local history | Shallow retrieval of foundation, preserving its parent identity |

The foundation PR has 33 commits and 21 changed files, documentation/governance only. Its title is “Qdrat foundation: universal private Company OS, automation fabric, agents, voice and source landscape”. Re-query before acting; this table is a snapshot.

The historical 11 September build was network-bound and INCONCLUSIVE; it establishes no passing tests. No application runtime tests were run during research. requirements.txt mixes pins and intentional platform ranges; the Docker image, apt packages and pip bootstrap are not fully reproducible. The spaCy model wheel has a direct remote URL that needs artifact integrity and offline qualification.

The inherited unit-test workflow targets dev/v2.0 and 2.0, not Qdrat main/foundation. Therefore an open Qdrat PR cannot be assumed tested merely because workflows exist. Preserve the Makefile's coverage floor of 26 and PostgreSQL test backend. Do not replace narrow correctness lint with a repository-wide style rewrite.

Production/development composition includes web, PostgreSQL, Redis and a separate scheduler. The production override does not by itself establish TLS or a private network. Existing media, tenant, scheduler and backup controls require the source-backed review in 31 and baseline qualification in G0.

The original empty local checkout contained no user code to preserve. This planning branch was created from the exact foundation SHA. GitHub CLI authentication was unavailable; the connected GitHub service and read-only public Git retrieval worked. Credentials were not changed.

Machine counterpart: evidence/repository-snapshot.json. The final handoff must additionally bind the planning commit; never replace that binding with “latest”.
