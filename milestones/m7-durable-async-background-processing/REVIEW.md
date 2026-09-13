# Review

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
