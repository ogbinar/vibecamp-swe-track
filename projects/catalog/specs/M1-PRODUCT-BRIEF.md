# M1 product brief — catalog clients need a stable contract

## Users and decision owner

- A storefront client lists active products and opens one product by SKU.
- A staff client creates, replaces, and retires products.
- The product owner decides visible behavior; the learner chooses internal code.

## Required behavior

Product identity is a case-sensitive, non-empty `sku`. Money is a positive
two-decimal string. A product has `sku`, `name`, `price`, `active`, and optional
`retirement_reason` fields.

| Request | Required response |
|---|---|
| `POST /products` | `201`, product JSON, and `Location: /products/{sku}` |
| Repeat the same create | `409` with the error envelope |
| `GET /products/{sku}` | `200`, including retired products |
| Unknown SKU | `404` with code `product_not_found` |
| `PUT /products/{sku}` | Full replacement of name and price; `200` |
| Missing replacement field | `422`; existing product remains unchanged |
| `POST /products/{sku}/retire` | `200`; requires a non-empty reason |
| Repeat the same retirement | `200` with the same resulting representation |

Errors use one stable shape:

```json
{"error": {"code": "product_not_found", "message": "Product was not found"}}
```

Core domain errors are fixed:

| Situation | HTTP status | Code | Message |
|---|---:|---|---|
| SKU already exists | 409 | `product_exists` | `Product already exists` |
| Product is missing | 404 | `product_not_found` | `Product was not found` |
| Retirement reason is blank | 422 | `invalid_retirement_reason` | `Retirement reason is required` |

FastAPI request-shape validation may keep its standard HTTP 422 body. That
transport error is distinct from the domain-error envelope above.

List active products with `GET /products?limit=2&after=SKU`. Order by SKU.
`limit` is 1–100 and defaults to 20. `after` means strictly after that SKU.
Return `{"items": [...], "next": "LAST_RETURNED_SKU_OR_NULL"}`. An empty or
final page has `next: null`.

## Compatibility and non-goals

Existing M0 `/health` and `/products/sample` behavior remains unchanged. The
OpenAPI document is part of the public contract. M1 deliberately has no
database, authentication, cache, background worker, deployment, or claim that
memory survives a restart.

## Examples to prove

- Create `KB-1`, retrieve it, and compare the entire representation.
- Retrieve `MISSING` and compare the exact error body above.
- Replace `KB-1` without `price`; observe 422 and prove the old value remains.
- Retire `KB-1` twice with the same reason; both responses must be identical.
- Create `C`, `A`, and `B`; list two at a time and observe `A,B` then `C`.
- Activate the compatibility fault; the unchanged consumer contract must fail
  because application output changed, then pass after reset.
