# M5 identity, access, and order contract

The Core client is a first-party browser. Store a random opaque session server
side and send only its identifier in a cookie with `HttpOnly`, `Secure` in the
production profile, and an explicit `SameSite` policy. Rotate it at login and
privilege change; expire it on logout and recovery. Passwords use Argon2 via
`pwdlib`; neither passwords nor session values appear in logs.

Registration, login, logout, and recovery return generic responses that do not
reveal whether an email exists. Recovery uses a synthetic delivery adapter.

| Capability | Customer | Staff | Administrator |
|---|---:|---:|---:|
| Read/update own profile, cart, address, order | yes | no | no implicit bypass |
| Read another customer's order | no | only assigned support flow | no implicit bypass |
| Fulfil paid order | no | yes | no |
| Refund paid/fulfilled order | no | yes | no |
| Grant/revoke roles | no | no | yes |

Object ownership is checked after authentication and before loading or mutating
the response object. Lists are scoped too. Use synthetic Alice/Bob/staff/admin
fixtures and test-only mutations for missing scope, client-supplied role,
enumeration, stale session, and forbidden state transition. Compare JWT in a
short decision record; implementing it is Stretch.
