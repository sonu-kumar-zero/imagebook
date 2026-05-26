# app/ui/styles/theme.py

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Theme:
    APP_BG: str = "#0F1117"

    CARD_BG: str = "rgba(24,24,32,230)"
    CARD_BG_HOVER: str = "rgba(34,34,44,240)"

    BORDER_SOFT: str = "rgba(255,255,255,0.08)"
    BORDER_SOFT_HOVER: str = "rgba(255,255,255,0.14)"

    TEXT_PRIMARY: str = "white"
    TEXT_SECONDARY: str = "rgba(255,255,255,0.65)"

    RADIUS_CARD: int = 28
    RADIUS_IMAGE: int = 22

    TITLE_SIZE: int = 22
    SUBTITLE_SIZE: int = 14


theme = Theme()