# Qdrat — Product and Standards Reference Sources

This file records non-donor sources used to define Qdrat's product requirements, interoperability direction, country packs, privacy posture, and competitive benchmark. These sources are references, not code donors, unless separately listed in `SOURCE_AUTHORIZATIONS.md`.

## Permission vocabulary

- `FOUNDER_ATTESTED_SOURCE`: source-code use authorization is recorded separately in `SOURCE_AUTHORIZATIONS.md`.
- `PUBLIC_REFERENCE_ONLY`: study public product behavior, documentation, standards, and published interfaces; no proprietary source-code permission is asserted here.
- `PUBLIC_STANDARD/DATASET`: public standard or dataset subject to its published terms.
- `OFFICIAL_REGULATORY_REFERENCE`: official government/regulatory source; verify effective dates before implementing statutory behavior.

## Founder-supplied commercial product references

| Source | URL | Permission/use status | Qdrat use |
|---|---|---|---|
| Zoho People | https://www.zoho.com/ar/people/?sredirect=true | PUBLIC_REFERENCE_ONLY | HRIS breadth, employee self-service, workflows, AI/product UX benchmark |
| BambooHR | https://www.bamboohr.com | PUBLIC_REFERENCE_ONLY | HRIS UX, employee records, onboarding, analytics, compensation and platform simplicity benchmark |

## Additional competitive references

| Source | URL | Permission/use status | Qdrat use |
|---|---|---|---|
| Workday HCM | https://www.workday.com | PUBLIC_REFERENCE_ONLY | Enterprise HCM, skills, workforce planning, process automation and talent benchmark |
| Oracle Fusion Cloud HCM | https://www.oracle.com/human-capital-management/ | PUBLIC_REFERENCE_ONLY | Enterprise HCM breadth, journeys, AI/agent and global HR benchmark |
| SAP SuccessFactors | https://www.sap.com/products/hcm.html | PUBLIC_REFERENCE_ONLY | Global HCM, talent, learning, compensation and workforce benchmark |
| Rippling | https://www.rippling.com | PUBLIC_REFERENCE_ONLY | Employee lifecycle linked to identity, apps, devices, payroll and IT operations |
| Deel | https://www.deel.com | PUBLIC_REFERENCE_ONLY | Global workforce, payroll, contractor/employment lifecycle and compliance benchmark |
| Personio | https://www.personio.com | PUBLIC_REFERENCE_ONLY | European HR platform UX, workflows and people operations benchmark |
| HiBob | https://www.hibob.com | PUBLIC_REFERENCE_ONLY | Employee experience, people data, performance and modern HR UX benchmark |
| Factorial | https://factorialhr.com | PUBLIC_REFERENCE_ONLY | SMB/mid-market HR operations, time, documents and workflow benchmark |

## Interoperability, skills and data references

| Source | URL | Status | Qdrat use |
|---|---|---|---|
| HR Open Standards | https://www.hropenstandards.org | PUBLIC_STANDARD/DATASET | HR interoperability mappings, canonical exchange concepts |
| ESCO | https://esco.ec.europa.eu | PUBLIC_STANDARD/DATASET | Skills/occupations taxonomy and local skills graph seed subject to published dataset terms |
| O*NET | https://www.onetcenter.org | PUBLIC_STANDARD/DATASET | Occupation, task, knowledge, ability and skill reference mappings subject to published terms |
| SCIM | https://www.rfc-editor.org/rfc/rfc7644 | PUBLIC_STANDARD/DATASET | Identity provisioning protocol |
| OpenID Connect | https://openid.net/developers/how-connect-works/ | PUBLIC_STANDARD/DATASET | Authentication/federation interoperability |
| OAuth 2.0 | https://www.rfc-editor.org/rfc/rfc6749 | PUBLIC_STANDARD/DATASET | Authorization protocol reference |

## Saudi Arabia official references

Qdrat's Saudi country pack must be implemented from effective official rules, not remembered summaries. At minimum track these authorities and portals:

| Authority/source | URL | Status | Qdrat use |
|---|---|---|---|
| Ministry of Human Resources and Social Development | https://www.hrsd.gov.sa | OFFICIAL_REGULATORY_REFERENCE | Labor rules, employment services and official guidance |
| Qiwa | https://www.qiwa.sa | OFFICIAL_REGULATORY_REFERENCE | Employment contract/workforce workflows and official employer services |
| Saudi Data & AI Authority / PDPL resources | https://sdaia.gov.sa | OFFICIAL_REGULATORY_REFERENCE | Personal-data governance, privacy controls and implementation evidence |
| General Organization for Social Insurance | https://www.gosi.gov.sa | OFFICIAL_REGULATORY_REFERENCE | Social-insurance data/rules and payroll integration requirements |
| Mudad | https://mudad.com.sa | OFFICIAL_REGULATORY_REFERENCE | Wage protection/payroll-related employer services where officially supported |

## Research rule

Every benchmark or statutory implementation claim must be traceable to a dated source snapshot, official documentation, or reproducible public observation. Product references can inspire requirements and UX patterns but proprietary code, assets, private APIs, protected text, and trademarks are not imported unless separately authorized and recorded.

## Relationship to source-code permissions

All GitHub repositories and organizations for which the founder stated full-source permission are recorded in `SOURCE_AUTHORIZATIONS.md`. Their engineering role and public-license boundary are recorded in `SOURCE_LANDSCAPE.md` and `DONOR_REGISTRY.md`. This file intentionally keeps non-code references separate so Qdrat does not confuse public observation with source-code authorization.