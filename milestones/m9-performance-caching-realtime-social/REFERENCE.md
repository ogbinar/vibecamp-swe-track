# M9 reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M9 concepts through a slow feed

## “One page caused 101 queries”

**Example:** one post query triggers one profile query per post. **Term — N+1:**
one collection query plus one query for each item. **Rule:** count statements and
read the plan before changing SQL or indexes.

## “The cache served a deleted private post”

**Example:** PostgreSQL changed but Redis did not. **Term — cache invalidation:**
removing or replacing a cached copy when authoritative truth changes. **Rule:**
experiment with Redis, test its failure modes, and remove it if net value is
absent.

## “The benchmark did not represent real feed traffic”

**Example:** a tiny uniform dataset hides high-fan-out users. **Term — percentile
latency:** the response time below which a percentage such as 95% of requests
finish. **Rule:** predeclare size, skew, request mix, concurrency, environment,
warmup, duration, throughput, errors, and p50/p95/p99.

## “Offset pages duplicated posts during insertion”

**Example:** a new row shifts every later offset. **Term — cursor pagination:**
the next page starts after a value in a stable total order. **Rule:** prove no
duplicates or omissions while inserts occur.

## “Redis was faster but made private data stale”

**Example:** a cache key omits user scope. **Term — cache-aside:** the application
reads authoritative storage on a miss and stores a copy. **Rule:** test staleness,
invalidation, outage, stampede, key scope, and time-to-live; removal is valid.

## “The realtime transport could not replay a gap”

**Example:** server-sent events reconnect after process restart. **Term — replay
policy:** which missed events can be recovered and from where. **Rule:** choose
polling, SSE, or WebSockets by directionality and define restart, gaps, and slow consumers.

### Tools earned here

- **PostgreSQL `EXPLAIN (ANALYZE, BUFFERS)`/statistics:** find actual plan/cardinality/I/O problems.
- **Committed synthetic-data and load harnesses:** repeat workload with fixed seed and report percentiles/errors.
- **Redis through the maintained Python client (controlled evaluation):** PostgreSQL remains durable truth; test hit value, invalidation, staleness, outage, stampede, TTL, and user/tenant key scope; removal is valid.
- **SSE:** earned option for one-way updates only after polling misses a declared latency target; it does not promise durable replay.
- **WebSockets:** Stretch only for demonstrated bidirectional low-latency requirements, with connection auth, backpressure, restart, and protocol-state tests.

Keep synchronous database access unless the representative workload isolates it as the limiting factor and an equal-harness async comparison justifies added session/pool/failure complexity. Avoid benchmark-only indexes, unbounded feed fan-out, cache-before-measurement, or optional pagination libraries that change stable ordering/cursor semantics.

Record the Redis decision by revisiting the [complexity rejection record](../../templates/COMPLEXITY-REJECTION.md): measured benefit may justify adoption, or equal-harness evidence may support continued rejection/removal.

## Evaluate after evidence

Evaluate only optional tools after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M9

Open these only after capturing query count, plan, dataset, and budget evidence. Reviewed 2026-09-14.

- [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — Why did PostgreSQL choose this plan? Applicable tool: current PostgreSQL.
- [SQLAlchemy relationship loading](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html) — Which loading strategy removes the observed N+1 without over-fetching? Applicable tool: SQLAlchemy 2.0.
- [Redis client-side caching](https://redis.io/docs/latest/develop/clients/client-side-caching/) — What invalidation responsibilities appear when cached state is shared? Applicable tool: current Redis.
- [FastAPI server-sent events](https://fastapi.tiangolo.com/tutorial/server-sent-events/) and [WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) — How does the fixed one-way latency need map to native SSE, and what later bidirectional need would earn WebSockets? Applicable APIs: current FastAPI/browser platform.

Cache or realtime infrastructure must follow a measured requirement and written failure policy.
