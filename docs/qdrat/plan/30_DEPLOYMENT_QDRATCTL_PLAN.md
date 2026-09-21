# Deployment and administration

Default is a single customer instance. Runtime profiles are additive and must state hardware, dependencies, egress and tested platform matrix.

| Profile | Contract |
|---|---|
| Developer | Linux container runtime on Linux/WSL2/macOS virtualization; synthetic data and clearly unsafe dev credentials |
| Laptop | No-AI baseline, local browser, persistent encrypted storage, sleep/restart recovery; not HA |
| Small organization/single server | TLS reverse proxy, web, PostgreSQL, workers, backup target; no mandatory model/vector/BI service |
| Private HA | Multiple web/workers, fenced jobs, managed PG replication/failover, durable blob storage; tested failure domains |
| Kubernetes | Supported manifests/operators with equivalent policies; no K8s requirement for small users |
| Air-gapped | Signed complete bundle with images/wheels/fonts/locales/migrations; optional model packs; local trust roots and zero internet dependency |

Target initial capacity profiles, not measured claims: laptop 4 cores/8 GB RAM/20 GB free without models; small server 8 cores/16 GB/100 GB plus customer blobs. Baseline qualification measures actual peaks and adjusts declared minimums before release. No GPU assumption. Preserve Redis in inherited deploy until G0 inventory proves how to remove or scope it.

qdratctl commands: preflight, install, start, stop, status, health, migrate --plan/--apply, backup, restore --verify, upgrade --plan/--apply, rollback --plan, bundle verify/import, model-pack import/remove, diagnostics, sbom, provenance and egress-check. Destructive apply requires a bound reviewed plan and operator credentials; read-only plan commands are safe. Secrets come from protected input/file descriptors or OS store, never command-line arguments/logs.

Preflight validates architecture/kernel/runtime versions, disk/RAM, time, TLS/name resolution, DB compatibility, trust keys, backup access and egress policy. Production install refuses default credentials/debug exposure. First boot produces a single expiring local bootstrap action; it does not expose a reusable administrator password.

Offline bundle includes exact images and transitive artifacts; verify checksums/signatures/notices before load. Diagnostics redact identifiers/secrets and require explicit export; no automatic vendor upload. Health distinguishes liveness, readiness, dependency freshness and degraded optional components.

Installation proof includes clean VM, no-internet bootstrap, no-AI operation, backup to separate customer storage, restore to another host, upgrade/rollback and declared unsupported-host rejection. HA qualification comes after singleton jobs and storage assumptions are removed, not from increasing replicas.
