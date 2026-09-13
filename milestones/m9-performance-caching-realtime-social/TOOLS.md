# Tools earned here

- **PostgreSQL `EXPLAIN (ANALYZE, BUFFERS)`/statistics:** find actual plan/cardinality/I/O problems.
- **Committed synthetic-data and load harnesses:** repeat workload with fixed seed and report percentiles/errors.
- **Redis cache-aside (controlled evaluation):** test hit value, invalidation, staleness, outage, stampede, and key scope; removal is valid.
- **SSE:** default earned option for one-way updates after polling misses need.
- **WebSockets:** Stretch only for demonstrated bidirectional requirements.

Avoid benchmark-only indexes, unbounded feed fan-out, cache-before-measurement, or optional pagination libraries that change the contract.

Record the Redis decision by revisiting the [complexity rejection record](../../templates/COMPLEXITY-REJECTION.md): measured benefit may justify adoption, or equal-harness evidence may support continued rejection/removal.
