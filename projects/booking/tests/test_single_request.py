from threading import Barrier, Thread

from booking_lab.reservations import NaiveInventory, final_seat_inventory


def test_one_seat_can_be_reserved_once() -> None:
    inventory = NaiveInventory(remaining=1)
    assert inventory.reserve_once() is True
    assert inventory.reserve_once() is False
    assert inventory.remaining == 0
    assert inventory.confirmed == 1


def test_concurrency_fixture_reproduces_documented_symptom() -> None:
    inventory = final_seat_inventory()
    barrier = Barrier(2)
    threads = [Thread(target=inventory.reserve_at_barrier, args=(barrier,)) for _ in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=2)
    assert not any(thread.is_alive() for thread in threads)
    assert (inventory.confirmed, inventory.remaining) == (2, -1)
