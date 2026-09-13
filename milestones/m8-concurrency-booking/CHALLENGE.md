# M8 challenge brief

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
3. Use the PostgreSQL concurrency link in `RESOURCES.md`.

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
3. Use the PostgreSQL locking link in `RESOURCES.md`.

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
3. Use the deadlock link in `RESOURCES.md`.

### Reset

End both test transactions, run the bounded reset, and run
`uv run --locked pytest tests/m8/test_time_and_deadlock.py -q`.

Ship honest conflict/retry semantics and scaling limits.
