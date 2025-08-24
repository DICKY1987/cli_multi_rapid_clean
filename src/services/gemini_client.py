"""Gemini (Google Generative AI) service client.

This module defines a thin wrapper around the Google Generative AI API. It
inherits from :class:`BaseServiceClient`. The implementation is a stub
pending integration with the actual Gemini service; it simply echoes the
input prompt. When wiring up the real service, ensure that you handle
authentication using the API key configured in ``self.settings.gemini_api_key``.
"""

from __future__ import annotations

from typing import Any, Dict

from .base_client import BaseServiceClient


class GeminiClient(BaseServiceClient):
    """Concrete client for Google Gemini.

    The Google Generative AI API accepts a prompt and various parameters
    controlling generation. See https://ai.google.dev for usage details. At
    runtime, replace the body of :meth:`execute_task` with a real API
    invocation using an HTTP client such as ``requests``.
    """

    def execute_task(self, task_context: Dict[str, Any]) -> Dict[str, Any]:
        prompt: str = task_context["prompt"]
        # TODO: Add real HTTP request to Google Gemini API using the API key.
        return {
            "status": "success",
            "result": f"[Gemini stub] Echo: {prompt}",
            "cost": 0.0,
        }