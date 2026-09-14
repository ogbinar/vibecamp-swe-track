# Resources for M6

Open these after observing timeout, duplicate, signature, or unknown-outcome behavior. Reviewed 2026-09-14.

- [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) — Which phase timed out and what limit should be bounded? Applicable tool: HTTPX 0.28+.
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) — What does a mature provider require for safe request replay? Applicable example: current Stripe API.
- [Stripe sandboxes](https://docs.stripe.com/sandboxes) — What separates test from live access, and how should a bounded test credential be handled? Applicable example: current Stripe API.
- [Stripe webhook signatures](https://docs.stripe.com/webhooks/signature) — What exact bytes and secret are authenticated? Applicable example: current Stripe API.
- [Stripe refunds](https://docs.stripe.com/refunds) — What provider facts and failure states must refund/lookup expose? Applicable example: current Stripe API.

Stripe is the reference protocol and sandbox example, not a required vendor for
local Core. A real sandbox call requires separate authority.
