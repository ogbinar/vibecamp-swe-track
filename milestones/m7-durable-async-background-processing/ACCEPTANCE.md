# Acceptance gate

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
