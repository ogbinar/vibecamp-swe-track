# M5 concepts through access mistakes

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
