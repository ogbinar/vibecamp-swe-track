# Acceptance gate

Required maturity: **Level B** for concurrent booking correctness.

## Core

- **A1:**
  - [ ] C1 deterministically violates the naive invariant and records transaction interleaving
  - [ ] the production path is repaired while the reproduction remains isolated.
- **A2:**
  - [ ] C2 runs at least 100 final-capacity races across multiple app processes with exact allowed winners, stable losers, and zero database invariant violations
  - [ ] chosen locking/control and isolation are explained.
- **A3:**
  - [ ] C3 deterministic tests establish confirm/expire/cancel winner semantics using documented time policy
  - [ ] induced deadlock/serialization failure receives bounded retry or stable response and no hang.
- **A4:**
  - [ ] Load evidence reports conflict rate, latency distribution, database errors, final invariant query, and environment
  - [ ] clean API/integration/migration/lint/validator commands pass.

## Execution map

Each checklist bullet is a local step in order. From `projects/booking/`, use
README Block 1 for A1, Block 2 for A2, and Block 3 for A3. For A4 run
`uv run --locked ruff check . && uv run --locked mypy && uv run --locked pytest`
with the documented database variable. Record under matching A headings; recover
with the bounded reset and rerun `tests/test_postgres.py`.

## Stretch

Compare optimistic and pessimistic strategies with the same harness, or model atomic multi-resource booking with a proved lock order.

## Review

### Review

Answer one question at a time in `evidence/M8/index.md`:

1. What is the exact naive two-request interleaving?
2. Which database mechanism protects the invariant?
3. Which isolation assumption does that choice require?
4. Why is coordinated concurrency stronger evidence than merely fast traffic?
5. What does optimistic control trade for retries?
6. What does pessimistic control trade for waiting and deadlocks?
7. Who wins at the exact expiry boundary?
8. Which layer owns bounded retry?
9. Does the test query final database truth after counting responses?
10. What contention limit did you measure?

Draw one failed and one corrected timeline from evidence.
