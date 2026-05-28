from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class WindowConfig:
    WIDTH: int = 1080
    HEIGHT: int = 720
    TITLE_CAMELCASE: str = "Image Book"
    TITLE_CAPS: str = "IMAGE BOOK"
    TITLE_SMALL: str = "image book"


@dataclass(frozen=True, slots=True)
class UIConfig:
    WINDOW: WindowConfig = WindowConfig()


CONFIG = UIConfig()