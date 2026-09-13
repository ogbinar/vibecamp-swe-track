# Resources for M9

Open these only after capturing query count, plan, dataset, and budget evidence. Reviewed 2026-09-13.

- [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — Why did PostgreSQL choose this plan? Applicable tool: current PostgreSQL.
- [SQLAlchemy relationship loading](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html) — Which loading strategy removes the observed N+1 without over-fetching? Applicable tool: SQLAlchemy 2.0.
- [Redis client-side caching](https://redis.io/docs/latest/develop/clients/client-side-caching/) — What invalidation responsibilities appear when cached state is shared? Applicable tool: current Redis.
- [MDN server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) and [WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) — Does the product need one-way events or two-way messaging? Applicable browser APIs: current web platform.

Cache or realtime infrastructure must follow a measured requirement and written failure policy.
