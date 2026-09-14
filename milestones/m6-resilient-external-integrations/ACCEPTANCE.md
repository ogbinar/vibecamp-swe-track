# Acceptance gate

Required maturity: **Level B plus contextual Level C reliability/diagnostics**.

## Core

- **A1:**
  - [ ] the immediate-payment port uses `pay`, `refund`, and `lookup` consistently; success, decline, connect/read/total/before-processing timeout, post-processing unknown, and refund success/failure/unknown are deterministic
  - [ ] SDK and application retries share one maximum-three-attempt/five-second budget, and decline is never retried
  - [ ] C1 tests distinguish connect, read, and total timeouts.
  - [ ] Retry tests cover classification, exponential backoff with jitter, and maximum attempts/elapsed budget.
  - [ ] `Retry-After` is honored within the budget.
  - [ ] Unknown outcomes never create a duplicate semantic effect.
- **A2:**
  - [ ] C2 validates raw-body signature, timestamp, and account before side effects.
  - [ ] Replay is rejected and event identity is durable.
  - [ ] Duplicate delivery is idempotent and out-of-order delivery preserves state-machine truth.
- **A3:**
  - [ ] Client/API idempotency records bind key to operation/payload
  - [ ] structured redacted logs correlate request, attempts, webhook, and reconciliation
  - [ ] C3 postmortem links a regression test and recovery evidence.
- **A4:**
  - [ ] Degraded and unknown states remain visible until reconciliation converges them.
  - [ ] A [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) traces provider payload/identifier copies, logs, and replay records.
  - [ ] The review covers retention, deletion, and access.
  - [ ] integration/unit/API/migration/lint/validator commands pass cleanly.

Local A1–A4 finish offline. The separately authorized Stripe-like sandbox is a
required experiment only for the real-provider evidence claim. If access is
missing or the provider is unavailable, record `PENDING — ACCESS/PROVIDER
OUTAGE`; do not replace it with fake evidence or block independent local work.

## Execution map

Each checklist bullet is a local step in order. From `projects/ecommerce/`, use
README Block 1 for A1, Block 2 for A2, and Block 3 for A3–A4. Also run
`test -s evidence/M6/data-lifecycle.md` for the lifecycle step. Expected:
uncertain outcomes remain explicit and repeated delivery converges. Record under
matching A headings; reset the deterministic fake and rerun one focused test.

## Stretch

Add a circuit breaker only after quantified cascading harm and test half-open/recovery semantics; compare a second provider only from a real continuity requirement.
