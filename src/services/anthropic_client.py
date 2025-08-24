"""Anthropic (Claude) service client.

This client provides a minimal wrapper around the Anthropic API (Claude 3
family) for executing tasks. It inherits from :class:`BaseServiceClient`
defined in ``base_client.py``. For now, the implementation is a stub that
illustrates how an API call could be structured without making any
external network requests.

When you are ready to integrate with the real Anthropic API, populate
``_call_anthropic`` with a request using ``httpx`` or ``requests`` and
handle authentication via the API key stored on the settings object.
"""

from __future__ import annotations

from typing import Any, Dict

from .base_client import BaseServiceClient


class AnthropicClient(BaseServiceClient):
    """Concrete client for the Anthropic Claude service.

    The Anthropic API accepts a prompt and optional parameters such as
    temperature or max_tokens and returns a completion. See
    https://docs.anthropic.com/claude/ for detailed documentation. This
    stub method simply echoes the prompt and returns a placeholder
    response with a cost of zero. Replace the body of
    :meth:`execute_task` with a real API call when integrating the
    service.
    """

    def execute_task(self, task_context: Dict[str, Any]) -> Dict[str, Any]:
        # Extract the prompt from the task context. If it's missing we raise
        # a KeyError so the caller knows to populate the field correctly.
        prompt: str = task_context["prompt"]

        # TODO: Integrate the Anthropic Claude API here. Use the API key
        # available via ``self.settings.anthropic_api_key`` and send an HTTP
        # request to the service's endpoint. Catch any exceptions and let
        # them propagate; the workflow engine will handle retries.

        # For now we return a dummy response containing the prompt.
        return {
            "status": "success",
            "result": f"[Anthropic stub] Echo: {prompt}",
            "cost": 0.0,
        }