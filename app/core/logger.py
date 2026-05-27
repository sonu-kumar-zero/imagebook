# app/core/logger.py

from pathlib import Path
from typing import Any


def dprint(
    file: str,
    *args: Any,
) -> None:
    relative_path = (
        Path(file)
        .resolve()
        .relative_to(Path.cwd())
    )

    print(
        f"[{relative_path}]",
        *args,
    )