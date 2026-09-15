# VibeCamp Software Engineering Track

> **“Practical engineering without compromise. Use the smallest tool that preserves correctness, security, maintainability, and operability. Add complexity only when the product earns it.”**

This is a self-paced course for learning how to build, test, break, repair,
deploy, and operate useful software. Air makes the product visible in the
browser; FastAPI preserves the backend/API contract. Software engineering is
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
reports **eight passing tests**. You now have a working
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

You need Git, a GitHub account, Python 3.13, and uv now. Docker Desktop or
Docker Engine is first needed at M2. PostgreSQL runs through Docker; you do not
need to install it separately. No provider account or secret is needed to start
or to complete deterministic/local Core work. M6 introduces one required,
separately authorized Stripe-like sandbox experiment only after its local Core;
M7 and M10 keep the listed provider work optional.

## Roadmap

The milestone label stays stable (`M0` through `M10`). The business problem tells
what is hurting now; the product capability tells what becomes useful next.
Learner completion belongs in [PROGRESS](PROGRESS.md), not this map.

| Milestone | Business problem | Product capability | Start here |
|---|---|---|---|
| M0 | A catalog works only on its author's machine. | Make the catalog easy to run. | [Start M0](milestones/m0-engineering-baseline/README.md) |
| M1 | Storefront and staff clients cannot predict catalog responses. | Make the catalog predictable for clients. | [Start M1](milestones/m1-production-api-foundation/README.md) |
| M2 | Stock and carts disappear when the POS restarts. | Make stock survive a restart. | [Start M2](milestones/m2-pos-persistence-data-modeling/README.md) |
| M3 | A failed checkout can leave inventory, money, and receipts disagreeing. | Make checkout safe. | [Start M3](milestones/m3-transactions-correctness/README.md) |
| M4 | A small receipt request touches too many POS files. | Change the POS without breaking it. | [Start M4](milestones/m4-maintainability-testing-refactoring/README.md) |
| M5 | Customers can see or change accounts and orders they do not own. | Protect customer accounts and orders. | [Start M5](milestones/m5-secure-multi-user-ecommerce/README.md) |
| M6 | A payment timeout does not reveal whether money moved. | Handle uncertain payments. | [Start M6](milestones/m6-resilient-external-integrations/README.md) |
| M7 | Accepted fulfillment work disappears when a process crashes. | Finish accepted work after a crash. | [Start M7](milestones/m7-durable-async-background-processing/README.md) |
| M8 | Two buyers can both confirm the same final seat. | Stop the last seat being sold twice. | [Start M8](milestones/m8-concurrency-booking/README.md) |
| M9 | A correct feed becomes slow and misses timely updates as it grows. | Keep the feed fast as it grows. | [Start M9](milestones/m9-performance-caching-realtime-social/README.md) |
| M10 | One POS must safely serve several businesses and survive change. | Support multiple businesses safely. | [Start M10](milestones/m10-production-multitenant-saas-capstone/README.md) |

For depth, use the [full curriculum and concept trace](CURRICULUM.md), the
[earned stack policy](STACK.md), and the [quality gates](QUALITY-GATES.md).

## Reference

- [Stack and tools](STACK.md)
- [Quality gates](QUALITY-GATES.md)
- [Evolving projects](projects/README.md)
- [Challenge system](challenges/README.md)
- [Evidence template](templates/EVIDENCE-INDEX.md)

Each milestone keeps four predictable files. `README.md` is the learner route,
`CHALLENGE.md` owns deliberate failures and recovery, `ACCEPTANCE.md` owns Core,
Stretch, evidence, and review, and `REFERENCE.md` holds just-in-time concepts,
tool decisions, and sources. Start with the README; open support only when its
block points there.

Use one modular Air/FastAPI application and one PostgreSQL database when persistence
begins. The [stack policy](STACK.md#explicit-exclusions) owns advanced-tool
exclusions and the evidence required for exceptions.

## For curriculum maintainers

Learners can ignore this section. Use the [curriculum maintenance index](docs/maintainers/README.md)
for the active plan, checklist, rubric, audit inputs, and provenance.

This repository uses the [MIT License](LICENSE). Dependency licenses remain
their own.
