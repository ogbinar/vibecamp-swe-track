# Curriculum maintenance

Learners start at the [course home](../../README.md#start-now).

- [Current plan and decisions](../../PLAN.md): scope, dependencies and rationale.
- [Active checklist](../../TODO.md): the only maintenance completion ledger.
- [Usability rubric and review evidence](../../USABILITY.md): structural, starter,
  and human claims are separate.
- [Pre-migration business-first career-shifter review](business-first-career-shifter-review.md):
  historical diagnosis of product framing and the former milestone layout; the
  resolved current contract lives in PLAN and TODO.
- [Agent contract](../../AGENTS.md): curriculum constraints and change discipline.
- [Persona review index](../../PERSONA-REVIEW.md) and
  [analysis index](../../ANALYSIS.md): concise routes to dated inputs; current
  decisions live in PLAN.
- [2026-09-15 business-first provenance, rollback, and history bundle](archive/2026-09-15-business-first/README.md):
  all 44 removed-source hashes, merge destinations, pilot evidence, and the
  complete pre-closeout PLAN/TODO/USABILITY/analysis snapshots.
- [2026-09-13 provenance and removal manifest](archive/2026-09-13-remediation/README.md):
  protected paths, dispositions, cache regeneration and validation evidence.

From the repository root, run `python3 scripts/check_curriculum.py`,
`python3 scripts/test_validator_mutations.py`, and `git diff --check`.
Expected: structure/links/mutations pass with explicit human-evidence limits.
If a check fails, repair the smallest affected contract and rerun it before
checking an item in TODO. Hosted runs, named humans and real-target evidence
must remain open until actually observed. Preserve pre-existing dirty work.
