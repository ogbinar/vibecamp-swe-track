# M6 payment integration contract

Define a `PaymentProvider` architecture port with immediate `pay`, `refund`, and
`lookup` operations. This models a confirmed Stripe-like PaymentIntent without
pretending M6 teaches a separate authorize/capture lifecycle. Each request carries merchant account, amount/currency, local
operation ID, and idempotency key. Normalize provider results to succeeded,
declined, or unknown; never map a timeout-after-effect to a definite failure.

The supplied fake must cover connect timeout, read timeout, total timeout,
timeout before effect, timeout after effect, rate limit with retry hint, server
error, decline, and malformed response. Retry only bounded transient operations:
maximum three attempts, exponential backoff with jitter, total budget five
seconds in the deterministic clock. SDK and application retries share that one
budget; nested defaults must not multiply attempts. A decline is not retried.

Refunds cover success, definite failure, and timeout after provider processing.
The last result remains unknown locally until `lookup` establishes the provider
fact. A database rollback cannot undo either payment or refund money; reconcile
forward from durable local intent.

Webhook verification uses the exact raw body, signature, timestamp tolerance,
merchant account, and event identifier before parsing business data. Fixtures
include duplicate, delayed, out-of-order, expired, wrong-account, tampered, and
replayed events. Reconciliation input is a local unknown operation ID; output is
the provider fact plus the local transition taken. Invoke it through a named CLI
or admin command and preserve the transcript.
