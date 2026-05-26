# app/utils/paths.py

from pathlib import Path
from typing import Final
import sys


def get_base_path() -> Path:
    """
    Return project base path in both:
    - development mode
    - PyInstaller executable mode
    """

    meipass: str | None = getattr(
        sys,
        "_MEIPASS",
        None,
    )

    if meipass is not None:
        return Path(meipass)

    return Path(__file__).resolve().parents[2]


BASE_DIR: Final[Path] = get_base_path()

ASSETS_DIR: Final[Path] = (
    BASE_DIR / "app" / "ui" / "assets"
)