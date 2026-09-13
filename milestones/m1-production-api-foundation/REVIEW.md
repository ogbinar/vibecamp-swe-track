# Review

Explain: safe versus idempotent; transport validation versus product invariant; error distinctions; stable pagination ordering; a breaking change that server tests might miss; and why “production-minded API” is narrower than “production-ready product.”

Self-review every endpoint as a consumer: exact method/status/body, unknown input, retry, missing identity, and page boundary. Identify one test that could falsely pass, seed its defect, and improve it. Confirm no persistence/auth abstractions have arrived early.
