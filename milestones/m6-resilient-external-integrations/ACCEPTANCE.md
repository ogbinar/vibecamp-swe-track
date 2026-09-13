# Acceptance gate

Required maturity: **Level B plus contextual Level C reliability/diagnostics**.

## Core

- **A1:** C1 tests prove connect/read/total timeouts, retry classification, exponential backoff+jitter, maximum attempts/elapsed budget, `Retry-After` handling, and no duplicate semantic effect after unknown outcome.
- **A2:** C2 proves raw-body signature/timestamp/account validation, replay rejection, durable event identity, idempotent duplicate handling, and safe out-of-order state-machine behavior.
- **A3:** Client/API idempotency records bind key to operation/payload; structured redacted logs correlate request, attempts, webhook, and reconciliation; C3 postmortem links a regression test and recovery evidence.
- **A4:** Degraded/unknown states remain visible, reconciliation converges them, and a [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) traces provider payload/identifier copies, logs, replay records, retention/deletion, and access; integration/unit/API/migration/lint/validator commands pass cleanly.

## Stretch

Add a circuit breaker only after quantified cascading harm and test half-open/recovery semantics; compare a second provider only from a real continuity requirement.
