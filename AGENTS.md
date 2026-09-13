# Project working contract for coding agents

## Mission

Preserve this as a GitHub-only, self-paced software engineering curriculum. FastAPI is a teaching vehicle, not the objective.

> **“Practical engineering without compromise. Use the smallest tool that preserves correctness, security, maintainability, and operability. Add complexity only when the product earns it.”**

## Non-negotiable pedagogy

- Preserve exactly M0–M10 and the maturity arc documented in `CURRICULUM.md`.
- Use the recurring cycle: Understand problem → Design smallest correct solution → Build → Test → Break deliberately → Debug → Refactor → Operate → Ship.
- Teach problem-first through evolving software, seeded faults, diagnosis, and objective evidence—not tool-topic surveys.
- Every milestone directory contains exactly `README.md`, `CONCEPTS.md`, `CHALLENGE.md`, `TOOLS.md`, `ACCEPTANCE.md`, `REVIEW.md`, and `RESOURCES.md` with distinct responsibilities.
- Keep Core and Stretch separate. The Level A/B/C gates are cumulative and contextual, never three versions of every feature.
- Prefer a modular monolith, one PostgreSQL database, and `STACK.md`. Optional tools need observed need, evidence, operational cost, and removal criteria. FastCRUD follows fundamentals.
- Keep progress and assessment in GitHub issues, PRs, Actions, project-local evidence, `PROGRESS.md`, and annotated tags/releases. ADRs record only consequential architecture decisions.
- Preserve the diagnostic, complexity-rejection, portfolio, and data-lifecycle templates as focused evidence contracts. Career-shifter and data-specialist lenses use identical Core gates and must never become separate tracks.
- Do not implement learner applications unless explicitly asked. Never fabricate passing evidence.

## Change discipline

Read `README.md`, `CURRICULUM.md`, `STACK.md`, `QUALITY-GATES.md`, `PLAN.md`, and `TODO.md` before curriculum changes. Treat `PLAN.md` as the canonical revision rationale, scope, dependencies, and sequence; treat `TODO.md` as the single active curriculum-maintenance tracker. When implementation work is performed, update its checklist in the same change. Do not use `PROGRESS.md` for maintenance work: it is the learner course transcript.

Keep canonical content consolidated, links relative, milestone concept/challenge/acceptance IDs traceable, and run `python3 scripts/check_curriculum.py`. Preserve unchecked future work when making planning-only changes.

Do not add Kubernetes, Kafka, microservices, service mesh, CQRS, event sourcing, Elasticsearch, complex DI, or multiple databases without an explicit product constraint and ADR. Preserve user work. Never publish, push, create remotes, open external issues, commit, or alter tags without explicit authorization. Avoid secrets and personal/customer data.
