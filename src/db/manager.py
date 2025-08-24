"""Database manager for the Agentic Framework.

This class provides a simple interface around an SQLite database. It
creates the required tables on initialisation and exposes methods for
creating and retrieving :class:`WorkflowExecution` records. For
production use, consider using an ORM such as SQLAlchemy which provides
migrations, connection pooling and richer querying capabilities.
"""

from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from typing import Iterator, List, Optional

from .models import WorkflowExecution


class DatabaseManager:
    """Minimal SQLite database manager."""

    def __init__(self, db_path: str = "agentic.db") -> None:
        self.db_path = db_path
        self._initialise()

    def _initialise(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS workflow_executions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id TEXT NOT NULL,
                    service TEXT NOT NULL,
                    status TEXT NOT NULL,
                    result TEXT,
                    cost REAL NOT NULL DEFAULT 0.0,
                    created_at TEXT NOT NULL
                )
                """
            )

    @contextmanager
    def _connect(self) -> Iterator[sqlite3.Connection]:
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def create_execution(self, task_id: str, service: str, status: str = "pending", result: Optional[str] = None, cost: float = 0.0) -> int:
        """Insert a new workflow execution and return its ID."""
        with self._connect() as conn:
            cursor = conn.execute(
                """
                INSERT INTO workflow_executions (task_id, service, status, result, cost, created_at)
                VALUES (?, ?, ?, ?, ?, datetime('now'))
                """,
                (task_id, service, status, result, cost),
            )
            return cursor.lastrowid

    def update_execution(self, execution_id: int, status: Optional[str] = None, result: Optional[str] = None, cost: Optional[float] = None) -> None:
        """Update an existing workflow execution record."""
        with self._connect() as conn:
            fields = []
            values = []
            if status is not None:
                fields.append("status = ?")
                values.append(status)
            if result is not None:
                fields.append("result = ?")
                values.append(result)
            if cost is not None:
                fields.append("cost = ?")
                values.append(cost)
            values.append(execution_id)
            conn.execute(
                f"UPDATE workflow_executions SET {', '.join(fields)} WHERE id = ?",
                values,
            )

    def get_execution(self, execution_id: int) -> Optional[WorkflowExecution]:
        """Retrieve a workflow execution by ID, or ``None`` if not found."""
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT id, task_id, service, status, result, cost, created_at FROM workflow_executions WHERE id = ?",
                (execution_id,),
            )
            row = cursor.fetchone()
            if not row:
                return None
            execution = WorkflowExecution(
                task_id=row[1],
                service=row[2],
                status=row[3],
                result=row[4],
                cost=row[5],
            )
            execution.id = row[0]
            return execution

    def list_executions(self) -> List[WorkflowExecution]:
        """Return a list of all workflow executions."""
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT id, task_id, service, status, result, cost, created_at FROM workflow_executions"
            )
            rows = cursor.fetchall()
            executions = []
            for row in rows:
                execution = WorkflowExecution(
                    task_id=row[1],
                    service=row[2],
                    status=row[3],
                    result=row[4],
                    cost=row[5],
                )
                execution.id = row[0]
                executions.append(execution)
            return executions