# M6 concepts through provider failures

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
