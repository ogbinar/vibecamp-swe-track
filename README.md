# VibeCamp Software Engineering Track

> **“Practical engineering without compromise. Use the smallest tool that preserves correctness, security, maintainability, and operability. Add complexity only when the product earns it.”**

This is a self-paced, GitHub-only path from an ambiguous product request to software that can be changed, secured, operated, recovered, and released responsibly. FastAPI is the teaching vehicle; software engineering is the subject.

## Course outcome

> **“I can take a product idea, choose a small architecture, build it quickly, prove that it is correct, understand its failure modes, deploy it reproducibly, operate it confidently, and make it good enough that I could realistically charge someone to use it.”**

## How learning works

Every piece of work follows the same visible cycle:

**Understand problem → Design smallest correct solution → Build → Test → Break deliberately → Debug → Refactor → Operate → Ship**

Tools appear only when a product problem earns them. You first observe duplicated database code, an unsafe race, a slow query, or lost work; then introduce a boundary, lock, index, or queue and prove that it addresses the problem. Later milestones increasingly start from existing software and seeded faults: about 70% new build / 30% change-and-repair in M0–M2, 40/60 in M3–M5, and 20/80 in M6–M10. “Change-and-repair” includes incident diagnosis, failure injection, refactoring, migration recovery, and operation—not cosmetic edits.

## Start here

1. Read the [roadmap and concept coverage](CURRICULUM.md), [stack policy](STACK.md), and [quality gates](QUALITY-GATES.md).
2. For curriculum maintenance, follow the ranked [revision plan](PLAN.md) and keep the active [maintenance TODO](TODO.md) current.
3. For course work, open a milestone issue using `.github/ISSUE_TEMPLATE/milestone.yml` and begin [M0 — Engineering Baseline](milestones/m0-engineering-baseline/README.md).
4. Work through the milestone sequence and its challenge brief. Use focused branches and pull requests.
5. Store actual evidence using [the evidence index template](templates/EVIDENCE-INDEX.md); do not pre-fill claims.
6. Advance only when Actions pass, the milestone acceptance file is satisfied, and [PROGRESS.md](PROGRESS.md) links the evidence.

## Curriculum deliverables

| Need | Canonical source |
|---|---|
| Curriculum revision rationale and sequence | [PLAN.md](PLAN.md) |
| Active curriculum-maintenance work | [TODO.md](TODO.md) |
| Full milestone curriculum | [Curriculum roadmap](CURRICULUM.md) and the eleven [milestone folders](milestones/) |
| Recommended tools per milestone | Each milestone's `TOOLS.md`, governed by [STACK.md](STACK.md) |
| Expected concepts | Each milestone's `CONCEPTS.md` and the [concept coverage matrix](CURRICULUM.md#concept-coverage-matrix) |
| Exit criteria | Each milestone's `ACCEPTANCE.md` |
| Repository structure | This README's GitHub course model and milestone file contract |
| Quality gates | [QUALITY-GATES.md](QUALITY-GATES.md) |
| Learning workflow | The cycle below, [challenge lifecycle](challenges/README.md), and advancement workflow in [QUALITY-GATES.md](QUALITY-GATES.md) |
| Complexity to avoid | [Stack policy](STACK.md), including earned tools and explicit exclusions |
| Entry diagnostic | [Targeted diagnostic and remediation](templates/ENTRY-DIAGNOSTIC.md), used by M0 |
| Independent review | [Cold-review protocol](QUALITY-GATES.md#cold-review-protocol) and [evidence index](templates/EVIDENCE-INDEX.md) |
| Simplicity decision | [Complexity rejection record](templates/COMPLEXITY-REJECTION.md), distinct from an ADR |
| Portfolio narrative | [Evidence-backed case-study template](templates/PORTFOLIO-CASE-STUDY.md) |
| Data handling | [Data-lifecycle review](templates/DATA-LIFECYCLE.md), used only where applicable |

## GitHub is the course model

| GitHub surface | Course role |
|---|---|
| README | Course home and operating philosophy |
| [CURRICULUM](CURRICULUM.md) | Roadmap, dependencies, and concept traceability |
| [Milestones](milestones/) | Lessons, local challenges, tools, acceptance, and review |
| [Projects](projects/README.md) | Evolving product laboratories; no milestone copies |
| Issues | Requirements, backlog, defects, and advancement plan |
| Pull requests | Development history, review, evidence, and change discussion |
| Actions | Repeatable automated feedback and repository checks |
| ADRs | Only consequential architecture decisions, stored with the owning project |
| Releases and annotated tags | Reviewed product milestones and immutable evidence references |
| [PROGRESS](PROGRESS.md) | Engineering journal and progress transcript |

## Milestone file contract

Each of the exactly eleven milestone directories contains exactly seven files:

- `README.md` — capability, product/deliverable, sequence, prerequisites, and outputs.
- `CONCEPTS.md` — problem-driven mental models used by that milestone.
- `CHALLENGE.md` — build/change/break/debug/refactor/operate/ship work and seeded failures.
- `TOOLS.md` — why tools enter now, when to avoid or remove them, and earned options.
- `ACCEPTANCE.md` — objective Core/Stretch criteria, commands, evidence, and A/B/C applicability.
- `REVIEW.md` — learner explanation, self-review, debugging, and reflection prompts.
- `RESOURCES.md` — resource-selection categories and standards, without unverified citations.

The files collaborate rather than repeat: `README` routes; `CONCEPTS` teaches; `CHALLENGE` creates evidence; `ACCEPTANCE` judges it.

## Architecture and scope

The default is a modular monolith: one FastAPI deployable and one PostgreSQL database per project. Use Python, Pydantic, SQLAlchemy, Alembic, pytest, HTTPX, Ruff, uv, GitHub Actions, and—when its milestone earns it—Docker. FastCRUD may accelerate routine persistence only after explicit SQL/repository fundamentals are proven and its trade-offs are recorded.

Redis, Taskiq, SSE, WebSockets, OpenTelemetry, Logfire, Sentry, and similar tools are optional and must have measured need, failure analysis, ownership, and removal criteria. Kubernetes, Kafka, microservices, service meshes, CQRS, event sourcing, Elasticsearch, complex DI frameworks, and multiple databases are excluded unless an explicit product constraint and real ADR justify an exception.

Use synthetic data. Never commit secrets, customer data, generated environments, or database volumes. No LMS or project board is required.

## License

This repository is licensed under the [MIT License](LICENSE), matching the existing GitHub repository license. Dependency licenses remain their own.
