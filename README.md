# VibeCamp Software Engineering Track

Build, test, break, repair, and operate useful software through one self-paced
M0–M10 path. You need basic Python, terminal, and Git familiarity; production
experience is not required. Air renders human-facing pages and FastAPI keeps
the JSON/OpenAPI boundary, but software engineering is the subject.

## Start now

Install [Git](https://git-scm.com/downloads) and
[uv](https://docs.astral.sh/uv/getting-started/installation/), then use Linux,
macOS, or Windows Subsystem for Linux 2. Replace the placeholder with your
learner-owned repository URL:

```bash
git clone YOUR-REPOSITORY-URL vibecamp-swe-track
cd vibecamp-swe-track
git remote -v
cd projects/catalog
cp .env.example .env
uv sync --locked
uv run --locked pytest
```

Expected: pytest reports **six passing tests**. If it does not, use the
[Catalog setup recovery](projects/catalog/README.md#if-setup-fails). Then open
**[M0 — Make the catalog easy to run](milestones/m0-engineering-baseline/README.md)**.

## Roadmap

Each row is one click to the learner instructions. Do not set up later products
until their milestone asks you to.

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

## Course loop

A **milestone** is a capability you prove, not a calendar week. Each repeats:

**Understand problem → Design smallest correct solution → Build → Test → Break deliberately → Debug → Refactor → Operate → Ship**

`C1`, `C2`, and similar labels identify challenge scenarios. `A1`, `A2`, and
similar labels identify acceptance checks. **Core** is required; **Stretch** is
optional and never replaces Core. Evidence is a reproducible test, response,
transcript, or recovery record—not only a screenshot. Keep learner progress in
[PROGRESS.md](PROGRESS.md) and use the [contribution workflow](CONTRIBUTING.md)
when a milestone introduces it.

No provider account or secret is needed to start. All local Core work is
deterministic and credential-free. External provider, hosted, deployment, or
human-review claims require their separately stated authorization and evidence.

When a milestone asks for evidence, create
`projects/catalog/evidence/MN/index.md` (substitute the active product and
milestone). Evidence belongs to that product; do not create a competing root `evidence/` tree.

## Reference

- [Curriculum and concept trace](docs/reference/curriculum-map.md)
- [Stack and earned-tool policy](docs/reference/stack.md)
- [Quality and evidence gates](docs/reference/quality.md)
- [Learner glossary](docs/reference/glossary.md)
- [Evidence index template](templates/EVIDENCE-INDEX.md)
- [Maintainer plan and checklist](docs/maintainers/README.md)

This repository uses the [MIT License](LICENSE). Dependency licenses remain
their own.
