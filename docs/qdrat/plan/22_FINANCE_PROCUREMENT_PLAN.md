# Finance, purchasing and vendor operations

Owner: qdrat/finance; Directory owns vendor organizations. Finance starts as an operational control and integration layer above an existing ledger. A reporting projection must name its source ledger, legal entity, period and freshness.

Native first: Expense with receipts and policy checks; Budget and atomic BudgetReservation; PurchaseRequest with lines, approvals and supplier quotes; PurchaseOrder with acknowledged version; receiving evidence; vendor onboarding/risk reviews; InvoiceReference and payment-status projection. Match PO/receipt/invoice by exact line/quantity/currency with tolerance policy and exception queue. Do not auto-pay on an OCR match.

Segregate requester, approver, buyer, recipient and payment releaser by policy; emergency exceptions have expiry and evidence. Vendor bank changes require independent verification and two-person approval. Fraud-sensitive identifiers are field-restricted; logs/model contexts exclude full banking information.

AP/AR, tax, bank reconciliation, consolidation and statutory reporting CONNECT_FIRST. Initial ledger adapter exports balanced JournalProposal with debit/credit equality by currency, period, account mapping revision, source PayRun/Expense IDs and idempotency key. Remote posting is reconciled by provider transaction ID; unknown state cannot be retried blindly. Corrections use reversal plus replacement.

A future native double-entry ledger requires a separate certified gate: immutable posting, period close/reopen control, currency/rate policy, audit trail, tax/country qualification, opening balances, subledger reconciliation and parallel close cycles. It is intentionally outside the first People release. ERPNext/Odoo/BigCapital provide domain references, not copied accounting authority.

Saudi e-invoicing remains a qualified ZATCA integration before native issuance. Invoice numbers, signing/clearance/reporting and statutory retention cannot be inferred from generic PDF generation.

Test budget races, split invoices, duplicate bills, partial receipts, rejected posting, foreign exchange rounding, closed periods and restore/re-export safety. Admin screens show source ledger and reconciliation status. A finance dashboard without qualified accounting is labeled an operational view, not statutory accounts.
