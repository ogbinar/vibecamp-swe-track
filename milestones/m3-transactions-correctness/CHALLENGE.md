# Challenge brief

- **C1 — Partial checkout incident:** Seed failures after payment insert and after receipt creation but before stock movement. Trace the transaction, make all sale effects atomic, and prove recovery leaves no partial facts.
- **C2 — Invariant bypass and race:** Attempt oversell, duplicate completion, over-refund, forbidden transition, and direct SQL-invalid state. Coordinate two checkouts for scarce stock to expose the race; place each invariant deliberately in application/database/both.
- **C3 — Historical arithmetic:** Change product price after sale and seed tax/discount/rounding edge cases. Repair receipt snapshots and calculation order without rewriting history.

Refactor transaction ownership into a named use case only after failures reveal scattering. Operate by querying final ledgers/states. Ship an invariant map and rollback evidence.
