from enum import StrEnum
from pathlib import Path

ICON_DIR = (
    Path(__file__).parent / "icons"
)


class Icons(StrEnum):
    CROSS = "cross.svg"
    MINIMIZE = "minimize.svg"
    MAXIMIZE = "maximize.svg"
    MENU = "menu.svg"
    MAXIMIZE_MID = "maximize_mid.svg"

    @property
    def path(self) -> Path:
        return ICON_DIR / self.value
        