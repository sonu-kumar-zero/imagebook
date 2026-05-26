# app/ui/styles/stylesheet.py

from typing import Final

from app.ui.styles.theme import theme


APP_STYLE: Final[str] = f"""
QWidget {{
    background-color: {theme.APP_BG};
}}

QFrame[variant="card"] {{
    background-color: {theme.CARD_BG};
    border: 1px solid {theme.BORDER_SOFT};
    border-radius: {theme.RADIUS_CARD}px;
}}

QFrame[variant="card"]:hover {{
    background-color: {theme.CARD_BG_HOVER};
    border: 1px solid {theme.BORDER_SOFT_HOVER};
}}

QLabel[variant="title"] {{
    color: {theme.TEXT_PRIMARY};
    font-size: {theme.TITLE_SIZE}px;
    font-weight: 700;
}}

QLabel[variant="subtitle"] {{
    color: {theme.TEXT_SECONDARY};
    font-size: {theme.SUBTITLE_SIZE}px;
}}

QLabel[variant="image"] {{
    border-radius: {theme.RADIUS_IMAGE}px;
}}
"""