# M8 reference

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
