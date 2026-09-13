# Tools earned here

- **PostgreSQL `EXPLAIN (ANALYZE, BUFFERS)`/statistics:** find actual plan/cardinality/I/O problems.
- **Committed synthetic-data and load harnesses:** repeat workload with fixed seed and report percentiles/errors.
- **Redis through the maintained Python client (controlled evaluation):** PostgreSQL remains durable truth; test hit value, invalidation, staleness, outage, stampede, TTL, and user/tenant key scope; removal is valid.
- **SSE:** earned option for one-way updates only after polling misses a declared latency target; it does not promise durable replay.
- **WebSockets:** Stretch only for demonstrated bidirectional low-latency requirements, with connection auth, backpressure, restart, and protocol-state tests.

Keep synchronous database access unless the representative workload isolates it as the limiting factor and an equal-harness async comparison justifies added session/pool/failure complexity. Avoid benchmark-only indexes, unbounded feed fan-out, cache-before-measurement, or optional pagination libraries that change stable ordering/cursor semantics.

Record the Redis decision by revisiting the [complexity rejection record](../../templates/COMPLEXITY-REJECTION.md): measured benefit may justify adoption, or equal-harness evidence may support continued rejection/removal.
