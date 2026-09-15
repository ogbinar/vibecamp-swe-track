# MN evidence index

Store this file at `projects/<active-product>/evidence/MN/index.md`. Commands in
the milestone may say `evidence/MN/...` because their declared working directory
is that project. Copy this template only on first visit; preserve the existing
index when resuming.

## Context

- Date/environment/reference commit:
- Issue and PR:
- Required maturity level:
- Clean-checkout setup command:

## Acceptance mapping

| Criterion | Evidence link or command | Expected | Actual | Interpretation |
|---|---|---|---|---|
| A1 |  |  |  |  |

## Failure drills

| Scenario | Hypothesis | Reproduction | Diagnosis | Fix/regression proof | Recovery |
|---|---|---|---|---|---|
| C1 |  |  |  |  |  |

Preserve the minimal failing test/harness, sanitized before-output, diagnosis, and regression proof. Remove the defect from the callable production path. A disabled vulnerable fixture is acceptable only when isolated, clearly labeled non-production, safe by default, and needed to reproduce the lesson.

## Cross-cutting lens (same gate, optional framing)

- Career-shifter: prior-domain judgment translated into one requirement, debugging explanation, or review decision:
- Data-specialist: data/SQL strength translated into one API, transaction, security, ownership, or operational decision:
- Neither lens selected / another background framing:

## Review and release

- Learner answers to the milestone acceptance `Review` section:
- Cold-review mode (`peer` or `solo fresh-context`), reviewer/date/reference commit:
- Cold-review clean-checkout command, core path, failure reproduced, confusion/defects found, resolution, verdict:
- Security/data/migration/rollback review:
- Actions run:
- Annotated tag/release/checksums:
- Known limitations and next risk:

Redact credentials and personal data. Link source/tests instead of copying them; attach large generated evidence to a release with a checksum.

## Synthetic examples (shape only)

These examples are not learner evidence and never establish a passing claim.

| Slice | Useful evidence | Not enough |
|---|---|---|
| Migration | revision before/after, command, preserved legacy rows, recovery decision | “migration works” |
| Security | synthetic actor/object request, expected denial, actual status/body, unchanged row | screenshot of login |
| Worker | kill point, attempt history, duplicate deliveries, one semantic effect | one happy job |
| Performance | fixed dataset/environment, query count/plan, equal-harness percentiles, correctness test | fastest run |
| Recovery | backup checksum, isolated target, integrity/tenant/audit checks, measured RPO/RTO | backup file exists |

Mark irrelevant fields `N/A — <condition not present>`; never fabricate a
command or result.
