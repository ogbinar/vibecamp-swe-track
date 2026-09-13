# Problems and mental models

Authentication answers who presented credentials; authorization answers whether that principal may perform this action on this object. RBAC handles coarse capabilities, but object-level authorization must constrain order/cart/address ownership on every read, list, write, and indirect identifier path.

Passwords are stored with `pwdlib[argon2]`, unique salts, bounded input, and an upgrade policy—never reversible encryption. Authentication state follows the client and trust boundary: a first-party browser may be simpler and safer to control with an opaque server-side session referenced by a `Secure`, `HttpOnly`, appropriately `SameSite` cookie, while external/mobile clients may justify signed bearer tokens. Compare CSRF, token theft, revocation, scaling, and operational ownership rather than choosing by fashion.

When JWT is justified, use PyJWT. JWTs are signed claims, not sessions or encryption: use a fixed algorithm allowlist; validate issuer, audience, expiry/not-before, token type, and rotation/revocation assumptions; keep payloads nonsensitive. Neither option requires building an OAuth authorization server.

Order state machines prevent authorization from being bypassed through invalid transitions. Security spans validation, error leakage, rate/abuse assumptions, secret handling, and logs. Deny by default at a centralized policy boundary, then verify at the public API.
