# Resources for M6

Open these after observing timeout, duplicate, signature, or unknown-outcome behavior. Reviewed 2026-09-13.

- [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) — Which phase timed out and what limit should be bounded? Applicable tool: HTTPX 0.28+.
- [HTTPX exceptions](https://www.python-httpx.org/exceptions/) — Which failures are safe to classify or retry? Applicable tool: HTTPX 0.28+.
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) — What does a mature provider require for safe request replay? Applicable example: current Stripe API.
- [Stripe webhook signatures](https://docs.stripe.com/webhooks/signature) — What exact bytes and secret are authenticated? Applicable example: current Stripe API.

Stripe is an evidence-rich example, not a required payment vendor.
