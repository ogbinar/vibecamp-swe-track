# Problems and mental models

“Works on my machine” means hidden state is part of the system. Make runtime version, direct dependencies, lockfile, configuration names, process startup, and ignored artifacts explicit. A lockfile makes resolution repeatable; it does not guarantee compatible operating systems or safe dependencies.

Project structure begins with one vertical slice and clear entry points, not speculative layers. Typing and validation make assumptions executable at boundaries. Configuration is external input: validate it at startup, provide safe examples, and never leak values. A health check answers whether the process is alive; dependency readiness is introduced only when dependencies exist.

Git history, issues, PRs, Actions, and an annotated tag form the first release discipline loop. Automation must execute the same commands documented for a clean checkout.
