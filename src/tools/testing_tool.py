"""Testing tool.

This tool runs a test suite using ``pytest``. It is a simple wrapper
around the ``pytest`` command executed in a subprocess. The stub
implementation runs ``pytest -q`` and returns the exit code and
captured output.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Dict


class TestingTool:
    """Run the project's test suite using pytest."""

    def __init__(self, project_root: Path | str = ".") -> None:
        self.project_root = Path(project_root)

    def run(self) -> Dict[str, str]:
        """Execute ``pytest -q`` in the project root and return the results."""
        try:
            result = subprocess.run(
                ["pytest", "-q"],
                cwd=self.project_root,
                capture_output=True,
                text=True,
                check=True,
            )
            return {
                "status": "success",
                "output": result.stdout,
            }
        except subprocess.CalledProcessError as exc:
            return {
                "status": "failure",
                "output": exc.stdout + exc.stderr,
            }