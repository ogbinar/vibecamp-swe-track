# M3 — Transactions & Correctness

**Capability:** protect money, inventory, and sale state through atomic operations and enforceable invariants. **Deliverable:** extend the POS with checkout, payment records, immutable receipt snapshots, stock movements, void/refund rules, and an explicit sale state machine.

Prerequisite: M2 schema/migration competence. Sequence: write invariants → design transaction boundary → build checkout → failure-inject partial writes → test database bypass/races → debug/refactor → inspect recovery state → ship `m3-transactions-correctness`.

Outputs include invariant and transition tables, calculation policy, transaction-focused service code, database/application enforcement, and unit/integration/API evidence.
