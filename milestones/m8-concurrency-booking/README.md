# M8 — Stop the last seat being sold twice

[Course home](../../README.md) / M8

**Milestone 9 of 11 · M8**

## Business problem

Two requests see one remaining seat and both confirm it. Correct sequential code
is not necessarily correct when requests interleave.

## Product objective

- **Product can:** two buyers cannot both confirm the same final seat.
- **You will prove:** sequential behavior, concurrent reproduction, invariant, lock, deadlock, and contention evidence.

Use the [booking contract](../../projects/booking/specs/M8-BOOKING-CONTRACT.md).
Trace the supplied final-seat interleaving without repairing the in-memory
fixture. Rebuild the reservation invariant in PostgreSQL with holds,
confirmation, expiry, and cancellation. Compare conditional writes,
constraints, isolation, and locking; choose the smallest correct combination.
Complete C1–C3 in the [challenge brief](#challenge-brief), including deadlock and expiry races.

## Start here

- **Gate:** [A1–A4 / Level B](#core).
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/booking/README.md#booking-launch-kit-for-m8), then return to the saved block; first visit: [Block 1](#1-observe-and-rebuild-sequentially-required).

From `projects/booking/`, run its documented command block. Expected: the
ordinary test passes and the opt-in two-worker challenge fails deterministically.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Build

### 1. Observe and rebuild sequentially `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/booking/`;
focus on `tests/test_postgres.py` and the output named below. Record `evidence/M8/baseline.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 1](#1-observe-and-rebuild-sequentially-required) using that saved result; continue to Block 2.
When needed: [C1 scenario and hints](#c1--final-seat-race) and [concept explanation](#two-people-booked-one-seat). [Tool boundaries](#tools-earned-here) apply to this product.

Run the in-memory race exactly as documented, record its interleaving, and do
not repair it. Then read the [booking contract](../../projects/booking/specs/M8-BOOKING-CONTRACT.md),
create learner tables/routes at the supplied seams, and prove the sequential
API path. Record `evidence/M8/baseline.md`. Stop when ordinary PostgreSQL tests
are green and the toy race remains reproducible.

### 2. Protect the final unit `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/booking/`;
focus on `tests/m8/test_final_unit.py` and the output named below. Record `evidence/M8/final-unit.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 2](#2-protect-the-final-unit-required) using that saved result; continue to Block 3.
When needed: [C2 scenario and hints](#c2--database-enforced-fix) and [concept explanation](#which-concurrency-tool-should-i-choose).

Extend the two-independent-connection seam with a barrier. Observe overselling,
choose the smallest constraint/atomic-write/lock strategy, and rerun. Record
winner count, final SQL invariant, responses, and retry rule in
`evidence/M8/final-unit.md`. Reset with the booking script; stop at exactly one
winner and no negative capacity.

### 3. Exercise time and contention `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/booking/`;
focus on `tests/m8/test_time_and_deadlock.py` and the output named below. Record `evidence/M8/time-and-locks.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 3](#3-exercise-time-and-contention-required) using that saved result; continue to [Prove it](#prove-it).
When needed: [C3 scenario and hints](#c3--time-and-lock-incident) and [concept explanation](#expiry-and-confirmation-happened-together).

Race confirm/expire and cancel/confirm at the published boundary. Reproduce one
deadlock with inconsistent order, then establish consistent order and bounded
retry. Record waits, attempts, allowed outcomes, and recovery in
`evidence/M8/time-and-locks.md`. Stop when all outcomes are deterministic.

### Diagnose deliberate failures

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Understand

- **Race condition:** correctness depends on request timing.
- **Interleaving:** the order in which steps from concurrent requests occur.
- **Isolation:** how much one transaction can observe another's work.
- **Lock:** controlled exclusive access to a database resource.
- **Contention:** requests waiting or conflicting over the same resource.
- **Deadlock:** transactions wait on one another until the database aborts one.

## Use a tool if earned

Use the current project dependencies first. Open [Use now](#use-now) for the active pattern, [Evaluate after evidence](#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](#review) after the Core proof.

Prove [A1–A4](#core) with a deterministic harness, before/after failure
counts, invariant query, conflict API, contention observation, and retry policy.

## Done / next

The final-seat and lifecycle races have exact allowed outcomes, never violate
the database invariant, and all Core checks pass. Tag `m8-concurrency-booking`.

### Recovery

Use [targeted references](#resources-for-m8) only for the question left by the active hint ladder.

If the race becomes intermittent, return to the supplied two-worker barrier.
Before the PostgreSQL bridge exists, rerunning the test resets its fresh
in-memory state. After the bridge is added, use only the booking launch kit's
named course-database reset command.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M9](../m9-performance-caching-realtime-social/README.md).

[Previous milestone: M7](../m7-durable-async-background-processing/README.md) · [Course home](../../README.md) · [Next milestone: M9](../m9-performance-caching-realtime-social/README.md)


---

## Challenge brief

Run from `projects/booking/`. Use barriers, not sleeps, for correctness proof.

## **C1 — Final-seat race**

**PROVIDED** — run the in-memory barrier, then reproduce it on PostgreSQL.

### Steps

1. Record the supplied two-request interleaving without repairing it.
2. Create `tests/m8/test_sequential_booking.py` and then coordinate two database connections.
3. Preserve the oversell as an isolated reproduction and run README Block 1.

### Hints

1. Write both reads and writes in their observed order.
2. Inspect the supplied barrier and `run_on_two_connections_at_barrier` seam.
3. Use the PostgreSQL concurrency link in the Reference section below.

### Reset

Rerun the in-memory test for fresh state; for PostgreSQL use the bounded booking
reset and rerun `tests/test_postgres.py`.

## **C2 — Database-enforced fix**

**YOU BUILD** — choose the smallest database enforcement strategy.

### Steps

1. Create `tests/m8/test_final_unit.py` from the fixed final-unit outcome.
2. Compare constraint, atomic update, optimistic, and pessimistic options against the invariant.
3. Race repeatedly across connections; run README Block 2 and record winners.

### Hints

1. Query the final invariant rather than trusting response order.
2. Inspect constraint shape, write predicate, lock target, isolation, and retry boundary.
3. Use the PostgreSQL locking link in the Reference section below.

### Reset

Run the bounded reset, migrate to head, and rerun
`uv run --locked pytest tests/m8/test_final_unit.py -q`.

## **C3 — Time and lock incident**

**YOU BUILD** — inject boundary time and controlled lock order.

### Steps

1. Create `tests/m8/test_time_and_deadlock.py` for confirm/expire and cancel/confirm.
2. Reproduce inconsistent lock order and record the database-selected victim.
3. Establish consistent order and bounded retry; run README Block 3.

### Hints

1. State the exact boundary instant and allowed winners.
2. Inspect database time, lock acquisition order, wait, and retryable error code.
3. Use the deadlock link in the Reference section below.

### Reset

End both test transactions, run the bounded reset, and run
`uv run --locked pytest tests/m8/test_time_and_deadlock.py -q`.

Ship honest conflict/retry semantics and scaling limits.


---

## Acceptance gate

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


---

## Reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M8 concepts through booking races

## “Two people booked one seat”

**Example:** both transactions read capacity before either writes. **Term —
interleaving:** the order in which concurrent steps occur. **Rule:** enforce the
capacity invariant in PostgreSQL, across processes—not with a Python lock.

## “Both transactions waited forever”

**Example:** each holds one lock and waits for the other. **Term — deadlock:** a
wait cycle the database must break. **Rule:** keep lock order consistent and
retry only the bounded retryable outcome.

## “A stress test passed but never hit the dangerous timing”

**Example:** requests run quickly but never both read the final seat first. **Term —
time-of-check/time-of-use gap:** truth changes between a check and its write.
**Rule:** coordinate the exact interleaving with barriers; speed is not proof.

## “Which concurrency tool should I choose?”

**Example:** a conditional update can enforce capacity without a broad lock.
**Term — optimistic control:** detect conflict and retry instead of waiting first.
**Rule:** compare atomic writes, constraints, locks, isolation, and versions against
the invariant, contention, deadlock, and retry behavior.

## “Expiry and confirmation happened together”

**Example:** app clocks disagree at the hold boundary. **Term — authoritative
time:** the one clock used for the business decision. **Rule:** use database time,
declare allowed winners, keep lock order consistent, and bound retryable failures.

### Tools earned here

- **PostgreSQL constraints, isolation, row/advisory locks, atomic SQL:** cross-process correctness mechanisms chosen per invariant.
- **Barrier-controlled asyncio/thread/process harness:** deterministic interleavings plus repeated stress.
- **Database lock/activity views and time:** diagnose waits/deadlocks and make expiry policy explicit.
- **pytest + HTTPX:** assert both internal invariant and client conflict contract.

No Redis/distributed lock or availability microservice. Avoid raising isolation globally without measurement. Remove application locks that create false single-process confidence.

## Evaluate after evidence

Evaluate optional tools only after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M8

Use these after the supplied barrier reproduces the final-seat race. Reviewed 2026-09-13.

- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — Why can two individually valid requests conflict? Applicable tool: current PostgreSQL.
- [PostgreSQL explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html) — Which row, table, or advisory lock matches the protected resource? Applicable tool: current PostgreSQL.
- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) — Can the database reject the invalid final state regardless of writer? Applicable tool: current PostgreSQL.

Choose from measured interleavings; do not reach for a distributed lock by default.
