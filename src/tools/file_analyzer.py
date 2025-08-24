"""File analysis tool.

This tool performs basic analysis on a file. Currently it reports the
file size in bytes. Extend this stub with more sophisticated logic such
as computing line counts, file hashes or syntactic analysis depending
on the file type.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Union


class FileAnalyzerTool:
    """Analyze properties of a file on disk."""

    def run(self, path: Union[str, Path]) -> Dict[str, int]:
        """Return a dictionary containing basic file statistics.

        Currently returns the file size in bytes. Additional metrics can be
        added as needed.
        """
        p = Path(path)
        return {"size_bytes": p.stat().st_size}