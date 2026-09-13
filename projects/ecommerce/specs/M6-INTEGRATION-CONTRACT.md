# M6 payment integration contract

Define a `PaymentProvider` architecture port with authorize, capture, and lookup
operations. Each request carries merchant account, amount/currency, local
operation ID, and idempotency key. Normalize provider results to succeeded,
declined, or unknown; never map a timeout-after-effect to a definite failure.

The supplied fake must cover connect timeout, read timeout, total timeout,
timeout before effect, timeout after effect, rate limit with retry hint, server
error, decline, and malformed response. Retry only bounded transient operations:
maximum three attempts, exponential backoff with jitter, total budget five
seconds in the deterministic clock. A decline is not retried.

Webhook verification uses the exact raw body, signature, timestamp tolerance,
merchant account, and event identifier before parsing business data. Fixtures
include duplicate, delayed, out-of-order, expired, wrong-account, tampered, and
replayed events. Reconciliation input is a local unknown operation ID; output is
the provider fact plus the local transition taken. Invoke it through a named CLI
or admin command and preserve the transcript.
