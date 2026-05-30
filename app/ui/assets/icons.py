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
    EXPLORE = "explore.svg"
    GALLERY = "gallery.svg"
    COLLECTIONS = "collections.svg"
    FAVORITES = "favorites.svg"
    UPLOAD = "upload.svg"
    HOME = "home.svg"
    SETTINGS = "settings.svg"
    USER = "user.svg"
    ADD = "add.svg"

    @property
    def path(self) -> Path:
        return ICON_DIR / self.value
        