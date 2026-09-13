# Curriculum maintenance

Learners start at the [course home](../../README.md#start-now).

- [Current plan and decisions](../../PLAN.md): scope, dependencies and rationale.
- [Active checklist](../../TODO.md): the only maintenance completion ledger.
- [Usability rubric and review evidence](../../USABILITY.md): structural, starter,
  and human claims are separate.
- [Agent contract](../../AGENTS.md): curriculum constraints and change discipline.
- [Original persona review](../../PERSONA-REVIEW.md) and
  [resolution analysis](../../ANALYSIS.md): dated inputs; current decisions live in PLAN.
- [2026-09-13 provenance and removal manifest](archive/2026-09-13-remediation/README.md):
  protected paths, dispositions, cache regeneration and validation evidence.

From the repository root, run `python3 scripts/check_curriculum.py`,
`python3 scripts/test_validator_mutations.py`, and `git diff --check`.
Expected: structure/links/mutations pass with explicit human-evidence limits.
If a check fails, repair the smallest affected contract and rerun it before
checking an item in TODO. Hosted runs, named humans and real-target evidence
must remain open until actually observed. Preserve pre-existing dirty work.
