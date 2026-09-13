# Acceptance gate

Required maturity: **Level C for the asynchronous fulfillment slice**.

## Core

- **A1:** Order and outbox intent commit atomically; pre-commit failure leaves neither, post-commit/API crash cannot lose intent, and status exposes eventual consistency until completion.
- **A2:** C2 replay and competing-worker tests prove at-least-once execution with one semantic effect, idempotent consumers, normal exclusive claims, and expired-lease recovery.
- **A3:** Retry scheduling is bounded; C3 poison work quarantines without blocking peers, authorized replay retains history, graceful shutdown stops claims safely, and depth/oldest-age/duration/retry/terminal metrics diagnose backlog.
- **A4:** Clean migration/test/lint/validator plus executed inspect/replay/recovery runbook prove API/worker restart behavior; a [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) covers payload copies, attempt/error history, quarantine, retention, replay access, and deletion implications.

Evidence includes timestamped job state and side-effect identity before/after every kill point.

## Stretch

Compare Taskiq or Redis only after Core and retain it only if all guarantees remain observable with a measured benefit.
