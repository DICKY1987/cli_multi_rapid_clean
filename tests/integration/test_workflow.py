"""Integration tests for the workflow engine."""

from src.config import Settings
from src.quota import QuotaManager
from src.service_router import CostOptimizedServiceRouter
from src.db.manager import DatabaseManager
from src.workflow.engine import LangGraphWorkflowEngine


def test_execute_simple_task() -> None:
    settings = Settings()
    router = CostOptimizedServiceRouter(settings)
    quota = QuotaManager(max_daily_cost=5.0)
    db = DatabaseManager(":memory:")  # Use in-memory DB for tests
    engine = LangGraphWorkflowEngine(router, quota, db)
    result = engine._execute_task({"task_id": "t1", "prompt": "hi"})
    assert result["status"] == "success"
    # Execution record should exist in the database
    executions = db.list_executions()
    assert len(executions) == 1
    assert executions[0].status == "completed"