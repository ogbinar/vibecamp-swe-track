"""Small state model used to choose deterministic M7 worker kill points."""

from dataclasses import dataclass
from enum import StrEnum


class KillPoint(StrEnum):
    AFTER_CLAIM = "after-claim"
    AFTER_EFFECT = "after-effect"
    NEVER = "never"


@dataclass
class WorkItem:
    attempts: int = 0
    effects: int = 0
    acknowledged: bool = False


def run_once(item: WorkItem, *, kill_at: KillPoint) -> None:
    """Expose crash windows; this is a harness, not a durable worker."""
    item.attempts += 1
    if kill_at is KillPoint.AFTER_CLAIM:
        raise SystemExit("worker died after claim")
    item.effects += 1
    if kill_at is KillPoint.AFTER_EFFECT:
        raise SystemExit("worker died after effect and before acknowledgement")
    item.acknowledged = True
