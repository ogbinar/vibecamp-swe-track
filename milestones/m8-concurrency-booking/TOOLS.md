# Tools earned here

- **PostgreSQL constraints, isolation, row/advisory locks, atomic SQL:** cross-process correctness mechanisms chosen per invariant.
- **Barrier-controlled asyncio/thread/process harness:** deterministic interleavings plus repeated stress.
- **Database lock/activity views and time:** diagnose waits/deadlocks and make expiry policy explicit.
- **pytest + HTTPX:** assert both internal invariant and client conflict contract.

No Redis/distributed lock or availability microservice. Avoid raising isolation globally without measurement. Remove application locks that create false single-process confidence.
