# Analytics and semantic metrics

Owner: qdrat/analytics. A MetricDefinition pins business meaning, grain, numerator/denominator, permitted dimensions, filters, time basis, source lineage, freshness, aggregation and suppression policy. Metric revisions explain restatements. Dashboard caches and exports enforce current query permissions.

Initial operational dashboards use authorized PostgreSQL read models: headcount as-of date, leave balance, payroll reconciliation, work throughput, case SLA and connector health. Avoid joining raw multi-valued relationships into inflated totals. Every metric includes grain and dedupe keys. Financial figures identify currency, period and authoritative ledger. HR cohorts below configured minimum size are suppressed; repeated overlapping queries must not trivially undo suppression.

Advanced BI is optional Superset against read-only scoped views or warehouse snapshots. Customer SQL and analyst queries have budgets and isolation; a BI service account cannot make all employee salaries broadly visible. Cube's semantic-layer patterns, Nao's context/evaluation and OpenLineage inform contracts. Do not deploy separate BI/search/agent metric definitions.

Materializations carry source checkpoint, schema revision and retention state; late-arriving corrections trigger explicit rebuild/restate. DuckDB is a later isolated analytical-file adapter, not a database authority or unrestricted file reader. Reverse ETL uses C04 write-through intents, not unreviewed “sync back” SQL.

Evidence: additive/nonadditive metrics, denominator changes, missingness, timezone/effective-date boundaries, restricted dimensions, small cohorts, deletion/rebuild and cross-currency controls. UX exposes data freshness and metric definition alongside results; AI narrative uses exactly the same query results and citations.
