"""Service router.

The service router is responsible for selecting the appropriate service
client based on the task context. It supports simple strategies such
as cost optimisation or explicit service selection. In this minimal
implementation, the router always returns a default client. Extend
``select_client`` to incorporate more sophisticated logic.
"""

from __future__ import annotations

from typing import Dict, Any

from .services.anthropic_client import AnthropicClient
from .services.gemini_client import GeminiClient
from .services.ollama_client import OllamaClient
from .services.aider_client import AiderClient
from .config import Settings


class CostOptimizedServiceRouter:
    """Select a service client based on cost, availability or explicit hints."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        # Instantiate clients lazily when first used to avoid unnecessary
        # connections during startup.
        self._clients: Dict[str, Any] = {}

    def _get_client(self, service: str):
        if service not in self._clients:
            if service == "anthropic":
                self._clients[service] = AnthropicClient(self.settings)
            elif service == "gemini":
                self._clients[service] = GeminiClient(self.settings)
            elif service == "ollama":
                self._clients[service] = OllamaClient(self.settings)
            elif service == "aider":
                self._clients[service] = AiderClient(self.settings)
            else:
                raise ValueError(f"Unknown service: {service}")
        return self._clients[service]

    def select_client(self, task_context: Dict[str, Any]):
        """Return the appropriate client for the given task context.

        The task context may include an explicit ``service`` key. If
        omitted, Anthropic is used as the default. Future implementations
        could inspect cost estimates, model capabilities or quotas to
        decide.
        """
        service = task_context.get("service", "anthropic")
        return self._get_client(service)