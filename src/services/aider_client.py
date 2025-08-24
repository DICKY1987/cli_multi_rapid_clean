"""Aider service client.

Aider is a local CLI tool for code editing and transformation. This stub
client demonstrates how you might integrate with the aider CLI via a
subprocess call. The actual aider tool must be installed on the host
machine. When implementing the real version, capture stdout/stderr and
return structured results to the workflow engine.
"""

from __future__ import annotations

import subprocess
from typing import Any, Dict

from .base_client import BaseServiceClient


class AiderClient(BaseServiceClient):
    """Concrete client for interacting with the aider CLI tool."""

    def execute_task(self, task_context: Dict[str, Any]) -> Dict[str, Any]:
        command: str = task_context.get("command", "")
        # TODO: In a real implementation, build the aider CLI command from the
        # task_context and invoke it via subprocess.run. Capture the output
        # and convert it into a structured result.
        try:
            # For demonstration, we simply echo the command back. Do not
            # actually execute arbitrary shell commands in production without
            # proper sanitisation and security checks.
            result = subprocess.run(
                ["echo", f"[Aider stub] {command}"],
                capture_output=True,
                text=True,
                check=True,
            )
            return {
                "status": "success",
                "result": result.stdout.strip(),
                "cost": 0.0,
            }
        except subprocess.CalledProcessError as exc:
            raise RuntimeError(f"Aider execution failed: {exc}") from exc