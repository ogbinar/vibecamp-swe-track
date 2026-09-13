# Review

Explain why timeout is uncertainty, which errors are retryable, how backoff changes provider load, where idempotency identity lives, why signature verification uses raw bytes, and how reordered webhooks converge.

Self-review default client timeouts, retry multiplication, payload/key mismatch, sensitive logs, correlation gaps, swallowed failures, and optimistic success states. For every post-response action, state whether loss is acceptable; if not, show the persisted intent rather than `BackgroundTasks`. If files exist, defend direct object-storage transfer and its authorization/lifecycle—or explain why no object store was added. Reconstruct C3 using only evidence, then identify the earliest missed signal.

Trace one provider field through request, provider, webhook, idempotency record, and logs using the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md). Lens prompt (same A1–A4 gate): a career-shifter states incident impact for a nontechnical stakeholder; a data specialist explains why payload persistence and reconciliation are application/security responsibilities, not merely ingestion.
