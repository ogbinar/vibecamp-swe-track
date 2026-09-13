# Problems and mental models

Clients fail when servers treat HTTP as function calls. Define resource identity, methods, safe/idempotent meaning, status codes, headers/media types, error envelopes, full versus partial update, and compatibility before route volume. Pagination needs deterministic order, bounded limits, and defined empty/end behavior.

Pydantic typing/validation protects transport shape; product invariants still deserve named logic. Decimal-safe money is a product contract. Tests have distinct jobs: unit tests isolate rules, API tests prove serialization/routing/errors, and contract/OpenAPI checks detect consumer-visible drift.

Production-minded means predictable boundary behavior under malformed input and repeat calls. It does not imply durable storage, hardened security, deployment, recovery, or operational SLOs.
