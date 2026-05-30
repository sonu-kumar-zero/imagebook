from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class WindowConfig:
    WIDTH: int = 1080
    HEIGHT: int = 720
    TITLE_CAMELCASE: str = "Image Book"
    TITLE_CAPS: str = "IMAGE BOOK"
    TITLE_SMALL: str = "image book"

@dataclass(frozen=True, slots=True)
class SideBarConfig:
    WIDTH:int = 260
    COLLAPSE_THRESHOLD: int = 1220
    COLLAPSE_WIDTH: int = 100

@dataclass(frozen=True, slots=True)
class CarousalConfig:
    HEIGHT: int = 200
    ANIMATION_DURATION: int = 350  # ms
    AUTO_SCROLL_INTERVAL: int = 3000 # ms

@dataclass(frozen=True, slots=True)
class UIConfig:
    WINDOW: WindowConfig = WindowConfig()
    SIDEBAR: SideBarConfig = SideBarConfig()
    CAROUSEL: CarousalConfig = CarousalConfig()


CONFIG = UIConfig()