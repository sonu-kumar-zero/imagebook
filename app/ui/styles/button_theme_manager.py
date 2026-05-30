from dataclasses import dataclass


# ==========================================================
# COLOR TOKENS
# ==========================================================

@dataclass(frozen=True)
class ColorTokens:
    primary: str = "#3b82f6"
    success: str = "#22c55e"
    warning: str = "#facc15"
    danger: str = "#ef4444"
    neutral: str = "#6b7280"

    bg: str = "#0f172a"
    surface: str = "#111827"
    text: str = "#e5e7eb"


# ==========================================================
# SPACING SYSTEM (Tailwind-like scale)
# ==========================================================

@dataclass(frozen=True)
class SpacingTokens:
    xs: int = 4
    sm: int = 8
    md: int = 12
    lg: int = 16
    xl: int = 24


# ==========================================================
# RADIUS SYSTEM
# ==========================================================

@dataclass(frozen=True)
class RadiusTokens:
    sm: int = 4
    md: int = 8
    lg: int = 12
    full: int = 999


# ==========================================================
# TYPOGRAPHY SYSTEM
# ==========================================================

@dataclass(frozen=True)
class TypographyTokens:
    xs: int = 10
    sm: int = 12
    md: int = 14
    lg: int = 16
    xl: int = 20
    
    
from dataclasses import dataclass


@dataclass
class Theme:
    name: str
    colors: ColorTokens
    spacing: SpacingTokens
    radius: RadiusTokens
    typography: TypographyTokens


# ==========================================================
# PREBUILT THEMES
# ==========================================================

LIGHT_THEME = Theme(
    name="light",
    colors=ColorTokens(
        bg="#ffffff",
        surface="#f3f4f6",
        text="#111827",
    ),
    spacing=SpacingTokens(),
    radius=RadiusTokens(),
    typography=TypographyTokens(),
)

DARK_THEME = Theme(
    name="dark",
    colors=ColorTokens(
        bg="#0f172a",
        surface="#111827",
        text="#e5e7eb",
    ),
    spacing=SpacingTokens(),
    radius=RadiusTokens(),
    typography=TypographyTokens(),
)


# ==========================================================
# GLOBAL THEME MANAGER
# ==========================================================

class ThemeManager:
    _theme: Theme = DARK_THEME

    @classmethod
    def set_theme(cls, theme: Theme):
        cls._theme = theme

    @classmethod
    def get(cls) -> Theme:
        return cls._theme
    
    
from enum import Enum


class UIState(str, Enum):
    DEFAULT = "default"
    HOVER = "hover"
    PRESSED = "pressed"
    DISABLED = "disabled"
    ACTIVE = "active"
    LOADING = "loading"