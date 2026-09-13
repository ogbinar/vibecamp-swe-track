from dataclasses import dataclass
from threading import Barrier


@dataclass
class NaiveInventory:
    remaining: int
    confirmed: int = 0

    def reserve_once(self) -> bool:
        if self.remaining < 1:
            return False
        self.remaining -= 1
        self.confirmed += 1
        return True

    def reserve_at_barrier(self, barrier: Barrier) -> bool:
        available = self.remaining > 0
        barrier.wait()
        if not available:
            return False
        self.remaining -= 1
        self.confirmed += 1
        return True


def final_seat_inventory() -> NaiveInventory:
    """Return the deterministic one-seat starting state for the M8 harness."""
    return NaiveInventory(remaining=1)
