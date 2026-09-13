# M2 — POS Persistence / Data Modeling

**Capability:** make product state durable and relationally trustworthy. **Deliverable:** start `projects/pos/` with products, inventory locations, stock receipts, carts, and line items backed by PostgreSQL while preserving an explicit API contract.

Prerequisite: M1 boundary competence. Sequence: model queries/invariants → write SQL/schema → add repository/session boundaries → migrate empty and existing data → test constraints/query shape → break and recover a migration → containerize PostgreSQL → ship `m2-pos-persistence`.

Outputs: ER rationale, explicit SQL examples, SQLAlchemy mappings, Alembic history, indexes justified by query paths, repository boundary, database/API tests, and migration recovery evidence.
