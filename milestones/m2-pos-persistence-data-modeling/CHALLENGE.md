# Challenge brief

- **C1 — Model from behavior:** Given cart/stock requirements and sample queries, design the relational model, write representative SQL, then attempt duplicate SKU, orphan lines, negative quantities, and bypassed API validation. Decide application versus database enforcement.
- **C2 — Slow/duplicated data access:** Seed duplicated SQL across endpoints, a missing index, and N+1 product loading. Observe query counts/plans, introduce the smallest repository boundary/index, and prove change without hiding SQL.
- **C3 — Failed migration incident:** Upgrade both empty and prior-revision databases. Seed incompatible rows and interrupt a backfill; diagnose state, recover without data loss, rerun safely, and document Docker volume persistence/reset semantics.

Refactor only after C2 evidence. Operate by inspecting connections, rollback state, and migration revision. Ship schema notes and upgrade evidence.
