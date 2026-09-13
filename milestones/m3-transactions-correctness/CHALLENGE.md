# M3 challenge brief

Run from `projects/pos/`. Each scenario owns its test, hints, evidence, and reset.

## **C1 — Partial checkout incident**

**YOU BUILD** — add deterministic kill hooks at the published transaction boundaries.

### Steps

1. Create `tests/m3/test_atomic_checkout.py` with happy-path and rollback cases.
2. Fail after payment insert and after receipt creation but before stock movement.
3. Run README Block 1 and prove each failure leaves no partial business fact.

### Hints

1. Query every affected table before and after the failure.
2. Inspect the use-case transaction owner and every flush or commit.
3. Use the SQLAlchemy transaction link in `RESOURCES.md`.

### Reset

Disable the kill hook and run `uv run --locked pytest tests/m3/test_atomic_checkout.py -q`.

## **C2 — Invariant bypass and race**

**YOU BUILD** — coordinate two independent database connections with a barrier.

### Steps

1. Create `tests/m3/test_final_unit_race.py` and reproduce check-then-write oversell.
2. Attempt duplicate completion, over-refund, forbidden transition, and direct-SQL invalid state.
3. Place each invariant deliberately, rerun Block 3, and record winners and final rows.

### Hints

1. Write the interleaving and final invariant before selecting a lock.
2. Inspect constraints, isolation, lock target, and retry boundary.
3. Use the PostgreSQL isolation link in `RESOURCES.md`.

### Reset

Use the POS bounded reset, migrate to head, and rerun the coordinated test; do
not replace the barrier with sleeps. The focused rerun is
`uv run --locked pytest tests/m3/test_final_unit_race.py -q`.

## **C3 — Historical arithmetic**

**PROVIDED** — money examples and expected totals are fixed in the contract.

### Steps

1. Create `tests/m3/test_money_and_repeats.py` from the decimal examples.
2. Change current product price after sale and exercise rounding, void, and refund.
3. Run README Block 2 and prove receipt history does not change.

### Hints

1. Print named intermediate decimal amounts.
2. Inspect calculation order, receipt snapshots, and allowed transitions.
3. Use the Python decimal and state-machine links in `RESOURCES.md`.

### Reset

Restore fixed synthetic prices and run
`uv run --locked pytest tests/m3/test_money_and_repeats.py -q`.

Ship an invariant map, exact money examples, and rollback evidence.
