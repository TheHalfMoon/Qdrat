# Relationships, sales and customer success

Owner: qdrat/relationships. Organization/Person stay in Directory. AccountRole and ContactRole attach commercial context, source authority, consent, owner and territory without duplicating master identities. Lead qualifies into an existing or new linked account/contact and Opportunity through a reversible, audited merge decision.

Opportunity owns stage, expected value/currency, probability source, close date, participants, products and next action. Stage transitions are typed actions with required evidence. Activities use shared Conversation/Work/Calendar links. Contract and InvoiceReference connect sale → delivery → support → renewal without exposing employee or unrelated account data.

Enrichment uses generic Data mappings and Automation WaterfallStep. Each result records provider, timestamp, confidence, rights/use restriction, validation and expiration. Do not equate personal-data availability with consent to outreach. Suppression/unsubscribe is checked at send time across campaign and service contexts. Browser research produces cited observations; no undisclosed contact scraping or hidden third-party egress.

Signals have source, condition revision, evaluation window, confidence and TTL. Dedupe/coalesce before creating a task. HealthAssessment combines explainable, versioned factors (support/service adoption, contract/renewal state and permitted customer signals); missing values are unknown. Scores are advisory and never silently change customer access or contract terms.

Native order: account/contact ownership and timeline → opportunity pipeline → activities/contract links → enrichment preview → customer onboarding/renewals/health → campaigns via connectors. Salesforce/HubSpot/Dynamics/Zoho/Attio/Pipedrive connect first when authoritative. Bulk import supports dry-run, field authority, merge candidates and rejection ledger.

API: typed account-role/opportunity/renewal queries and action transitions; no direct writes to finance settlement. UI reuses object page, table, board, timeline and Inbox. Test duplicate identity merges, revoked territory access, stale enrichment, opt-out during queued outreach, budget exhaustion, source deletion, cross-account attachments and currency totals. CPQ, advertising exchange, contact-data resale and autonomous unsolicited outreach are non-goals until separately specified.
