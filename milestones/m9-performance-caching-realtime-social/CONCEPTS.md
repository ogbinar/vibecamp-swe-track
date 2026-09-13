# M9 concepts through a slow feed

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
