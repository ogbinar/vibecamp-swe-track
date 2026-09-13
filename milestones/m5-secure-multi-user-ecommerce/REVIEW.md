# Review

Explain authentication versus authorization; RBAC versus object ownership; password hash upgrade; why the declared client boundary earned an opaque cookie session or JWT; the selected mechanism's guarantees and non-guarantees; where identity is established/revoked; and how state transition plus permission interact.

Self-review every identifier, list, nested route, error, log, secret, and default role. Test as anonymous, wrong user, each role, expired/malformed session credential, revoked/logged-out user, and legitimate owner. For cookies, inspect CSRF and cookie attributes; for JWT, inspect algorithm/claim/refresh behavior. Describe one residual threat rather than claiming the system is “secure.”

Use the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md) to find copies that authentication tests alone miss: logs, session records or token claims, order snapshots, and retained audit/security records.
