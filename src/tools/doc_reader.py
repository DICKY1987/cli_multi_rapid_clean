"""Document reader tool.

This tool reads the contents of a text document from the local filesystem.
It is intentionally kept simple to avoid external dependencies. For
structured documents like PDFs or Word files, consider integrating with
libraries such as ``pdfminer.six`` or ``python-docx`` in the future.
"""

from __future__ import annotations

from pathlib import Path
from typing import Union


class DocumentReaderTool:
    """Read the contents of a document from disk."""

    def run(self, path: Union[str, Path]) -> str:
        """Return the contents of the file at ``path`` as a string.

        If the file cannot be read (e.g. due to encoding issues), an
        exception will be raised. The caller should handle any exceptions
        gracefully.
        """
        p = Path(path)
        return p.read_text(encoding="utf-8")