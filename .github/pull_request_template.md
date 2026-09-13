## Outcome

PR mode: `WORKING` / `MILESTONE GATE`

For a working PR, complete Outcome, narrow checks, risk, and next step; mark
later gate-only fields `N/A — milestone gate not reached`. For a milestone-gate
PR, complete every applicable section and link evidence.

What observable behavior or course artifact changed?

Closes #

- Stakeholder/decision owner and changed acceptance (when applicable):
- Smallest next action if this is a working PR:

## Gate evidence

- Milestone/core A-criterion and challenge C-ID:
- Evidence link:
- Clean-clone or setup command:
- Test/check commands and results:
- Failure drill and recovery:
- Preserved safe reproduction + sanitized before-output + regression proof:
- Data-lifecycle evidence or why not applicable:

## Risk and operations

- Security/data impact:
- Migration/deployment impact:
- Rollback plan (or why none):
- New dependency/service and evidence it is earned:
- Complexity rejected/removed and revisit trigger (when applicable):

## AI assistance and verification

- Assistance used:
- What I independently explained, reproduced, modified, and debugged:

## Self-review

- [ ] Acceptance examples pass at the public boundary.
- [ ] Core exit criteria link to evidence; stretch is clearly separated.
- [ ] Tests fail for the intended seeded defect and pass after restoration.
- [ ] Docs, configuration examples, and progress ledger are current.
- [ ] The full problem-first learning cycle and required maturity level are evidenced.
- [ ] No secrets, personal data, generated environments, or unrelated changes are included.

## Cold review

- Mode (`peer` or `solo fresh-context`), reviewer/date/reference commit:
- Clean-checkout command, Core path, and failure reproduced:
- Confusion or defects found and resolved:
- Verdict: `PASS` / `NEEDS WORK`
