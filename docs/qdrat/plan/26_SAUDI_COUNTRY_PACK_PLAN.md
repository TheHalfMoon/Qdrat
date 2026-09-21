# Saudi Arabia country pack

Owner: qdrat/country/sa; People/Finance own transactions. Pack = jurisdiction, version, effective interval, authoritative source digest/article, cohort/applicability predicates, formulas, rounding, fixtures, reviewer signoff and supersession. Core contains no Saudi constants. New rules do not retroactively rewrite closed pay runs.

Official sources inspected during research:
- [HRSD labour-law amendments](https://www.hrsd.gov.sa/sites/default/files/2025-03/Amendments%20to%20Labor%20Law%20Articles_0.pdf), effective-date announcement for 19 February 2025.
- [GOSI new-system text](https://beta.gosi.gov.sa/ar/new-system) and [contributor eligibility](https://beta.gosi.gov.sa/en/persona/contributor): new-entry and prior-contribution cohorts differ; phased contribution dates must be represented.
- [HRSD Nitaqat 2026 calculator](https://es.hrsd.gov.sa/Services/Inquiry/NitaqatCalculatorMotawar2026.aspx) and [new-phase announcement](https://www.hrsd.gov.sa/si/node/5579002). Old 2021/2023 tables are not a current universal formula.
- [SDAIA PDPL knowledge center](https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/) and [implementing regulations](https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulation.pdf).
- [HRSD WPS upload service](https://www.hrsd.gov.sa/en/ministry-services/services/رفع-ملف-حماية-الأجور) and [WPS user guide](https://www.hrsd.gov.sa/sites/default/files/2025-08/dlyl-almstkhdm-lbrnamj-hmayt-alajwr.pdf).
- [ZATCA e-invoicing phases](https://zatca.gov.sa/en/E-Invoicing/Introduction/Pages/Roll-out-phases.aspx).

These establish design inputs, not a completed legal interpretation or payroll certification. Public Qiwa navigation was not fully retrievable. No public partner/API entitlement was proved for Qiwa/Mudad/GOSI. Therefore initial integration is assisted export/import with human submission acknowledgment; exact provider API adapters are gated on documented access and conformance, never reverse-engineered automation.

Rule inventory: working-time/weekly rest/Ramadan applicability; overtime base and premiums; leave types/accrual/carry/termination; contract type/probation/notice; wage components/deductions; GOSI cohort/contribution periods/ceilings; EOSB tenure/termination reasons/wage base; Nitaqat activity/entity/eligible worker weighting; WPS file version and reconciliation. Each row needs official article and positive/negative/boundary fixtures before activation. A payroll specialist's acceptance is a release requirement, not an architecture question for the founder.

Store Gregorian instants/local dates plus selected calendar display; Hijri conversion policy must name its calendar implementation/version. Never calculate service duration by subtracting display strings. Arabic/English contracts retain legally reviewed wording, original language and signed bytes.

PDPL pack includes processing inventory, purpose/basis, data-subject rights, hold/deletion handling and transfer assessment. Do not encode a blanket statement that every transfer is prohibited or always allowed. Remote AI and enrichments pass the same transfer controls. Retention periods are purpose/entity/rule-specific with evidence; no invented single retention constant.

Saudi live payroll remains disabled until frozen source/artifact matrix, independent formula review, golden cases, parallel payroll reconciliation, WPS acknowledgment and recovery rehearsal pass G4. A late regulatory change produces a new effective-dated pack and impacted-run report.
