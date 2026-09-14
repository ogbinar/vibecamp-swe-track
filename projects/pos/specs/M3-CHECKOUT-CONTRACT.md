# M3 checkout and correctness contract

`POST /checkouts` accepts a cart identifier, local payment-intent reference, and
idempotency key. On success it returns 201 with local sale, payment-intent,
inventory, and receipt facts.
Unknown cart is 404; empty/already-checked-out cart is 409; insufficient stock
is 409. The same key and request returns the same sale; the same key with a
different request is 409.

State rules:

- a cart is open or checked out;
- a sale is pending, completed, voided, or refunded;
- inventory never becomes negative;
- payment success without a committed sale becomes an explicit unknown outcome,
  never an invented failure;
- a receipt exists exactly once for a completed sale.

M3 deliberately has no remote money call. Its database transaction can roll
back only local facts. When M6 adds a provider, a timeout-after-effect becomes
unknown and must be resolved by durable idempotency, provider lookup, and
reconciliation; database rollback cannot undo provider money.

Money uses `Decimal`: line subtotal is quantity × unit price; a fixed 10%
discount applies only when subtotal is at least 100.00; tax is 12% after
discount. Round each final line tax to two decimals using `ROUND_HALF_UP`, then
sum. Example: 3 × 33.33 = 99.99, no discount, tax 12.00, total 111.99.

Void is allowed only before settlement and restores stock once. Refund is
allowed only after completion, never exceeds paid amount, and records each
attempt. Build a two-connection final-unit harness with a barrier before
commit; allowed outcome is exactly one completed sale and non-negative stock.
