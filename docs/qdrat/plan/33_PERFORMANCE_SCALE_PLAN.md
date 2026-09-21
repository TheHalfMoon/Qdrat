# Performance and scale qualification

Targets below are engineering budgets to test, not measured product claims. Define workload/hardware/data sizes before measurement and record cold/warm cache separately.

| Profile/workload | Initial acceptance budget |
|---|---|
| Small server, 1,000 people, 25 concurrent active users | p95 ordinary authorized reads <500 ms, commands <1 s excluding external work |
| Grid 100k work/case records, page 50 | p95 filtered page <750 ms with declared indexes; no unbounded count/query |
| Local FTS 1m bounded chunks | p95 authorized query <1.5 s on stated hardware; ACL verification included |
| Durable worker | no lost committed run over crash/restart tests; stable queue growth at declared admitted rate |
| UI | primary route usable <3 s on declared laptop/LAN; long grids virtualized with keyboard access |
| Cancellation | dispatch stops within 5 s target; running-process termination/profile bound measured separately |

Rate admission is tenant/principal/action-specific. Pagination, query limits, index quotas, upload sizes, loop bounds, parallel fanout and budget reservations prevent one user consuming the host. Export/ingestion/payroll run asynchronously with progress and cancellation; they never hold a web transaction for a long job.

Measure database query plans, lock contention, connections, outbox age, worker queue delay, conversion/model memory and blob growth. Avoid premature partitioning/sharding. Introduce read replicas only for queries that can state staleness; authorization changes and command preconditions use authoritative reads.

HA qualification tests web/worker loss, PostgreSQL failover, network partition, stale lease fencing, blob unavailability and restoration. External effects remain potentially unknown under partition. Strong consistency requirements stop rather than serve stale permission/financial state.

Scale triggers for optional services are recorded ADRs: inability to meet qualified FTS/vector budgets, analytical contention despite snapshots, or native durable-engine limits. Choose one replacement adapter and demonstrate migration; do not retain two authoritative engines. Initial targets may be revised only with evidence and documented customer impact, not silently weakened after a failed benchmark.
