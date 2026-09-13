from concurrent.futures import ThreadPoolExecutor
from threading import Barrier

from booking_lab.reservations import final_seat_inventory


def test_two_requests_cannot_confirm_one_seat() -> None:
    inventory = final_seat_inventory()
    barrier = Barrier(2)
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(lambda _: inventory.reserve_at_barrier(barrier), range(2)))
    assert sum(results) == 1
    assert inventory.remaining == 0
    assert inventory.confirmed == 1
