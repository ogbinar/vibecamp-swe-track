# Curriculum maintenance

Learners start at the [course home](../../README.md#start-now).

- [Current plan and decisions](../../PLAN.md): scope, dependencies and rationale.
- [Active checklist](../../TODO.md): the only maintenance completion ledger.
- [Usability rubric](usability.md): structural, starter, and human claims
  are separate.
- [Subtraction cleanup evidence](subtraction-cleanup.md): current ownership,
  rollback, contract decisions, local checks, and external limits.
- [Semantic-audit worksheet](templates/SEMANTIC-AUDIT.md): verify that a
  consolidation preserves requirements, scenarios, Core checks, and evidence.
- [Transition-review worksheet](templates/TRANSITION-REVIEW.md): record a
  maintainer or authorized human traversal without overstating the review mode.
- [Agent contract](../../AGENTS.md): curriculum constraints and change discipline.

The immutable rollback source for the active cleanup is commit `8942980`.
Historical planning snapshots were removed from the default branch after their
active decisions were retained in PLAN, TODO, AGENTS, and the current evidence.

Seeded challenges expose a symptom and success condition while leaving diagnosis
and design to the learner. A supplied deterministic fixture is appropriate when
diagnosis is the skill; learners construct the harness when harness design is
the skill. Keep defects out of production paths, preserve only safe sanitized
failure evidence, and never retain secrets, real personal data, callable
vulnerable routes, destructive defaults, or bulky logs.

From the repository root, run `python3 scripts/check_curriculum.py`,
`python3 scripts/test_validator_mutations.py`, and `git diff --check`.
Expected: structure/links/mutations pass with explicit human-evidence limits.
If a check fails, repair the smallest affected contract and rerun it before
checking an item in TODO. Hosted runs, named humans and real-target evidence
must remain open until actually observed. Preserve pre-existing dirty work.
