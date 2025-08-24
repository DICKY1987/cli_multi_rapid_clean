"""Unit tests for the service router."""

from src.config import Settings
from src.service_router import CostOptimizedServiceRouter


def test_select_default_client() -> None:
    settings = Settings()
    router = CostOptimizedServiceRouter(settings)
    client = router.select_client({"prompt": "hello"})
    # Default should be AnthropicClient
    from src.services.anthropic_client import AnthropicClient
    assert isinstance(client, AnthropicClient)


def test_select_specific_client() -> None:
    settings = Settings()
    router = CostOptimizedServiceRouter(settings)
    client = router.select_client({"prompt": "hi", "service": "gemini"})
    from src.services.gemini_client import GeminiClient
    assert isinstance(client, GeminiClient)