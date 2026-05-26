# app/ui/styles/utilities.py

from typing import Final

from app.ui.styles.theme import Theme
from app.ui.styles.types import UtilityClass


UTILITIES: Final[dict[UtilityClass, str]] = {
    "bg-card": f"""
        background-color: {Theme.CARD_BG};
    """,

    "bg-card-hover": f"""
        background-color: {Theme.CARD_BG_HOVER};
    """,

    "border-soft": f"""
        border: 1px solid {Theme.BORDER_SOFT};
    """,

    "border-soft-hover": f"""
        border: 1px solid {Theme.BORDER_SOFT_HOVER};
    """,

    "rounded-card": f"""
        border-radius: {Theme.RADIUS_CARD}px;
    """,

    "rounded-image": f"""
        border-radius: {Theme.RADIUS_IMAGE}px;
    """,

    "text-primary": f"""
        color: {Theme.TEXT_PRIMARY};
    """,

    "text-secondary": f"""
        color: {Theme.TEXT_SECONDARY};
    """,

    "title": f"""
        font-size: {Theme.TITLE_SIZE}px;
        font-weight: 700;
    """,

    "subtitle": f"""
        font-size: {Theme.SUBTITLE_SIZE}px;
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