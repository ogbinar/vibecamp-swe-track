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
