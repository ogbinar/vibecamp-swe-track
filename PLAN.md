# Pareto-ranked curriculum revision plan

## Objective

Close the highest-leverage gaps identified by the seven-persona review and ranked backlog while preserving the existing capability progression. The revision should make entry, independent review, disciplined simplicity, learner relevance, and portfolio proof more explicit without expanding the course into parallel tracks or adding bureaucracy that does not improve evidence.

This file is the canonical rationale, scope, dependency map, and implementation order. [TODO.md](TODO.md) is the single active execution checklist.

## Active follow-up — minimal stack hardening

The persona-driven curriculum revision below is complete. The next bounded
revision incorporates the 2026-09-13 stack review without adding application
code or turning optional infrastructure into course-wide defaults.

### Outcome

Make the recommended stack executable rather than merely conceptual, and make
its boundaries explicit enough that learners do not accidentally equate
"FastAPI" with an application server, `async def` with an async database,
`BackgroundTasks` with durable execution, JWT with universal authentication,
or Docker Compose with a complete production platform.

### Pareto-ranked changes

| ID | Priority | Change | Why it matters | Primary files |
|---|---|---|---|---|
| S1 | Tier 1 | Add the ASGI runtime and PostgreSQL driver explicitly: `fastapi[standard]` (including Uvicorn) and Psycopg 3 | The documented core must be installable and capable of serving requests and connecting to PostgreSQL | `STACK.md`, M0/M1/M2 `TOOLS.md` |
| S2 | Tier 1 | Add exactly one static type checker, defaulting to mypy, alongside Ruff | Ruff linting/formatting does not prove cross-module type consistency | `STACK.md`, M0/M4 `TOOLS.md` and acceptance gates |
| S3 | Tier 1 | Establish synchronous SQLAlchemy/Psycopg as the teaching baseline; require measured need before async DB access | Avoids incidental complexity while preserving an evidence-based path to async I/O | `STACK.md`, M2/M9 `TOOLS.md`/`REVIEW.md` |
| S4 | Tier 1 | Correct operational boundaries for Compose, GitHub Actions CD, `BackgroundTasks`, and Taskiq | Prevents best-effort or local tooling from being mistaken for durable production behavior | `STACK.md`, M0/M7/M10 milestone files, `QUALITY-GATES.md` |
| S5 | Tier 1 | Make authentication choice problem-driven: cookie session or JWT; retain PyJWT plus `pwdlib[argon2]` when JWT/password auth is earned | Avoids teaching JWT as a universal default while preserving concrete security practice | `STACK.md`, M5 `CONCEPTS.md`/`TOOLS.md`/`REVIEW.md` |
| S6 | Tier 2 | Tighten optional-tool contracts for FastCRUD, pagination, Redis, realtime, object storage, and observability | Ensures each addition has a source-of-truth boundary, trigger, proof, and removal condition | `STACK.md`, focused M6/M7/M9/M10 files |
| S7 | Tier 2 | Clarify that service/repository is an earned shape, not a mandatory four-layer pipeline; place transaction ownership at the use-case boundary | Prevents pass-through layers and repository-local commits from becoming architecture theater | `STACK.md`, M3/M4 `CONCEPTS.md`/`REVIEW.md` |

### Decisions to preserve

- PostgreSQL remains the durable source of truth; Redis must not own
  correctness-critical inventory, booking, payment, or tenant state.
- PostgreSQL-backed integration tests prove constraints, locks, migrations, and
  concurrency behavior; SQLite is not a substitute for those gates.
- `BackgroundTasks` is limited to short, noncritical, best-effort work. A
  durable obligation must first be persisted and then handled by an idempotent
  worker; Taskiq does not create exactly-once execution.
- Docker Compose remains valid for local development, integration/CI, and a
  deliberately bounded single-host deployment. M10 must still prove TLS,
  secrets, restart behavior, migrations, backups, monitoring, and rollback.
- CI begins early. Automated deployment is earned only after a real target,
  migration sequence, secrets boundary, health checks, and rollback exist.
- OpenTelemetry is instrumentation, not a telemetry backend. Begin with
  structured logs and request IDs, then select the smallest useful managed or
  self-hosted backend; do not require OpenTelemetry, Logfire, and Sentry
  together.
- FastCRUD and pagination libraries remain accelerators after learners have
  implemented and explained the underlying SQLAlchemy, transaction, and API
  contract behavior.

### Implementation sequence and gates

1. Update `STACK.md` as the single source of truth for S1–S7.
2. Add only milestone-local exercises or review prompts that make those policy
   decisions observable; do not copy the entire stack policy into milestones.
3. Extend acceptance and validator checks only for stable, objective claims:
   runtime starts, PostgreSQL connects, type checking passes, and prohibited
   durability claims do not appear.
4. Run the full repository validator, concept traceability, Markdown links,
   GitHub YAML parsing, exact 11×7 milestone contract, and a duplication scan.
5. Update [TODO.md](TODO.md) in the same implementation change. Do not mark an
   item complete from documentation intent alone when its acceptance evidence
   has not been checked.

### Implementation outcome — 2026-09-13

- **S1–S3 implemented:** the canonical stack now names `fastapi[standard]`,
  Uvicorn, Psycopg 3, and mypy; M0–M4 contain focused executable gates; sync
  SQLAlchemy/Psycopg is the baseline and async database access requires an
  equal-harness measured justification.
- **S4–S5 implemented:** CI and CD are separated; Compose's single-host role
  and missing production controls are explicit; `BackgroundTasks` is bounded
  to loss-tolerant work; durable work begins with persisted intent; M5 selects
  cookie session or JWT from the client boundary while every learner still
  proves the required JWT validation concepts in-product or in an isolated
  lab.
- **S6–S7 implemented:** every optional tool now has a concrete trigger,
  correctness/source-of-truth boundary, evidence requirement, operational
  cost, and removal condition. Direct route-to-SQLAlchemy remains valid for a
  simple path; services/repositories are earned, pass-through layers are
  rejected, and use cases own transactions.
- **Validation passed:** the dependency-free validator, all relative links,
  58 concept traces, exact 11×7 milestone structure, GitHub YAML parsing,
  whitespace checks, empty-file scan, and policy-conflict audit passed. The
  validator now guards a small set of stable stack-policy markers without
  grading prose.
- **Scope held:** no learner application, infrastructure service, dependency
  lockfile, new milestone file, deployment, or learner evidence was created.

This follow-up is complete when S1–S5 are implemented and validated. S6–S7 may
be implemented in the same pass only if they remain focused edits; otherwise
retain them explicitly as deferred work. No new infrastructure, learner
application code, dependency lockfile, deployment, or fabricated evidence is
part of this documentation revision.

## Non-goals and invariants

- Do not change the exactly eleven M0–M10 milestones or their maturity arc.
- Do not add or remove files inside a milestone directory; preserve the exact seven-file contract.
- Do not create separate career-switcher, data-engineering, analytics, or career tracks. Career-shifter and data-specialist needs are cross-cutting lenses on the same engineering work.
- Do not implement learner applications, seeded defects, or claimed learner evidence.
- Do not introduce an LMS, mandatory project board, speculative infrastructure, extra databases, enterprise architecture, or blanket new dependencies.
- Do not turn templates into required paperwork unless an acceptance gate consumes the artifact.
- Do not publish, push, add a remote, create a commit/tag/release, or open external issues/PRs during this revision.

## Audit: already implemented versus real gaps

The current repository already provides: the exact M0–M10 and 11×7 structure; the problem-first learning cycle; rising brownfield/repair ratios; seeded technical-debt, incident, race, migration, job, integration, query, and security failures; Level A/B/C gates; 58 concepts traced from curriculum matrix to challenge and acceptance IDs; the GitHub-only course model; minimal FastAPI modular-monolith stack; earned-tool/removal rules; explicit enterprise exclusions; and evidence, ADR, requirements, and postmortem templates.

These are foundations to preserve, not duplicate. At plan creation, the remaining gaps were:

1. M0 has failure drills but no entry diagnostic that routes prior experience to targeted remediation without allowing core gates to be skipped.
2. Self-review exists, but no global cold-review by someone—or a later self in a clean context—who did not author the change.
3. Complexity has removal criteria, but rejected options are not captured in a lightweight, reusable decision record.
4. Career-shifter and data-specialist relevance is implicit, not applied consistently as cross-cutting prompts/evidence.
5. There is no portfolio case-study template converting engineering evidence into a defensible narrative.
6. The requirements template partly covers product intent, but stakeholder ambiguity/change and acceptance negotiation are not an explicit challenge.
7. Data lifecycle is strong in M10 but not reviewed consistently when earlier milestones collect, retain, cache, queue, export, or delete data.
8. Failure evidence is required, but PR guidance does not clearly preserve the failing reproduction while removing the production defect.
9. `PROGRESS.md` has a current-focus block, but not a compact active-milestone dashboard for risks, gate state, review, and evidence gaps.

## Pareto priorities

Tier 1 is required because these changes improve learner routing, evidence credibility, decision quality, audience accessibility, and employability across the whole course. Tier 2 and Tier 3 are optional after measuring whether Tier 1 leaves meaningful friction.

| Phase | Priority | Outcome | Depends on |
|---|---|---|---|
| 1 — Entry and review credibility | Tier 1 | P1 diagnostic/remediation and P2 cold review | Existing M0 and quality gates |
| 2 — Disciplined simplicity and common lenses | Tier 1 | P3 rejection record and P4 cross-cutting lenses | Phase 1 signals/review contract |
| 3 — Portfolio proof | Tier 1 | P5 evidence-backed case study | Phases 1–2 evidence |
| 4 — Measured workflow depth | Tier 2 | P6–P9 only where Tier 1 use exposes friction | Tier 1 cold-review findings |
| 5 — Validation and optional polish | Required verification; Tier 3 optional | Structural/traceability audit, then only justified polish | Selected prior work |

## Tier 1 — Required, highest leverage

### P1. M0 entry diagnostic and targeted remediation

**Problem:** A uniform starting point either bores experienced learners or strands learners with gaps; neither should weaken the M0 gate.

**Change:** Add a short, executable diagnostic covering Git/shell, Python/typing, HTTP, test interpretation, and environment/configuration. Route each failed signal to a bounded remediation exercise and re-check. A strong diagnostic result may reduce practice repetition, never bypass Core acceptance. Avoid a large prerequisite course.

**Affected files:** `milestones/m0-engineering-baseline/README.md`, `CHALLENGE.md`, `ACCEPTANCE.md`, `REVIEW.md`, and a reusable `templates/ENTRY-DIAGNOSTIC.md`; update `CURRICULUM.md` only for routing visibility.

**Dependencies:** Existing M0 clean-checkout contract and A/B/C policy. **Acceptance evidence:** every diagnostic item has a command or artifact, pass/fail interpretation, remediation target, re-check, and explicit no-skip rule. **Validation:** links resolve; M0 retains existing C/A IDs or any changes update the 58-concept matrix; 11×7 remains exact. **Risks:** gate inflation, testing trivia, discouraging novices, or turning prior experience into an exemption.

### P2. Global cold-review gate

**Problem:** Author self-review can reproduce the author’s assumptions; passing automation alone does not prove another engineer can understand and operate the work.

**Change:** Add one cumulative cold-review requirement to the global definition of done. The reviewer uses a clean checkout and only repository docs to reproduce one core path, one failure, and one explanation. Solo learners may wait for context decay and review without implementation notes or use a peer; AI may critique but cannot be the sole source of claimed independent evidence.

**Affected files:** `QUALITY-GATES.md`, `.github/pull_request_template.md`, `templates/EVIDENCE-INDEX.md`, and `PROGRESS.md` dashboard fields. Milestone acceptance files should reference the global gate only where local clarification is essential; do not paste it eleven times.

**Dependencies:** P1 clarifies clean-entry instructions; existing advancement workflow. **Acceptance evidence:** named review mode/date/reference commit, commands attempted, confusion/defects found, resolution, and reviewer verdict. **Validation:** a dry-run against one milestone shows the gate is executable and non-duplicative. **Risks:** fake independence, unavailable peers, excessive delay, sensitive evidence exposure.

### P3. Complexity-rejection record

**Problem:** The curriculum tells learners to avoid unjustified complexity but preserves only adopted consequential decisions; valuable evidence of saying “no” disappears.

**Change:** Add a one-page record for a proposed tool/abstraction that was rejected or removed: pressure, simplest baseline, evidence, alternatives, lifecycle/operational cost, decision, and revisit trigger. Keep it lighter than an ADR and link it from PR/evidence. Require at least one meaningful rejection by M4 and revisit it when optional infrastructure is evaluated in M7/M9/M10.

**Affected files:** `templates/COMPLEXITY-REJECTION.md`, `STACK.md`, `QUALITY-GATES.md`, `.github/pull_request_template.md`, M4 `CHALLENGE.md`/`ACCEPTANCE.md`, and focused references in M7/M9/M10 `TOOLS.md` or `REVIEW.md`.

**Dependencies:** Existing earned-tool table and ADR threshold. **Acceptance evidence:** one real rejected/removed option tied to observed evidence and a measurable revisit trigger; clearly not an ADR. **Validation:** no required new infrastructure; reviewer can distinguish rejection record from ADR. **Risks:** performative rejection, documenting trivial choices, or creating an anti-tool ideology.

### P4. Cross-cutting career-shifter and data-specialist lenses

**Problem:** The same engineering competencies transfer to different backgrounds, but learners are not prompted to translate evidence or close predictable gaps.

**Change:** Add two concise lenses to the roadmap and review prompts, never separate sequences. Career-shifter lens: vocabulary translation, debugging narration, review communication, and connecting prior-domain judgment to requirements/incidents. Data-specialist lens: SQL/modeling strength translated into API contracts, transactional application behavior, security, service ownership, and operation. Each lens selects alternative reflection/evidence framing while all learners pass identical Core gates.

**Affected files:** `CURRICULUM.md` canonical lens definitions; `templates/EVIDENCE-INDEX.md`; targeted `REVIEW.md` files at M0, M2, M4, M6, M9, and M10; README deliverables link if needed.

**Dependencies:** P1 diagnostic identifies gaps; P2 tests whether explanations transfer. **Acceptance evidence:** each lens appears at entry, middle, and capstone; prompts produce concrete artifacts or explanations while acceptance criteria remain identical. **Validation:** search confirms no new track/directory/milestone; no gate is easier by persona. **Risks:** stereotypes, duplicated curriculum, career coaching displacing engineering, or data work becoming a separate syllabus.

### P5. Portfolio case-study template

**Problem:** Raw repositories and screenshots do not demonstrate engineering judgment to a hiring reviewer or stakeholder.

**Change:** Add a compact case-study template grounded in existing evidence: ambiguous problem, constraints, smallest design, failure discovered, diagnosis, decision/trade-off, before/after proof, security/operations/recovery, personal contribution, and limitations. Require one evolving case study, finalized at M10; allow M4 or M7 as an interim checkpoint. Explicitly prohibit fabricated metrics and secret/customer data.

**Affected files:** `templates/PORTFOLIO-CASE-STUDY.md`, `QUALITY-GATES.md`, `PROGRESS.md` dashboard/link field, M4 and M10 `ACCEPTANCE.md`/`REVIEW.md`, and README deliverables.

**Dependencies:** P2 cold review and P3 decision evidence strengthen credibility; existing evidence index. **Acceptance evidence:** every claim links to repository evidence; before/after metrics retain context; limitations and ownership are explicit; cold reviewer can follow the narrative. **Validation:** template has no required screenshot or external hosting and does not duplicate the evidence index. **Risks:** marketing over truth, excessive writing, leaking sensitive data, or rewarding visual polish over engineering.

## Tier 2 — Optional workflow depth after Tier 1

### P6. Product/stakeholder change brief

**Change/affected files:** Extend `templates/REQUIREMENTS.md` with stakeholder, decision owner, conflicting needs, change request, acceptance negotiation, and out-of-scope decision. Exercise it in M1 and again against existing software in M4 or M10; update `.github/ISSUE_TEMPLATE/milestone.yml` and the selected `CHALLENGE.md`/`ACCEPTANCE.md` files.

**Dependencies:** P2 cold review and existing requirements examples. **Acceptance evidence:** before/after requirement, decision owner/trail, negotiated acceptance change, and linked tests. **Validation:** a reviewer can distinguish requested outcome from proposed implementation; no fictional meeting artifact is mandatory. **Risk:** role-play replacing product behavior.

### P7. Data-lifecycle review where data actually changes form

**Change/affected files:** Add `templates/DATA-LIFECYCLE.md` covering source, purpose, classification, storage, derived/cached/queued copies, retention, export/deletion, access, and recovery. Link it only from applicable M2/M5/M6/M7/M9/M10 `REVIEW.md`/`ACCEPTANCE.md` files.

**Dependencies:** Existing schemas, security, queue, cache, and recovery work. **Acceptance evidence:** trace one representative field through copies and prove deletion/retention/recovery or record a precise deferral. **Validation:** every milestone reference corresponds to a real data transformation; identical boilerplate is absent. **Risk:** privacy paperwork disconnected from schema and operations.

### P8. Preserve-the-failure PR guidance

**Change/affected files:** Clarify in `challenges/README.md`, `.github/pull_request_template.md`, `QUALITY-GATES.md`, and `templates/EVIDENCE-INDEX.md` that production defects are removed while minimal reproduction, sanitized before-output, diagnosis, and regression test remain reviewable. Define the narrow use of disabled fixtures and prohibit callable insecure/broken production paths.

**Dependencies:** Existing seeded challenge lifecycle and evidence index. **Acceptance evidence:** one example PR shape distinguishes retained evidence from removed defect. **Validation:** guidance bounds artifact size, sanitization, and execution safety. **Risk:** dangerous code or huge logs being retained.

### P9. Active milestone dashboard

**Change/affected files:** Refine `PROGRESS.md` current focus into a compact dashboard: active milestone/level, branch or issue, current C/A IDs, evidence gaps, cold-review state, top risk, blocked decision, next smallest action, and last validated commit/date. Link it from README only if discoverability remains weak.

**Dependencies:** P2 cold-review state and existing progress ledger. **Acceptance evidence:** a filled synthetic example can identify the next action without repeating journal/evidence detail. **Validation:** every field routes a decision or link and the historical ledger stays intact. **Risk:** duplicate status bookkeeping.

## Tier 3 — Optional polish, only if friction remains

- Add validator checks for newly stable Tier 1 artifact headings/links only after wording settles; avoid encoding prose style.
- Add an optional cold-review GitHub issue template if actual use shows the milestone issue/PR cannot carry review cleanly.
- Curate verified primary-resource links milestone by milestone only when maintenance ownership and version policy are clear.
- Add a one-page maintainer release checklist only if `TODO.md`, Actions, and the PR template prove insufficient.
- Improve navigation anchors or compact diagrams only when cold reviewers report discoverability problems.

## Implementation outcome — 2026-09-13

- **P1–P5 implemented:** bounded M0 diagnostic/remediation, cumulative peer/solo cold review, lightweight complexity rejection, common career-shifter/data-specialist lenses, and an evidence-backed M4→M10 portfolio case study.
- **P6–P9 implemented after review:** each consumes existing work and directly improves requirement change, field-level data ownership, safe failure evidence, or next-action visibility. Scope is limited to the milestones where the behavior occurs; no new track or process service was added.
- **Tier 3 implemented:** stable validator checks for required templates/headings, README navigation, and empty files. This catches structural drift without grading prose.
- **Tier 3 declined:** a separate cold-review issue template duplicates the PR/evidence flow; a maintainer checklist duplicates `TODO.md` plus the PR template; extra diagrams/navigation are unsupported by the cold read. **Deferred:** live resource-link curation until a maintainer owns version review; existing milestone resource-selection standards remain safer than stale links.

### Maintenance cold-review record

An isolated read-only copy was created under `/tmp` with `mktemp`, `cp -a`, and `chmod -R a-w`; only public repository docs were used. The validator passed there, D1 repository/status interpretation and D2 Decimal command were executed, and navigation/template/gate assertions passed. D3–D5 were **not run** because no learner application exists; only their placeholders, expected interpretation, remediation routes, and no-skip rule were inspected. This is curriculum-maintenance validation, not learner evidence.

The first review script used an overly literal wording assertion for the lens rule; it failed, was diagnosed as a reviewer-check defect because the document already said “neither creates a track,” and the corrected semantic check passed. The cold read found no duplicated global gate, persona-specific acceptance, missing required navigation, or need for another issue/checklist/diagram artifact.

### Final critical-review findings

- **Navigation:** the README table exposes each new contract once; details remain in canonical templates/global rules.
- **Duplication and gate conflict:** global cold-review/preserve-failure rules are not copied across eleven milestones; local files add only milestone-specific evidence.
- **Gate integrity and personas:** lenses change prompts, never Core criteria; M0 diagnostic routes practice but grants no exemption.
- **Paperwork:** stakeholder briefs appear only at M1/M4, lifecycle review only where data changes form, one rejection record is required by M4, and the case study is a link layer over evidence.
- **Safety:** failure artifacts must be isolated/sanitized; data and portfolio templates prohibit fabricated or sensitive evidence.

## Recommended implementation order

1. Implement P1 so later reviews have a consistent learner-entry and remediation contract.
2. Implement P2 globally before local milestone edits; dry-run it against M0.
3. Implement P3, because explicit simplicity decisions should shape optional-tool work.
4. Implement P4 across the roadmap and selected reviews, checking that gates remain common.
5. Implement P5 last within Tier 1 so it can consume diagnostic, cold-review, and decision evidence.
6. Run all validation and a duplication/link audit; close Tier 1 only after a cold read.
7. Decide each Tier 2 item independently from observed friction; recommended sequence is P6 → P7 → P8 → P9.
8. Treat Tier 3 as a backlog, not implied scope.

Within every package: update the canonical global/template file first, add only focused milestone references second, update [TODO.md](TODO.md) immediately, then run validation. Avoid mixing packages in one review unit.

## Definition of plan completion

The required revision is complete when P1–P5 are checked in `TODO.md`; all new artifacts are linked rather than duplicated; one audit confirms identical Core gates across learner lenses; the cold-review and case-study requirements are executable from a clean checkout; the validator, link scan, 58-concept traceability, GitHub YAML, exact 11×7 structure, legacy-path scan, and Git-state checks pass; and Tier 2/Tier 3 items are explicitly retained, promoted with rationale, or declined—not silently implemented.
