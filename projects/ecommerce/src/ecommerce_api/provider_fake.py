"""Controllable provider double for M6 failure experiments."""

import hashlib
import hmac
from dataclasses import dataclass
from enum import StrEnum


class ProviderMode(StrEnum):
    SUCCESS = "success"
    TIMEOUT_BEFORE = "timeout-before"
    TIMEOUT_AFTER = "timeout-after"
    CONNECT_TIMEOUT = "connect-timeout"
    READ_TIMEOUT = "read-timeout"
    TOTAL_TIMEOUT = "total-timeout"
    DECLINED = "declined"
    RATE_LIMITED = "rate-limited"
    SERVER_ERROR = "server-error"
    MALFORMED = "malformed"


class ProviderTimeout(TimeoutError):
    """The caller cannot know whether the provider completed the request."""


@dataclass
class FakeProvider:
    mode: ProviderMode = ProviderMode.SUCCESS
    calls: int = 0
    completed_keys: set[str] | None = None

    def __post_init__(self) -> None:
        if self.completed_keys is None:
            self.completed_keys = set()

    def charge(self, *, idempotency_key: str) -> str:
        self.calls += 1
        if self.mode in {
            ProviderMode.TIMEOUT_BEFORE,
            ProviderMode.CONNECT_TIMEOUT,
            ProviderMode.READ_TIMEOUT,
            ProviderMode.TOTAL_TIMEOUT,
        }:
            raise ProviderTimeout("timed out before provider processing")
        if self.mode is ProviderMode.DECLINED:
            return "declined"
        if self.mode is ProviderMode.RATE_LIMITED:
            return "429:retry-after=2"
        if self.mode is ProviderMode.SERVER_ERROR:
            return "503"
        if self.mode is ProviderMode.MALFORMED:
            return "{not-json"
        assert self.completed_keys is not None
        self.completed_keys.add(idempotency_key)
        if self.mode is ProviderMode.TIMEOUT_AFTER:
            raise ProviderTimeout("timed out after provider processing")
        return "charged"


@dataclass(frozen=True)
class WebhookDelivery:
    event_id: str
    sequence: int
    body: bytes
    timestamp: int = 1_700_000_000
    account: str = "merchant-test"
    signature: str = ""


def webhook_scenario() -> list[WebhookDelivery]:
    """Return delayed, duplicate, and out-of-order synthetic deliveries."""
    paid = WebhookDelivery("evt-paid", 1, b'{"state":"paid"}')
    fulfilled = WebhookDelivery("evt-fulfilled", 2, b'{"state":"fulfilled"}')
    return [fulfilled, paid, paid]


def signed_webhook_fixtures() -> dict[str, WebhookDelivery]:
    """Return safe synthetic inputs; the learner implements verification."""
    key = b"synthetic-course-key"

    def signed(
        name: str, body: bytes, *, timestamp: int = 1_700_000_000, account: str = "merchant-test"
    ) -> WebhookDelivery:
        payload = str(timestamp).encode() + b"." + body
        signature = hmac.new(key, payload, hashlib.sha256).hexdigest()
        return WebhookDelivery(name, 1, body, timestamp, account, signature)

    valid = signed("evt-valid", b'{"state":"paid"}')
    tampered = WebhookDelivery(
        "evt-tampered", 1, b'{"state":"refunded"}', valid.timestamp, valid.account, valid.signature
    )
    return {
        "valid": valid,
        "duplicate": valid,
        "delayed": signed("evt-delayed", b'{"state":"paid"}', timestamp=1_600_000_000),
        "wrong_account": signed("evt-account", b'{"state":"paid"}', account="other-test"),
        "tampered": tampered,
        "replay": valid,
    }
