# Qdrat People — Donor and Reference Registry

## Rules

Every external source is classified before code is copied. Classification options are `BASE`, `CODE_DONOR`, `DEPENDENCY`, `REFERENCE_ONLY`, or `REJECTED`. File-level provenance and license obligations must be recorded for copied code. No dependency or source may be introduced merely because its repository is public.

GPL-family source code is not copied into the Qdrat codebase unless the project deliberately accepts the resulting licensing obligations after review. Product behavior and public documentation may still be studied as references without copying protected implementation or text.

## Current registry

| Source | Role | License observed | Current use |
|---|---|---|---|
| horilla/horilla-hr | BASE | LGPL-2.1 | Full inherited Git history and source baseline; preserve notices and upstream provenance. |
| frappe/hrms | REFERENCE_ONLY | GPL-3.0 | Study domain/workflow ideas; do not copy code under current policy. |
| orangehrm/orangehrm | REFERENCE_ONLY | GPL-3.0 | Study HR flows and module boundaries; do not copy code under current policy. |
| qdrant/qdrant | DEPENDENCY candidate | Apache-2.0 | Local semantic/vector retrieval. |
| keycloak/keycloak | DEPENDENCY candidate | Apache-2.0 | Optional enterprise identity federation. |
| openfga/openfga | DEPENDENCY candidate | Apache-2.0 | Optional relationship-based authorization engine. |
| ollama/ollama | DEPENDENCY candidate | MIT | Local model runtime and development ergonomics. |
| ggml-org/llama.cpp | DEPENDENCY candidate | MIT | Local/edge inference runtime option. |
| temporalio/temporal | DEPENDENCY candidate | MIT | Future durable workflow engine if native automation is insufficient. |
| docling-project/docling | DEPENDENCY candidate | MIT | Local document parsing and extraction. |

## Candidate code/reference sources requiring qualification

The following open-source HR projects are useful research candidates but must pass repository-level and file-level license/provenance review before any implementation is copied: OpenHRApp, HRKit, Sevendyne HRMS, open-source-hrm, and other modern HRIS/HRMS projects discovered during research.

## Proprietary product references

BambooHR, Zoho People, Workday, Oracle HCM, SAP SuccessFactors, Rippling, Deel, Personio, HiBob, and Factorial are feature/UX references only. Qdrat must not copy proprietary code, private APIs, protected assets, or substantial copyrighted text.

## Supply-chain gate

Before dependency adoption or code donation, record repository URL, exact commit/tag, license/SPDX identifier, notice/attribution requirements, dependency tree impact, security posture, maintenance status, data-egress behavior, and whether the component is necessary in air-gapped deployments. Produce SBOMs for releases and fail release gates on unknown or forbidden licenses.
