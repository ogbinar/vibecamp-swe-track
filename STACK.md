# Stack policy

## Minimal default

- Python, FastAPI, Pydantic, and `pydantic-settings`
- PostgreSQL, explicit SQL, SQLAlchemy 2, and Alembic
- pytest, HTTPX, and Ruff
- uv, Git, GitHub, and GitHub Actions
- Docker and Docker Compose when persistence/deployment reproducibility becomes the problem

Start with one modular monolith and one PostgreSQL database per project. Prefer FastAPI dependency functions and an explicit composition root over a DI framework. Keep transport, product rules, and persistence responsibilities visible; do not manufacture generic layers before changes expose coupling.

## Earned tools

| Tool | Earliest useful point | Evidence required | Remove/avoid when |
|---|---|---|---|
| FastCRUD | After M2 fundamentals | Handwritten SQL/repository behavior and constraints are already understood; comparison shows reduced repetition without contract loss | Hooks obscure invariants, transactions, query shape, or testing |
| `fastapi-pagination` | After M1 contract | Existing ordering/cursor/limit semantics are preserved by adapter tests | Library dictates the public contract or hides unstable ordering |
| Redis | M9 | Measured miss of a declared target; cache-aside failure/invalidation tests; ownership plan | Database meets target, stale data risk is unacceptable, or outage worsens service |
| Taskiq or another queue library | After M7 database-backed semantics | At-least-once, idempotency, replay, and observability remain provable | Broker adds more failure modes than measured value |
| SSE | M9 | One-way update requirement and reconnect/loss semantics | Polling meets need or durable replay is falsely implied |
| WebSockets | M9 Stretch | Bidirectional low-latency requirement that SSE cannot meet | Traffic is one-way or connection state cost is unjustified |
| OpenTelemetry/Logfire/Sentry | M10 | A concrete diagnostic question, data policy, cost/retention plan | No one owns signals or sensitive data cannot be controlled |

For one meaningful candidate by M4, preserve the decision to say “not yet” in the [complexity rejection record](templates/COMPLEXITY-REJECTION.md). Unlike an ADR, it records an option not adopted and a measurable revisit trigger. Revisit the record when evaluating Taskiq/Redis in M7/M9 or operational tooling in M10; rejection is provisional evidence, not ideology.

## Explicit exclusions

Kubernetes, Kafka, microservices, service mesh, CQRS, event sourcing, Elasticsearch, complex dependency-injection frameworks, and multiple databases are outside the course. An exception needs an explicit product constraint and a real ADR covering simpler alternatives, failure modes, operations, rollback, and removal.
