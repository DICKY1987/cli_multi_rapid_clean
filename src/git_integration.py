"""Git lane manager and worktree integration.

The Git lane manager is responsible for creating isolated worktrees for
each lane (branch) so that concurrent agent runs do not interfere
with each other. This stub implementation creates a worktree directory
under ``worktrees/`` and checks out the requested branch. In a real
environment, error handling should be added and edge cases (e.g.,
existing worktrees, branch divergence) must be considered.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Dict


class GitLaneManager:
    """Manage Git worktrees for agent lanes."""

    def __init__(self, repo_dir: Path | str) -> None:
        self.repo_dir = Path(repo_dir)
        self.worktrees_dir = self.repo_dir / "worktrees"
        self.worktrees_dir.mkdir(exist_ok=True)

    def create_lane_worktree(self, lane_name: str) -> Dict[str, str]:
        """Create a worktree for ``lane_name`` and return its path.

        If the worktree already exists, it is reused. This implementation
        assumes that ``git`` is installed and available in the PATH. It
        checks out the lane starting from the default branch (``main``).
        """
        worktree_path = self.worktrees_dir / lane_name.replace("/", "-")
        if worktree_path.exists():
            return {"path": str(worktree_path)}
        # Create the worktree by running `git worktree add`
        subprocess.run(
            ["git", "worktree", "add", str(worktree_path), lane_name],
            cwd=self.repo_dir,
            check=True,
        )
        return {"path": str(worktree_path)}