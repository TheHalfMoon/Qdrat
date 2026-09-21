# One knowledge and document plane

Owner: qdrat/knowledge; C07/C08 govern humans and agents alike. PostgreSQL full-text search is the baseline. Arabic normalization preserves original text and searchable alternate forms; stemming/folding are explicit index-version choices tested against names and legal terms. Exact identifiers remain exact.

Ingestion stages: acquire authorized bytes → quarantine → identify MIME/size → scan → extract in isolated worker → classify → permission-bound chunks → publish derivative/index generation. A failed parser retains original custody and reports failure. Archive nesting, decompression, page count and conversion time have limits. Gotenberg/Docling/Tesseract/OCRmyPDF are optional adapters, each pinned and offline-qualified; disable outbound URL fetch in converter workers.

DocumentRevision is immutable; edit creates a new revision. Knowledge articles add review owner, effective/expiry dates and publication audience. Wiki hierarchy is presentation, not independent authorization. Signed documents retain exact original content, signing events, certificates/verification evidence and derivative provenance. Drawing a signature image is not automatically a legally qualified signature; jurisdiction/provider qualification is an explicit integration gate.

Hybrid retrieval combines authorized SQL/FTS with optional embeddings and bounded graph expansion. pgvector is the first optional vector candidate; it adds no mandatory separate service. Embedding profiles bind model digest, dimension, tokenizer and classification policy; model change builds a new index generation. Results reauthorize source records before snippets/citations are returned. AI answers cite exact source spans and expose stale or missing evidence.

File shares require a purpose, audience, expiry and download audit; external sharing is disabled unless configured. Retention applies to originals, derivatives, indexes, caches, exports, backups and legal holds. Deletion produces tombstones; restored backups replay deletion/hold journals before outbound services resume.

Knowledge collaboration starts with versioned edit/optimistic concurrency. Yjs/CRDT is a later qualified document editor adapter, never the authority for access control or payroll. Diagrams use local rendering; no automatic hosted Kroki call. E-signing and meeting providers connect through the same Action contract.

Acceptance includes cross-tenant/field permission tests, index revocation, corrupt/oversized file handling, Arabic PDF font embedding, permission-aware snippets and deterministic source citation reconstruction.
