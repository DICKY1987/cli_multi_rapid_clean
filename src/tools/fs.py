"""File system tool.

This tool exposes basic file system operations such as listing files,
creating directories and removing files. It is intentionally limited in
scope to avoid accidental modification of arbitrary parts of the file
system. Additional safeguards (e.g. path allow lists) should be added
when expanding functionality.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


class FileSystemTool:
    """Perform simple file system operations."""

    def __init__(self, base_dir: Path | str = ".") -> None:
        self.base_dir = Path(base_dir)

    def list_files(self, pattern: str = "*") -> List[str]:
        """Return a list of file paths under ``base_dir`` matching ``pattern``."""
        return [str(p) for p in self.base_dir.glob(pattern) if p.is_file()]

    def make_dir(self, relative_path: str) -> Dict[str, Any]:
        """Create a directory relative to the base directory."""
        path = self.base_dir / relative_path
        path.mkdir(parents=True, exist_ok=True)
        return {"created": str(path)}

    def remove_file(self, relative_path: str) -> Dict[str, Any]:
        """Remove a file relative to the base directory."""
        path = self.base_dir / relative_path
        if path.exists():
            path.unlink()
            return {"removed": str(path)}
        return {"removed": False, "reason": "file not found"}