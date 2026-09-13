# M2 concepts through data problems

## “The product vanished after restart”

**Example:** a catalog held only in a Python dictionary disappears. **Term —
persistence:** keeping facts beyond one process lifetime. **Rule:** model product
identity, relationships, and required reads before choosing tables.

## “One write bypassed the API check”

**Example:** direct SQL inserts negative quantity. **Term — constraint:** a
database rule that protects every writer. **Rule:** keep friendly validation in
the application and critical truth in the database too.

## “The tables do not support the required reads”

**Example:** a cart needs several fragile joins because identities and relationships
were never written down. **Term — relational model:** tables, keys, and
relationships representing product facts. **Rule:** begin with identity,
cardinality, lifecycle, access paths, and invariants; treat ORM mappings as one
client of the SQL design.

## “The index made writes slower but did not help the query”

**Example:** an index does not match the cart filter or ordering. **Term — query
plan:** the database’s chosen path for executing SQL. **Rule:** connect every
index to a named read and compare the plan while accounting for write/storage cost.

## “The empty migration passed but existing data failed”

**Example:** a required column cannot be added to legacy rows in one unsafe step.
**Term — migration:** a versioned schema/data change. **Rule:** test empty and
existing-data paths, interruption, restart, compatibility, and rollback or
roll-forward. Diagnose N+1 by query count and shape, not latency alone.
