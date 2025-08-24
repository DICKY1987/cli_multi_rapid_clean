"""Agent tools package.

This package aggregates tool implementations used by agents within the
framework. Each tool encapsulates a discrete capability such as web
searching, document reading, file analysis or running tests. Tools
provide a common ``run`` method which accepts structured parameters and
returns a result. Having a unified interface simplifies wiring tools
into agents and allows the router to treat them uniformly.
"""

from .web_search import WebSearchTool  # noqa: F401
from .doc_reader import DocumentReaderTool  # noqa: F401
from .file_analyzer import FileAnalyzerTool  # noqa: F401
from .code_analyzer import CodeAnalyzerTool  # noqa: F401
from .git_tool import GitTool  # noqa: F401
from .testing_tool import TestingTool  # noqa: F401
from .github_api import GitHubAPITool  # noqa: F401
from .fs import FileSystemTool  # noqa: F401

__all__ = [
    "WebSearchTool",
    "DocumentReaderTool",
    "FileAnalyzerTool",
    "CodeAnalyzerTool",
    "GitTool",
    "TestingTool",
    "GitHubAPITool",
    "FileSystemTool",
]