# Isolated M5 security scenarios

These are attack descriptions, not callable vulnerable routes.

1. Enumeration: login and recovery must not reveal whether an email exists.
2. Object access: customer A requests customer B's order by a valid identifier.
3. Token validation: expired, wrong-audience, wrong-type, and revoked tokens arrive.
4. State transition: a customer attempts to move a fulfilled order back to pending.

The learner builds tests that demonstrate denial before implementing the repair.
Fixtures must use synthetic users and must never log passwords or tokens.
