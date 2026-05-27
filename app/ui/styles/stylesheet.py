# app/ui/styles/stylesheet.py

from typing import Final

from app.ui.styles.theme import theme


APP_STYLE: Final[str] = f"""
/* --------------------------------
   Base
-------------------------------- */

QWidget {{
    color: {theme.TEXT_PRIMARY};
    background: transparent;
    font-family: "Segoe UI";
}}

/* --------------------------------
   Main Window
-------------------------------- */

QWidget[variant="window"] {{
    background-color: {theme.APP_BG};
    border-radius: 24px;
    border: 1px solid {theme.BORDER_SOFT};
}}

QWidget[variant="test1"] {{
}}

/* --------------------------------
    Top Bar
-------------------------------- */
QWidget[variant="top-bar"]{{
}}

/* --------------------------------
   Surface / Card
-------------------------------- */

QFrame[variant="card"] {{
    background-color: {theme.CARD_BG};
    border: 1px solid {theme.BORDER_SOFT};
    border-radius: {theme.RADIUS_CARD}px;
}}

QFrame[variant="card"]:hover {{
    background-color: {theme.CARD_BG_HOVER};
    border: 1px solid {theme.BORDER_SOFT_HOVER};
}}

/* Glass section / sidebar surface */
QFrame[variant="surface"] {{
    background-color: {theme.CARD_BG};
    border: 1px solid {theme.BORDER_SOFT};
    border-radius: {theme.RADIUS_CARD}px;
}}

/* --------------------------------
   Typography
-------------------------------- */

QLabel[variant="title"] {{
    color: {theme.TEXT_PRIMARY};
    font-size: {theme.FONT_TITLE}px;
    font-weight: 700;
    background: transparent;
}}

QLabel[variant="subtitle"] {{
    color: {theme.TEXT_SECONDARY};
    font-size: {theme.FONT_SUBTITLE}px;
    background: transparent;
}}

QLabel[variant="image"] {{
    border-radius: {theme.RADIUS_IMAGE}px;
    background: transparent;
}}

/* --------------------------------
   Buttons
-------------------------------- */

QPushButton[variant="primary"] {{
    background-color: {theme.CARD_BG_HOVER};
    border: 1px solid {theme.BORDER_SOFT};
    border-radius: 14px;
    padding: 10px 18px;
    font-weight: 600;
}}

QPushButton[variant="primary"]:hover {{
    border: 1px solid {theme.BORDER_SOFT_HOVER};
}}

QPushButton[variant="primary"]:pressed {{
    padding-top: 11px;
}}

/* --------------------------------
   Scroll Area
-------------------------------- */

QScrollArea {{
    border: none;
    background: transparent;
}}

QScrollBar:vertical {{
    background: transparent;
    width: 10px;
    margin: 4px;
}}

QScrollBar::handle:vertical {{
    background: {theme.BORDER_SOFT};
    border-radius: 5px;
}}

QScrollBar::handle:vertical:hover {{
    background: {theme.BORDER_SOFT_HOVER};
}}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {{
    height: 0;
}}
"""