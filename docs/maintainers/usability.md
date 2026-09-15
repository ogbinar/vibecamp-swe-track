# Learner-experience and language rubric

This is a maintainer quality gate, not required learner reading. Current local
evidence is preserved in the
[subtraction-cleanup record](subtraction-cleanup.md).

## Target learner

Evaluate the Core path as a person studying alone with basic Python syntax and
basic Git use, but little production-engineering vocabulary or workflow
experience. Prior experience may shorten practice; it never lowers a Core gate.

## Scoring

Score every dimension from 0 to 4: 0 blocked, 1 high friction, 2 interpretive,
3 mostly self-service, and 4 immediate. Multiply the score by one quarter of
the weight. Release requires **85/100 overall and no dimension below 3**.

| Dimension | Weight | A score of 4 means |
|---|---:|---|
| Audience and outcome clarity | 10 | The first screen states audience, prerequisites, product path, and outcome |
| Time to first successful run | 15 | With prerequisites installed, a clean clone reaches a working product and green test within 15 minutes |
| Executable instructions | 20 | Active commands are copyable, with expected output and recovery; no placeholders remain |
| Language and terminology | 15 | The plain-language problem precedes the term; necessary terms and acronyms are defined before use |
| Progressive disclosure/navigation | 10 | One next action is obvious; reference and maintainer material are secondary |
| Guided scaffolding | 10 | The starting state is supplied while engineering decisions remain learner work |
| Automated feedback and recovery | 10 | Local and GitHub checks identify the failed gate and route to recovery guidance |
| Failure-lab reproducibility | 5 | Safe activation/reset is deterministic and does not reveal the diagnosis before the attempt |
| Pause and resume | 5 | `PROGRESS.md` reveals the next action and evidence gap in under two minutes |

## Language contract

1. Describe the concrete problem before naming the concept or pattern.
2. Define a necessary term at first use and link the glossary.
3. Expand an acronym before using it alone.
4. Write instructions as action → reason → expected observation → recovery.
5. Keep one primary requirement per learner checklist item.
6. Use one term consistently unless a distinction is explicitly taught.
7. Show a small example before an abstract rule where practical.
8. Explain M/C/A labels, Core, Stretch, levels, evidence, and cold review before
   using them as instructions.
9. Prefer short sentences and concrete verbs without removing precise terms.

## Cold-test worksheet

| Observation | Result |
|---|---|
| Environment and reference commit | |
| Time to locate first command | |
| Time to green tests and working product | |
| Wrong turns or backtracking | |
| Undefined or confusing terms | |
| Help requested from a person | |
| Commands that failed | |
| Recovery guidance used successfully | |
| Next action stated correctly | |
| Rubric dimensions and weighted score | |

Use a clean clone and public learner instructions for a real cold test. Prefer
a career shifter who did not author the material. Local fresh-context review is
useful maintenance evidence but cannot establish human comprehension.

## Readiness status vocabulary

- **STRUCTURALLY READY:** the named repository shape, links, identifiers, and
  trace contracts pass automated checks.
- **STARTER VERIFIED:** the named supplied starter and documented recovery were
  executed in the stated local environment.
- **HUMAN SELF-STUDY VERIFIED:** a named target learner completed the stated
  transition without author intervention, with environment and wrong turns
  recorded.

These statuses are independent and always name their scope.

## Current candidate status

The current candidate has one README controller per milestone. Its local
structure, starter, runtime, and recovery evidence lives in the
[subtraction-cleanup record](subtraction-cleanup.md). Superseded layout and
starter results are intentionally not repeated here because they are not
release authority.

**HUMAN SELF-STUDY VERIFIED** remains unset. Provider, hosted, deployment, and
named-human results must stay separate from local maintainer review.
