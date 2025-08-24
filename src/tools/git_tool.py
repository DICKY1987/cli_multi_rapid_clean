"""Git tool.

This tool wraps basic Git operations to allow agents to interact with a
repository. In this stub implementation, only a limited set of
operations are provided (e.g., obtaining the current branch and status).
Extend this class to support committing changes, creating branches or
querying remote repositories.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any, Dict, List


class GitTool:
    """Perform simple Git operations using subprocess."""

    def __init__(self, repo_dir: Path | str) -> None:
        self.repo_dir = Path(repo_dir)

    def run(self, command: List[str]) -> Dict[str, Any]:
        """Execute a git command and return its stdout/stderr.

        ``command`` should be a list of strings passed directly to the
        ``git`` executable. The return value includes the exit code and
        captured output. If the command fails, an exception is raised.
        """
        try:
            result = subprocess.run(
                ["git", *command],
                cwd=self.repo_dir,
                capture_output=True,
                text=True,
                check=True,
            )
            return {
                "exit_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }
        except subprocess.CalledProcessError as exc:
            return {
                "exit_code": exc.returncode,
                "stdout": exc.stdout,
                "stderr": exc.stderr,
            }