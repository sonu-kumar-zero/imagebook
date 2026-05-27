# app/ui/styles/utilities.py

from typing import Final

from app.ui.styles.types import UtilityClass
from app.ui.styles.theme import theme

from typing import Final

UTILITIES: Final[dict[UtilityClass, str]] = {
    # =========================
    # BACKGROUNDS
    # =========================
    "bg-app": f"""
        background-color: {theme.APP_BG};
    """,

    "bg-surface-1": f"""
        background-color: {theme.SURFACE_1};
    """,

    "bg-surface-2": f"""
        background-color: {theme.SURFACE_2};
    """,

    "bg-surface-3": f"""
        background-color: {theme.SURFACE_3};
    """,

    "bg-card": f"""
        background-color: {theme.CARD_BG};
    """,

    "bg-card-hover": f"""
        background-color: {theme.CARD_BG_HOVER};
    """,

    # =========================
    # BORDERS
    # =========================
    "border-soft": f"""
        border: 1px solid {theme.BORDER_SOFT};
    """,

    "border-soft-hover": f"""
        border: 1px solid {theme.BORDER_SOFT_HOVER};
    """,

    "border-accent": f"""
        border: 1px solid {theme.ACCENT_SOFT};
    """,

    "border-accent-hover": f"""
        border: 1px solid {theme.CARD_BORDER_HOVER};
    """,

    # =========================
    # RADIUS
    # =========================
    "rounded-card": f"""
        border-radius: {theme.RADIUS_CARD}px;
    """,

    "rounded-image": f"""
        border-radius: {theme.RADIUS_IMAGE}px;
    """,

    "rounded-button": f"""
        border-radius: {theme.RADIUS_BUTTON}px;
    """,

    "rounded-input": f"""
        border-radius: {theme.RADIUS_INPUT}px;
    """,

    # =========================
    # TEXT
    # =========================
    "text-primary": f"""
        color: {theme.TEXT_PRIMARY};
    """,

    "text-secondary": f"""
        color: {theme.TEXT_SECONDARY};
    """,

    "text-muted": f"""
        color: {theme.TEXT_MUTED};
    """,

    "text-disabled": f"""
        color: {theme.TEXT_DISABLED};
    """,

    "text-accent": f"""
        color: {theme.TEXT_ACCENT};
    """,

    # =========================
    # TYPOGRAPHY
    # =========================
    "title": f"""
        font-size: {theme.FONT_TITLE}px;
        font-weight: {theme.FONT_WEIGHT_BOLD};
        color: {theme.TEXT_PRIMARY};
    """,

    "subtitle": f"""
        font-size: {theme.FONT_SUBTITLE}px;
        font-weight: {theme.FONT_WEIGHT_MEDIUM};
        color: {theme.TEXT_SECONDARY};
    """,

    "body": f"""
        font-size: {theme.FONT_BODY}px;
        font-weight: {theme.FONT_WEIGHT_NORMAL};
        color: {theme.TEXT_SECONDARY};
    """,

    "small": f"""
        font-size: {theme.FONT_SMALL}px;
        color: {theme.TEXT_MUTED};
    """,

    # =========================
    # EFFECTS (premium feel)
    # =========================
    "shadow-card": f"""
        box-shadow: {theme.CARD_SHADOW};
    """,

    "shadow-card-hover": f"""
        box-shadow: {theme.CARD_SHADOW_HOVER};
    """,

    "glow-accent": f"""
        box-shadow: 0px 0px 20px {theme.ACCENT_SOFT};
    """,

    # =========================
    # SPACING HELPERS
    # =========================
    "p-sm": f"""
        padding: {theme.SPACE_SM}px;
    """,

    "p-md": f"""
        padding: {theme.SPACE_MD}px;
    """,

    "p-lg": f"""
        padding: {theme.SPACE_LG}px;
    """,

    "gap-sm": f"""
        spacing: {theme.SPACE_SM}px;
    """,

    "gap-md": f"""
        spacing: {theme.SPACE_MD}px;
    """,

    "gap-lg": f"""
        spacing: {theme.SPACE_LG}px;
    """,
}

def tw(*classes: UtilityClass) -> str:
    """
    Tailwind-style utility combiner.
    """

    return "\n".join(
        UTILITIES[class_name]
        for class_name in classes
    )