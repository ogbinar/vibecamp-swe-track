# Seeded challenge system

Milestone `CHALLENGE.md` files are executable briefs, not implemented defects. Each scenario has an ID (`C1`, `C2`, …), initial condition, trigger, observable symptom, constraints, and required proof. A mentor may provide a prepared branch or the learner may inject the fault, but the final production path must be repaired.

## Brief lifecycle

1. Start from the tagged prior milestone or stated fixture and open an issue for the ambiguous symptom.
2. Record a hypothesis before inspecting the cause.
3. Reproduce with the smallest deterministic test/harness; preserve the failing output.
4. Diagnose across boundaries, implement the smallest correct fix, and add a regression guard.
5. Run the operate/recovery step and link results from the PR/evidence index.

## Preserve the failure safely

The repaired production path must not retain the defect. Preserve only what makes the learning reviewable: the smallest failing test or isolated harness, sanitized before-output, initial hypothesis, diagnosis, and regression proof. A deliberately vulnerable fixture may remain disabled only when it cannot be reached by production configuration, is clearly labeled, and has a safe invocation. Never preserve secrets, real user data, callable insecure routes, destructive defaults, or bulky logs.

Scenarios cover technical debt, production incidents, races, slow queries, failed migrations, duplicate jobs, external API failures, and security mistakes. They must never depend on hidden trivia: the briefing exposes the symptom and success condition while leaving diagnosis and design to the learner.

The brownfield share rises deliberately: M0–M2 approximately 30%, M3–M5 60%, and M6–M10 80% change/repair/operate work. This is a target by meaningful challenge effort, not a line-count quota.
