# Problems and mental models

Persistence is not replacing a dictionary with an ORM. Start from identities, cardinality, lifecycle, access paths, and invariants; then choose tables, keys, normalization, constraints, indexes, and timestamps. SQL is the database contract; ORM mappings are one client of it.

Boundary validation improves errors, while unique/foreign-key/check/not-null constraints protect truth from every writer. Indexes accelerate particular reads but charge writes and storage. A session/transaction must have an explicit request/use-case lifetime and recover after rollback.

Migrations are deployed product behavior. Empty-database success does not prove an existing-data backfill is safe, restartable, compatible, or reversible. N+1 is diagnosed by query count/shape, not assumed from latency alone.
