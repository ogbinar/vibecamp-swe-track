# Active maintenance plan

The business-first Air-primary migration is the only active local curriculum
plan. Completed planning and execution chronology is preserved in the
[dated history snapshot](docs/maintainers/archive/2026-09-15-business-first/PLAN-history.md).
The actionable ledger is [TODO.md](TODO.md).

## Objective

Give a career shifter the shortest useful route through each milestone:

> business problem → product objective → build → engineering problem → concept
> → earned tool → proof → next action

Keep exactly M0–M10, the five-product capability arc, all 58 concept traces,
Core/Stretch separation, deliberate failure and recovery, objective evidence,
and learner-owned solutions. Air is the primary page/form/fragment layer;
FastAPI retains JSON, OpenAPI, dependencies, health, and readiness. Both call
shared Python behavior in one process and never call each other over HTTP.

## Stable replacement contract

- Every milestone has exactly `README.md`, `CHALLENGE.md`, `ACCEPTANCE.md`, and
  `REFERENCE.md`.
- Controllers use this order: Business problem, Product objective, Start here,
  Build, Understand, Use a tool if earned, Prove it, Done / next.
- Stable labels remain M0–M10, while learner-facing titles describe the product
  outcome.
- Every starter uses Python 3.13 and exactly `air==0.48.1`. Human routes use an
  OpenAPI-excluded `AirRouter` at `/` or `/app/...` over the retained FastAPI
  application.
- Ordinary forms precede HTMX. M6 earns the first focused HTMX fragment from
  uncertain payment status; M9 earns one-way SSE after the measured feed need.
- Jinja, AirDB, AirDragon/Tailwind, custom JavaScript, SPA frameworks, Node, a
  separate frontend service, and browser-to-own-API calls remain excluded.
- `README.md` is the learner entrance; `CURRICULUM.md`, `STACK.md`,
  `QUALITY-GATES.md`, `PROGRESS.md`, and milestone references own detail.

## Execution decision and state

The staged Catalog M0/M1, POS M2, Ecommerce M6, and Social M9 pilots passed
their local runtime, API/OpenAPI, HTML/form/HTMX/SSE, structure, and content
checks. The recorded decision is **ROLL OUT**. The remaining milestone and
application rollout, stable validation, full local verification, simplicity
repair, and truthful closeout are complete. Exact results and external limits
are recorded in USABILITY and TODO.

The dated [provenance and rollback manifest](docs/maintainers/archive/2026-09-15-business-first/README.md)
records every removed source, merge destination, pilot evidence, and recovery
boundary. A rollback must be scoped to the affected slice and must not reset or
overwrite the repository's pre-existing dirty work.

## Completion gate

Local completion requires all of the following:

1. exactly eleven four-file milestones and exactly 58 trace IDs;
2. intact Core/Stretch, API/OpenAPI, learner-solution, failure/recovery, and
   evidence boundaries;
3. consistent Python/Air declarations, one-process Air/FastAPI composition, no
   internal HTTP or second frontend runtime, and earned HTMX/SSE only;
4. green curriculum validation and controlled mutations, relative links and
   anchors, starter lint/format/type/tests/migrations, deliberate red/reset
   checks, page/form/fragment/SSE/API/OpenAPI checks, runtime/container checks,
   provenance audit, safety scans, and `git diff --check`;
5. a fresh local source traversal with repaired wrong turns and truthful limits.

## External limits

The required M6 sandbox experiment, optional provider/tool endorsements,
hosted GitHub rendering and Actions observation, optional real deployment, and
named-human career-shifter review remain separately unchecked. Local source or
runtime evidence cannot satisfy those items. No commit, push, publication,
deployment, provider call, credential use, external message, or human review is
authorized by this plan.
