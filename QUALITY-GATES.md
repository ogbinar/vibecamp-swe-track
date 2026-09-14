# Quality gates and definition of done

## Cumulative maturity levels

- **Level A — Works:** observable functionality behaves as expected at its public boundary.
- **Level B — Engineered:** Level A plus validation, appropriate unit/integration/API tests, coherent boundaries, data integrity, and explicit failure handling.
- **Level C — Production:** Levels A and B plus context-appropriate security, observability, deployment, migrations, operational behavior, documentation, recovery thinking, and disciplined release.

These are cumulative, contextual gates—not three versions of every feature. For example, M1 proves selected Level B qualities at the API boundary but cannot claim Level C while state is volatile and operational controls do not exist. Each milestone `ACCEPTANCE.md` declares what applies now.

## Universal definition of done

Every milestone is complete only when:

1. Every Core criterion links to reproducible evidence; Stretch is separately marked and non-blocking.
2. The documented clean-checkout setup, Ruff lint/format, mypy, test, and relevant run/migration commands succeed. The production run command uses the declared ASGI runtime without development reload.
3. Acceptance behavior is proven at the public boundary; important rules are also proven at their owning unit/database/integration boundary.
4. At least one seeded defect fails for the intended reason, is diagnosed rather than replaced wholesale, and gains a regression test.
5. Failure drills record environment, command/setup, expected result, actual result, interpretation, recovery, and date.
6. Actions pass, the milestone-gate PR self-review is complete, and
   `PROGRESS.md` links the issue, PR, evidence index, and tag.
7. The learner answers `REVIEW.md` in their own words and can reproduce,
   explain, modify, and debug the result.

## Conditional gates

Apply a row only when its condition is true. In the evidence index, write
`N/A — condition not present` instead of inventing evidence.

| Condition | Additional required proof |
|---|---|
| Stores durable data | clean migration, existing-data case, constraints, rollback/roll-forward decision |
| Handles identity or private data | threat cases, authorization scope, secret/personal-data scan, redacted logs |
| Calls an external system | timeout/retry/idempotency contract, unknown outcome, reconciliation |
| Accepts durable background work | persisted intent, kill point, duplicate execution, replay/recovery |
| Claims performance improvement | representative workload, equal harness, correctness guard, before/after evidence |
| Uses cache or realtime state | authority, staleness/gap/outage policy, invalidation or replay proof |
| Claims production deployment | immutable artifact, readiness, migration order, secret custody, backup/restore, rollback/roll-forward |
| Reaches a milestone gate | cold reviewer reproduces one Core path and one failure; record verdict |

External evidence is classified separately. All milestones complete their local
Core without credentials. M6 has one required, separately authorized sandbox
experiment for the stronger real-provider claim; unavailable access remains
`PENDING — ACCESS/PROVIDER OUTAGE`. M7 email and M10 storage, OAuth/OIDC,
monitoring, SQLAdmin, and real deployment are optional endorsements. No fake,
local simulation, or CI run may be presented as provider or deployment evidence.

A screenshot alone is not correctness evidence. Prefer tests, sanitized HTTP captures, migration transcripts, constraint failures, query plans, load summaries, telemetry correlations, and restore records. Never fabricate a passing result.

Evidence is owned by the active product: while working in
`projects/<product>/`, write `evidence/MN/...`, which resolves to
`projects/<product>/evidence/MN/...`. Root documents spell out the qualified
path. Keep an existing index on resume; never overwrite it by copying the
template again.

## Cold-review protocol

Use either a peer who did not author the change or a **solo fresh-context review**: start from the candidate commit in a clean clone/worktree after putting implementation notes aside; use only course/project docs; predict results before commands; reproduce one representative Core behavior and one documented failure; then answer one `REVIEW.md` question. Record mode, reviewer, date, reference commit, commands, gaps found, fixes, and `PASS`/`NEEDS WORK` in the evidence index.

For an uncommitted curriculum-maintenance audit, an isolated copy may be used and must be labeled maintenance validation, never learner gate evidence. AI can suggest review questions but cannot be the sole independent reviewer for a learner claim. A cold review samples reproducibility and explanation; it does not replace automated or milestone-specific evidence.

## Evidence worth preserving

Remove defects from callable production paths, but retain the smallest safe failing test/harness, sanitized before-output, diagnosis, and regression test. A disabled vulnerable fixture is allowed only when isolated, unmistakably non-production, and safe by default. Do not retain secrets, exploitable routes, database dumps, or oversized raw logs.

Use a [complexity rejection record](templates/COMPLEXITY-REJECTION.md) for a meaningful tool/abstraction considered and rejected or removed; use an [ADR](templates/ADR.md) for consequential architecture actually adopted. At M4, draft the [portfolio case study](templates/PORTFOLIO-CASE-STUDY.md) from evidence; at M10, cold-review its final form. These are course checkpoints, not extra versions of every milestone feature.

## Advancement workflow

1. Open one milestone issue; translate ambiguity into acceptance examples and identify seeded scenarios.
2. Use a **working PR** for one focused behavior: narrow tests, risk note, and
   next step. Use one **milestone-gate PR** only after all Core work: full
   acceptance evidence, failure/recovery, review, progress update, and tag plan.
3. Follow the complete learning cycle and update the evidence index as facts emerge.
4. Let Actions run the repository validator plus project-specific Ruff, mypy, tests, migration checks, and immutable-image build when those artifacts exist. Treat this as CI; add deployment only after the M10 CD gates exist.
5. Perform written self-review and cold review, close all Core gaps, merge through normal review, and update `PROGRESS.md`.
6. Create an annotated `mN-short-name` tag on the reviewed commit. Add a GitHub Release when behavior, artifacts, or operational instructions are user-facing.
7. If later evidence invalidates a gate, mark it `REOPENED`, link a regression issue, fix forward, and add a regression test. Never move a passed tag.

Large raw artifacts may be release assets with checksums; concise indexes and conclusions stay in the repository.
