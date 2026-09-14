# VibeCamp Software Engineering Track

> **“Practical engineering without compromise. Use the smallest tool that preserves correctness, security, maintainability, and operability. Add complexity only when the product earns it.”**

This is a self-paced course for learning how to build, test, break, repair,
deploy, and operate software. FastAPI is the vehicle; software engineering is
the subject.

You can begin if you know basic Python syntax, can use a terminal, and have seen
basic Git commands. You do not need production experience. Unfamiliar words are
defined when they first matter and collected in the [learner glossary](GLOSSARY.md).

You will evolve five familiar products: a catalog, point-of-sale system,
ecommerce application, booking system, and social platform. The final product
is a multi-tenant software-as-a-service candidate that another person could
realistically evaluate and operate.

## Start now

Supported learning environments are Linux, macOS, and Windows Subsystem for
Linux 2 (WSL2). Native Windows PowerShell commands have not been verified.

Before cloning, create a repository you can write to:

1. Sign in to GitHub and open the course repository.
2. Select **Use this template** → **Create a new repository**.
3. Leave **Include all branches** unchecked, choose your account, and create it.
4. Copy the clone URL shown for that new repository.

That repository will be your `origin`: the default remote you pull from and
push to. Install [Git](https://git-scm.com/downloads) and
[uv](https://docs.astral.sh/uv/getting-started/installation/) first. Then replace
`YOUR-REPOSITORY-URL` below with the URL you copied:

```bash
git clone YOUR-REPOSITORY-URL vibecamp-swe-track
cd vibecamp-swe-track
git remote -v
cd projects/catalog
cp .env.example .env
uv sync --locked
uv run --locked pytest
```

Expected result: `git remote -v` shows your repository as `origin`, then pytest
reports **four passing tests**. You now have a working
application and repeatable Python environment. If a command fails, use the
[starter troubleshooting guide](projects/catalog/README.md#if-setup-fails).

Next: follow the numbered lesson in
**[M0 — Engineering Baseline](milestones/m0-engineering-baseline/README.md)**.

Later product changes start from the runnable launch kits in
[`projects/`](projects/README.md). Do not set all five up now; open a project
only when its milestone tells you to.

## How the course works

A **milestone** is a capability you prove, not a calendar week. `M0` is the
first milestone; `M10` is the capstone. Every milestone follows this loop:

**Understand problem → Design smallest correct solution → Build → Test → Break deliberately → Debug → Refactor → Operate → Ship**

- A **challenge** such as `C1` gives you a problem or safe seeded fault.
- A **Core acceptance criterion** such as `A1` must pass before you advance.
- **Stretch** work is optional and never replaces Core work.
- Levels A, B, and C mean **Works**, **Engineered**, and **Production**. They are
  explained in the [quality gates](QUALITY-GATES.md).
- **Evidence** is a reproducible result supporting a claim: a test, HTTP
  response, migration transcript, or recovery record—not only a screenshot.
- A **cold review** repeats part of the work from a clean checkout without
  relying on the author's memory.

At the start of each milestone, create its evidence index in the active product
(replace `MN` with `M0`, `M1`, and so on). From the repository root, the example
below uses Catalog:

```bash
cd projects/catalog
mkdir -p "evidence/MN"
cp ../../templates/EVIDENCE-INDEX.md "evidence/MN/index.md"
```

Expected: `projects/catalog/evidence/MN/index.md` is one editable index for
commands, observations, decisions, and links. Later milestones use their named
project in the same way; do not create a competing root `evidence/` tree. Write
`N/A — condition not present` for a conditional gate that does not
apply. The [synthetic examples](templates/EVIDENCE-EXAMPLES.md) show useful
evidence without pretending to be learner results.

First get the supplied M0 starter green. Then the lesson introduces the
professional GitHub loop: issue → branch → pull request → automated checks →
evidence → annotated milestone tag.

For branch, pull request, and authentication details, use the
[learner-owned workflow](CONTRIBUTING.md#milestone-change-loop).

You need Git, a GitHub account, Python 3.12, and uv now. Docker Desktop or
Docker Engine is first needed at M2. PostgreSQL runs through Docker; you do not
need to install it separately. No provider account or secret is needed to start
or to complete deterministic/local Core work. M6 introduces one required,
separately authorized Stripe-like sandbox experiment only after its local Core;
M7 and M10 keep the listed provider work optional.

## Roadmap

M0 is the stable label for **Milestone 1 of 11**; M5 is Milestone 6 of 11.
The `#` column keeps ordinal and label together. This is the five-product course
route, not your completion record; use [PROGRESS](PROGRESS.md#active-milestone-dashboard)
to stop and resume.

| # | Milestone / Capability | Project | Key concepts | FastAPI / Python tools | Real integration |
|---|---|---|---|---|---|
| 1 · M0 | [Engineering Baseline / Reproducible](milestones/m0-engineering-baseline/README.md) | Catalog | Reproducible setup, configuration, typing, tests, Git/CI, diagnosis | FastAPI, Uvicorn, Pydantic, settings; uv, pytest, HTTPX, Ruff, mypy | Deterministic/local Core; no provider account |
| 2 · M1 | [Production-minded API Foundation / Functional](milestones/m1-production-api-foundation/README.md) | Catalog | HTTP semantics, validation, errors, OpenAPI, ordering, pagination | `APIRouter`, `Depends`, OpenAPI; `fastapi-pagination` only after the handwritten contract | Deterministic/local Core; no provider account |
| 3 · M2 | [POS Persistence & Data Modeling / Persistent](milestones/m2-pos-persistence-data-modeling/README.md) | POS | Relational modeling, constraints, indexes, migrations, transaction ownership | Pydantic boundaries, PostgreSQL, Psycopg, SQLAlchemy, Alembic; FastCRUD only after explicit CRUD | Deterministic/local Core; no provider account |
| 4 · M3 | [Transactions & Correctness / Correct](milestones/m3-transactions-correctness/README.md) | POS | Atomic checkout, isolation, money, invariants, retries, races | `Depends`, PostgreSQL, SQLAlchemy, pytest | Deterministic/local Core; no provider account |
| 5 · M4 | [Maintainability, Testing & Refactoring / Maintainable](milestones/m4-maintainability-testing-refactoring/README.md) | POS | Characterization tests, cohesion, coupling, refactoring, earned boundaries | `APIRouter` and `Depends` when the boundary earns them; pytest, Ruff, mypy | Deterministic/local Core; no provider account |
| 6 · M5 | [Secure Multi-user Ecommerce / Secure](milestones/m5-secure-multi-user-ecommerce/README.md) | Ecommerce | Authentication, authorization, ownership, sessions, passwords, threats | FastAPI Security after the concepts; secure cookies and `pwdlib`; PyJWT is Stretch | Deterministic/local Core; no provider account |
| 7 · M6 | [Resilient External Integrations / Resilient](milestones/m6-resilient-external-integrations/README.md) | Ecommerce | Timeouts, retry budgets, webhooks, idempotency, refunds, reconciliation | FastAPI webhook/dependencies; HTTPX or provider SDK after the fake; `BackgroundTasks` only for disposable work | **Required after local Core:** exactly one Stripe-like payment sandbox |
| 8 · M7 | [Durable Async & Background Processing / Durable](milestones/m7-durable-async-background-processing/README.md) | Ecommerce | Persisted intent, outbox, workers, at-least-once delivery, replay | PostgreSQL worker; `BackgroundTasks` as contrast; Taskiq only if earned | Deterministic/local Core; optional email test provider |
| 9 · M8 | [Concurrency Lab / Concurrent](milestones/m8-concurrency-booking/README.md) | Booking | Final-seat races, locks, database invariants, deadlocks, contention | FastAPI dependencies, PostgreSQL, SQLAlchemy, Alembic, two-connection harness | Deterministic/local Core; no provider account |
| 10 · M9 | [Performance, Caching & Realtime / Performant](milestones/m9-performance-caching-realtime-social/README.md) | Social | N+1, query plans, pagination, cache authority, streaming gaps | SQLAlchemy; Redis after a measured miss; SSE if earned; WebSockets for earned two-way need | Deterministic/local Core; no provider account |
| 11 · M10 | [Production Multi-tenant SaaS Capstone / Operable/sellable](milestones/m10-production-multitenant-saas-capstone/README.md) | Multi-tenant POS SaaS | Tenant isolation, audit, observability, releases, recovery, handoff | FastAPI composition, Docker/Compose; optional SQLAdmin and Sentry or Logfire after tenant auth/audit | Deterministic/local Core; optional S3-compatible storage, OAuth/OIDC, monitoring, and authorized deployment |

For depth, use the [full curriculum and concept trace](CURRICULUM.md), the
[earned stack policy](STACK.md), and the [quality gates](QUALITY-GATES.md).

## Reference

- [Stack and tools](STACK.md)
- [Quality gates](QUALITY-GATES.md)
- [Evolving projects](projects/README.md)
- [Challenge system](challenges/README.md)
- [Evidence template](templates/EVIDENCE-INDEX.md)

Each milestone keeps seven predictable reference files. Its `README.md` is the
learner route; `CONCEPTS.md`, `CHALLENGE.md`, `TOOLS.md`, `ACCEPTANCE.md`,
`REVIEW.md`, and `RESOURCES.md` support the relevant step. You do not read all
seven before starting.

Use one modular FastAPI application and one PostgreSQL database when persistence
begins. The [stack policy](STACK.md#explicit-exclusions) owns advanced-tool
exclusions and the evidence required for exceptions.

## For curriculum maintainers

Learners can ignore this section. Use the [curriculum maintenance index](docs/maintainers/README.md)
for the active plan, checklist, rubric, audit inputs, and provenance.

This repository uses the [MIT License](LICENSE). Dependency licenses remain
their own.
