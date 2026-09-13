# M9 feed, cache, and realtime contract

The feed contains visible posts from followed authors, ordered by
`created_at DESC, id DESC`. Cursor pagination encodes both values. An insertion
between requests causes no duplicate; posts inserted ahead of the cursor appear
only in a fresh traversal. Private or deleted posts never appear.

Reference workload: 100 posts (70 from one author, 30 across nine), 20-item
pages, 80% first-page and 20% next-page requests, one then eight concurrent
clients. Record machine/container limits, query count, plan, p50/p95/p99,
throughput, and errors. Core user target: p95 under 200 ms locally with at most
two SQL statements per page; if the environment cannot support the latency,
retain the query-count gate and explain the measured limit.

Run Redis cache-aside as a required experiment. Fixtures cover stale private and
deleted posts, missed invalidation, wrong-user key, outage, stampede, and expiry.
PostgreSQL stays authoritative; removing Redis after measurement is valid.

Core live updates are one-way server-sent events (SSE). Publish post-created
identifiers, reconnect with a last-event identifier, and document replay window,
gap response, restart behavior, malformed event handling, and slow-consumer
limit. Compare WebSockets; implementation is Stretch.
