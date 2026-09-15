"""Dependency-free validation of curriculum structure, traceability, and links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MILESTONES = ROOT / "milestones"
REQUIRED_ROOT = {
    "README.md", "CURRICULUM.md", "STACK.md", "QUALITY-GATES.md", "USABILITY.md",
    "GLOSSARY.md", "PROGRESS.md", "CONTRIBUTING.md",
    "PLAN.md", "TODO.md", "projects", "challenges", "templates", ".github/workflows",
}
OLD_MILESTONE_FILES = {
    "README.md", "CONCEPTS.md", "CHALLENGE.md", "TOOLS.md",
    "ACCEPTANCE.md", "REVIEW.md", "RESOURCES.md",
}
NEW_MILESTONE_FILES = {"README.md", "CHALLENGE.md", "ACCEPTANCE.md", "REFERENCE.md"}
MILESTONE_FILES = OLD_MILESTONE_FILES | NEW_MILESTONE_FILES
REQUIRED_TEMPLATES = {
    "ADR.md", "COMPLEXITY-REJECTION.md", "DATA-LIFECYCLE.md",
    "ENTRY-DIAGNOSTIC.md", "EVIDENCE-INDEX.md", "INCIDENT-POSTMORTEM.md",
    "PORTFOLIO-CASE-STUDY.md", "REQUIREMENTS.md", "TRANSITION-REVIEW.md",
    "SEMANTIC-AUDIT.md", "EVIDENCE-EXAMPLES.md", "RUNBOOK-MIGRATION.md",
    "RUNBOOK-RELEASE-REJECTION.md", "RUNBOOK-RESTORE.md", "RUNBOOK-INCIDENT.md",
}
PROJECT_REQUIREMENTS = {
    "catalog": {"README.md", "pyproject.toml", "uv.lock", "contracts/test_m1_contract.py", "src/catalog_api/main.py", "src/catalog_api/web.py"},
    "pos": {
        "README.md", "pyproject.toml", "uv.lock", "compose.yml", "alembic.ini",
        "migrations/versions/0001_baseline.py", "tests/test_postgres.py", "REQUIREMENTS.md",
        "compose.production.yml", "compose.unhealthy.yml", "scripts/rehearse_m10.sh",
        "src/pos_api/main.py", "src/pos_api/web.py",
    },
    "ecommerce": {
        "README.md", "pyproject.toml", "uv.lock", "compose.yml", "alembic.ini",
        "migrations/versions/0001_baseline.py", "fixtures/SECURITY-SCENARIOS.md",
        "tests/test_failure_harnesses.py", "tests/test_postgres.py", "REQUIREMENTS.md",
        "src/ecommerce_api/main.py", "src/ecommerce_api/web.py",
    },
    "booking": {"README.md", "pyproject.toml", "uv.lock", "compose.yml", "alembic.ini", "migrations/versions/0001_baseline.py", "challenges/test_double_booking.py", "tests/test_postgres.py", "src/booking_api/main.py", "src/booking_api/web.py"},
    "social": {"README.md", "pyproject.toml", "uv.lock", "compose.yml", "alembic.ini", "migrations/versions/0001_baseline.py", "challenges/test_query_budget.py", "tests/test_postgres.py", "src/social_api/main.py", "src/social_api/web.py"},
}
TEMPLATE_HEADINGS = {
    "ENTRY-DIAGNOSTIC.md": {"## Protocol", "## Signals and routing", "## Routing result"},
    "COMPLEXITY-REJECTION.md": {"## Observed pressure", "## Smallest current solution", "## Revisit trigger"},
    "PORTFOLIO-CASE-STUDY.md": {"## Problem, user, and constraints", "## Failure → diagnosis → change", "## Reader path"},
    "DATA-LIFECYCLE.md": {"## Review questions"},
}
REQUIRED_STACK_MARKERS = {
    "fastapi[standard]",
    "Psycopg 3",
    "mypy",
    "synchronous SQLAlchemy",
    "FastAPI `BackgroundTasks`",
    "PostgreSQL owns durable truth",
    "CI before CD",
    "service when orchestration",
}
REQUIRED_CATALOG_FILES = {
    ".env.example",
    ".gitignore",
    ".python-version",
    "README.md",
    "pyproject.toml",
    "uv.lock",
    "scripts/challenge.py",
    "src/catalog_api/__init__.py",
    "src/catalog_api/app.py",
    "src/catalog_api/main.py",
    "src/catalog_api/models.py",
    "src/catalog_api/service.py",
    "src/catalog_api/settings.py",
    "src/catalog_api/web.py",
    "tests/test_api.py",
    "evidence/M0/EXAMPLE.md",
}
M0_ACTIVE_FILES = {
    "README.md",
    "milestones/m0-engineering-baseline/README.md",
    "milestones/m0-engineering-baseline/CHALLENGE.md",
    "templates/ENTRY-DIAGNOSTIC.md",
    "projects/catalog/README.md",
}
REQUIRED_CONCEPTS = {
    "HTTP semantics", "API contracts", "Typing and validation", "Dependency injection",
    "Project structure", "Configuration", "Relational modeling", "SQL", "Constraints",
    "Indexes", "Migrations", "Transactions", "ACID", "Race conditions", "Locking",
    "Application vs database invariants", "Unit tests", "Integration tests", "API tests",
    "Refactoring", "Cohesion and coupling", "Service/repository boundaries",
    "Authentication", "Authorization", "RBAC", "Object-level authorization",
    "Password hashing", "JWT", "State machines", "Timeouts", "Retries and backoff",
    "Webhooks", "Idempotency", "Queues and workers", "At-least-once execution",
    "Idempotent consumers", "Eventual consistency", "Query optimization", "N+1",
    "EXPLAIN/query plans", "Pagination", "Redis/cache-aside", "Cache invalidation",
    "SSE vs WebSockets", "Structured logging", "Correlation/request IDs", "Metrics",
    "Traces", "Health/readiness checks", "Docker", "CI/CD", "Migration deployment",
    "Secrets", "Tenant isolation", "Audit logs", "Backup/recovery", "Release discipline",
    "Incident/postmortem thinking",
}
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ROW = re.compile(r"^\| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \|$")
REF = re.compile(r"M(10|[0-9]) `([AC][0-9](?:,[AC][0-9])*)`")
ROADMAP_HEADERS = (
    "Milestone",
    "Business problem",
    "Product capability",
    "Start here",
)
ROADMAP_BUSINESS_MARKERS = (
    "author's machine",
    "cannot predict catalog responses",
    "disappear when the POS restarts",
    "inventory, money, and receipts disagreeing",
    "touches too many POS files",
    "orders they do not own",
    "does not reveal whether money moved",
    "disappears when a process crashes",
    "same final seat",
    "becomes slow",
    "serve several businesses",
)

PROJECTS = ("catalog", "pos", "ecommerce", "booking", "social")
OUTCOME_TITLES = {
    "M0": "Make the catalog easy to run",
    "M1": "Make the catalog predictable for clients",
    "M2": "Make stock survive a restart",
    "M3": "Make checkout safe",
    "M4": "Change the POS without breaking it",
    "M5": "Protect customer accounts and orders",
    "M6": "Handle uncertain payments",
    "M7": "Finish accepted work after a crash",
    "M8": "Stop the last seat being sold twice",
    "M9": "Keep the feed fast as it grows",
    "M10": "Support multiple businesses safely",
}
NEW_ROUTE_HEADINGS = (
    "Business problem",
    "Product objective",
    "Start here",
    "Build",
    "Understand",
    "Use a tool if earned",
    "Prove it",
    "Done / next",
)


def classify_milestone_contract(entries: set[str]) -> tuple[str, str | None]:
    """Classify one milestone during the seven-to-four-file migration."""
    contract_entries = entries & MILESTONE_FILES
    extras = entries - MILESTONE_FILES
    if extras:
        return "invalid", f"unexpected files={sorted(extras)}"
    if contract_entries == OLD_MILESTONE_FILES:
        return "old", None
    if contract_entries == NEW_MILESTONE_FILES:
        return "new", None
    missing_old = sorted(OLD_MILESTONE_FILES - contract_entries)
    missing_new = sorted(NEW_MILESTONE_FILES - contract_entries)
    return (
        "hybrid",
        "undocumented hybrid contract; finish the old or new file set before validation "
        f"(missing-old={missing_old}, missing-new={missing_new})",
    )


def classify_runtime(pyproject: str, python_version: str) -> tuple[str, str | None]:
    """Classify one starter's coordinated Python/Air migration state."""
    requires_312 = 'requires-python = "==3.12.*"' in pyproject
    requires_313 = 'requires-python = "==3.13.*"' in pyproject
    mypy_312 = 'python_version = "3.12"' in pyproject
    mypy_313 = 'python_version = "3.13"' in pyproject
    ruff_312 = 'target-version = "py312"' in pyproject
    ruff_313 = 'target-version = "py313"' in pyproject
    exact_air = re.search(r'^[ \t]*"air==0\.48\.1",?[ \t]*$', pyproject, re.MULTILINE)
    any_air = re.search(r'^[ \t]*"air[^"\n]*"', pyproject, re.MULTILINE)
    if requires_312 and mypy_312 and ruff_312 and python_version.strip() == "3.12" and not any_air:
        return "pre-Air", None
    if (
        requires_313
        and mypy_313
        and ruff_313
        and python_version.strip() == "3.13"
        and exact_air
        and "fastapi[standard]" in pyproject.lower()
    ):
        return "Air", None
    return (
        "hybrid",
        "runtime migration must be wholly Python 3.12 without Air or wholly Python 3.13 "
        "with exact air==0.48.1 and explicit fastapi[standard]",
    )


def heading_anchors(markdown: str) -> set[str]:
    """Return GitHub-style anchors needed by this repository's simple headings."""
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for line in markdown.splitlines():
        if not re.match(r"^#{1,6} ", line):
            continue
        heading = re.sub(r"^#{1,6} ", "", line).strip().lower()
        heading = re.sub(r"[`*_~]", "", heading)
        anchor = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE).replace(" ", "-")
        suffix = counts.get(anchor, 0)
        counts[anchor] = suffix + 1
        anchors.add(anchor if suffix == 0 else f"{anchor}-{suffix}")
    return anchors


def milestone_map(directories: list[Path]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in directories:
        match = re.fullmatch(r"m(10|[0-9])-[a-z0-9-]+", path.name)
        if match:
            result[f"M{match.group(1)}"] = path
    return result


def markdown_cells(line: str) -> tuple[str, ...]:
    """Split this repository's plain Markdown tables into trimmed cells."""
    if not line.startswith("|") or not line.endswith("|"):
        return ()
    return tuple(cell.strip() for cell in line[1:-1].split("|"))


def readme_roadmap_rows(readme: str) -> tuple[tuple[str, ...], list[tuple[str, ...]]]:
    """Return the primary README Roadmap header and data rows."""
    if "## Roadmap" not in readme:
        return (), []
    section = readme.split("## Roadmap", 1)[1].split("\n## ", 1)[0]
    table_lines = [line for line in section.splitlines() if line.startswith("|")]
    if len(table_lines) < 2:
        return (), []
    return markdown_cells(table_lines[0]), [markdown_cells(line) for line in table_lines[2:]]


def check_navigation(root: Path, by_code: dict[str, Path]) -> list[str]:
    """Validate settled navigation facts, never learner status or comprehension."""
    errors: list[str] = []
    readme = (root / "README.md").read_text(encoding="utf-8")
    headers, rows = readme_roadmap_rows(readme)
    if headers != ROADMAP_HEADERS:
        errors.append(
            "README.md: primary roadmap needs exact four business-first headers: "
            + "; ".join(ROADMAP_HEADERS)
        )
    if len(rows) != 11:
        errors.append("README.md: IA route map needs eleven ordered rows")
    for number, row in enumerate(rows[:11]):
        code = f"M{number}"
        target = by_code.get(code)
        if len(row) != len(ROADMAP_HEADERS):
            errors.append(
                f"README.md: primary roadmap row {number + 1} needs exactly four columns"
            )
            continue
        if row[0] != code:
            errors.append(
                f"README.md: IA route row {number + 1} has wrong ordinal or label"
            )
        capability_link = re.fullmatch(r"\[[^\]]+\]\(([^)]+)\)", row[3])
        expected_target = f"{target.relative_to(root)}/README.md" if target else ""
        if not capability_link or capability_link.group(1) != expected_target:
            errors.append(
                f"README.md: IA route row {number + 1} has wrong controller link"
            )
        if ROADMAP_BUSINESS_MARKERS[number] not in row[1]:
            errors.append(
                f"README.md: business route row {number + 1} has wrong problem"
            )
        if OUTCOME_TITLES[code].lower().replace("the ", "") not in row[2].lower().replace("the ", ""):
            errors.append(
                f"README.md: business route row {number + 1} has wrong product capability"
            )
    if "No provider account or secret is needed to start" not in readme:
        errors.append("README.md: start must not imply a provider account or secret prerequisite")
    for number in range(11):
        code = f"M{number}"
        directory = by_code.get(code)
        if directory is None:
            continue
        controller = directory / "README.md"
        text = controller.read_text(encoding="utf-8")
        ordinal = re.findall(r"Milestone (\d+) of 11 · M(\d+)", text)
        if ordinal != [(str(number + 1), str(number))]:
            errors.append(f"{code}: IA ordinal/label must be Milestone {number + 1} of 11 · {code}")
        breadcrumb = f"[Course home](../../README.md) / {code}"
        if breadcrumb not in text.split("\n## ", 1)[0]:
            errors.append(f"{code}: IA breadcrumb missing")
        footer_heading = "\n## Done / next" if (directory / "REFERENCE.md").exists() else "\n## Next"
        footer = text.rsplit(footer_heading, 1)[-1]
        previous = "[Previous: Course start](../../README.md#start-now)"
        if number:
            neighbor = by_code.get(f"M{number - 1}")
            previous = (
                f"[Previous milestone: M{number - 1}](../{neighbor.name}/README.md)"
                if neighbor else "MISSING"
            )
        following = (
            "[Next: Portfolio review / evidence-led next product]"
            "(../../templates/PORTFOLIO-CASE-STUDY.md#reader-path)"
        )
        if number < 10:
            neighbor = by_code.get(f"M{number + 1}")
            following = (
                f"[Next milestone: M{number + 1}](../{neighbor.name}/README.md)"
                if neighbor else "MISSING"
            )
        routes = (
            ("previous", previous),
            ("home", "[Course home](../../README.md)"),
            ("next", following),
        )
        for role, link in routes:
            if footer.count(link) != 1:
                errors.append(f"{code}: IA footer {role} route missing or duplicated")
    return errors


def check_cs_contracts(root: Path) -> list[str]:
    """Validate settled CS facts, not prose quality or learner comprehension."""
    errors: list[str] = []
    required_markers = {
        "README.md": (
            "projects/catalog/evidence/MN/index.md",
            "do not create a competing root `evidence/` tree",
        ),
        "QUALITY-GATES.md": (
            "Evidence is owned by the active product",
            "PENDING — ACCESS/PROVIDER OUTAGE",
        ),
        "STACK.md": (
            "Deterministic offline Core",
            "Required real-provider experiment",
            "M5 Stretch",
            "SQLAdmin",
        ),
        "CURRICULUM.md": (
            "Add an optional cashier display name while untangling the POS",
        ),
        "PLAN.md": ("decision is **ROLL OUT**", "exactly `air==0.48.1`"),
        "TODO.md": (
            "External evidence — unchanged and unchecked",
            "HUMAN SELF-STUDY VERIFIED",
        ),
        "milestones/m0-engineering-baseline/README.md": (
            "**Do:**",
            "**Understand:**",
            "**Check:**",
            "**If it fails:**",
            "**Stop/resume:**",
        ),
        "milestones/m6-resilient-external-integrations/README.md": (
            "`pay`/`refund`/`lookup`",
            "sandbox remains separately authorized and pending",
        ),
        "projects/ecommerce/src/ecommerce_api/provider_fake.py": (
            "def pay(",
            "def refund(",
            "def lookup(",
            "class RetryBudget",
        ),
    }
    for relative, markers in required_markers.items():
        content = (root / relative).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in content:
                errors.append(f"{relative}: missing stable CS contract {marker!r}")
    m4_paths = (
        "CURRICULUM.md",
        "milestones/m4-maintainability-testing-refactoring/README.md",
    )
    for relative in m4_paths:
        m4 = (root / relative).read_text(encoding="utf-8")
        if "Add configurable promotions and returns" in m4:
            errors.append(f"{relative}: M4 multiple Core stakeholder changes remain")
    return errors


def main() -> int:
    errors: list[str] = []
    contract_states: dict[str, str] = {}
    runtime_states: dict[str, str] = {}
    for name in REQUIRED_ROOT:
        if not (ROOT / name).exists():
            errors.append(f"missing required root path: {name}")

    templates = ROOT / "templates"
    missing_templates = REQUIRED_TEMPLATES - {path.name for path in templates.glob("*.md")}
    if missing_templates:
        errors.append(f"missing required templates: {sorted(missing_templates)}")
    for filename, headings in TEMPLATE_HEADINGS.items():
        path = templates / filename
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        absent = headings - set(text.splitlines())
        if absent:
            errors.append(f"{path.relative_to(ROOT)}: missing stable headings {sorted(absent)}")

    directories = sorted(path for path in MILESTONES.iterdir() if path.is_dir())
    by_code = milestone_map(directories)
    expected_codes = {f"M{i}" for i in range(11)}
    if len(directories) != 11 or set(by_code) != expected_codes:
        errors.append(f"expected exactly milestone directories M0-M10; found {[p.name for p in directories]}")

    for directory in directories:
        entries = {path.name for path in directory.iterdir()}
        state, contract_error = classify_milestone_contract(entries)
        contract_states[directory.name] = state
        if contract_error:
            errors.append(f"{directory.relative_to(ROOT)}: {contract_error}")
        elif state != "new":
            errors.append(
                f"{directory.relative_to(ROOT)}: stable contract requires exactly "
                "README.md, CHALLENGE.md, ACCEPTANCE.md, and REFERENCE.md"
            )
        acceptance = directory / "ACCEPTANCE.md"
        if acceptance.exists():
            acceptance_text = acceptance.read_text(encoding="utf-8")
            for heading in ("## Core", "## Stretch"):
                if acceptance_text.splitlines().count(heading) != 1:
                    errors.append(f"{acceptance.relative_to(ROOT)}: expected exactly one {heading}")
            if "Required maturity:" not in acceptance_text:
                errors.append(f"{acceptance.relative_to(ROOT)}: missing required maturity declaration")
        readme_path = directory / "README.md"
        if readme_path.exists():
            milestone_readme = readme_path.read_text(encoding="utf-8")
            if state == "old":
                for marker in ("Starting", "Terms used here", "Failures", "Done", "Recovery", "Next"):
                    if marker not in milestone_readme:
                        errors.append(f"{readme_path.relative_to(ROOT)}: missing learner-route marker {marker!r}")
                route_patterns = (
                    r"^## Why", r"^## Starting", r"^## Terms used here",
                    r"^## Product brief", r"^## Work blocks", r"^## Failures", r"^## Evidence",
                    r"^## Done", r"^## Recovery", r"^## Next",
                )
                route_positions = []
                for pattern in route_patterns:
                    match = re.search(pattern, milestone_readme, flags=re.MULTILINE | re.IGNORECASE)
                    route_positions.append(match.start() if match else -1)
                if any(position < 0 for position in route_positions) or route_positions != sorted(route_positions):
                    errors.append(f"{readme_path.relative_to(ROOT)}: learner-route sections missing or out of order")
            elif state == "new":
                positions = [
                    milestone_readme.find(f"\n## {heading}\n") for heading in NEW_ROUTE_HEADINGS
                ]
                if any(position < 0 for position in positions) or positions != sorted(positions):
                    errors.append(
                        f"{readme_path.relative_to(ROOT)}: business-first sections missing or out of order"
                    )
                code_match = re.match(r"m(10|[0-9])-", directory.name)
                code = f"M{code_match.group(1)}" if code_match else ""
                if not milestone_readme.startswith(f"# {code} — {OUTCOME_TITLES.get(code, '')}"):
                    errors.append(f"{readme_path.relative_to(ROOT)}: outcome-first title is missing")
                for marker in ("**Product can:**", "**You will prove:**"):
                    if milestone_readme.count(marker) != 1:
                        errors.append(
                            f"{readme_path.relative_to(ROOT)}: expected exactly one {marker} summary"
                        )
                for stale in (
                    "## Terms used here",
                    "five visible cues",
                    "Each block keeps the action",
                    "### Literal command map",
                    "### Command map for required blocks",
                ):
                    if stale in milestone_readme:
                        errors.append(
                            f"{readme_path.relative_to(ROOT)}: superseded learner-route content remains {stale!r}"
                        )
        if state == "old" and directory.name not in {"m0-engineering-baseline"}:
            resources = (directory / "RESOURCES.md").read_text(encoding="utf-8")
            url_count = len(re.findall(r"https?://", resources))
            if not 2 <= url_count <= 5:
                errors.append(
                    f"{(directory / 'RESOURCES.md').relative_to(ROOT)}: expected 2-5 curated links; found {url_count}"
                )

        challenge_path = directory / "CHALLENGE.md"
        challenge_text = challenge_path.read_text(encoding="utf-8")
        sections = re.split(r"(?=^## \*\*C\d+)", challenge_text, flags=re.MULTILINE)[1:]
        for section in sections:
            heading = section.splitlines()[0]
            modes = sum(mode in section for mode in ("**PROVIDED**", "**YOU BUILD**"))
            if modes != 1:
                errors.append(
                    f"{challenge_path.relative_to(ROOT)}: {heading} must declare exactly one challenge mode"
                )
            for marker in ("### Steps", "### Hints", "### Reset"):
                if section.count(marker) != 1:
                    errors.append(
                        f"{challenge_path.relative_to(ROOT)}: {heading} must contain one {marker}"
                    )
            for number in ("1.", "2.", "3."):
                if not re.search(rf"^{re.escape(number)} ", section, flags=re.MULTILINE):
                    errors.append(
                        f"{challenge_path.relative_to(ROOT)}: {heading} missing local step/hint {number}"
                    )
            reset = section.split("### Reset", 1)[1] if "### Reset" in section else ""
            if "`" not in reset:
                errors.append(
                    f"{challenge_path.relative_to(ROOT)}: {heading} reset lacks a literal command"
                )

        acceptance_text = (directory / "ACCEPTANCE.md").read_text(encoding="utf-8")
        acceptance_ids = [int(value) for value in re.findall(r"\*\*A(\d+)(?:\s|—|:)", acceptance_text)]
        readme_ids = [int(value) for value in re.findall(r"A1[–-]A(\d+)", milestone_readme)]
        if acceptance_ids and readme_ids and any(value != max(acceptance_ids) for value in readme_ids):
            errors.append(
                f"{readme_path.relative_to(ROOT)}: advertised acceptance range {readme_ids} "
                f"does not match acceptance maximum A{max(acceptance_ids)}"
            )

        if state == "old" and directory.name not in {"m0-engineering-baseline", "m1-production-api-foundation"}:
            if "## Work blocks" not in milestone_readme:
                errors.append(f"{readme_path.relative_to(ROOT)}: missing executable work blocks")
            for marker in ("[REQUIRED", "evidence/", "Stop"):
                if marker.lower() not in milestone_readme.lower():
                    errors.append(f"{readme_path.relative_to(ROOT)}: work blocks missing {marker!r}")

        if state == "old" and directory.name != "m0-engineering-baseline":
            command_marker = (
                "### Command map for required blocks"
                if directory.name == "m1-production-api-foundation"
                else "### Literal command map"
            )
            if command_marker not in milestone_readme:
                errors.append(f"{readme_path.relative_to(ROOT)}: missing literal command map")
            for marker in (
                "Copyable command", "Expected stop condition", "Before:", "After:",
                "Recovery", "Pause",
            ):
                if marker.lower() not in milestone_readme.lower():
                    errors.append(
                        f"{readme_path.relative_to(ROOT)}: command contract missing {marker!r}"
                    )
            block_count = len(re.findall(r"^##?##? \d+", milestone_readme, flags=re.MULTILINE))
            command_rows = len(re.findall(r"^\| \d+ \|", milestone_readme, flags=re.MULTILINE))
            if block_count != command_rows:
                errors.append(
                    f"{readme_path.relative_to(ROOT)}: {block_count} required blocks but "
                    f"{command_rows} literal command rows"
                )

            concepts = (directory / "CONCEPTS.md").read_text(encoding="utf-8")
            if "## Rules to carry" in concepts:
                errors.append(
                    f"{(directory / 'CONCEPTS.md').relative_to(ROOT)}: dense Rules to carry section remains"
                )
            if concepts.count("**Example:**") != concepts.count("**Term —"):
                errors.append(
                    f"{(directory / 'CONCEPTS.md').relative_to(ROOT)}: concept cards need paired example/term labels"
                )

            if "## Execution map" not in acceptance_text:
                errors.append(
                    f"{acceptance.relative_to(ROOT)}: missing command/result/evidence execution map"
                )
            for marker in ("local step", "Record", "recover"):
                if marker.lower() not in acceptance_text.lower():
                    errors.append(
                        f"{acceptance.relative_to(ROOT)}: execution map missing {marker!r}"
                    )

        if state == "new":
            reference_text = (directory / "REFERENCE.md").read_text(encoding="utf-8")
            reference_sections = (
                "## Use now", "## Evaluate after evidence", "## Do not add yet", "## Sources"
            )
            positions = [reference_text.find(f"\n{marker}\n") for marker in reference_sections]
            for marker in reference_sections:
                if reference_text.splitlines().count(marker) != 1:
                    errors.append(
                        f"{(directory / 'REFERENCE.md').relative_to(ROOT)}: missing merged reference section {marker!r}"
                    )
            if all(position >= 0 for position in positions) and positions != sorted(positions):
                errors.append(
                    f"{(directory / 'REFERENCE.md').relative_to(ROOT)}: reference sections are out of order"
                )
            if acceptance_text.splitlines().count("## Review") != 1:
                errors.append(
                    f"{acceptance.relative_to(ROOT)}: four-file contract must merge review prompts under ## Review"
                )

    errors.extend(check_navigation(ROOT, by_code))
    errors.extend(check_cs_contracts(ROOT))

    curriculum = (ROOT / "CURRICULUM.md").read_text(encoding="utf-8")
    rows: dict[str, tuple[str, str, str]] = {}
    for line in curriculum.splitlines():
        match = ROW.match(line)
        if match and match.group(1) in REQUIRED_CONCEPTS:
            rows[match.group(1)] = (match.group(2), match.group(3), match.group(4))
    missing = REQUIRED_CONCEPTS - set(rows)
    extra = set(rows) - REQUIRED_CONCEPTS
    if missing or extra:
        errors.append(f"coverage matrix mismatch: missing={sorted(missing)}, extra={sorted(extra)}")

    stack = (ROOT / "STACK.md").read_text(encoding="utf-8")
    absent_stack_markers = REQUIRED_STACK_MARKERS - set(
        marker for marker in REQUIRED_STACK_MARKERS if marker in stack
    )
    if absent_stack_markers:
        errors.append(f"STACK.md: missing stable stack-policy markers: {sorted(absent_stack_markers)}")

    for concept, (_, practice, proof) in rows.items():
        for cell, expected_prefix, filename in (
            (practice, "C", "CHALLENGE.md"), (proof, "A", "ACCEPTANCE.md")
        ):
            refs = REF.findall(cell)
            if not refs:
                errors.append(f"{concept}: {filename} cell has no traceable milestone ID: {cell}")
                continue
            for number, ids in refs:
                code = f"M{number}"
                target = by_code.get(code)
                if not target:
                    errors.append(f"{concept}: references unknown {code}")
                    continue
                target_text = (target / filename).read_text(encoding="utf-8")
                for identifier in ids.split(","):
                    if not identifier.startswith(expected_prefix) or not re.search(
                        rf"\*\*{re.escape(identifier)}(?:\s|—|:)", target_text
                    ):
                        errors.append(f"{concept}: {code} {identifier} missing from {filename}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    cycle = "Understand problem → Design smallest correct solution → Build → Test → Break deliberately → Debug → Refactor → Operate → Ship"
    if cycle not in readme:
        errors.append("README.md: recurring learning cycle is missing or altered")
    for required_link in ("GLOSSARY.md", "docs/maintainers/README.md"):
        if f"]({required_link})" not in readme:
            errors.append(f"README.md: required navigation link missing: {required_link}")

    quickstart = (
        "git clone YOUR-REPOSITORY-URL vibecamp-swe-track",
        "cd vibecamp-swe-track",
        "git remote -v",
        "cd projects/catalog",
        "cp .env.example .env",
        "uv sync --locked",
        "uv run --locked pytest",
    )
    positions = [readme.find(command) for command in quickstart]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        errors.append("README.md: learner quickstart is missing or out of order")

    catalog = ROOT / "projects" / "catalog"
    missing_catalog = sorted(
        name for name in REQUIRED_CATALOG_FILES if not (catalog / name).is_file()
    )
    if missing_catalog:
        errors.append(f"projects/catalog: missing runnable M0 files: {missing_catalog}")

    for project, required in PROJECT_REQUIREMENTS.items():
        missing_project = sorted(
            name for name in required if not (ROOT / "projects" / project / name).is_file()
        )
        if missing_project:
            errors.append(f"projects/{project}: missing launch-kit files: {missing_project}")

    for project in PROJECTS:
        project_root = ROOT / "projects" / project
        runtime_state, runtime_error = classify_runtime(
            (project_root / "pyproject.toml").read_text(encoding="utf-8"),
            (project_root / ".python-version").read_text(encoding="utf-8"),
        )
        runtime_states[project] = runtime_state
        if runtime_error:
            errors.append(f"projects/{project}: {runtime_error}")
        elif runtime_state != "Air":
            errors.append(
                f"projects/{project}: stable runtime requires Python 3.13 and exact air==0.48.1"
            )
        lockfile = (project_root / "uv.lock").read_text(encoding="utf-8")
        if 'name = "air"\nversion = "0.48.1"' not in lockfile:
            errors.append(f"projects/{project}/uv.lock: exact air 0.48.1 is not locked")

        package = f"{project}_api"
        main_source = (project_root / "src" / package / "main.py").read_text(encoding="utf-8")
        web_source = (project_root / "src" / package / "web.py").read_text(encoding="utf-8")
        combined_source = main_source + "\n" + web_source
        for marker in ("create_app(", "air.Air(fastapi_app=api)", "air.AirRouter(include_in_schema=False)"):
            if marker not in combined_source:
                errors.append(f"projects/{project}: Air/FastAPI composition missing {marker!r}")
        if "include_router(" not in combined_source or "include_in_schema=False" not in combined_source:
            errors.append(f"projects/{project}: human routes are not explicitly excluded from OpenAPI")
        if re.search(r"^(?:from|import) (?:httpx|requests|urllib)", web_source, re.MULTILINE):
            errors.append(f"projects/{project}: web layer must not call its own API over HTTP")

    htmx_projects = {
        project for project in PROJECTS
        if "hx_" in (ROOT / "projects" / project / "src" / f"{project}_api" / "web.py").read_text(encoding="utf-8")
    }
    if htmx_projects != {"ecommerce", "social"}:
        errors.append(f"earned HTMX must appear only in ecommerce and social; found {sorted(htmx_projects)}")
    sse_projects = {
        project for project in PROJECTS
        if "SSEResponse" in (ROOT / "projects" / project / "src" / f"{project}_api" / "web.py").read_text(encoding="utf-8")
    }
    if sse_projects != {"social"}:
        errors.append(f"earned SSE must appear only in social; found {sorted(sse_projects)}")
    catalog_web = (ROOT / "projects/catalog/src/catalog_api/web.py").read_text(encoding="utf-8")
    if "AirForm[ProductDraft]" not in catalog_web or "ProductDraftForm.from_request(request)" not in catalog_web:
        errors.append("projects/catalog: explicit Pydantic-backed AirForm.from_request validation is missing")

    for forbidden in ("package.json",):
        if any(path.name == forbidden and ".venv" not in path.parts for path in ROOT.rglob(forbidden)):
            errors.append(f"second frontend runtime marker exists: {forbidden}")
    project_javascript = [
        path for path in (ROOT / "projects").rglob("*.js") if ".venv" not in path.parts
    ]
    if project_javascript:
        errors.append(f"custom project JavaScript exists: {[str(path.relative_to(ROOT)) for path in project_javascript]}")
    for forbidden in ("AirDB", "air.Jinja", "AirDragon"):
        for path in (ROOT / "projects").glob("*/src/**/*.py"):
            if forbidden in path.read_text(encoding="utf-8"):
                errors.append(f"{path.relative_to(ROOT)}: excluded presentation tool {forbidden}")

    database_dependencies = ("alembic", "fastapi[standard]", "psycopg", "pydantic-settings", "sqlalchemy")
    for project in ("pos", "ecommerce", "booking", "social"):
        pyproject = (ROOT / "projects" / project / "pyproject.toml").read_text(encoding="utf-8").lower()
        for dependency in database_dependencies:
            if dependency not in pyproject:
                errors.append(f"projects/{project}/pyproject.toml: missing Core dependency {dependency}")

    for filename in M0_ACTIVE_FILES:
        active_text = (ROOT / filename).read_text(encoding="utf-8")
        for placeholder in ("<documented", "<port>", "<command>"):
            if placeholder in active_text:
                errors.append(f"{filename}: unresolved learner-path placeholder {placeholder!r}")

    challenge = (catalog / "scripts" / "challenge.py").read_text(encoding="utf-8")
    for scenario in ('"health"', '"type"', '"config"', '"automation"', '"compatibility"'):
        if scenario not in challenge:
            errors.append(f"projects/catalog/scripts/challenge.py: missing {scenario} scenario")

    workflow = (ROOT / ".github" / "workflows" / "repository-hygiene.yml").read_text(
        encoding="utf-8"
    )
    for command in (
        "uv sync --locked",
        "uv run --locked ruff check .",
        "uv run --locked ruff format --check .",
        "uv run --locked mypy",
        "uv run --locked pytest",
    ):
        if command not in workflow:
            errors.append(f"repository-hygiene.yml: catalog check missing: {command}")

    generated_parts = {".git", ".venv", ".mypy_cache", ".pytest_cache", ".ruff_cache", "__pycache__"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or generated_parts.intersection(path.parts):
            continue
        if path.stat().st_size == 0:
            errors.append(f"empty repository file: {path.relative_to(ROOT)}")

    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        markdown = path.read_text(encoding="utf-8")
        if "apps" + "/" in markdown:
            errors.append(f"{path.relative_to(ROOT)}: stale legacy application-path reference")
        for raw in LINK.findall(markdown):
            pieces = raw.split("#", 1)
            target_name = pieces[0].strip()
            anchor = unquote(pieces[1]).lower() if len(pieces) == 2 else ""
            if not target_name or "://" in target_name or target_name.startswith("mailto:"):
                resolved = path if anchor and not target_name else None
                if resolved is None:
                    continue
            else:
                resolved = (path.parent / unquote(target_name)).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {raw}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken relative link: {raw}")
            elif anchor and resolved.suffix.lower() == ".md":
                target_markdown = resolved.read_text(encoding="utf-8")
                if anchor not in heading_anchors(target_markdown):
                    errors.append(f"{path.relative_to(ROOT)}: broken Markdown anchor: {raw}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or generated_parts.intersection(path.parts):
            continue
        if path.suffix.lower() in {".tar", ".gz", ".zip", ".dump"} and "dist" not in path.parts:
            errors.append(f"generated archive outside dist/: {path.relative_to(ROOT)}")
        if path.name == "test_validator_mutations.py":
            continue
        if path.suffix.lower() in {".md", ".py", ".yml", ".yaml", ".toml", ".env"}:
            content = path.read_text(encoding="utf-8", errors="ignore")
            if re.search(r"(?:ghp_|github_pat_|sk-)[A-Za-z0-9_\-]{20,}", content):
                errors.append(f"likely secret in {path.relative_to(ROOT)}")

    for workflow_path in (ROOT / ".github" / "workflows").glob("*.yml"):
        workflow_text = workflow_path.read_text(encoding="utf-8")
        for action in re.findall(r"uses:\s*([^\s#]+)", workflow_text):
            if re.search(r"@v\d+(?:\.\d+)*$", action):
                errors.append(f"{workflow_path.relative_to(ROOT)}: action is not commit-pinned: {action}")

    controlled_vocabulary = {
        "projects/ecommerce": (r"\bshipped\b", "use fulfilled"),
        "milestones/m5-secure-multi-user-ecommerce": (r"\bshipped\b", "use fulfilled"),
    }
    for relative, (pattern, instruction) in controlled_vocabulary.items():
        for path in (ROOT / relative).rglob("*"):
            if path.is_file() and not generated_parts.intersection(path.parts):
                if re.search(pattern, path.read_text(encoding="utf-8", errors="ignore"), re.IGNORECASE):
                    errors.append(f"{path.relative_to(ROOT)}: controlled vocabulary violation; {instruction}")

    ecommerce_source = ROOT / "projects" / "ecommerce" / "src"
    for path in ecommerce_source.rglob("*.py"):
        source = path.read_text(encoding="utf-8")
        if "VULNERABLE_ROUTE" in source or '"/debug/login-as"' in source:
                errors.append(f"{path.relative_to(ROOT)}: callable vulnerable teaching fixture")

    booking_test = (ROOT / "projects/booking/tests/test_postgres.py").read_text(encoding="utf-8")
    for marker in ("Barrier", "ThreadPoolExecutor", "run_on_two_connections_at_barrier", "pg_backend_pid"):
        if marker not in booking_test:
            errors.append(f"projects/booking/tests/test_postgres.py: missing neutral concurrency seam {marker!r}")

    production_compose = (ROOT / "projects/pos/compose.production.yml").read_text(encoding="utf-8")
    for marker in ("migrate:", "service_completed_successfully", "healthcheck:", "/ready"):
        if marker not in production_compose:
            errors.append(f"projects/pos/compose.production.yml: missing release gate {marker!r}")

    image_workflow = (ROOT / ".github/workflows/m10-image.yml").read_text(encoding="utf-8")
    for marker in (
        "needs: [curriculum, starters]", "uv lock --check", "ruff check .", "mypy",
        "alembic upgrade head", "pytest", "pip-audit==", "--local", "push: true", "does not deploy",
    ):
        if marker not in image_workflow:
            errors.append(f"m10-image.yml: missing immutable release prerequisite {marker!r}")

    rehearsal = (ROOT / "projects/pos/scripts/rehearse_m10.sh").read_text(encoding="utf-8")
    for marker in (
        "PREVIOUS_IMAGE_REF", "pg_dump", "psql -v ON_ERROR_STOP=1",
        "compose.unhealthy.yml", "trap cleanup", "--volumes --remove-orphans",
    ):
        if marker not in rehearsal:
            errors.append(f"projects/pos/scripts/rehearse_m10.sh: missing bounded drill {marker!r}")

    dockerfile = (ROOT / "projects/pos/Dockerfile").read_text(encoding="utf-8")
    if not re.search(r"^FROM python:3\.13-slim@sha256:[0-9a-f]{64}$", dockerfile, re.MULTILINE):
        errors.append("projects/pos/Dockerfile: Python 3.13 base image must be digest-pinned")

    provenance = (
        ROOT / "docs/maintainers/archive/2026-09-15-business-first/README.md"
    ).read_text(encoding="utf-8")
    provenance_rows = re.findall(
        r"^\| M(?:10|[0-9]) \| `(?:CONCEPTS|TOOLS|RESOURCES|REVIEW)\.md` \| `[0-9a-f]{64}` \| `(?:REFERENCE\.md|ACCEPTANCE\.md#review)` \|$",
        provenance,
        re.MULTILINE,
    )
    if len(provenance_rows) != 44:
        errors.append(f"BF provenance manifest needs 44 exact source rows; found {len(provenance_rows)}")

    usability = (ROOT / "USABILITY.md").read_text(encoding="utf-8")
    if re.search(r"\bself-service ready\b", usability, flags=re.IGNORECASE):
        errors.append("USABILITY.md: unsupported unqualified self-service-ready claim")

    todo_external = (ROOT / "TODO.md").read_text(encoding="utf-8").split(
        "## External evidence — unchanged and unchecked", 1
    )
    if len(todo_external) != 2 or re.search(r"^- \[x\]", todo_external[-1], re.MULTILINE):
        errors.append("TODO.md: external evidence must remain visible and unchecked")

    if (ROOT / "apps").exists():
        errors.append("stale legacy application directory exists")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    old_count = sum(state == "old" for state in contract_states.values())
    new_count = sum(state == "new" for state in contract_states.values())
    pre_air = [name for name, state in runtime_states.items() if state == "pre-Air"]
    air = [name for name, state in runtime_states.items() if state == "Air"]
    print(
        f"OK: 11 milestone directories; 4 contract files each; "
        f"{len(REQUIRED_CONCEPTS)} concepts traced to challenge and acceptance evidence; links resolve."
    )
    print(f"RUNTIME: Air/Python-3.13={air}.")
    print("LIMIT: structural and semantic lint cannot prove learner understanding or human self-study readiness.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
