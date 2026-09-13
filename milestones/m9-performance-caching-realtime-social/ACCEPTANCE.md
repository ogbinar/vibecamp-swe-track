# Acceptance gate

Required maturity: **Level B plus contextual Level C performance/operations behavior**.

## Core

- **A1:** Predeclared workload and equal-harness baseline/final evidence report dataset skew, mix, concurrency, environment, p50/p95/p99, throughput/errors; N+1 guard, SQL/query-plan interpretation, justified indexes, and cursor insertion test prove query optimization/pagination.
- **A2:** C2 Redis cache-aside branch measures benefit and tests invalidation, private/deleted staleness, TTL, key scope, outage fallback, and stampede control; final decision to retain or remove is evidence-based.
- **A3:** C3 compares SSE vs WebSockets (and polling) against directionality; retained path tests disconnect/reconnect, restart, gaps/replay/loss, and slow consumers with documented semantics.
- **A4:** Final critical path meets the predeclared target on the reference environment; a [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) traces post/profile data through authoritative rows, Redis keys, live buffers, invalidation, retention/deletion, and outage recovery; performance regression and clean functional/migration/lint/validator commands pass.

## Stretch

Retain WebSockets for a real bidirectional feature or compare feed fan-out strategies under the same correctness contract.
