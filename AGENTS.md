# Project working contract for coding agents

## Mission

Preserve this as a GitHub-only, self-paced software engineering curriculum.
Air is the primary human-facing web layer and FastAPI remains the backend/API
layer; neither framework is the objective.

> **“Practical engineering without compromise. Use the smallest tool that preserves correctness, security, maintainability, and operability. Add complexity only when the product earns it.”**

## Non-negotiable pedagogy

- Preserve exactly M0–M10 and the maturity arc documented in `docs/reference/curriculum-map.md`.
- Use the recurring cycle: Understand problem → Design smallest correct solution → Build → Test → Break deliberately → Debug → Refactor → Operate → Ship.
- Teach problem-first through evolving software, seeded faults, diagnosis, and objective evidence—not tool-topic surveys.
- Keep every milestone directory at exactly one learner controller:
  `README.md`. Do not restore retired support files or create a hybrid
  milestone. Challenge scenarios, acceptance gates, recovery, and references
  stay inside that controller.
- Keep Core and Stretch separate. The Level A/B/C gates are cumulative and contextual, never three versions of every feature.
- Prefer one Air/FastAPI modular monolith, one PostgreSQL database, and
  `docs/reference/stack.md`. Air owns pages/forms/components; FastAPI owns JSON/OpenAPI and
  operational endpoints; both reuse the same models, use cases, services, and
  database logic. Optional tools need observed need, evidence, operational cost,
  and removal criteria. FastCRUD follows fundamentals.
- Keep progress and assessment in GitHub issues, PRs, Actions, project-local evidence, `PROGRESS.md`, and annotated tags/releases. ADRs record only consequential architecture decisions.
- Preserve the diagnostic, complexity-rejection, portfolio, and data-lifecycle templates as focused evidence contracts. Career-shifter and data-specialist lenses use identical Core gates and must never become separate tracks.
- Treat `docs/maintainers/usability.md` as the learner-experience gate. Write learner material in plain language before terminology; define terms at first use; expand acronyms; use consistent vocabulary; show examples before abstractions; and structure instructions as action, reason, expected observation, and recovery.
- Keep `README.md` as the only learner front door. Put one next action before
  reference or maintainer material, and validate the Air/FastAPI presentation
  pattern on Catalog M0–M1 before broad rollout.
- Every milestone README is the learner controller in this order: Business
  problem → Product objective → Start here → Build → Understand → Use a tool if
  earned → Prove it → Done / next. Use compact `Goal`, `Do`, `Expected`, `If
  not`, `Understand`, and `Save/next` blocks. Define terms when the observed
  problem first requires them; do not restore a front-loaded term inventory or
  duplicate command map.
- Use Air Tags and Air routers as the default UI pattern. Use explicit
  `AirForm.from_request()` validation when forms are earned. Introduce ordinary
  server-rendered forms before HTMX; introduce HTMX only for a concrete partial-
  update need, and keep browser JavaScript small and explicit. Do not add Jinja,
  AirDB, AirDragon/Tailwind, a SPA framework, Node toolchain, separate frontend
  service, or browser-to-own-API calls without evidence that the simpler Air
  pattern fails.
- Preserve existing FastAPI paths, response models, error contracts, OpenAPI,
  health/readiness behavior, dependency boundaries, and tests unless a product
  requirement explicitly changes them. Register human-facing routes through an
  Air router excluded from OpenAPI; share application state instead of mounting
  disconnected Air and FastAPI applications.
- Every active command names its working directory, expected observation, and recovery route. Expand each C/A ID into atomic learner checks. Hints progress from observation questions, to the relevant boundary/files, to one targeted reference without supplying final code.
- Do not implement learner applications unless explicitly asked. Never fabricate passing evidence.

## Change discipline

Read `README.md`, `docs/reference/curriculum-map.md`, `docs/reference/stack.md`, `docs/reference/quality.md`, `docs/maintainers/usability.md`, `PLAN.md`, and `TODO.md` before curriculum changes. Treat `PLAN.md` as the canonical revision rationale, scope, dependencies, and sequence; treat `TODO.md` as the single active curriculum-maintenance tracker. When implementation work is performed, update its checklist in the same change. Do not use `PROGRESS.md` for maintenance work: it is the learner course transcript.

Keep canonical content consolidated, links relative, milestone concept/challenge/acceptance IDs traceable, and run `python3 scripts/check_curriculum.py`. Keep the active cleanup decision and rollback evidence in `docs/maintainers/subtraction-cleanup.md`; Git history owns retired-source provenance. Preserve unchecked future work when making planning-only changes.

Do not add Kubernetes, Kafka, microservices, service mesh, CQRS, event sourcing, Elasticsearch, complex DI, or multiple databases without an explicit product constraint and ADR. Preserve user work. Never publish, push, create remotes, open external issues, commit, or alter tags without explicit authorization. Avoid secrets and personal/customer data.
