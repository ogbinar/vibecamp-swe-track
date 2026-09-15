# M7 — Finish accepted work after a crash

[Course home](../../README.md) / M7

**Milestone 8 of 11 · M7**

## Business problem

The API accepted fulfillment work, then the process died before the work ran.
Persist the obligation before acknowledging it and make repetition safe.

## Product objective

- **Product can:** accepted fulfillment work survives process failure and can be replayed safely.
- **You will prove:** persisted intent, crash-window, duplicate, quarantine, and replay evidence.

Follow the [job contract](../../projects/ecommerce/specs/M7-JOB-CONTRACT.md).
First demonstrate that FastAPI `BackgroundTasks` loses accepted work on process
death. Then build a PostgreSQL-backed outbox, worker, claim/lease behavior,
bounded retries, quarantine, and replay. Complete C1–C3 in
[challenge brief](#challenge-brief), killing the process before and after each durable
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

## Start here

- **Gate:** [A1–A5 / C for async slice](#core).
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/ecommerce/README.md#ecommerce-launch-kit-for-m5), then return to the saved block; first visit: [Block 1](#1-preserve-accepted-intent-required).

Start from `m6-resilient-integrations`. Run ecommerce tests and reproduce one
idempotent external operation before introducing a worker.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Build

### 1. Preserve accepted intent `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/ecommerce/`;
focus on `tests/m7/test_worker.py` and the output named below. Record `evidence/M7/intent.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 1](#1-preserve-accepted-intent-required) using that saved result; continue to Block 2.
When needed: [C1 scenario and hints](#c1--lost-accepted-work) and [concept explanation](#the-api-accepted-work-then-died). [Tool boundaries](#tools-earned-here) apply to this product.

Read the [job contract](../../projects/ecommerce/specs/M7-JOB-CONTRACT.md).
First run the supplied kill-window tests. Then add outbox metadata and store
business state plus intent in one transaction. Record the before/after crash
observation in `evidence/M7/intent.md`. Stop when accepted work survives restart.

### 2. Claim, retry, and deduplicate `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/ecommerce/`;
focus on `tests/m7/test_worker.py` and the output named below. Record `evidence/M7/execution.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 2](#2-claim-retry-and-deduplicate-required) using that saved result; continue to Block 3.
When needed: [C2 scenario and hints](#c2--duplicate-execution) and [concept explanation](#the-worker-sent-the-email-twice).

Build one-worker and competing-worker commands using injected clock, IDs, and
kill hooks. Exercise lease expiry and after-effect/before-acknowledgement replay.
Observe one semantic effect with visible attempt history. Record
`evidence/M7/execution.md`. Stop when no job remains permanently leased.

### 3. Quarantine and authorized replay `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/ecommerce/`;
focus on `tests/m7/test_worker.py` and the output named below. Record `evidence/M7/replay.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 3](#3-quarantine-and-authorized-replay-required) using that saved result; continue to [Prove it](#prove-it).
When needed: [C3 scenario and hints](#c3--poison-and-backlog-incident) and [concept explanation](#one-poison-job-stopped-healthy-work).

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

### Diagnose deliberate failures

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Understand

- **Durable intent:** a committed record that work is owed.
- **Outbox:** business state and pending work stored in one database transaction.
- **Worker:** a separate process claiming and executing jobs.
- **At-least-once:** a job may run again after a crash.
- **Lease:** time-bounded ownership allowing abandoned work to be reclaimed.
- **Poison work:** a repeatedly failing job moved aside for investigation.
- **Eventual consistency:** related views become consistent after background work finishes.

## Use a tool if earned

Use the current project dependencies first. Open [Use now](#use-now) for the active pattern, [Evaluate after evidence](#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](#review) after the Core proof.

Prove [A1–A5](#core) with crash/replay counts, backlog metrics,
duplicate-effect prevention, poison-work recovery, and an executed runbook.

## Done / next

Accepted durable work survives every kill point, duplicate delivery has one
semantic effect, poison work is isolated, and Core passes. Tag `m7-durable-async`.

### Recovery

Use [targeted references](#resources-for-m7) only for the question left by the active hint ladder.

Stop claims, inspect durable job state, follow the authorized replay runbook, and
return to the last green migration before changing retry code.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M8](../m8-concurrency-booking/README.md).

[Previous milestone: M6](../m6-resilient-external-integrations/README.md) · [Course home](../../README.md) · [Next milestone: M8](../m8-concurrency-booking/README.md)


---

## Challenge brief

Run from `projects/ecommerce/`. Preserve job attempts and use injected time.

## **C1 — Lost accepted work**

**PROVIDED** — the kill window is supplied; bridge durable intent to PostgreSQL.

### Steps

1. Create the `accepted_intent` case in `tests/m7/test_worker.py`.
2. Kill the API after the business commit and observe missing in-process work.
3. Store business state and outbox intent atomically; run README Block 1.

### Hints

1. Compare acknowledged response, committed business row, and durable intent.
2. Inspect the business transaction and commit/publish gap.
3. Use the transactional-outbox link in the Reference section below.

### Reset

Disable the kill hook and run
`uv run --locked pytest tests/m7/test_worker.py -q -k accepted_intent`.

## **C2 — Duplicate execution**

**PROVIDED** — naive replay is supplied; you build the idempotent consumer.

### Steps

1. Add one-worker, competing-worker, lease-expiry, and after-effect cases.
2. Kill after effect but before acknowledgement and record every attempt.
3. Add stable semantic identity and run README Block 2.

### Hints

1. Separate durable intent, claim, external effect, and acknowledgement.
2. Inspect lease expiry, attempt history, idempotency key, and stored result.
3. Use the at-least-once link in the Reference section below; do not claim exactly once.

### Reset

Stop workers, advance only the injected synthetic clock, and rerun one selector
with `uv run --locked pytest tests/m7/test_worker.py -q -k lease_expiry`.

## **C3 — Poison and backlog incident**

**YOU BUILD** — create bounded poison input and authorized replay.

### Steps

1. Add the poison case and exhaust the fixed retry budget.
2. Quarantine without blocking healthy work; expose backlog and oldest-job age.
3. Preview and confirm one bounded replay using README Block 3.

### Hints

1. Ask whether one bad item blocks unrelated ready work.
2. Inspect retry count, next-attempt time, terminal state, actor, and audit entry.
3. Use the worker-operations link in the Reference section below.

### Reset

Use preview first; restore only the synthetic poison job, then run
`uv run --locked pytest tests/m7/test_worker.py -q -k poison`.

Ship API and worker as one codebase with separate processes.


---

## Acceptance gate

Required maturity: **Level C for the asynchronous fulfillment slice**.

## Core

- **A1:**
  - [ ] Order and outbox intent commit atomically
  - [ ] pre-commit failure leaves neither, post-commit/API crash cannot lose intent, and status exposes eventual consistency until completion.
- **A2:**
  - [ ] C2 replay and competing-worker tests prove at-least-once execution with one semantic effect, idempotent consumers, normal exclusive claims, and expired-lease recovery.
- **A3:**
  - [ ] Retry scheduling is bounded
  - [ ] C3 quarantines poison work without blocking healthy peers.
  - [ ] Authorized replay retains attempt and error history.
  - [ ] Graceful shutdown stops new claims without abandoning owned work silently.
  - [ ] Depth, oldest age, duration, retry, and terminal metrics diagnose backlog.
- **A4:**
  - [ ] Clean migration/test/lint/validator plus executed inspect/replay/recovery runbook prove API/worker restart behavior
  - [ ] a [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) covers payload copies, attempt/error history, quarantine, retention, replay access, and deletion implications.
- **A5:**
  - [ ] No accepted durable obligation relies on FastAPI `BackgroundTasks`
  - [ ] documentation makes the kill boundary and at-least-once—not exactly-once—claim explicit.
  - [ ] optional email evidence distinguishes provider acceptance from mailbox delivery and states the deduplication window and residual duplicate risk.
  - [ ] If Taskiq is retained, evidence names the broker/acknowledgement/redelivery/result/shutdown policies and repeats C1–C3 against that path.

## Execution map

Each checklist bullet is a local step in order. From `projects/ecommerce/`, use
README Block 1 for A1, Block 2 for A2, and Block 3 for A3. For A4 run the full
project checks and `test -s evidence/M7/data-lifecycle.md`; for A5 run
`rg -n 'BackgroundTasks|at-least-once|exactly-once' evidence/M7` and explain each
match. Record under matching A headings; recover by stopping claims, advancing
the injected clock, and rerunning one selector.

Evidence includes timestamped job state and side-effect identity before/after every kill point.

## Stretch

Compare Taskiq or Redis only after the PostgreSQL Core baseline and retain it only if all guarantees remain observable with a measured benefit and owned operational cost.

## Review

### Review

Answer one question at a time in `evidence/M7/index.md`:

1. Why can accepted FastAPI `BackgroundTasks` work vanish?
2. How does the outbox close the business-change/publish gap?
3. Why is execution at least once rather than exactly once?
4. Which stable identity makes the consumer idempotent?
5. What happens when a lease expires?
6. What does the user see while state is eventually consistent?
7. Which metric detects stuck work first?
8. Can two workers claim the same job?
9. Can retries or poison work grow without a bound?
10. Who may replay work, and what audit record is created?
11. What do you predict at each kill point before running it?

Use the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md) to decide how completed, failed, and quarantined payloads expire without destroying audit/recovery needs. If optional queue infrastructure is proposed, show whether the M4 revisit trigger actually fired.


---

## Reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M7 concepts through lost and repeated work

## “The API accepted work, then died”

**Example:** an in-process callback never runs. **Term — durable intent:** a
committed record that work is owed. **Rule:** store business state and outbox
intent atomically before acknowledging acceptance.

## “The worker sent the email twice”

**Example:** it dies after the effect but before acknowledgement. **Term —
at-least-once execution:** the job may run again. **Rule:** use stable semantic
identity so repetition produces one business effect.

## “The order committed but its job did not”

**Example:** the process dies between database commit and queue publication.
**Term — transactional outbox:** durable work intent stored with the business
change. **Rule:** persist both atomically before acknowledging the obligation.

## “BackgroundTasks disappeared on restart”

**Example:** process-local work dies with the API. **Term — best-effort work:**
work whose loss is acceptable. **Rule:** use FastAPI `BackgroundTasks` only for
that case; a worker framework does not itself create durability or exactly-once behavior.

## “The worker repeated an external effect”

**Example:** it crashes after sending but before acknowledging. **Term —
idempotent consumer:** repeated delivery converges to one business effect.
**Rule:** use stable semantic identity and stored results; expose accepted versus
completed states as eventual consistency.

For optional email, provider acceptance means only that the provider accepted
the request. It does not prove mailbox receipt, display, or reading. State the
deduplication window and remaining duplicate risk; never claim exactly-once
external delivery.

## “One poison job stopped healthy work”

**Example:** the same invalid item consumes every retry slot. **Term — quarantine:**
a terminal holding area for failed work. **Rule:** bound retries, isolate poison,
audit replay, shut down gracefully, and monitor depth, oldest age, duration, and failures.

### Tools earned here

- **PostgreSQL outbox/job tables:** atomic intent and inspectable baseline queue semantics.
- **Polling worker + database locking/leases:** expose claim, timeout, retry, and crash behavior directly.
- **Alembic:** deploy job state and indexes safely.
- **Metrics/structured logs:** queue health and per-job history/correlation.
- **Provider fakes:** deterministic pre/post-side-effect crashes.

Taskiq is optional only after Core. Select and document the production broker, acknowledgement/redelivery and result policy, shutdown behavior, retention, monitoring, and local recovery; compare how it preserves atomic intent, at-least-once behavior, replay, and operations. Redis is not required and may not replace PostgreSQL as business truth. Avoid FastAPI `BackgroundTasks` for every accepted durable obligation.

Revisit the M4 [complexity rejection record](../../templates/COMPLEXITY-REJECTION.md) if Taskiq or Redis is proposed. Adopt only when its measurable trigger is now true; otherwise update the evidence and keep the simpler queue.

An email provider is optional after Core. Retain it only for a named delivery
question with an owner, test recipient, credential/data boundary, cost cap, and
removal trigger. API acceptance is not mailbox delivery.

## Evaluate after evidence

Evaluate optional tools only after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M7

Consult these after proving that accepted work can be lost or repeated. Reviewed 2026-09-14.

- [FastAPI background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) — What does in-process post-response work provide, and what does it not make durable? Applicable tool: current FastAPI.
- [PostgreSQL SELECT](https://www.postgresql.org/docs/current/sql-select.html) — How can FOR UPDATE SKIP LOCKED coordinate competing workers? Applicable tool: current PostgreSQL.
- [Taskiq guide](https://taskiq-python.github.io/guide/) — When does an external broker/worker earn its operational cost? Applicable tool: current Taskiq.

Build and test the database-backed durable-intent path before adding Taskiq.
