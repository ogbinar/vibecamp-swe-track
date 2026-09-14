# Curriculum roadmap and concept coverage

The maturity arc is cumulative: **reproducible → functional → persistent → correct → maintainable → secure → resilient → durable → concurrent → performant → operable/sellable**. Estimated weeks are intentionally absent; evidence, not time spent, unlocks the next milestone.

## Roadmap

| Milestone | Capability | Product change | Required level | Work profile |
|---|---|---|---|---|
| [M0 — Engineering Baseline](milestones/m0-engineering-baseline/README.md) | Reproducible | Catalog walking skeleton and deterministic workspace | A | Mostly build |
| [M1 — Production-minded API Foundation](milestones/m1-production-api-foundation/README.md) | Functional | In-memory catalog with honest public contracts | A, selected B | Build plus boundary failures |
| [M2 — POS Persistence & Data Modeling](milestones/m2-pos-persistence-data-modeling/README.md) | Persistent | Start POS and replace volatile state with PostgreSQL | B | Build plus migration repair |
| [M3 — Transactions & Correctness](milestones/m3-transactions-correctness/README.md) | Correct | Make checkout, inventory, payments, and receipts atomic | B | Change and race/failure diagnosis |
| [M4 — Maintainability, Testing & Refactoring](milestones/m4-maintainability-testing-refactoring/README.md) | Maintainable | Add returns/promotions while untangling the POS | B | Mostly change/refactor |
| [M5 — Secure Multi-user Ecommerce](milestones/m5-secure-multi-user-ecommerce/README.md) | Secure | Add accounts, roles, ownership, and safe order state | B + contextual C | Mostly security repair |
| [M6 — Resilient External Integrations](milestones/m6-resilient-external-integrations/README.md) | Resilient | Harden payment/shipping/webhook boundaries | B + contextual C | Mostly failure diagnosis |
| [M7 — Durable Async & Background Processing](milestones/m7-durable-async-background-processing/README.md) | Durable | Add recoverable fulfillment jobs/outbox | C for async slice | Mostly crash/replay work |
| [M8 — Concurrency Lab using Booking](milestones/m8-concurrency-booking/README.md) | Concurrent | New focused booking lab, then break/fix final-seat races | B | Small build, mostly races |
| [M9 — Performance, Caching & Realtime using Social](milestones/m9-performance-caching-realtime-social/README.md) | Performant | New focused social lab, then diagnose realistic load | B + contextual C | Small build, mostly optimization/operation |
| [M10 — Production Multi-tenant SaaS Capstone](milestones/m10-production-multitenant-saas-capstone/README.md) | Operable/sellable | Evolve POS into a tenant-safe production candidate | C | Change, operate, recover, release |

Levels are cumulative and contextual; see [QUALITY-GATES.md](QUALITY-GATES.md). M1 is production-minded at the API boundary, not a claim that an in-memory app is operationally production-ready.

M0 begins with the [entry diagnostic](templates/ENTRY-DIAGNOSTIC.md) to select targeted remediation. It never skips or lowers a gate.

## Project evolution

- `projects/catalog/`: M0–M1, establishing reproducibility and boundary behavior.
- `projects/pos/`: M2–M4, then hardened into the M10 SaaS capstone.
- `projects/ecommerce/`: M5–M7, from identity to uncertain integrations and durable work.
- `projects/booking/`: focused M8 concurrency laboratory.
- `projects/social/`: focused M9 performance lab.

The deliberate shift from greenfield to brownfield is part of the curriculum. Seed briefs live in [challenges](challenges/README.md); learners inject or receive the described defects, but this curriculum repository does not implement them.

## Cross-cutting learner lenses

The course has one sequence and identical Core gates. A learner may use either lens to choose remediation and frame evidence; neither creates a track, substitutes for a concept, or lowers acceptance.

- **Career-shifter lens:** translate prior-domain judgment into concrete requirements and incident impact; make engineering vocabulary explicit; narrate a debugging hypothesis, review decision, and trade-off so a new team can follow the reasoning.
- **Data-specialist lens:** carry SQL/modeling strengths across the application boundary by proving HTTP contracts, transaction ownership, authorization, service behavior, deployment, and recovery—not only query correctness.

Use the M0 diagnostic to locate gaps, selected milestone `REVIEW.md` prompts to practice transfer, and the portfolio case study to show the same engineering evidence to a cold reader. Learners may select neither lens or describe another background without changing the gate.

## Coverage notation

`I` introduces the mental model through a concrete problem. `P` practices it in a challenge or failure drill. `V` proves it through objective acceptance evidence. Entries name the milestone(s) where each stage occurs. Every row routes to a challenge and acceptance file; milestone IDs in those files make evidence traceable.

## Concept coverage matrix

| Engineering concept | Introduced | Practiced | Proven |
|---|---|---|---|
| HTTP semantics | M1 | M1 `C1` | M1 `A1` |
| API contracts | M1 | M1 `C1,C2` | M1 `A1,A2` |
| Typing and validation | M0/M1 | M1 `C2` | M1 `A2` |
| Dependency injection | M4 | M4 `C2` | M4 `A2` |
| Project structure | M0 | M0 `C1`; M4 `C1` | M0 `A1`; M4 `A1` |
| Configuration | M0 | M0 `C2`; M10 `C3` | M0 `A2`; M10 `A3` |
| Relational modeling | M2 | M2 `C1` | M2 `A1` |
| SQL | M2 | M2 `C1,C2`; M9 `C1` | M2 `A1,A2`; M9 `A1` |
| Constraints | M2 | M2 `C1`; M3 `C2` | M2 `A1`; M3 `A2` |
| Indexes | M2 | M2 `C2`; M9 `C1` | M2 `A2`; M9 `A1` |
| Migrations | M2 | M2 `C3`; M10 `C3` | M2 `A3`; M10 `A3` |
| Transactions | M3 | M3 `C1` | M3 `A1` |
| ACID | M3 | M3 `C1,C2` | M3 `A1,A2` |
| Race conditions | M3 | M3 `C2`; M8 `C1` | M8 `A1` |
| Locking | M8 | M8 `C2,C3` | M8 `A2,A3` |
| Application vs database invariants | M2/M3 | M3 `C2` | M3 `A2` |
| Unit tests | M1 | M1 `C2`; M4 `C3` | M1 `A2`; M4 `A3` |
| Integration tests | M2 | M2 `C1,C3`; M4 `C3` | M2 `A1,A3`; M4 `A3` |
| API tests | M0/M1 | M1 `C1,C2` | M1 `A1,A2` |
| Refactoring | M4 | M4 `C1,C2` | M4 `A1,A2` |
| Cohesion and coupling | M4 | M4 `C1` | M4 `A1` |
| Service/repository boundaries | M2/M4 | M4 `C2` | M4 `A2` |
| Authentication | M5 | M5 `C1` | M5 `A1` |
| Authorization | M5 | M5 `C2,C3` | M5 `A2,A3` |
| RBAC | M5 | M5 `C2` | M5 `A2` |
| Object-level authorization | M5 | M5 `C3` | M5 `A3` |
| Password hashing | M5 | M5 `C1` | M5 `A1` |
| JWT | M5 | M5 `C1` | M5 `A1` |
| State machines | M3/M5 | M5 `C4` | M5 `A4` |
| Timeouts | M6 | M6 `C1` | M6 `A1` |
| Retries and backoff | M6 | M6 `C1` | M6 `A1` |
| Webhooks | M6 | M6 `C2` | M6 `A2` |
| Idempotency | M6 | M6 `C2,C3`; M7 `C2` | M6 `A2,A3`; M7 `A2` |
| Queues and workers | M7 | M7 `C1,C3` | M7 `A1,A3` |
| At-least-once execution | M7 | M7 `C2` | M7 `A2` |
| Idempotent consumers | M7 | M7 `C2` | M7 `A2` |
| Eventual consistency | M6/M7 | M7 `C1,C3` | M7 `A1,A3` |
| Query optimization | M9 | M9 `C1` | M9 `A1` |
| N+1 | M2 | M2 `C2`; M9 `C1` | M2 `A2`; M9 `A1` |
| EXPLAIN/query plans | M9 | M9 `C1` | M9 `A1` |
| Pagination | M1 | M1 `C1`; M9 `C1` | M1 `A1`; M9 `A1` |
| Redis/cache-aside | M9 | M9 `C2` | M9 `A2` |
| Cache invalidation | M9 | M9 `C2` | M9 `A2` |
| SSE vs WebSockets | M9 | M9 `C3` | M9 `A3` |
| Structured logging | M6 | M6 `C3`; M10 `C1` | M6 `A3`; M10 `A1` |
| Correlation/request IDs | M6 | M6 `C3`; M10 `C1` | M6 `A3`; M10 `A1` |
| Metrics | M7 | M7 `C3`; M10 `C1` | M7 `A3`; M10 `A1` |
| Traces | M10 | M10 `C1` | M10 `A1` |
| Health/readiness checks | M0/M10 | M0 `C1`; M10 `C3` | M0 `A1`; M10 `A3` |
| Docker | M2 | M2 `C3`; M10 `C3` | M2 `A3`; M10 `A3` |
| CI/CD | M0/M10 | M0 `C3`; M10 `C3` | M0 `A3`; M10 `A3` |
| Migration deployment | M10 | M10 `C3` | M10 `A3` |
| Secrets | M0/M5 | M5 `C1`; M10 `C3` | M5 `A1`; M10 `A3` |
| Tenant isolation | M10 | M10 `C2` | M10 `A2` |
| Audit logs | M10 | M10 `C2` | M10 `A2` |
| Backup/recovery | M10 | M10 `C4` | M10 `A4` |
| Release discipline | M0 | every Ship step; M10 `C3` | each gate; M10 `A3` |
| Incident/postmortem thinking | M6 | M6 `C3`; M10 `C4` | M6 `A3`; M10 `A4` |

## Dependency and decision rules

Complete Core gates in order. Stretch work never substitutes for Core. An ADR is warranted only for a costly-to-reverse decision, a new service, a public-contract change, or a material security/operations trade-off. A dependency must name the observed problem, alternatives, operational cost, and removal trigger.

The detailed adoption/removal sequence lives in [STACK.md](STACK.md#earned-tools).
Every milestone has deterministic offline Core. Exactly one separately
authorized Stripe-like sandbox experiment follows M6 local Core; M7 email and
M10 storage, OAuth/OIDC, monitoring, SQLAdmin, and real deployment are optional
endorsements and never account prerequisites. This classification does not add
a second roadmap table.
