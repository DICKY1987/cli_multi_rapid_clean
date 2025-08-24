"""Database models for the Agentic Framework.

This module defines the data structures persisted to the database. For
simplicity, we model a single table ``workflow_executions`` which stores
records of tasks executed through the framework. Each record contains
basic metadata such as the task ID, service used, status, result and
cost. Additional tables can be added in the future as needed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class WorkflowExecution:
    """Dataclass representing a workflow execution record."""

    id: int = field(init=False)
    task_id: str
    service: str
    status: str = "pending"
    result: Optional[str] = None
    cost: float = 0.0
    created_at: datetime = field(default_factory=datetime.utcnow)