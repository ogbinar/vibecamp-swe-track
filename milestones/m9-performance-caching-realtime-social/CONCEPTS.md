# Problems and mental models

Performance begins with user-facing targets and representative size/skew/request mix—not a profiler screenshot. Measure p50/p95/p99, throughput, errors, saturation, environment, warmup, and duration. Query optimization follows evidence: bound N+1, read `EXPLAIN (ANALYZE, BUFFERS)`, understand cardinality, then change SQL/indexes and account for write cost.

Cursor pagination needs stable total order and insertion-between-pages semantics. Redis cache-aside adds staleness, invalidation, outage, stampede, key/tenant scope, TTL, and operational cost; it is optional even though the curriculum requires exercising it. A controlled branch can prove then remove it if net value is absent.

Polling, SSE, and WebSockets answer different directionality/latency needs. SSE is simple one-way streaming; WebSockets support bidirectional messages but add connection/protocol state. Neither creates durable replay automatically; define restart, reconnect, gap, and slow-consumer behavior.
