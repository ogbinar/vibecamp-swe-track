# Stack policy

## Minimal default

- Python 3.13, pinned in `.python-version`, `pyproject.toml`, the type checker,
  container image, CI, and the uv lockfile
- Air `0.48.1` pinned exactly as the primary HTML/UI framework during its alpha
  period; `fastapi[standard]` keeps FastAPI, its CLI, and Uvicorn explicit as
  backend/API and ASGI runtime dependencies
- Pydantic and `pydantic-settings` for shared API, form, and configuration boundaries
- PostgreSQL, Psycopg 3, explicit SQL, SQLAlchemy 2, and Alembic
- pytest, HTTPX, Ruff, and mypy
- uv, Git, GitHub, and GitHub Actions
- Docker for the immutable runtime artifact; Docker Compose for local, test/CI, and deliberately bounded single-host environments

Use synchronous SQLAlchemy sessions with Psycopg first. Air/FastAPI's asynchronous
transport does not itself prove that async database access is needed. Adopt
`AsyncSession` only after a representative workload shows blocked capacity or
latency that cannot be corrected more simply; record the comparison, added
failure/debugging cost, pool behavior, and removal/revisit trigger.

Start with one modular monolith, one ASGI process, and one PostgreSQL database per
project. The composition root creates the existing FastAPI backend, wraps it
with `air.Air(fastapi_app=api)`, and includes an `AirRouter` for pages. Air owns
human-facing HTML routes under `/` and `/app/...`; FastAPI keeps existing JSON,
OpenAPI, `/health`, and `/ready` behavior. Page and API handlers call the same
use case or service directly—never each other over HTTP. Prefer explicit
dependencies over a DI framework. Route-to-SQLAlchemy is acceptable for a
genuinely simple use case. Add a service when orchestration or business
invariants need ownership, including when page/API duplication exposes that
need; add a repository when query/data-access duplication or substitution
creates a real seam. Do not require every endpoint to traverse ceremonial
layers. The use-case/service boundary owns the
transaction; repositories expose persistence operations and do not independently
commit.

Use Air Tags for pages and fragments. Keep the page router out of OpenAPI and
retain FastAPI response models for JSON routes. Use ordinary POST/redirect/render
forms before HTMX. When partial updates are earned, use explicit Air `hx_*`
attributes and focused fragment routes; the non-HTMX product behavior and
backend invariant must remain testable. Use `AirForm.from_request()` explicitly
for Pydantic-backed form validation while Air's dependency-injected form path is
not a stable course contract.

Ruff owns linting and formatting; mypy owns static type consistency across module boundaries. PostgreSQL-backed integration tests—not SQLite substitutes—prove constraints, migrations, locks, transaction behavior, and database-specific queries.

## Earned tools

Use this learning order: make the M0 product visible with an Air page while
FastAPI/Uvicorn/Pydantic/settings expose its backend and HTTP behavior; add an
ordinary Air form in M1; add `APIRouter`, `Depends`, and OpenAPI when route
composition or contract inspection creates the need; hand-build stable
ordering/cursors/errors before evaluating `fastapi-pagination`; write explicit
CRUD and transaction ownership before comparing FastCRUD; establish
authentication, authorization, sessions, and negative cases before framework
security helpers; earn HTMX in M6 from a payment-status partial-update need;
crash disposable `BackgroundTasks` work before building the M7 outbox/worker;
and measure before Redis, SSE, WebSockets, SQLAdmin, Sentry, or Logfire. Every
retained optional tool names its observed need, simpler baseline,
operational/data cost, owner, and removal trigger.

| Tool | Earliest useful point | Evidence required | Remove/avoid when |
|---|---|---|---|
| [Air Tags and `AirRouter`](https://docs.airwebframework.org/learn/quickstart/) | M0 | One human-facing catalog page makes the product behavior visible while existing FastAPI JSON/OpenAPI and health contracts remain green | The page duplicates business logic, pollutes OpenAPI, or creates a separate frontend/runtime |
| [Air forms / `AirForm.from_request()`](https://docs.airwebframework.org/learn/cookbook/forms/) | M1 | A browser user needs validated input; Pydantic-backed errors preserve entered values and the same use case serves page and API handlers | Form handling bypasses the API/domain contract or dependency-injected form behavior is used before it is stable |
| HTMX through Air `hx_*` attributes | M6 | A measured partial-update need such as uncertain payment status is awkward with full-page refresh; normal form behavior and backend tests already pass | Ordinary navigation is sufficient, fragments become a second business-logic path, or custom JavaScript grows without an earned need |
| FastCRUD | After M2 fundamentals | Handwritten SQL/repository behavior and constraints are understood; commodity admin CRUD is repetitive; comparison preserves contract, transaction ownership, query shape, and tests | Hooks obscure domain invariants or transactional workflows; a small explicit query is clearer |
| `fastapi-pagination` | After M1 contract | Ordering, cursor/limit, insertion-between-pages, and error semantics exist first and adapter tests preserve them | Library dictates the public contract or hides unstable ordering/query cost |
| Redis using the maintained Python client | M9 | A declared target is missed; cache-aside tests cover value, staleness, invalidation, stampede, outage, TTL, and user/tenant key scope | PostgreSQL meets target, Redis becomes correctness authority, or outage/stale-data cost exceeds benefit |
| Taskiq with an explicitly selected production broker/result policy | After M7 database-backed semantics | Broker acknowledgement/failure behavior is documented; atomic intent, at-least-once delivery, idempotency, replay, backpressure, and observability remain provable | The database queue meets need or broker operations add more failure modes than measured value |
| FastAPI `BackgroundTasks` | M6 at earliest | Work is short, noncritical, same-process, and explicitly safe to lose or repeat | The accepted obligation must survive crash/redeploy, needs retry/audit, or performs correctness-critical effects |
| Air `SSEResponse` with the HTMX SSE extension | M9 | Polling misses a stated one-way latency requirement; reconnect, gaps, slow consumers, and loss semantics are tested | Polling meets need or durable replay is falsely implied |
| WebSockets | M9 Stretch | A bidirectional low-latency requirement that SSE cannot meet; connection/auth/backpressure behavior is tested | Traffic is one-way or connection/protocol state cost is unjustified |
| S3-compatible object storage | M6 or later | Files must outlive/scale independently from application instances; access, retention, deletion, checksum, and failure behavior are defined | The product has no file requirement or local storage safely meets its bounded deployment; do not store blobs in PostgreSQL by reflex |
| OpenTelemetry | M10 | Portable traces/metrics answer a named diagnostic question; propagation, sampling, redaction, retention, backend, and cost are owned | A simpler signal answers the question or no one owns the telemetry pipeline |
| Logfire or Sentry | M10 | One managed backend answers a named error/performance question with acceptable data handling, retention, and cost | It duplicates another backend, leaks sensitive data, or produces unowned noise |
| PyJWT | M5 Stretch | Stateless signed claims are justified by a client other than the declared first-party browser; validation, expiry, rotation, refresh/revocation, and theft behavior are tested | The Core secure-cookie session is simpler or immediate revocation/session control dominates |
| SQLAdmin | M10 optional | Tenant authorization and append-only audit are already proven; every admin action retains tenant scope, authorization, and audit evidence | It creates a public/default admin surface or bypasses ordinary operator controls |
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
- **Authentication follows the client boundary:** M5 Core's first-party browser uses a server-controlled secure `HttpOnly` cookie session and compares it with JWT. PyJWT implementation is Stretch unless a different client earns it; then use a fixed algorithm allowlist and validate issuer, audience, expiry/not-before, token type, rotation, and revocation assumptions. Password authentication uses `pwdlib[argon2]`; neither choice creates an OAuth authorization server.

## Integration classification

- **Deterministic offline Core:** every M0–M10 milestone; CI requires no provider secret.
- **Required real-provider experiment:** exactly one separately authorized M6
  Stripe-like sandbox after local Core. Missing access/outage is recorded as
  pending and never replaced with simulation.
- **Optional endorsements:** M7 email; M10 S3-compatible storage, OAuth/OIDC,
  one of Sentry/Logfire, SQLAdmin, and an authorized deployment. Each defaults
  to do not add yet until need, owner, cost/data boundary, removal trigger,
  access, and authority are recorded.

Primary tool/provider references were rechecked on 2026-09-15. Air `0.48.1` is
the reviewed migration target, is still alpha, and requires Python 3.13 or
newer. Every checked-in starter now pins that exact Air release and Python 3.13;
UI registration stays isolated behind each project's `web.py` so an upgrade is
deliberate and reversible. Optional packages remain intentionally uninstalled.
- **Observability starts small:** begin with structured redacted logs and request/correlation IDs. Add metrics and traces for named questions. OpenTelemetry is instrumentation and still needs an owned backend; choose rather than stacking OpenTelemetry, Logfire, and Sentry indiscriminately.

## Explicit exclusions

Kubernetes, Kafka, microservices, service mesh, CQRS, event sourcing,
Elasticsearch, complex dependency-injection frameworks, multiple databases,
React or another SPA framework, a Node build toolchain, and a separate frontend
service are outside the course. AirDB, Jinja, AirDragon/Tailwind, or custom
JavaScript requires an observed product need that Air Tags, ordinary forms, and
small HTMX fragments cannot meet. An exception needs an explicit product
constraint and a real ADR covering simpler alternatives, failure modes,
operations, rollback, and removal.
