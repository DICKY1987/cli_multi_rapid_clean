"""Application configuration.

This module centralises the configuration settings for the framework.
Using Pydantic's :class:`~pydantic.BaseSettings` allows environment
variables to be loaded automatically and validated. The ``Settings``
class can be instantiated once at application startup and passed to
components such as service clients, the database manager and the quota
manager.
"""

from __future__ import annotations

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Configuration settings loaded from environment variables or a .env file."""

    # API keys for external services
    anthropic_api_key: str = Field("", env="ANTHROPIC_API_KEY")
    gemini_api_key: str = Field("", env="GEMINI_API_KEY")
    github_token: str = Field("", env="GITHUB_TOKEN")

    # Local service configuration
    ollama_api_base: str = Field("http://localhost:11434", env="OLLAMA_API_BASE")
    aider_cli_path: str = Field("aider", env="AIDER_CLI_PATH")

    # Database configuration
    db_url: str = Field("agentic.db", env="AGENTIC_DB")

    # Redis configuration (for quota and caching)
    redis_url: str = Field("redis://localhost:6379/0", env="REDIS_URL")

    # Quota management
    max_daily_cost: float = Field(10.0, env="MAX_DAILY_COST")

    # Git configuration
    default_branch: str = Field("main", env="DEFAULT_BRANCH")
    lanes_config_path: str = Field("lanes.yaml", env="LANES_CONFIG_PATH")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"