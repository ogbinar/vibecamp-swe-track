# M8 — Booking Concurrency Lab

[Course home](../../README.md) / M8

**Milestone 9 of 11 · M8**

## Why

Two requests see one remaining seat and both confirm it. Correct sequential code
is not necessarily correct when requests interleave.

## Starting checkpoint

- **At a glance:** Concurrent · Booking.
- **You will leave with:** Final-seat race reproduction and repair; Time/contention evidence.
- **Gate:** [A1–A4 / Level B](ACCEPTANCE.md#core).
- **Repository support:** supplied starter locally verified; your learner gate needs your own evidence. [Dated scope and limits](../../USABILITY.md#readiness-status-vocabulary)
separate local structure/starter checks from pending hosted and human evidence.
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/booking/README.md#booking-launch-kit-for-m8), then return to the saved block; first visit: [Block 1](#1-observe-and-rebuild-sequentially-required).

From `projects/booking/`, run its documented command block. Expected: the
ordinary test passes and the opt-in two-worker challenge fails deterministically.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Terms used here

- **Race condition:** correctness depends on request timing.
- **Interleaving:** the order in which steps from concurrent requests occur.
- **Isolation:** how much one transaction can observe another's work.
- **Lock:** controlled exclusive access to a database resource.
- **Contention:** requests waiting or conflicting over the same resource.
- **Deadlock:** transactions wait on one another until the database aborts one.

## Product brief

Use the [booking contract](../../projects/booking/specs/M8-BOOKING-CONTRACT.md).
Trace the supplied final-seat interleaving without repairing the in-memory
fixture. Rebuild the reservation invariant in PostgreSQL with holds,
confirmation, expiry, and cancellation. Compare conditional writes,
constraints, isolation, and locking; choose the smallest correct combination.
Complete C1–C3 in [CHALLENGE.md](CHALLENGE.md#m8-challenge-brief), including deadlock and expiry races.

## Work blocks

Use the five visible cues in each block: **Do** is its start/work/command;
**Understand** is the exact concept or support link; **Check** is its expected
observation and evidence; **If it fails** is the named hint/reset/recovery; and
**Stop/resume** is its saved last-green boundary and return anchor. The compact
scope lines below state those facts in that order without replacing C/A IDs.

### 1. Observe and rebuild sequentially `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/booking/`;
focus on `tests/test_postgres.py` and the output named below. Record `evidence/M8/baseline.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 1](#1-observe-and-rebuild-sequentially-required) using that saved result; continue to Block 2.
When needed: [C1 scenario and hints](CHALLENGE.md#c1--final-seat-race) and [concept explanation](CONCEPTS.md#two-people-booked-one-seat). [Tool boundaries](TOOLS.md#tools-earned-here) apply to this product.

Run the in-memory race exactly as documented, record its interleaving, and do
not repair it. Then read the [booking contract](../../projects/booking/specs/M8-BOOKING-CONTRACT.md),
create learner tables/routes at the supplied seams, and prove the sequential
API path. Record `evidence/M8/baseline.md`. Stop when ordinary PostgreSQL tests
are green and the toy race remains reproducible.

### 2. Protect the final unit `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/booking/`;
focus on `tests/m8/test_final_unit.py` and the output named below. Record `evidence/M8/final-unit.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 2](#2-protect-the-final-unit-required) using that saved result; continue to Block 3.
When needed: [C2 scenario and hints](CHALLENGE.md#c2--database-enforced-fix) and [concept explanation](CONCEPTS.md#which-concurrency-tool-should-i-choose).

Extend the two-independent-connection seam with a barrier. Observe overselling,
choose the smallest constraint/atomic-write/lock strategy, and rerun. Record
winner count, final SQL invariant, responses, and retry rule in
`evidence/M8/final-unit.md`. Reset with the booking script; stop at exactly one
winner and no negative capacity.

### 3. Exercise time and contention `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/booking/`;
focus on `tests/m8/test_time_and_deadlock.py` and the output named below. Record `evidence/M8/time-and-locks.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 3](#3-exercise-time-and-contention-required) using that saved result; continue to [Evidence](#evidence).
When needed: [C3 scenario and hints](CHALLENGE.md#c3--time-and-lock-incident) and [concept explanation](CONCEPTS.md#expiry-and-confirmation-happened-together).

Race confirm/expire and cancel/confirm at the published boundary. Reproduce one
deadlock with inconsistent order, then establish consistent order and bounded
retry. Record waits, attempts, allowed outcomes, and recovery in
`evidence/M8/time-and-locks.md`. Stop when all outcomes are deterministic.

### Literal command map

Run from `projects/booking/`; create the M8 learner tests named below.

Before: create the learner database test and observe the coordinated race
violate capacity. File-not-found is setup feedback, not concurrency evidence.
After: the row’s stop condition is deterministic and recorded.

| Block | Copyable command | Expected stop condition |
|---|---|---|
| 1 | `BOOKING_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5434/vibecamp_booking uv run --locked pytest tests/test_postgres.py tests/m8/test_sequential_booking.py -q` | Sequential PostgreSQL behavior is green; separately preserve the supplied toy race as an expected failure. |
| 2 | `BOOKING_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5434/vibecamp_booking uv run --locked pytest tests/m8/test_final_unit.py -q` | Exactly one winner remains across the coordinated final-unit race. |
| 3 | `BOOKING_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5434/vibecamp_booking uv run --locked pytest tests/m8/test_time_and_deadlock.py -q` | Boundary-time outcomes, deadlock handling, and bounded retry match the contract. |

An absent learner target is the create-it signal. Recover with the booking
bounded reset and rerun `tests/test_postgres.py`; record the next race before pausing.

Pause: record both connection states, the barrier point, and next race.

## Failures and hints

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Evidence

Answer [review prompts](REVIEW.md#review) after the Core proof.

Prove [A1–A4](ACCEPTANCE.md#core) with a deterministic harness, before/after failure
counts, invariant query, conflict API, contention observation, and retry policy.

## Done when

The final-seat and lifecycle races have exact allowed outcomes, never violate
the database invariant, and all Core checks pass. Tag `m8-concurrency-booking`.

## Recovery

Use [targeted references](RESOURCES.md#resources-for-m8) only for the question left by the active hint ladder.

If the race becomes intermittent, return to the supplied two-worker barrier.
Before the PostgreSQL bridge exists, rerunning the test resets its fresh
in-memory state. After the bridge is added, use only the booking launch kit's
named course-database reset command.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

## Next

Continue to [M9](../m9-performance-caching-realtime-social/README.md).

[Previous milestone: M7](../m7-durable-async-background-processing/README.md) · [Course home](../../README.md) · [Next milestone: M9](../m9-performance-caching-realtime-social/README.md)
