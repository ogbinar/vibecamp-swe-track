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

At the start of each milestone, create its evidence index from the repository
root (replace `MN` with `M0`, `M1`, and so on):

```bash
mkdir -p "evidence/MN"
cp templates/EVIDENCE-INDEX.md "evidence/MN/index.md"
```

Expected: one editable index exists for commands, observations, decisions, and
links. Write `N/A — condition not present` for a conditional gate that does not
apply. The [synthetic examples](templates/EVIDENCE-EXAMPLES.md) show useful
evidence without pretending to be learner results.

First get the supplied M0 starter green. Then the lesson introduces the
professional GitHub loop: issue → branch → pull request → automated checks →
evidence → annotated milestone tag.

For branch, pull request, and authentication details, use the
[learner-owned workflow](CONTRIBUTING.md#milestone-change-loop).

You need Git, a GitHub account, Python 3.12, and uv now. Docker Desktop or
Docker Engine is first needed at M2. PostgreSQL runs through Docker; you do not
need to install it separately. M10 explains optional real-host accounts, cost,
Transport Layer Security (TLS), and domain prerequisites only when you reach it.

## Roadmap

M0 is the stable label for **Milestone 1 of 11**; M5 is Milestone 6 of 11.
The table describes repository support, not your completion. Record your own
status in [PROGRESS](PROGRESS.md#active-milestone-dashboard).

| Position | Label | Capability / product | You will produce | Gate | Repository support |
|---|---|---|---|---|---|
| Milestone 1 of 11 | [M0](milestones/m0-engineering-baseline/README.md) | Reproducible / Catalog | Green baseline transcript; Failure diagnosis and reset record; CI-backed gate PR and annotated tag | A1–A3 plus A0 diagnostic / Level A | Starter locally verified; learner gate not started |
| Milestone 2 of 11 | [M1](milestones/m1-production-api-foundation/README.md) | Functional / Catalog | Tested HTTP request matrix; Compatibility-change evidence | A1–A4 / A + selected B | Starter locally verified; learner gate not started |
| Milestone 3 of 11 | [M2](milestones/m2-pos-persistence-data-modeling/README.md) | Persistent / POS | Schema and migration; Query/persistence evidence | A1–A5 / Level B | Starter locally verified; learner gate not started |
| Milestone 4 of 11 | [M3](milestones/m3-transactions-correctness/README.md) | Correct / POS | Atomic checkout regression; Money/repeat and final-unit race evidence | A1–A4 / Level B | Starter locally verified; learner gate not started |
| Milestone 5 of 11 | [M4](milestones/m4-maintainability-testing-refactoring/README.md) | Maintainable / POS | Cashier-name change and boundary check; Refactor evidence and portfolio draft | A1–A6 / Level B | Starter locally verified; learner gate not started |
| Milestone 6 of 11 | [M5](milestones/m5-secure-multi-user-ecommerce/README.md) | Secure / Ecommerce | Session and role/object matrix; Order-state attack regressions and threat record | A1–A6 / B + contextual C | Starter locally verified; learner gate not started |
| Milestone 7 of 11 | [M6](milestones/m6-resilient-external-integrations/README.md) | Resilient / Ecommerce | Provider boundary and retry/webhook tests; Reconciliation and incident record | A1–A4 / B + contextual C | Starter locally verified; learner gate not started |
| Milestone 8 of 11 | [M7](milestones/m7-durable-async-background-processing/README.md) | Durable / Ecommerce | Persisted job/outbox flow; Crash/duplicate/quarantine/replay evidence | A1–A5 / C for async slice | Starter locally verified; learner gate not started |
| Milestone 9 of 11 | [M8](milestones/m8-concurrency-booking/README.md) | Concurrent / Booking | Final-seat race reproduction and repair; Time/contention evidence | A1–A4 / Level B | Starter locally verified; learner gate not started |
| Milestone 10 of 11 | [M9](milestones/m9-performance-caching-realtime-social/README.md) | Performant / Social | Feed query comparison; Redis retain/remove decision; One-way update evidence | A1–A4 / B + contextual C | Starter locally verified; learner gate not started |
| Milestone 11 of 11 | [M10](milestones/m10-production-multitenant-saas-capstone/README.md) | Operable/sellable candidate / Multi-tenant POS SaaS | Tenant-isolation proof; Release/recovery record; Runbooks and cold-reviewed handoff | A1–A7 / Level C local Core; real-target endorsement optional | Starter locally verified; learner gate not started |

See the [full curriculum](CURRICULUM.md) when you want the detailed roadmap or
concept coverage. Use [PROGRESS.md](PROGRESS.md) to stop and resume.

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
