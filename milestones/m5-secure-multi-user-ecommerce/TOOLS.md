# Tools earned here

- **`pwdlib[argon2]`:** adaptive password hashing, verification, and upgrade; never invent cryptography.
- **Server-side opaque session plus secure cookie (Core):** the declared client is a first-party browser. Prove CSRF/session fixation/rotation/logout behavior.
- **PyJWT (Stretch comparison):** consider bearer tokens only if a different client/trust boundary is later earned; require short-lived claims, fixed-algorithm validation, issuer/audience/time/type checks, and explicit refresh/revocation behavior.
- **FastAPI security/dependency boundaries:** authenticate once, authorize per action/object.
- **pytest/HTTPX security matrix:** prove negative paths at the API boundary.
- **`pydantic-settings`/CI secrets:** keep secret values outside source and output.

No OAuth server, external identity platform, payment SDK, WAF, or broad security scanner is required. Core compares the mechanisms but implements only the cookie session. Earn JWT or refresh tokens only from a new client requirement and document revocation/theft behavior.
