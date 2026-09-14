# M2 persistence contract

Route-to-SQLAlchemy is acceptable for a simple endpoint. Add a service only
when orchestration or invariants need one owner; add a repository only for
repeated/complex access or a real substitution seam. The request/use case owns
commit and rollback. Repositories expose persistence operations and never
commit independently.

Core uses these fixed examples; the learner owns table and repository design.

| Request | Success | Domain error |
|---|---|---|
| `POST /products` with SKU/name/price | 201 and stored product | duplicate SKU: 409 `product_exists` |
| `POST /locations` with code/name | 201 and stored location | duplicate code: 409 `location_exists` |
| `POST /stock-receipts` with SKU/location/quantity | 201 and new on-hand total | unknown reference: 404; quantity ≤ 0: 422 |
| `POST /carts` | 201 and empty cart | none |
| `POST /carts/{id}/lines` with SKU/quantity | 200 and complete cart | unknown SKU/cart: 404; quantity ≤ 0: 422 |
| `GET /inventory?sku=...&location=...` | 200 and exact total | unknown pair: 404 |

Responses use decimal money strings, never binary floats. Domain errors use
`{"error":{"code":"...","message":"..."}}`; transport-shape errors may use
FastAPI's standard 422 body.

Implementation seams to create: declarative `Base.metadata`, one learner
migration after `0001_baseline`, request-scoped session dependency, repositories
for repeated persistence, API tests, and PostgreSQL integration tests. A
repository owns queries; the service or use case owns transaction completion.

Use `fixtures/m2-legacy-products.sql` as the pre-migration checkpoint. Preserve
both rows, backfill the new required value explicitly, interrupt a disposable
migration once, and prove rerun/recovery from documented commands. Capture the
SQL statement count for cart loading so an N+1 regression is observable.
