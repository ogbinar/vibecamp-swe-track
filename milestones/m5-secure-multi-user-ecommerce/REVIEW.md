# Review

Explain authentication versus authorization; RBAC versus object ownership; password hash upgrade; JWT guarantees and non-guarantees; where identity is established; and how state transition plus permission interact.

Self-review every identifier, list, nested route, error, log, secret, and default role. Test as anonymous, wrong user, each role, expired token, malformed token, and legitimate owner. Describe one residual threat rather than claiming the system is “secure.”

Use the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md) to find copies that authentication tests alone miss: logs, token claims, order snapshots, and retained audit/security records.
