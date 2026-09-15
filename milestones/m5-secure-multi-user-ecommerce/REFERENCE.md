# M5 reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M5 concepts through access mistakes

## “Alice guessed Bob’s order ID”

**Example:** Alice is logged in but reads an object she does not own. **Term —
object-level authorization:** checking permission for this specific object.
**Rule:** scope reads, lists, writes, and nested identifiers; login alone is not
authorization.

## “The password database leaked”

**Example:** reversible encryption reveals every password. **Term — password
hashing:** one-way, salted password verification. **Rule:** use Argon2 through
`pwdlib`, bound input, and never log credentials.

## “A staff role was trusted from request JSON”

**Example:** a client sends `role=admin`. **Term — role-based access control
(RBAC):** broad permissions assigned from trusted server-side roles. **Rule:**
deny by default and combine role permission with object scope on every path.

## “The browser session worked, but cross-site requests could use it”

**Example:** cookies are sent automatically with a forged request. **Term —
cross-site request forgery (CSRF):** another site triggers an authenticated browser
request. **Rule:** choose authentication from the client/trust boundary and test
cookie attributes, CSRF defense, fixation, expiry, logout, theft, and revocation.

## “A token was decoded but not safely validated”

**Example:** a JSON Web Token (JWT) accepts the wrong audience or algorithm.
**Term — signed claim:** data whose integrity is verifiable but not encrypted.
**Rule:** when JWT is justified, use PyJWT with a fixed algorithm, issuer,
audience, time, type, and rotation/revocation policy; keep payloads nonsensitive.

## “A permitted user forced an impossible order state”

**Example:** an owner pays an already cancelled order. **Term — state machine:**
the allowed states and transitions. **Rule:** enforce authorization and transition
policy together, return nonrevealing errors, protect secrets, and log safely.

### Tools earned here

- **`pwdlib[argon2]`:** adaptive password hashing, verification, and upgrade; never invent cryptography.
- **Server-side opaque session plus secure cookie (Core):** the declared client is a first-party browser. Prove CSRF/session fixation/rotation/logout behavior.
- **PyJWT (Stretch comparison):** consider bearer tokens only if a different client/trust boundary is later earned; require short-lived claims, fixed-algorithm validation, issuer/audience/time/type checks, and explicit refresh/revocation behavior.
- **FastAPI security/dependency boundaries:** authenticate once, authorize per action/object.
- **pytest/HTTPX security matrix:** prove negative paths at the API boundary.
- **`pydantic-settings`/CI secrets:** keep secret values outside source and output.

No OAuth server, external identity platform, payment SDK, WAF, or broad security scanner is required. Core compares the mechanisms but implements only the cookie session. Earn JWT or refresh tokens only from a new client requirement and document revocation/theft behavior.

## Evaluate after evidence

Evaluate optional tools only after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M5

Read after an attack case fails, not as a security-themed tutorial dump. Reviewed 2026-09-14.

- [FastAPI security tools](https://fastapi.tiangolo.com/reference/security/) — Which framework helper follows, rather than defines, the authentication decision? Applicable tool: current FastAPI.
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — What must be checked beyond “the user is logged in”? Applicable guidance: current OWASP Cheat Sheet Series.
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) — Which password-storage properties and parameters matter? Applicable guidance: current OWASP Cheat Sheet Series.
- [PyJWT usage](https://pyjwt.readthedocs.io/en/stable/usage.html) — Stretch only: which claims and algorithms must decoding verify explicitly? Applicable tool: PyJWT 2.

Examples are starting points; the milestone threat cases decide the policy.
