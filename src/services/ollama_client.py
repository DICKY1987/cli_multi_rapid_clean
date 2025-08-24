"""Ollama service client.

Ollama is a local runtime for large language models which exposes a REST
interface by default on ``http://localhost:11434``. This client provides
a minimal wrapper for submitting prompts to an Ollama model. The default
model can be configured via the settings object. For now, the
implementation simply returns the prompt for demonstration purposes.
"""

from __future__ import annotations

from typing import Any, Dict

from .base_client import BaseServiceClient


class OllamaClient(BaseServiceClient):
    """Concrete client for local Ollama models.
    See https://github.com/ollama/ollama for usage details.
    """

    def execute_task(self, task_context: Dict[str, Any]) -> Dict[str, Any]:
        prompt: str = task_context["prompt"]
        # TODO: Connect to the Ollama REST API. Use
        # ``self.settings.ollama_api_base`` as the base URL. Determine the
        # desired model from ``task_context.get('model')`` or from the
        # configuration. Implement retry and timeout logic as needed.
        return {
            "status": "success",
            "result": f"[Ollama stub] Echo: {prompt}",
            "cost": 0.0,
        }