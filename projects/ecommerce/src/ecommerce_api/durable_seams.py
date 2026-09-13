"""Interfaces and deterministic controls for M7; no durable implementation."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


@dataclass(frozen=True)
class PendingJob:
    message_id: str
    kind: str
    payload: bytes


class OutboxRepository(Protocol):
    def add(self, job: PendingJob) -> None: ...
    def claim(self, *, worker_id: str, now: datetime) -> PendingJob | None: ...
    def succeed(self, *, message_id: str) -> None: ...
    def fail(self, *, message_id: str, retryable: bool) -> None: ...


Clock = Callable[[], datetime]
IdentifierSource = Callable[[], str]
KillHook = Callable[[str], None]


def not_implemented_repository() -> OutboxRepository:
    """Name the learner extension point without supplying durable semantics."""
    raise NotImplementedError("Implement a PostgreSQL outbox during M7")
