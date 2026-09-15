# Requirements-to-evidence semantic audit

Use this maintainer worksheet before releasing a milestone. Structural checks
can prove that files and identifiers exist; this review checks that they mean
the same thing.

| Requirement and source | Challenge ID and mode | Acceptance ID | Exact command | Expected observation | Evidence path | Result |
|---|---|---|---|---|---|---|
| | `PROVIDED` / `YOU BUILD` | | | | | Pass / repair |

For each Core behavior, read the row left to right and then right to left. Fail
the audit if a requirement has no exercise, an acceptance check introduces new
behavior, a command cannot demonstrate the claim, or the evidence would not let
a second person reproduce it. Record new conflicts in [PLAN.md](../../../PLAN.md),
track repairs in [TODO.md](../../../TODO.md), and repair the canonical product
contract before editing tests.

This worksheet does not measure whether a learner understands the lesson. Use a
human transition review for that claim.
