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
[CHALLENGE.md](CHALLENGE.md#m9-challenge-brief).

## Start here

- **Gate:** [A1–A4 / B + contextual C](ACCEPTANCE.md#core).
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
When needed: [C1 scenario and hints](CHALLENGE.md#c1--slow-feed-incident) and [concept explanation](REFERENCE.md#one-page-caused-101-queries). [Tool boundaries](REFERENCE.md#tools-earned-here) apply to this product.

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
When needed: [C2 scenario and hints](CHALLENGE.md#c2--cache-correctness) and [concept explanation](REFERENCE.md#redis-was-faster-but-made-private-data-stale).

On a branch, implement narrow cache-aside and exercise staleness, invalidation,
wrong-user keys, outage, stampede, and expiry. Compare the same workload and
record `evidence/M9/cache.md`. Stop by explicitly retaining or removing Redis;
retention is optional, and both choices need evidence.

### 3. Deliver one-way updates `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/social/`;
focus on `tests/m9/test_sse.py` and the output named below. Record `evidence/M9/realtime.md`.
Stop when this block's listed command passes and its evidence is saved.
Resume at [Block 3](#3-deliver-one-way-updates-required) using that saved result; continue to [Prove it](#prove-it).
When needed: [C3 scenario and hints](CHALLENGE.md#c3--realtime-mismatch) and [concept explanation](REFERENCE.md#the-realtime-transport-could-not-replay-a-gap).

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

Use the current project dependencies first. Open [Use now](REFERENCE.md#use-now) for the active pattern, [Evaluate after evidence](REFERENCE.md#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](REFERENCE.md#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](ACCEPTANCE.md#review) after the Core proof.

Prove [A1–A4](ACCEPTANCE.md#core) with query counts/plans, a repeatable workload,
percentiles, semantic regression tests, a cache decision, and reconnect policy.

## Done / next

The declared user target passes on the reference dataset without correctness
loss and every retained cache/realtime component has a failure policy. Tag
`m9-performance-social`.

### Recovery

Use [targeted references](REFERENCE.md#resources-for-m9) only for the question left by the active hint ladder.

If timing is noisy, gate on query count and plan shape while recording timing
separately. Reset the deterministic dataset before comparing results.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M10](../m10-production-multitenant-saas-capstone/README.md).

[Previous milestone: M8](../m8-concurrency-booking/README.md) · [Course home](../../README.md) · [Next milestone: M10](../m10-production-multitenant-saas-capstone/README.md)
