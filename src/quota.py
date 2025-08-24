"""Quota management.

This module defines a simple quota manager used to enforce daily cost
limits across service calls. It stores the accumulated cost in memory
per instance. For production use, consider persisting quota usage in
Redis or another data store so that usage is shared across processes
and survives restarts.
"""

from __future__ import annotations

from typing import Dict


class QuotaExceededError(Exception):
    """Raised when a service call would exceed the configured quota."""


class QuotaManager:
    """Track and enforce a daily cost quota for service calls."""

    def __init__(self, max_daily_cost: float) -> None:
        self.max_daily_cost = max_daily_cost
        self.current_cost: float = 0.0

    def check_quota(self, cost: float) -> None:
        """Ensure that adding ``cost`` does not exceed the daily quota.

        If the quota would be exceeded, :class:`QuotaExceededError` is
        raised. Otherwise, the cost is added to the current usage.
        """
        if self.current_cost + cost > self.max_daily_cost:
            raise QuotaExceededError(
                f"Quota exceeded: {self.current_cost + cost} > {self.max_daily_cost}"
            )
        self.current_cost += cost

    def reset(self) -> None:
        """Reset the current usage to zero (e.g. at the start of a new day)."""
        self.current_cost = 0.0

    def to_dict(self) -> Dict[str, float]:
        """Return the current quota state as a dictionary."""
        return {
            "max_daily_cost": self.max_daily_cost,
            "current_cost": self.current_cost,
        }