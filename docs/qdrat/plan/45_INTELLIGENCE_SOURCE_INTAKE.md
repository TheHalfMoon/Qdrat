# Qdrat Intelligence Fabric — source intake map

Status: **RESEARCH / INTAKE MAP**

This document records the first architecture-level disposition of the founder-supplied intelligence sources. It is not source admission, runtime dependency admission, or permission to bypass path-level provenance.

## Source matrix

| Source | Observed public posture | High-value mechanisms | Qdrat destination | Do not inherit |
|---|---|---|---|---|
| `google/ax` | Apache-2.0 | Task/Workspace/Gateway/Model, sandbox workload orchestration, egress fencing, suspend/resume | G9-04 optional cluster backend; G11 scale profile | Kubernetes as baseline requirement; AX domain types as Qdrat authority |
| `superdesigndev/treg` | Apache-2.0 text plus additional hosted-service restriction; founder states separate permission | capability search, tool/CLI/skill registry, credential injection, pricing/audit, MCP | G9-03 Capability Fabric; G8-07 adapters; G7-03 provider waterfalls | hosted billing model as core; silent provider routing; raw secrets in clients |
| `aayushch/laya` | Apache-2.0 | action cards, daily briefings, Coherence, context association, hybrid BM25/vector retrieval, agent workspaces, budget UX | Qdrat Home/My Work/Inbox; G9-02; G9-03 | separate SQLite/Chroma authority; notification-centric domain model |
| `TheoLeeCJ/SemIf` | MIT | direct typed option scoring, shared-state reuse, local GGUF/MLX/MPS/CUDA backends, calibration | G9-01 PLD provider; G9-06 evaluation | treating model score as policy or fact |
| `Mapika/decider` | Apache-2.0 | trained Choice/Score/Noul decisions, Jev-compatible wire shape, calibration, local CUDA/MPS/CPU options | G9-01 PLD provider; G9-06 benchmark | fixed model as universal default |
| `bespokelabs/Bespoke-Nimble-9B` | Apache-2.0 model metadata | structured prediction/evidence-grounded 9B adapter | G9-01 optional quality PLD model; G10-02 model bundle | assuming base-model/adapter runtime fits every device |
| `tinyfish-io/agentql` | MIT | semantic selectors, structured extraction, resilient web automation | G7-03/G9-03 local research/browser adapter patterns | hosted API as local baseline |
| `tinyfish-io/bigset-oss` | AGPL-3.0 public posture | NL-to-dataset, schema inference, fan-out research, verification, dedupe, refresh cadence | G7-03 workflow/reference; isolated service only unless grant/path review allows more | cloud API dependency; reciprocal code in Qdrat core without explicit grant handling |
| `tinyfish-io/tf-playwright-stealth` | MIT | browser automation resilience patterns | G9 research/browser qualification | anti-detection behavior as a goal; policy bypass |
| `tinyfish-io/agentql-mcp` and integrations | MIT observed on inspected repos | MCP/browser integration patterns | G8-07/G9-03 adapter references | MCP as separate authority |
| `tinyfish-io/tinyfish-mcp-server` | MIT | local loopback proxy/security patterns | remote-provider adapter reference only | calling hosted TinyFish "local"; remote dependency in air-gapped profile |
| `wonderwhy-er/DesktopCommanderMCP` | MIT | filesystem/terminal/process/session management, bounded output, local audit, file editing | explicit host-capability provider under G9-04/G9-05 | describing guardrails as a sandbox; ambient host authority |

## Intake rule

Before copying any path:

1. pin the exact upstream revision;
2. record the original path and destination;
3. re-read the license/grant applicable to that exact path;
4. record notices and third-party dependencies;
5. run security and data-egress review;
6. prefer the smallest reusable primitive over wholesale import;
7. keep Qdrat contracts authoritative;
8. retain an update/removal/fallback strategy.

Founder standing authorization removes the need to ask again for ordinary source-use permission. It does not erase provenance, notices, third-party rights, trademark boundaries or dependency obligations.
