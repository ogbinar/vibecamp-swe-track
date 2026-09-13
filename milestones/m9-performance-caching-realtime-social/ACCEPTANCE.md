# Acceptance gate

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
