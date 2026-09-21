# Security and privacy threat model

## Overview

Scope: TheHalfMoon/Qdrat source at 933f9c1070c151876c1e198d6141413f33e4b6d3 plus explicitly labeled target architecture. This is a source-backed planning model, not completed vulnerability-audit coverage or an exploitation report. An independent architecture reviewer provided interim observations but could not finish due to an account usage limit; the parent verified the material anchors below sequentially. Independent final review remains an evidence obligation.

| Component | Current source evidence |
|---|---|
| Django web/media entry | base/urls.py:2079; base/views.py:8746 |
| Company policy context | base/auth_backends.py:34; horilla/horilla_middlewares.py:19 |
| API JWT company context | horilla_api/authentication.py:47 |
| Default company permission flag | horilla/settings/base.py:487 |
| Local blob path | horilla/settings/base.py:284 |
| Optional external storage override | horilla/settings/addons.py:10 |
| Scheduler/backup path | horilla_backup/scheduler.py:21 and :89 |
| Backup credential model | horilla_backup/models.py:44 |
| Build/CI boundary | .github/workflows/unit-tests.yml:7 |

| Deployment or workflow | Resource/capability | Configuration/precedence | Effective value/location | Readers/writers | Control/evidence or unknown |
|---|---|---|---|---|---|
| Dev web/scheduler | Source tree | Compose bind mount | checkout mounted at /app | web and scheduler | Development trust only; docker-compose.yml:13 and :46 |
| Dev/prod files | Shared media | base MEDIA_ROOT, optional addons, then local overrides | default /app/media, named media volume | web/scheduler; nginx has no media mount | base.py:284; Compose :15/:47; prod :30/:51 |
| Optional external storage | FileField backend and namespace | AWS-presence guard selects STORAGES backend; namespace joins configured root | configured backend/bucket plus configured MEDIA_ROOT/NAMESPACE | backend credentials/application | addons.py:10–32; deployment value not supplied; no remote-storage qualification claimed |
| Production web | HTTP exposure | prod ports replaces base | host port 8000; nginx port 80 from base | reachable according to host/firewall/proxy configuration | prod :31; Compose :104; TLS not established by these files |
| Production scheduler | Scheduled jobs | command run_scheduler, replicas 1 | same application and media authority | scheduler process | Compose :44/:64, prod :53; multiple replicas unqualified |
| Legacy backup | Dump/archive and external transfer | runtime GoogleDriveBackup row; per-process scheduler | working-directory backupdb.dump/media.zip and settings.MEDIA_ROOT | backup process and configured external account | scheduler :93 references removed service-account field; models :44 uses OAuth; current successful restore unproved |

## Trust boundaries and assumptions

Protected assets: employment/payroll/identity data, candidate/customer records, documents, secrets, integrity of payments/approvals, recoverability and source authority. Actors: unauthenticated visitors, employee/manager, external portal user, integration principal, administrator and (future) delegated agent. A normal actor is not assumed to control the host, database administrator or release signing key.

Current company scoping is application/context based; it is not proof of universal row-level isolation. JWT authentication deliberately resolves company scope and permits superuser behavior; retain these controls while mapping every bypass-sensitive consumer. Current media handling establishes path/authentication/active-content controls, but this inspected function does not resolve the business object's ownership. The target C08 owner-aware file policy requires explicit implementation and migration coverage.

Assume production operator controls host, TLS and trusted configuration; validate effective overrides at preflight. Third-party APIs and remote storage are conditional configurations. Air-gap, secret encryption, immutable audit, no-AI operation, sandbox confinement and egress enforcement are target requirements, not inherited guarantees.

## Prioritized scenarios and mitigations

Scenarios below are design hypotheses/control gaps to qualify, not reproduced findings.

| Priority | Scenario/capability gain | Prerequisite | Impact | Current counterevidence/control | Target mitigation |
|---|---|---|---|---|---|
| High | User receives a document outside their business scope | Sensitive document served by generic media consumer | Confidentiality | safe_join, hidden-file rejection, authentication, attachment/no-sniff handling at base/views.py:8757–8815 | C08 owner/field policy, migrated file registry, policy regression tests |
| High | Background work runs under wrong company/authority | Job omits correct principal context | Integrity/confidentiality | company backend/context and scoped JWT exist | explicit task principal, no ambient global manager, reauthorization |
| High | Repeated/unknown external effect duplicates payroll/send | retries, crashes or multiple job runners | Financial/data integrity | singleton scheduler declaration | C04/C05 idempotency, leases, reconciliation, human release |
| High | Recovery archive incomplete or unusable | Current backup feature assumed sufficient | Availability/data loss | backup code/model mismatch observed | offline encrypted backup/restore contract and independent restore rehearsal |
| High | Optional connector or document processing crosses host/data boundary | Future connector/parser enabled | Credential/data exposure | No target sandbox guarantees established | isolated worker, brokered credentials, enforced egress, size/time limits |
| High | Derived AI/search result broadens permissions | Future indexing/caching/agent enabled | Disclosure or unauthorized action | Future design only | C02/C07 query-time checks, source ACL freshness, no model grants |
| High | Update bundle or extension changes authority unexpectedly | Trusted install/upgrade workflow | Persistent integrity loss | Existing workflows are not a complete signed-distribution chain | offline trust root, signed digest, manifest capability diff, restore point |
| Medium | Production exposed with incomplete TLS/proxy controls | Host publishes configured ports without intended TLS front end | Session/privacy exposure | production DEBUG/secret requirements exist | preflight fail unsafe production exposure; explicit reverse-proxy configuration |
| Medium | Audit/diagnostic/backup retains secrets or deleted data | Export/restore enabled | Privacy | No comprehensive current evidence | redacted diagnostics, key separation, deletion/hold journal and retention |

## Severity calibration

Critical requires credible unauthenticated or low-privilege compromise of broad production authority or widespread irreversible effects, with actual reachable prerequisites. An administrator already owning the host is not a new remote privilege escalation. High covers cross-scope sensitive records, payment/identity integrity and unusable recovery with realistic paths. Medium covers bounded exposure requiring specific configuration or recovery workflow; Low covers limited self-only informational issues. Confidence is separate from impact. No severity here implies exploit validation.

Before customer data, G1 must close owner-aware file access, explicit principal propagation and baseline recovery gaps; G10 validates operations, signed distribution and privacy controls. R3 security changes require independent review of the exact implementation revision.
