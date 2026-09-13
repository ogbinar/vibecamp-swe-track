# Complexity rejection record

Use this for one meaningful tool, abstraction, or service considered and rejected/removed. It is lighter than an ADR: no architecture was adopted. If a costly-to-reverse architecture is chosen, use [ADR.md](ADR.md) instead.

- Date, milestone, issue/PR:
- Candidate and decision: `REJECTED` or `REMOVED`

## Observed pressure

Name the concrete duplication, latency, failure, or maintenance cost. Link the baseline evidence; “best practice” is not pressure.

## Smallest current solution

Describe what already meets the requirement and its known limit.

## Candidate comparison

| Option | Measured benefit | New failure/operations/lifecycle cost | Reversibility |
|---|---|---|---|
| Keep baseline |  |  |  |
| Candidate |  |  |  |

## Decision and boundary

Why is rejection/removal the smallest correct choice now? State what work is intentionally not done.

## Revisit trigger

Name a measurable condition, owner, and evidence command that would reopen the decision. Do not reject tools permanently or create records for trivial choices.
