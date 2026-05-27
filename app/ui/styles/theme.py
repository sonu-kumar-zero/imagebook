# app/ui/styles/theme.py
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Theme:
    # =========================
    # BASE BACKGROUND
    # =========================
    APP_BG: str = "#0B0D12"              # softer than pure #0F1117
    APP_BG_GRADIENT_TOP: str = "#0B0D12"
    APP_BG_GRADIENT_BOTTOM: str = "#0E111A"

    SURFACE_1: str = "rgba(20, 22, 30, 0.92)"
    SURFACE_2: str = "rgba(28, 30, 40, 0.95)"
    SURFACE_3: str = "rgba(36, 38, 52, 0.98)"

    # =========================
    # ACCENT SYSTEM (IMPORTANT)
    # =========================
    ACCENT: str = "#7C5CFF"              # premium violet
    ACCENT_SOFT: str = "rgba(124, 92, 255, 0.15)"
    ACCENT_HOVER: str = "#9A7BFF"
    ACCENT_ACTIVE: str = "#5A3DFF"

    # =========================
    # CARDS (ELEVATION LAYERS)
    # =========================
    CARD_BG: str = "rgba(20, 22, 30, 0.85)"
    CARD_BG_HOVER: str = "rgba(28, 30, 40, 0.92)"
    CARD_BORDER: str = "rgba(255, 255, 255, 0.06)"
    CARD_BORDER_HOVER: str = "rgba(124, 92, 255, 0.25)"

    CARD_SHADOW: str = "0px 10px 30px rgba(0, 0, 0, 0.45)"
    CARD_SHADOW_HOVER: str = "0px 18px 50px rgba(0, 0, 0, 0.65)"

    # =========================
    # BORDERS / DIVIDERS
    # =========================
    BORDER_SOFT: str = "rgba(255, 255, 255, 0.06)"
    BORDER_SOFT_HOVER: str = "rgba(255, 255, 255, 0.12)"
    DIVIDER: str = "rgba(255, 255, 255, 0.05)"

    # =========================
    # TEXT HIERARCHY
    # =========================
    TEXT_PRIMARY: str = "#F5F7FF"
    TEXT_SECONDARY: str = "rgba(245, 247, 255, 0.65)"
    TEXT_MUTED: str = "rgba(245, 247, 255, 0.45)"
    TEXT_DISABLED: str = "rgba(245, 247, 255, 0.25)"

    TEXT_ACCENT: str = "#A48CFF"

    # =========================
    # TYPOGRAPHY SCALE
    # =========================
    FONT_TITLE: int = 26
    FONT_SUBTITLE: int = 16
    FONT_BODY: int = 13
    FONT_SMALL: int = 11

    FONT_WEIGHT_BOLD: int = 700
    FONT_WEIGHT_MEDIUM: int = 500
    FONT_WEIGHT_NORMAL: int = 400

    # =========================
    # RADIUS (MODERN SOFT UI)
    # =========================
    RADIUS_CARD: int = 22
    RADIUS_IMAGE: int = 18
    RADIUS_BUTTON: int = 14
    RADIUS_INPUT: int = 12

    # =========================
    # SPACING SYSTEM (IMPORTANT FOR PREMIUM FEEL)
    # =========================
    SPACE_XS: int = 6
    SPACE_SM: int = 10
    SPACE_MD: int = 16
    SPACE_LG: int = 24
    SPACE_XL: int = 32

    # =========================
    # IMAGE SPECIFIC
    # =========================
    IMAGE_OVERLAY: str = "rgba(0, 0, 0, 0.35)"
    IMAGE_HOVER_OVERLAY: str = "rgba(124, 92, 255, 0.12)"

    # =========================
    # EFFECTS
    # =========================
    BLUR_BG: int = 18
    DROP_SHADOW_INTENSITY: float = 0.6


theme = Theme()