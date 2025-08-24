"""GitHub API tool.

This tool provides a minimal wrapper for interacting with the GitHub API.
It uses the ``requests`` library to send authenticated requests to
retrieve repository information. At present, the implementation only
supports fetching repository metadata. To add more functionality, extend
the :meth:`run` method to handle different actions and endpoints.
"""

from __future__ import annotations

from typing import Any, Dict

import requests


class GitHubAPITool:
    """Interact with the GitHub REST API."""

    def __init__(self, token: str) -> None:
        self.token = token

    def run(self, repo: str) -> Dict[str, Any]:
        """Return basic information about a GitHub repository.

        ``repo`` should be in the form ``owner/name``. The returned
        dictionary contains selected fields from the repository object. In
        case of an error (e.g. network failure), a dictionary with an
        ``error`` key is returned instead.
        """
        url = f"https://api.github.com/repos/{repo}"
        headers = {"Authorization": f"token {self.token}"} if self.token else {}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            return {
                "full_name": data.get("full_name"),
                "description": data.get("description"),
                "stargazers_count": data.get("stargazers_count"),
                "forks_count": data.get("forks_count"),
            }
        except Exception as exc:
            return {"error": str(exc)}