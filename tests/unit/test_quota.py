"""Unit tests for the QuotaManager."""

import pytest

from src.quota import QuotaManager, QuotaExceededError


def test_quota_allows_within_limit() -> None:
    qm = QuotaManager(max_daily_cost=10.0)
    # Add costs that sum to less than the limit
    qm.check_quota(3.0)
    qm.check_quota(2.0)
    assert qm.current_cost == pytest.approx(5.0)


def test_quota_exceeded_raises() -> None:
    qm = QuotaManager(max_daily_cost=5.0)
    qm.check_quota(5.0)
    with pytest.raises(QuotaExceededError):
        qm.check_quota(0.1)