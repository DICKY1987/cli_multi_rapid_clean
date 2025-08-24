"""Base service client definition.

This module defines an abstract base class for service clients. A service
client is responsible for submitting a task to a downstream large language
model or tool and returning a result. Concrete clients such as
``AnthropicClient`` or ``GeminiClient`` should subclass
``BaseServiceClient`` and implement the :meth:`execute_task` method.

Keeping a common interface for clients allows the rest of the codebase –
particularly the service router and workflow engine – to remain agnostic
about which backend is used. Clients can also share common initialisation
logic through the base class.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseServiceClient(ABC):
    """Abstract base class for all service clients.

    Subclasses must implement the :meth:`execute_task` method, which
    performs the actual call to the underlying service. Instances are
    expected to be long‑lived and thread‑safe; avoid storing per‑call state
    on the instance.
    """

    def __init__(self, settings: Any) -> None:
        """Initialise the client with a settings object.

        The settings object should expose any configuration required by the
        client such as API keys, base URLs or timeouts. Using dependency
        injection here simplifies testing and decouples clients from
        environment variables.
        """
        self.settings = settings

    @abstractmethod
    def execute_task(self, task_context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a task and return a result.

        The ``task_context`` dictionary contains all information required
        for execution, such as the user prompt, any file references, and
        optional parameters controlling cost or temperature. Implementations
        should return a dictionary containing at least a ``status`` key and
        optionally a ``result`` and ``cost``. If an error occurs, clients
        should raise an exception rather than returning an error object; the
        workflow engine is responsible for handling exceptions uniformly.
        """

        raise NotImplementedError