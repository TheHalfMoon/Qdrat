# Ops, assets and facilities

Owner: qdrat/ops. Asset is owned/leased property; ConfigurationItem is an observed managed component; Service is delivered capability. Link them explicitly. AssetAssignment binds custodian, effective dates, acknowledgment and condition; retirement preserves history. Stock quantities and financial depreciation remain connected to authoritative inventory/ledger until those modules qualify.

Initial capabilities: asset catalog, serial/asset tag uniqueness within scope, assignment/return, warranty/contract links, maintenance work, facility/location, room/equipment reservations and vendor service requests. Person departure uses the same offboarding Flow to reconcile entitlements, assets and outstanding work.

CMDB adapters read approved inventory sources such as NetBox/Snipe-IT/GLPI. Reconciliation uses source authority, observation age and conflict queue. Service topology and impact are derived twin queries with confidence and permission checks. No network scanner, remote endpoint manager or patch deployment is implicitly authorized by asset visibility.

Reservation locks prevent double-booking and respect timezone/buffer/maintenance windows. Maps use optional PostGIS only for demonstrated location/geofence needs; no mandatory hosted geocoding or tile service. Offline maps require licensed bundled tiles, otherwise show list/location text. Exact employee tracking is not a baseline feature.

Device-control actions, if later introduced, require separate principal grants, inventory freshness, target identity, preview, maintenance window and recovery contract. Facilities requests use Service, repairs use Work, spend uses Finance, documents use Knowledge.

Tests: duplicate imports, lost device identifiers, reassignment races, stale CI relationships, private facility records, reservation overlap, asset-return partial failure and retirement/restore. Metrics: assignment discrepancy, overdue maintenance, unowned services and reconciliation backlog.
