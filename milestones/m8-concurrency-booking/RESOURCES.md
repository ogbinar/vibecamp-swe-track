# Resource guide

Prioritize PostgreSQL primary documentation for transaction isolation, explicit/advisory locking, constraints, deadlocks, and database time; use SQLAlchemy docs for transaction APIs and Python docs for the chosen coordination primitive.

Select resources with explicit transaction timelines. Reject generic “use a lock” advice that omits process/database scope, lock ordering, timeouts, or isolation. Confirm every behavior on the pinned PostgreSQL version.
