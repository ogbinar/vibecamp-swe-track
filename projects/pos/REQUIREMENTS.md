# M2 POS requirements brief

Build only the persistence slice needed to answer these questions:

- A product has a stable SKU, name, current price, and active state.
- A location receives stock. Each receipt records quantity, time, and source.
- A cart has ordered line items with positive quantities and captured unit prices.
- The system can report stock movements and current quantity per product/location.

Decide table keys, relationships, nullability, constraints, and indexes from the
named reads and writes. Do not implement checkout, payment, refunds, users,
workers, or caching in M2. Those belong to later failures.

Required example queries: find product by SKU; list a cart with lines; total
stock by location; list recent receipts. Required invalid cases: duplicate SKU,
orphan line, zero/negative quantity, and missing required price.

