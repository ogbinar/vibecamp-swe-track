# M9 — Keep the feed fast as it grows

[Course home](../../README.md) / M9

**Milestone 10 of 11 · M9**

## Business problem

The feed is correct for two posts but performs one profile lookup per post. Make
it fast for representative data without changing what users observe.

## Product objective

- **Product can:** readers get a bounded feed and one-way updates without making cache or SSE durable truth.
- **You will prove:** equal-workload query, cache-authority, SSE reconnect/gap/loss, and API evidence.

Use the [feed contract](../../projects/social/specs/M9-FEED-CONTRACT.md).
Reproduce the call-count shape with SQLAlchemy/PostgreSQL, deterministic data,
and `EXPLAIN`. Set a user-facing target, repair query shape and indexes, then
consider cursor pagination. Run a Redis cache-aside experiment after recording
the PostgreSQL baseline; retaining Redis is optional and requires evidence that
its benefit exceeds its failure and operating cost. Prove staleness,
invalidation, outage, and tenant/user key scope. Compare polling, server-sent
events (SSE), and WebSockets from the fixed one-way update. Core implements SSE;
WebSocket implementation is Stretch. Complete C1–C3 in
[challenge brief](#challenge-brief).

## Start here

- **Gate:** [A1–A4 / B + contextual C](#core).
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/social/README.md#social-launch-kit-for-m9), then return to the saved block; first visit: [Block 1](#1-measure-and-repair-the-database-feed-required).

From `projects/social/`, run its documented command block. Expected: the functional test
passes and the opt-in query-budget challenge reports 100 profile reads.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Build

### 1. Measure and repair the database feed `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/social/`;
focus on `tests/m9/test_database_feed.py` and the output named below. Record `evidence/M9/database.md`.
Stop when this block's listed command passes and its evidence is saved.
Resume at [Block 1](#1-measure-and-repair-the-database-feed-required) using that saved result; continue to Block 2.
When needed: [C1 scenario and hints](#c1--slow-feed-incident) and [concept explanation](#one-page-caused-101-queries). [Tool boundaries](#tools-earned-here) apply to this product.

Run the in-memory query-budget observation, then read the
[feed contract](../../projects/social/specs/M9-FEED-CONTRACT.md). Build the same
feed on PostgreSQL, capture statements and `EXPLAIN`, then repair query shape,
indexes, and cursor behavior. Record equal-harness evidence in
`evidence/M9/database.md`. Stop when correctness and the two-query gate pass.

### 2. Experiment with Redis `[REQUIRED EXPERIMENT]`

Start from Block 1 green with its result recorded. Work in `projects/social/`;
focus on `tests/m9/test_cache_experiment.py` and the output named below. Record `evidence/M9/cache.md`.
Stop when this block's listed command passes and its evidence is saved.
Resume at [Block 2](#2-experiment-with-redis-required-experiment) using that saved result; continue to Block 3.
When needed: [C2 scenario and hints](#c2--cache-correctness) and [concept explanation](#redis-was-faster-but-made-private-data-stale).

On a branch, implement narrow cache-aside and exercise staleness, invalidation,
wrong-user keys, outage, stampede, and expiry. Compare the same workload and
record `evidence/M9/cache.md`. Stop by explicitly retaining or removing Redis;
retention is optional, and both choices need evidence.

### 3. Deliver one-way updates `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/social/`;
focus on `tests/m9/test_sse.py` and the output named below. Record `evidence/M9/realtime.md`.
Stop when this block's listed command passes and its evidence is saved.
Resume at [Block 3](#3-deliver-one-way-updates-required) using that saved result; continue to [Prove it](#prove-it).
When needed: [C3 scenario and hints](#c3--realtime-mismatch) and [concept explanation](#the-realtime-transport-could-not-replay-a-gap).

Compare polling, SSE, and WebSockets, then implement Core SSE. Exercise
reconnect, last-event ID, gaps, restart, malformed events, and slow consumers.
Record `evidence/M9/realtime.md`. Stop when the published replay/loss policy is
observable. A WebSocket implementation is Stretch.

The neutral starter intentionally does not supply the SSE application or
`tests/m9/test_sse.py`: the contract, lesson, and acceptance requirements are
provided, while that implementation and its behavioral tests are learner work.

### Diagnose deliberate failures

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Understand

- **N+1 query:** one collection query followed by another query per result.
- **Query plan:** PostgreSQL's chosen operations for executing SQL.
- **Percentile:** a latency boundary met by a stated share of requests.
- **Cache-aside:** application-managed lookup and population of a cache.
- **Invalidation:** removing or replacing cached data after truth changes.
- **SSE:** server-sent events, a one-way HTTP update stream.
- **WebSocket:** a persistent two-way message connection.

## Use a tool if earned

Use the current project dependencies first. Open [Use now](#use-now) for the active pattern, [Evaluate after evidence](#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](#review) after the Core proof.

Prove [A1–A4](#core) with query counts/plans, a repeatable workload,
percentiles, semantic regression tests, a cache decision, and reconnect policy.

## Done / next

The declared user target passes on the reference dataset without correctness
loss and every retained cache/realtime component has a failure policy. Tag
`m9-performance-social`.

### Recovery

Use [targeted references](#resources-for-m9) only for the question left by the active hint ladder.

If timing is noisy, gate on query count and plan shape while recording timing
separately. Reset the deterministic dataset before comparing results.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M10](../m10-production-multitenant-saas-capstone/README.md).

[Previous milestone: M8](../m8-concurrency-booking/README.md) · [Course home](../../README.md) · [Next milestone: M10](../m10-production-multitenant-saas-capstone/README.md)


---

## Challenge brief

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
3. Use the SQLAlchemy/PostgreSQL links in the Reference section below.

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
3. Use the Redis cache-aside link in the Reference section below.

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
3. Use the FastAPI SSE reference in the Reference section below.

### Reset

Close test streams, restart the API, and run `uv run --locked pytest tests/m9/test_sse.py -q`.

Ship equal-harness evidence without cherry-picking.


---

## Acceptance gate

Required maturity: **Level B plus contextual Level C performance/operations behavior**.

## Core

- **A1:**
  - [ ] Predeclared workload and equal-harness baseline/final evidence report dataset skew, mix, concurrency, environment, p50/p95/p99, throughput/errors
  - [ ] N+1 guard, SQL/query-plan interpretation, justified indexes, and cursor insertion test prove query optimization/pagination.
- **A2:**
  - [ ] C2 runs the required Redis experiment, keeps PostgreSQL authoritative, and measures cache benefit under the same harness.
  - [ ] Tests cover invalidation, private/deleted staleness, and TTL behavior.
  - [ ] Tests cover user/tenant key scope, outage fallback, and stampede control.
  - [ ] final decision to retain or remove Redis includes operational cost and is evidence-based; removal is a valid Core result.
- **A3:**
  - [ ] C3 compares SSE vs WebSockets (and polling) against directionality.
  - [ ] Core SSE tests disconnect/reconnect, restart, gaps/replay/loss, and slow consumers with documented semantics.
- **A4:**
  - [ ] Final critical path meets the predeclared target on the reference environment
  - [ ] any async database adoption beats the synchronous baseline under the same harness and records pool/failure/complexity trade-offs
  - [ ] A [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) traces post/profile data through authoritative rows, Redis keys, and live buffers.
  - [ ] The review covers invalidation, retention/deletion, and outage recovery.
  - [ ] performance regression and clean functional/migration/Ruff/mypy/validator commands pass.

## Execution map

Each checklist bullet is a local step in order. From `projects/social/`, use
README Blocks 1, 2, and 3 for A1, A2, and A3. For A4 run the full project checks
and `test -s evidence/M9/data-lifecycle.md`. Record equal-harness results under
matching A headings; recover by disabling experimental cache/realtime paths,
reseeding PostgreSQL, and rerunning the baseline.

## Stretch

Retain WebSockets for a real bidirectional feature or compare feed fan-out strategies under the same correctness contract.

## Review

### Review

Answer one question at a time in `evidence/M9/index.md`:

1. Why does the dataset and request mix represent the fixed feed?
2. Which query-plan observation drove the database change?
3. What statement count detects N+1?
4. What write/storage cost does the index add?
5. How does the cursor prevent duplicates and omissions during insertion?
6. What remains authoritative while Redis is available or down?
7. How are invalidation, wrong-user keys, stampede, and stale authorization tested?
8. Why does the fixed requirement choose SSE instead of WebSockets?
9. What happens after reconnect, restart, gap, or a slow consumer?
10. Did the optimization change visible feed semantics?
11. If async access is proposed, what measured synchronous bottleneck earns it?

Use the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md) to test whether deletion/privacy changes reach cache and live copies. Lens prompt (same A1–A4 gate): a career-shifter explains the performance trade-off in user-impact language; a data specialist connects query-plan skill to cache correctness, API pagination, and live-operation limits.


---

## Reference

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
