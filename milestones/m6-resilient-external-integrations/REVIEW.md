# Review

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
