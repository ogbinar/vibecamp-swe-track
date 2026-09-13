# Challenge brief

- **C1 — Lost accepted work:** Begin with an in-process fulfillment task, kill API after order commit, observe loss, then introduce atomic outbox/job intent and prove eventual completion after restart.
- **C2 — Duplicate execution:** Kill worker after external effect but before acknowledgement; run competing workers and expire a lease. Build an idempotent consumer and prove at-least-once replay causes one semantic effect.
- **C3 — Poison/backlog incident:** Feed invalid work, exhaust bounded retries, quarantine, repair/replay, then accumulate backlog and restart gracefully. Diagnose via queue metrics and preserve attempt/error history.

Refactor only after the crash model is explicit. Operate with inspect/replay runbook and authorized assumptions. Ship worker/API together as one codebase with separate processes.
