# Quality gates and definition of done

## Cumulative maturity levels

- **Level A — Works:** observable functionality behaves as expected at its public boundary.
- **Level B — Engineered:** Level A plus validation, appropriate unit/integration/API tests, coherent boundaries, data integrity, and explicit failure handling.
- **Level C — Production:** Levels A and B plus context-appropriate security, observability, deployment, migrations, operational behavior, documentation, recovery thinking, and disciplined release.

These are cumulative, contextual gates—not three versions of every feature. For example, M1 proves selected Level B qualities at the API boundary but cannot claim Level C while state is volatile and operational controls do not exist. Each milestone `ACCEPTANCE.md` declares what applies now.

## Reusable definition of done

Every milestone is complete only when:

1. Every Core criterion links to reproducible evidence; Stretch is separately marked and non-blocking.
2. The documented clean-checkout setup, lint, test, and relevant run/migration commands succeed.
3. Acceptance behavior is proven at the public boundary; important rules are also proven at their owning unit/database/integration boundary.
4. At least one seeded defect fails for the intended reason, is diagnosed rather than replaced wholesale, and gains a regression test.
5. Failure drills record environment, command/setup, expected result, actual result, interpretation, recovery, and date.
6. Security, data, migration, dependency, and rollback impacts are reviewed; no unresolved critical/high correctness or security defect remains.
7. Actions pass, the PR self-review is complete, and `PROGRESS.md` links the issue, final PR, evidence index, and release/tag.
8. The learner answers `REVIEW.md` in their own words and can reproduce, explain, modify, and debug the result.
9. A cold reviewer reproduces one Core path and one failure from a clean checkout using repository instructions, records confusion/defects and their resolution, and gives a verdict against the same gate.

A screenshot alone is not correctness evidence. Prefer tests, sanitized HTTP captures, migration transcripts, constraint failures, query plans, load summaries, telemetry correlations, and restore records. Never fabricate a passing result.

## Cold-review protocol

Use either a peer who did not author the change or a **solo fresh-context review**: start from the candidate commit in a clean clone/worktree after putting implementation notes aside; use only course/project docs; predict results before commands; reproduce one representative Core behavior and one documented failure; then answer one `REVIEW.md` question. Record mode, reviewer, date, reference commit, commands, gaps found, fixes, and `PASS`/`NEEDS WORK` in the evidence index.

For an uncommitted curriculum-maintenance audit, an isolated copy may be used and must be labeled maintenance validation, never learner gate evidence. AI can suggest review questions but cannot be the sole independent reviewer for a learner claim. A cold review samples reproducibility and explanation; it does not replace automated or milestone-specific evidence.

## Evidence worth preserving

Remove defects from callable production paths, but retain the smallest safe failing test/harness, sanitized before-output, diagnosis, and regression test. A disabled vulnerable fixture is allowed only when isolated, unmistakably non-production, and safe by default. Do not retain secrets, exploitable routes, database dumps, or oversized raw logs.

Use a [complexity rejection record](templates/COMPLEXITY-REJECTION.md) for a meaningful tool/abstraction considered and rejected or removed; use an [ADR](templates/ADR.md) for consequential architecture actually adopted. At M4, draft the [portfolio case study](templates/PORTFOLIO-CASE-STUDY.md) from evidence; at M10, cold-review its final form. These are course checkpoints, not extra versions of every milestone feature.

## Advancement workflow

1. Open one milestone issue; translate ambiguity into acceptance examples and identify seeded scenarios.
2. Work in focused branches/PRs. Draft PRs expose assumptions early; multiple coherent PRs are welcome.
3. Follow the complete learning cycle and update the evidence index as facts emerge.
4. Let Actions run the repository validator plus project-specific lint/tests/migration checks when code exists.
5. Perform written self-review and cold review, close all Core gaps, merge through normal review, and update `PROGRESS.md`.
6. Create an annotated `mN-short-name` tag on the reviewed commit. Add a GitHub Release when behavior, artifacts, or operational instructions are user-facing.
7. If later evidence invalidates a gate, mark it `REOPENED`, link a regression issue, fix forward, and add a regression test. Never move a passed tag.

Large raw artifacts may be release assets with checksums; concise indexes and conclusions stay in the repository.
