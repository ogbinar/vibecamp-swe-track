# Tools earned here

- **HTTPX client with explicit limits:** controlled outbound timeouts and testable transport.
- **Small retry policy:** explicit classification/backoff/jitter/budget; avoid opaque retry-all decorators.
- **Provider fakes:** deterministically produce uncertain outcomes; do not mock internal business logic.
- **HMAC/signature library and constant-time comparison:** implement provider-specified verification with replay bounds.
- **Structured logging:** stable fields and correlation/request IDs, with redaction.

No circuit-breaker library, queue, broker, or fallback provider until measured need. Remove retries that amplify load or obscure terminal outcomes. Durable async work is earned in M7.
