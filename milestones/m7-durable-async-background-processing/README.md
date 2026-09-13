# M7 — Durable Background Processing

[Course home](../../README.md) / M7

**Milestone 8 of 11 · M7**

## Why

The API accepted fulfillment work, then the process died before the work ran.
Persist the obligation before acknowledging it and make repetition safe.

## Starting checkpoint

- **At a glance:** Durable · Ecommerce.
- **You will leave with:** Persisted job/outbox flow; Crash/duplicate/quarantine/replay evidence.
- **Gate:** [A1–A5 / C for async slice](ACCEPTANCE.md#core).
- **Repository support:** supplied starter locally verified; your learner gate needs your own evidence. [Dated scope and limits](../../USABILITY.md#readiness-status-vocabulary)
separate local structure/starter checks from pending hosted and human evidence.
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/ecommerce/README.md#ecommerce-launch-kit-for-m5), then return to the saved block; first visit: [Block 1](#1-preserve-accepted-intent-required).

Start from `m6-resilient-integrations`. Run ecommerce tests and reproduce one
idempotent external operation before introducing a worker.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Terms used here

- **Durable intent:** a committed record that work is owed.
- **Outbox:** business state and pending work stored in one database transaction.
- **Worker:** a separate process claiming and executing jobs.
- **At-least-once:** a job may run again after a crash.
- **Lease:** time-bounded ownership allowing abandoned work to be reclaimed.
- **Poison work:** a repeatedly failing job moved aside for investigation.
- **Eventual consistency:** related views become consistent after background work finishes.

## Product brief

Follow the [job contract](../../projects/ecommerce/specs/M7-JOB-CONTRACT.md).
First demonstrate that FastAPI `BackgroundTasks` loses accepted work on process
death. Then build a PostgreSQL-backed outbox, worker, claim/lease behavior,
bounded retries, quarantine, and replay. Complete C1–C3 in
[CHALLENGE.md](CHALLENGE.md#m7-challenge-brief), killing the process before and after each durable
boundary. Do not claim exactly-once execution.

Taskiq is optional only after the database semantics pass. It must not replace
persisted intent or idempotent consumers.

From `projects/ecommerce/`, run:

```bash
uv run --locked pytest tests/test_failure_harnesses.py -q -k worker
```

Expected: two green harness tests expose the after-effect/before-acknowledgement
crash window and show two effects after naive replay. Keep those observations;
your database-backed worker must add a separate assertion for one semantic effect.

## Work blocks

### 1. Preserve accepted intent `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/ecommerce/`;
focus on `tests/m7/test_worker.py` and the output named below. Record `evidence/M7/intent.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 1](#1-preserve-accepted-intent-required) using that saved result; continue to Block 2.
When needed: [C1 scenario and hints](CHALLENGE.md#c1--lost-accepted-work) and [concept explanation](CONCEPTS.md#the-api-accepted-work-then-died). [Tool boundaries](TOOLS.md#tools-earned-here) apply to this product.

Read the [job contract](../../projects/ecommerce/specs/M7-JOB-CONTRACT.md).
First run the supplied kill-window tests. Then add outbox metadata and store
business state plus intent in one transaction. Record the before/after crash
observation in `evidence/M7/intent.md`. Stop when accepted work survives restart.

### 2. Claim, retry, and deduplicate `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/ecommerce/`;
focus on `tests/m7/test_worker.py` and the output named below. Record `evidence/M7/execution.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 2](#2-claim-retry-and-deduplicate-required) using that saved result; continue to Block 3.
When needed: [C2 scenario and hints](CHALLENGE.md#c2--duplicate-execution) and [concept explanation](CONCEPTS.md#the-worker-sent-the-email-twice).

Build one-worker and competing-worker commands using injected clock, IDs, and
kill hooks. Exercise lease expiry and after-effect/before-acknowledgement replay.
Observe one semantic effect with visible attempt history. Record
`evidence/M7/execution.md`. Stop when no job remains permanently leased.

### 3. Quarantine and authorized replay `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/ecommerce/`;
focus on `tests/m7/test_worker.py` and the output named below. Record `evidence/M7/replay.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 3](#3-quarantine-and-authorized-replay-required) using that saved result; continue to [Evidence](#evidence).
When needed: [C3 scenario and hints](CHALLENGE.md#c3--poison-and-backlog-incident) and [concept explanation](CONCEPTS.md#one-poison-job-stopped-healthy-work).

Move poison work aside without blocking healthy work. Implement a replay command
with actor, reason, bounded IDs, preview, confirmation, and audit. Execute the
runbook twice and record `evidence/M7/replay.md`. Stop when the second run is
safe and backlog metrics explain every job.

Create the named integration file, then use these stable invocations:

```bash
uv run --locked pytest tests/m7/test_worker.py -q -k one_worker
uv run --locked pytest tests/m7/test_worker.py -q -k competing_workers
uv run --locked pytest tests/m7/test_worker.py -q -k lease_expiry
uv run --locked pytest tests/m7/test_worker.py -q -k after_effect
uv run --locked python scripts/replay_jobs.py --actor learner --reason "recover synthetic poison job" --message-id synthetic-1
```

The final command is a preview until `--confirm` is added. Before your durable
implementation it exits rather than pretending to replay. Evidence records one
semantic effect and visible attempt history for each test.

### Literal command map

Run from `projects/ecommerce/`; create `tests/m7/test_worker.py` before expecting green.

Before: the named kill/replay case loses or repeats work. After: the row’s stop
condition is green with durable state and attempt history recorded.

| Block | Copyable command | Expected stop condition |
|---|---|---|
| 1 | `uv run --locked pytest tests/m7/test_worker.py -q -k accepted_intent` | A committed obligation survives API termination and later completes. |
| 2 | `uv run --locked pytest tests/m7/test_worker.py -q -k 'one_worker or competing_workers or lease_expiry or after_effect'` | Attempt history remains visible, leases recover, and one semantic effect occurs. |
| 3 | `uv run --locked pytest tests/m7/test_worker.py -q -k poison && uv run --locked python scripts/replay_jobs.py --actor learner --reason 'recover synthetic poison job' --message-id synthetic-1` | Poison work is isolated and repeated preview/replay is bounded and auditable. |

An absent target is the create-it signal. Recover by stopping workers, expiring
only the synthetic lease through the injected clock, and rerunning one selector.
Record the next selector before pausing.

Pause: record the job ID, state, attempt, kill point, and next selector.

## Failures and hints

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Evidence

Answer [review prompts](REVIEW.md#review) after the Core proof.

Prove [A1–A5](ACCEPTANCE.md#core) with crash/replay counts, backlog metrics,
duplicate-effect prevention, poison-work recovery, and an executed runbook.

## Done when

Accepted durable work survives every kill point, duplicate delivery has one
semantic effect, poison work is isolated, and Core passes. Tag `m7-durable-async`.

## Recovery

Use [targeted references](RESOURCES.md#resources-for-m7) only for the question left by the active hint ladder.

Stop claims, inspect durable job state, follow the authorized replay runbook, and
return to the last green migration before changing retry code.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

## Next

Continue to [M8](../m8-concurrency-booking/README.md).

[Previous milestone: M6](../m6-resilient-external-integrations/README.md) · [Course home](../../README.md) · [Next milestone: M8](../m8-concurrency-booking/README.md)
