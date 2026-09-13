# Learner glossary

Use this as a quick reference, not a reading assignment. Milestones introduce
each term through a concrete problem before expecting you to use it.

- **ACID:** atomicity, consistency, isolation, and durability—the properties
  used to reason about database transactions.
- **Adapter:** code that translates between the application and an external
  interface, such as HTTP or a payment provider.
- **ADR (architecture decision record):** a short record for a consequential,
  hard-to-reverse design decision; not a diary for routine choices.
- **Atomic:** all effects happen as one unit, or none become visible.
- **Backoff:** waiting longer between bounded retry attempts so a struggling
  dependency has time to recover.

- **Acceptance criterion:** an observable condition that must be true before
  work is considered complete. This course labels them `A1`, `A2`, and so on.
- **Application programming interface (API):** a defined way for software to
  communicate. Here, clients send HTTP requests to a FastAPI application.
- **ASGI server:** the running process that receives network traffic and passes
  it to a Python web application. This course uses Uvicorn through FastAPI.
- **Challenge:** a build, failure, diagnosis, or recovery exercise. This course
  labels challenge scenarios `C1`, `C2`, and so on.
- **Branch:** a movable Git name for a line of work, such as
  `m2/persistence`. It lets a change be reviewed before reaching `main`.
- **Commit:** a named Git snapshot with its parent and author information.
- **Correlation ID:** an identifier carried across logs and calls so one
  operation can be reconstructed.
- **CI (continuous integration):** automated checks run for a proposed change.
  Passing CI means the checks passed; it does not mean the product was deployed.
- **Cold review:** reproducing work from a clean checkout using only repository
  instructions, without relying on the author's memory.
- **Configuration:** values that change how an application runs without changing
  its code, such as a service name or database address.
- **Core:** work that must pass before advancing. **Stretch** work is optional.
- **Dependency:** software the project relies on, such as FastAPI or pytest.
- **Dependency injection:** giving code the collaborator it needs instead of
  constructing a hidden global collaborator inside it.
- **Endpoint (or route):** an HTTP method and URL path handled by the API, such
  as `GET /health`.
- **Environment variable:** a named value supplied by the operating environment.
  Secrets and deployment-specific settings usually enter this way.
- **Evidence:** a reproducible result supporting a claim—such as a test, HTTP
  response, query plan, or recovery transcript—not merely a screenshot.
- **Health/liveness check:** a small endpoint showing that the application
  process is alive. It does not prove every dependency is ready.
- **HTTP request:** a client's message containing a method, path, headers, and
  sometimes a body. An **HTTP response** returns a status, headers, and body.
- **HTTP contract:** the public agreement formed by request methods, paths,
  headers, bodies, response status codes, and response shapes.
- **HTTP semantics:** the standard meaning of methods and status codes—for
  example, whether a request only reads data or may change it.
- **Invariant:** a fact that must remain true, such as stock never falling below zero.
- **Isolation level:** database rules controlling what concurrent transactions
  can observe about one another.
- **HTTP safe method:** an HTTP method intended only to read information, not
  request a state change. `GET` is safe. “Safe” here does not mean risk-free.
- **Idempotent operation:** an operation that can be repeated with the same
  intended final effect as doing it once. It may still change state on the first
  attempt. This matters for retries, payments, webhooks, and background jobs.
- **JWT (JSON Web Token):** a signed claims format; signing does not encrypt its contents.
- **Lease:** a time-bounded worker claim another worker may recover after expiry.
- **Linting:** automated checks for suspicious or inconsistent source code.
  Ruff performs linting and formatting in this course.
- **Lockfile:** a generated record of exact dependency versions. `uv.lock`
  allows another machine to install the same resolved versions.
- **Milestone:** a capability gate, not a calendar week. `M0` is the first
  milestone and `M10` is the capstone.
- **OpenAPI:** a machine-readable description of an HTTP API. FastAPI generates
  one, but examples and tests must still prove the intended behavior.
- **Outbox:** durable work intent stored in the same transaction as the business change.
- **Percentile:** a boundary met by a stated share of observations. A p95 latency
  of 200 ms means 95% of measured requests completed in 200 ms or less.
- **Pagination:** returning a large collection in bounded, predictably ordered
  pages rather than one unbounded response.
- **Regression:** previously correct behavior that a later change breaks. A
  regression test keeps the defect from silently returning.
- **Pull request (PR):** a GitHub proposal to merge one branch into another. A
  working PR gets early feedback; a milestone-gate PR proves completion.
- **Remote:** a short Git name for another repository. `origin` is the learner's
  owned repository; optional `upstream` is the original curriculum source.
- **Schema:** a defined data shape and its validation rules. Pydantic models
  describe request and response schemas; databases also have schemas.
- **Product invariant:** a rule that must remain true for the product, such as
  “price cannot be negative,” regardless of which request or job changes data.
- **N+1 query:** one query for a collection followed by one extra query per item.
- **Poison work:** repeatedly failing input isolated so it cannot block healthy work.
- **Architecture port:** the small interface the application expects an adapter
  to satisfy, such as a payment-provider interface.
- **Network port:** a numbered network entry point, such as `8000` for a local
  API. It is unrelated to an architecture port.
- **RBAC (role-based access control):** permission decisions based on assigned roles.
- **Reconciliation:** comparing local and external facts to resolve an uncertain outcome.
- **Repository (architecture):** code that owns repeated or complex persistence
  operations. It does not automatically own business rules or commits.
- **RPO (recovery point objective):** the maximum acceptable amount of data loss,
  measured as time.
- **RTO (recovery time objective):** the target time to restore an acceptable service.
- **Service or use case:** code that owns orchestration and business transaction
  intent when a route would otherwise coordinate several collaborators.
- **Seeded fault:** a deliberate, safe defect used to practice diagnosis.
- **Static type checking:** checking type annotations without running the normal
  program. This course uses mypy; Ruff has a different job.
- **SLO (service-level objective):** a measurable reliability target for a user-visible service.
- **SSE (server-sent events):** a one-way HTTP stream from server to client.
- **Walking skeleton:** the smallest end-to-end version that starts, handles a
  real request, and can be tested. It proves the basic path before features grow.
- **Transaction:** a group of database changes that must either all succeed or
  all fail together.
- **Transport validation:** checking whether an incoming HTTP request has the
  required shape and types before product rules run.
- **Worker:** a process that claims and performs background work outside the API
  request that originally created the obligation.
