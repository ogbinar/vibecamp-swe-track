# M9 challenge brief

Run from `projects/social/`. Use the same workload before and after each change.

## **C1 — Slow feed incident**

**PROVIDED** — observe the in-memory query budget before building the database feed.

### Steps

1. Create `tests/m9/test_database_feed.py` and load the fixed skewed dataset.
2. Capture query count and `EXPLAIN (ANALYZE, BUFFERS)` before changing SQL.
3. Repair query shape, index fit, and cursor behavior; run README Block 1.

### Hints

1. Count statements and verify page correctness before optimizing.
2. Inspect relationship loading, cardinality estimate, total order, and index columns.
3. Use the SQLAlchemy/PostgreSQL links in `RESOURCES.md`.

### Reset

Run the social bounded reset and deterministic seed, then run
`uv run --locked pytest tests/m9/test_database_feed.py -q`.

## **C2 — Cache correctness**

**YOU BUILD** — run the required isolated Redis experiment; retention is optional.

### Steps

1. Create `tests/m9/test_cache_experiment.py` after recording the PostgreSQL baseline.
2. Exercise stale/private rows, invalidation, stampede, outage, expiry, and wrong-user keys.
3. Run README Block 2 and record an evidence-based retain/remove decision.

### Hints

1. Name PostgreSQL as authority and the exact value being cached.
2. Inspect key scope, invalidation event, time-to-live, outage, and concurrency.
3. Use the Redis cache-aside link in `RESOURCES.md`.

### Reset

Disable or flush only the course cache namespace, prove PostgreSQL behavior is
green, and rerun `tests/m9/test_cache_experiment.py`.

## **C3 — Realtime mismatch**

**YOU BUILD** — implement Core server-sent events (SSE) for one-way updates.

### Steps

1. Create `tests/m9/test_sse.py` and write the replay/loss policy first.
2. Exercise reconnect, last-event ID, gaps, restart, malformed events, and slow consumers.
3. Run README Block 3; keep WebSockets as Stretch.

### Hints

1. Ask whether the client ever needs to send messages over the live connection.
2. Inspect event identity, replay source, reconnect cursor, and buffering limits.
3. Use the MDN SSE link in `RESOURCES.md`.

### Reset

Close test streams, restart the API, and run `uv run --locked pytest tests/m9/test_sse.py -q`.

Ship equal-harness evidence without cherry-picking.
