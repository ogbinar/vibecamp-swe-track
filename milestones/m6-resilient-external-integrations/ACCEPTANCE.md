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

## Review

### Review

Answer one question at a time in `evidence/M6/index.md`:

1. Why does a timeout create an unknown outcome?
2. Which failures are retryable, and which are not?
3. How does backoff change load on a struggling provider?
4. Where is the semantic idempotency key created and stored?
5. Why is the webhook signature checked against raw bytes?
6. How do duplicate and out-of-order events converge?
7. Can nested retries exceed the total budget?
8. Does any log expose payment or signature data?
9. Which accepted post-response action can be lost, and is that acceptable?
10. Can you reconstruct C3 only from evidence, and what was the earliest signal?
11. Why can database rollback not undo a provider payment or refund?
12. Which facts would a separately authorized sandbox prove that the fake cannot?

Trace one provider field through request, provider, webhook, idempotency record, and logs using the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md). Lens prompt (same A1–A4 gate): a career-shifter states incident impact for a nontechnical stakeholder; a data specialist explains why payload persistence and reconciliation are application/security responsibilities, not merely ingestion.
