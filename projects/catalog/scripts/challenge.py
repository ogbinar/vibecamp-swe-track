"""Safely activate, inspect, or reset one deterministic M0 defect."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / ".challenge-state.json"


@dataclass(frozen=True)
class Change:
    path: str
    baseline: str
    faulty: str


SCENARIOS = {
    "health": Change("src/catalog_api/app.py", 'status="ok"', 'status="warning"'),
    "type": Change("src/catalog_api/app.py", 'price=Decimal("19.99")', 'price="19.99"'),
    "config": Change(
        "src/catalog_api/settings.py",
        "service_name: str = Field(default=..., min_length=1)",
        'service_name: str = "Catalog from hidden default"',
    ),
    "automation": Change(
        "pyproject.toml", 'requires-python = "==3.12.*"', 'requires-python = "==3.13.*"'
    ),
    "compatibility": Change(
        "src/catalog_api/models.py",
        "name: str = Field(min_length=1)",
        'name: str = Field(min_length=1, serialization_alias="title")',
    ),
}


def replace(change: Change, old: str, new: str) -> None:
    path = ROOT / change.path
    text = path.read_text(encoding="utf-8")
    if old not in text:
        if new in text:
            return
        raise SystemExit(f"Refusing to alter {change.path}: expected text was not found.")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def activate(name: str) -> None:
    if name not in SCENARIOS:
        raise SystemExit(f"Unknown scenario {name!r}. Choose: {', '.join(SCENARIOS)}")
    if STATE.exists():
        raise SystemExit("A challenge is already active. Run `status` or `reset` first.")
    change = SCENARIOS[name]
    replace(change, change.baseline, change.faulty)
    STATE.write_text(json.dumps({"scenario": name}) + "\n", encoding="utf-8")
    print(f"Activated M0 challenge: {name}. Record a hypothesis before inspecting code.")


def reset() -> None:
    if not STATE.exists():
        print("No challenge is active.")
        return
    name = json.loads(STATE.read_text(encoding="utf-8"))["scenario"]
    change = SCENARIOS[name]
    replace(change, change.faulty, change.baseline)
    STATE.unlink()
    print(f"Reset M0 challenge: {name}.")


def status() -> None:
    if not STATE.exists():
        print("No challenge is active.")
        return
    name = json.loads(STATE.read_text(encoding="utf-8"))["scenario"]
    print(f"Active M0 challenge: {name}.")


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] not in {"activate", "reset", "status"}:
        raise SystemExit("Usage: python scripts/challenge.py activate NAME | status | reset")
    command = sys.argv[1]
    if command == "activate":
        if len(sys.argv) != 3:
            raise SystemExit("Usage: python scripts/challenge.py activate NAME")
        activate(sys.argv[2])
    elif command == "reset":
        reset()
    else:
        status()


if __name__ == "__main__":
    main()
