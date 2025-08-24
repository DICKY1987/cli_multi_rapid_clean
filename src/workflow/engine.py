"""LangGraph workflow engine.

This module defines a minimal workflow engine that executes tasks using
service clients while enforcing quota constraints. It is inspired by
LangGraph but does not implement a full state machine. Instead, it
provides a simple interface to execute a task in a single step. When
integrating a real workflow engine, extend this class with proper
state transitions and error handling.
"""

from __future__ import annotations

from typing import Any, Dict

from ..quota import QuotaManager, QuotaExceededError
from ..service_router import CostOptimizedServiceRouter
from ..db.manager import DatabaseManager


class LangGraphWorkflowEngine:
    """Execute tasks end‑to‑end with quota enforcement and persistence."""

    def __init__(
        self,
        service_router: CostOptimizedServiceRouter,
        quota_manager: QuotaManager,
        db_manager: DatabaseManager,
    ) -> None:
        self.service_router = service_router
        self.quota_manager = quota_manager
        self.db_manager = db_manager

    def _execute_task(self, task_context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a single task and return the result.

        This method selects the appropriate service client, checks the quota
        before dispatching the task, records the execution in the database
        and returns the client’s result. Errors are propagated so that
        callers can implement retry logic or surface errors to users.
        """
        # Persist the execution as pending
        exec_id = self.db_manager.create_execution(
            task_id=task_context.get("task_id", "unknown"),
            service=task_context.get("service", "anthropic"),
            status="pending",
        )
        try:
            # Estimate cost (if provided) and enforce quota
            estimated_cost = task_context.get("estimated_cost", 0.0)
            self.quota_manager.check_quota(estimated_cost)

            # Select the client and execute the task
            client = self.service_router.select_client(task_context)
            result = client.execute_task(task_context)

            # Update database record
            self.db_manager.update_execution(
                exec_id,
                status="completed",
                result=str(result.get("result")),
                cost=result.get("cost", estimated_cost),
            )
            return result
        except QuotaExceededError as qexc:
            self.db_manager.update_execution(exec_id, status="quota_exceeded", result=str(qexc))
            raise
        except Exception as exc:
            # Record failure and re‑raise
            self.db_manager.update_execution(exec_id, status="failed", result=str(exc))
            raise