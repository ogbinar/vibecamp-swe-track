# Tools earned here

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
