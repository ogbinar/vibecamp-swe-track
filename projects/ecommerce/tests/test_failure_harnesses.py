import pytest

from ecommerce_api.outbox_lab import KillPoint, WorkItem, run_once
from ecommerce_api.provider_fake import (
    FakeProvider,
    ProviderMode,
    ProviderTimeout,
    signed_webhook_fixtures,
    webhook_scenario,
)


def test_provider_exposes_unknown_outcome() -> None:
    provider = FakeProvider(mode=ProviderMode.TIMEOUT_AFTER)
    with pytest.raises(ProviderTimeout, match="after provider processing"):
        provider.charge(idempotency_key="order-1")
    assert provider.completed_keys == {"order-1"}


@pytest.mark.parametrize(
    "mode",
    [ProviderMode.CONNECT_TIMEOUT, ProviderMode.READ_TIMEOUT, ProviderMode.TOTAL_TIMEOUT],
)
def test_timeout_phase_is_controllable(mode: ProviderMode) -> None:
    provider = FakeProvider(mode=mode)
    with pytest.raises(ProviderTimeout, match="before provider processing"):
        provider.charge(idempotency_key="order-1")
    assert provider.completed_keys == set()


def test_worker_harness_exposes_duplicate_effect_window() -> None:
    item = WorkItem()
    with pytest.raises(SystemExit, match="before acknowledgement"):
        run_once(item, kill_at=KillPoint.AFTER_EFFECT)
    assert (item.effects, item.acknowledged) == (1, False)


@pytest.mark.parametrize(
    ("mode", "result"),
    [
        (ProviderMode.SUCCESS, "charged"),
        (ProviderMode.DECLINED, "declined"),
        (ProviderMode.RATE_LIMITED, "429:retry-after=2"),
        (ProviderMode.SERVER_ERROR, "503"),
        (ProviderMode.MALFORMED, "{not-json"),
    ],
)
def test_provider_modes_are_controllable(mode: ProviderMode, result: str) -> None:
    assert FakeProvider(mode=mode).charge(idempotency_key="order-1") == result


def test_webhook_scenario_is_out_of_order_and_duplicated() -> None:
    deliveries = webhook_scenario()
    assert [item.sequence for item in deliveries] == [2, 1, 1]
    assert deliveries[1] == deliveries[2]


def test_signed_webhook_fixture_matrix_is_bounded_and_synthetic() -> None:
    fixtures = signed_webhook_fixtures()
    assert set(fixtures) == {"valid", "duplicate", "delayed", "wrong_account", "tampered", "replay"}
    assert fixtures["valid"] == fixtures["duplicate"] == fixtures["replay"]
    assert fixtures["tampered"].body != fixtures["valid"].body


def test_worker_replay_exposes_duplicate_effect() -> None:
    item = WorkItem()
    with pytest.raises(SystemExit):
        run_once(item, kill_at=KillPoint.AFTER_EFFECT)
    run_once(item, kill_at=KillPoint.NEVER)
    assert (item.attempts, item.effects, item.acknowledged) == (2, 2, True)
