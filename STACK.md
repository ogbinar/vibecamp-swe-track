# Stack policy

## Minimal default

- One supported Python version, pinned in `.python-version`, `pyproject.toml`, and the uv lockfile
- `fastapi[standard]` (FastAPI, its CLI, and Uvicorn), Pydantic, and `pydantic-settings`
- PostgreSQL, Psycopg 3, explicit SQL, SQLAlchemy 2, and Alembic
- pytest, HTTPX, Ruff, and mypy
- uv, Git, GitHub, and GitHub Actions
- Docker for the immutable runtime artifact; Docker Compose for local, test/CI, and deliberately bounded single-host environments

Use synchronous SQLAlchemy sessions with Psycopg first. FastAPI's asynchronous transport does not itself prove that async database access is needed. Adopt `AsyncSession` only after a representative workload shows blocked capacity or latency that cannot be corrected more simply; record the comparison, added failure/debugging cost, pool behavior, and removal/revisit trigger.

Start with one modular monolith and one PostgreSQL database per project. Prefer FastAPI dependency functions and an explicit composition root over a DI framework. Route-to-SQLAlchemy is acceptable for a genuinely simple use case. Add a service when orchestration or business invariants need ownership; add a repository when query/data-access duplication or substitution creates a real seam. Do not require every endpoint to traverse ceremonial layers. The use-case/service boundary owns the transaction; repositories expose persistence operations and do not independently commit.

Ruff owns linting and formatting; mypy owns static type consistency across module boundaries. PostgreSQL-backed integration tests—not SQLite substitutes—prove constraints, migrations, locks, transaction behavior, and database-specific queries.

## Earned tools

| Tool | Earliest useful point | Evidence required | Remove/avoid when |
|---|---|---|---|
| FastCRUD | After M2 fundamentals | Handwritten SQL/repository behavior and constraints are understood; commodity admin CRUD is repetitive; comparison preserves contract, transaction ownership, query shape, and tests | Hooks obscure domain invariants or transactional workflows; a small explicit query is clearer |
| `fastapi-pagination` | After M1 contract | Ordering, cursor/limit, insertion-between-pages, and error semantics exist first and adapter tests preserve them | Library dictates the public contract or hides unstable ordering/query cost |
| Redis using the maintained Python client | M9 | A declared target is missed; cache-aside tests cover value, staleness, invalidation, stampede, outage, TTL, and user/tenant key scope | PostgreSQL meets target, Redis becomes correctness authority, or outage/stale-data cost exceeds benefit |
| Taskiq with an explicitly selected production broker/result policy | After M7 database-backed semantics | Broker acknowledgement/failure behavior is documented; atomic intent, at-least-once delivery, idempotency, replay, backpressure, and observability remain provable | The database queue meets need or broker operations add more failure modes than measured value |
| FastAPI `BackgroundTasks` | M6 at earliest | Work is short, noncritical, same-process, and explicitly safe to lose or repeat | The accepted obligation must survive crash/redeploy, needs retry/audit, or performs correctness-critical effects |
| SSE | M9 | Polling misses a stated one-way latency requirement; reconnect, gaps, slow consumers, and loss semantics are tested | Polling meets need or durable replay is falsely implied |
| WebSockets | M9 Stretch | A bidirectional low-latency requirement that SSE cannot meet; connection/auth/backpressure behavior is tested | Traffic is one-way or connection/protocol state cost is unjustified |
| S3-compatible object storage | M6 or later | Files must outlive/scale independently from application instances; access, retention, deletion, checksum, and failure behavior are defined | The product has no file requirement or local storage safely meets its bounded deployment; do not store blobs in PostgreSQL by reflex |
| OpenTelemetry | M10 | Portable traces/metrics answer a named diagnostic question; propagation, sampling, redaction, retention, backend, and cost are owned | A simpler signal answers the question or no one owns the telemetry pipeline |
| Logfire or Sentry | M10 | One managed backend answers a named error/performance question with acceptable data handling, retention, and cost | It duplicates another backend, leaks sensitive data, or produces unowned noise |
| PyJWT | M5 | Stateless signed claims are justified for the client/trust boundary; validation, expiry, rotation, refresh/revocation, and theft behavior are tested | A first-party secure cookie session is simpler or immediate revocation/session control dominates |
| `pwdlib[argon2]` | M5 | The product accepts passwords; input bounds, adaptive hash parameters, verification, upgrade, and recovery policy are tested | Authentication is delegated to an earned identity provider or the product accepts no passwords |

For one meaningful candidate by M4, preserve the decision to say “not yet” in the [complexity rejection record](templates/COMPLEXITY-REJECTION.md). Unlike an ADR, it records an option not adopted and a measurable revisit trigger. Revisit the record when evaluating Taskiq/Redis in M7/M9 or operational tooling in M10; rejection is provisional evidence, not ideology.

## Operational boundaries

CI grows with the risk being introduced: M0 adds locked lint/type/unit/API
checks; M2 adds PostgreSQL and migrations; M5 adds isolated security contract
collection and secret review; M7 adds worker/kill-point checks created by the
learner; M9 adds a deterministic performance guard; M10 builds the immutable
image. A later gate is not copied into an earlier milestone merely to look
“production ready.” Continuous deployment begins only at the M10 real-target
endorsement.

- **CI before CD:** GitHub Actions runs reproducible lint, type, test, migration, and build checks early. Automated deployment is earned only when a real target, immutable artifact, environment-scoped secrets, migration ordering, readiness gate, and rollback/roll-forward procedure exist.
- **Compose is bounded:** Compose may run a documented single-host deployment, but it does not supply TLS, secret custody, backup/restore, monitoring, safe migration rollout, or rollback by itself. M10 must prove those controls and state the deployment boundary honestly.
- **Durability begins with persisted intent:** an HTTP response or in-process callback is not a queue. Correctness-critical work is committed to PostgreSQL with its business state, then claimed by an idempotent worker. Taskiq is an optional transport/worker accelerator, not exactly-once semantics.
- **PostgreSQL owns durable truth:** Redis may cache or coordinate disposable state, but inventory, booking, payment, tenant, and audit truth remains in PostgreSQL.
- **Authentication follows the client boundary:** first-party browser products must compare a server-controlled secure `HttpOnly` cookie session with JWT. If JWT is chosen, use PyJWT with a fixed algorithm allowlist and validate issuer, audience, expiry/not-before, token type, rotation, and revocation assumptions. Password authentication uses `pwdlib[argon2]`; neither choice creates an OAuth authorization server.
- **Observability starts small:** begin with structured redacted logs and request/correlation IDs. Add metrics and traces for named questions. OpenTelemetry is instrumentation and still needs an owned backend; choose rather than stacking OpenTelemetry, Logfire, and Sentry indiscriminately.

## Explicit exclusions

Kubernetes, Kafka, microservices, service mesh, CQRS, event sourcing, Elasticsearch, complex dependency-injection frameworks, and multiple databases are outside the course. An exception needs an explicit product constraint and a real ADR covering simpler alternatives, failure modes, operations, rollback, and removal.
