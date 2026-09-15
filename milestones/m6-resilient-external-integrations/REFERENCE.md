# M6 reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M6 concepts through provider failures

## “The request timed out after the payment”

**Example:** the provider completed work but its response never arrived. **Term —
unknown outcome:** neither success nor failure is yet proven. **Rule:** preserve
that state and reconcile; do not blindly retry a money effect.

## “The webhook arrived twice and out of order”

**Example:** fulfilled arrives before paid, then paid repeats. **Term —
idempotent consumer:** repeated delivery converges to one intended effect.
**Rule:** verify raw signed input, identify the event, and apply declared state
rules.

## “Retries made the outage worse”

**Example:** every request retries immediately during a provider failure. **Term —
exponential backoff with jitter:** progressively longer, slightly randomized
delays. **Rule:** classify retryability and bound connect/read/overall time,
attempts, and total elapsed budget.

## “The webhook signature passed after parsing changed the bytes”

**Example:** normalized JSON differs from the signed request body. **Term — replay
window:** the allowed age of a signed event. **Rule:** verify raw bytes, timestamp,
event identity, and account before durable, idempotent handling.

## “Nobody could connect the request to the later webhook”

**Example:** logs omit the operation and correlation IDs. **Term — correlation
ID:** a safe identifier joining related work across boundaries. **Rule:** correlate
attempts and state changes, preserve uncertainty, redact data, and review incidents
through impact, timeline, recovery, and prevention rather than blame.

## “The database rolled back but the provider did not”

**Example:** the provider completed a payment or refund before the local
transaction failed. **Term — reconciliation:** compare durable local intent with
provider fact using the operation/idempotency key. **Rule:** a database rollback
cannot reverse external money; block unsafe repetition, look up, and reconcile
forward.

### Tools earned here

- **HTTPX client with explicit limits:** controlled outbound timeouts and testable transport.
- **Small retry policy:** explicit classification/backoff/jitter/budget; avoid opaque retry-all decorators.
- **Provider fakes:** deterministically produce uncertain outcomes; do not mock internal business logic.
- **Direct HTTP or one provider SDK (sandbox only):** evaluate after local Core; either adapter must preserve `pay`/`refund`/`lookup`, the combined retry/deadline budget, business idempotency, and reconciliation. Remove it if it obscures those facts.
- **HMAC/signature library and constant-time comparison:** implement provider-specified verification with replay bounds.
- **Structured logging:** stable fields and correlation/request IDs, with redaction.

FastAPI `BackgroundTasks` is allowed only for short, noncritical, same-process work whose loss or repetition is explicitly acceptable. It may not carry an accepted payment, fulfillment, webhook, or reconciliation obligation. Persist durable intent and defer its worker semantics to M7.

S3-compatible object storage is earned only if the integration introduces files that must outlive application instances. Prefer direct presigned transfer; define authorization, checksums, size/type limits, retention/deletion, orphan cleanup, and provider failure behavior. Do not proxy large media through FastAPI or add object storage for JSON records.

No circuit-breaker library, queue, broker, fallback provider, or object store without its trigger. Remove retries that amplify load or obscure terminal outcomes. Durable async work is earned in M7.

The sandbox is not a CI dependency. Keys remain test-only, least-privilege,
environment-isolated, redacted, and separately authorized; no key belongs in
Git, evidence, URLs, logs, fixtures, or workflow configuration.

## Evaluate after evidence

Evaluate only optional tools after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M6

Open these after observing timeout, duplicate, signature, or unknown-outcome behavior. Reviewed 2026-09-14.

- [HTTPX timeouts](https://www.python-httpx.org/advanced/timeouts/) — Which phase timed out and what limit should be bounded? Applicable tool: HTTPX 0.28+.
- [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) — What does a mature provider require for safe request replay? Applicable example: current Stripe API.
- [Stripe sandboxes](https://docs.stripe.com/sandboxes) — What separates test from live access, and how should a bounded test credential be handled? Applicable example: current Stripe API.
- [Stripe webhook signatures](https://docs.stripe.com/webhooks/signature) — What exact bytes and secret are authenticated? Applicable example: current Stripe API.
- [Stripe refunds](https://docs.stripe.com/refunds) — What provider facts and failure states must refund/lookup expose? Applicable example: current Stripe API.

Stripe is the reference protocol and sandbox example, not a required vendor for
local Core. A real sandbox call requires separate authority.
