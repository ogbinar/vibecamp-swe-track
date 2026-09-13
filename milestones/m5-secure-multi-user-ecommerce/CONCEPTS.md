# Problems and mental models

Authentication answers who presented credentials; authorization answers whether that principal may perform this action on this object. RBAC handles coarse capabilities, but object-level authorization must constrain order/cart/address ownership on every read, list, write, and indirect identifier path.

Passwords are stored with a current adaptive password-hashing library, unique salts, bounded input, and upgrade policy—never reversible encryption. JWTs are signed claims, not sessions or encryption: validate algorithm, issuer/audience, time claims, token type, and revocation/rotation assumptions; keep payloads nonsensitive.

Order state machines prevent authorization from being bypassed through invalid transitions. Security spans validation, error leakage, rate/abuse assumptions, secret handling, and logs. Deny by default at a centralized policy boundary, then verify at the public API.
