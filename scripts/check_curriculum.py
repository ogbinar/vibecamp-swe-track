"""Dependency-free validation of curriculum structure, traceability, and links."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MILESTONES = ROOT / "milestones"
REQUIRED_ROOT = {
    "README.md", "CURRICULUM.md", "STACK.md", "QUALITY-GATES.md", "PROGRESS.md",
    "PLAN.md", "TODO.md", "projects", "challenges", "templates", ".github/workflows",
}
REQUIRED_FILES = {
    "README.md", "CONCEPTS.md", "CHALLENGE.md", "TOOLS.md",
    "ACCEPTANCE.md", "REVIEW.md", "RESOURCES.md",
}
REQUIRED_TEMPLATES = {
    "ADR.md", "COMPLEXITY-REJECTION.md", "DATA-LIFECYCLE.md",
    "ENTRY-DIAGNOSTIC.md", "EVIDENCE-INDEX.md", "INCIDENT-POSTMORTEM.md",
    "PORTFOLIO-CASE-STUDY.md", "REQUIREMENTS.md",
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


def milestone_map(directories: list[Path]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in directories:
        match = re.fullmatch(r"m(10|[0-9])-[a-z0-9-]+", path.name)
        if match:
            result[f"M{match.group(1)}"] = path
    return result


def main() -> int:
    errors: list[str] = []
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
        if entries != REQUIRED_FILES:
            errors.append(
                f"{directory.relative_to(ROOT)}: expected exactly seven contract files; "
                f"missing={sorted(REQUIRED_FILES - entries)}, extra={sorted(entries - REQUIRED_FILES)}"
            )
        acceptance = directory / "ACCEPTANCE.md"
        if acceptance.exists():
            acceptance_text = acceptance.read_text(encoding="utf-8")
            for heading in ("## Core", "## Stretch"):
                if acceptance_text.count(heading) != 1:
                    errors.append(f"{acceptance.relative_to(ROOT)}: expected exactly one {heading}")
            if "Required maturity:" not in acceptance_text:
                errors.append(f"{acceptance.relative_to(ROOT)}: missing required maturity declaration")

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
    for required_link in ("PLAN.md", "TODO.md", "templates/ENTRY-DIAGNOSTIC.md", "templates/PORTFOLIO-CASE-STUDY.md"):
        if f"]({required_link})" not in readme:
            errors.append(f"README.md: required navigation link missing: {required_link}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
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
            target_name = raw.split("#", 1)[0].strip()
            if not target_name or "://" in target_name or target_name.startswith("mailto:"):
                continue
            resolved = (path.parent / unquote(target_name)).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {raw}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken relative link: {raw}")

    if (ROOT / "apps").exists():
        errors.append("stale legacy application directory exists")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(
        f"OK: 11 milestone directories; 7 contract files each; "
        f"{len(REQUIRED_CONCEPTS)} concepts traced to challenge and acceptance evidence; links resolve."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
