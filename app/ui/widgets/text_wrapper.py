from __future__ import annotations

from typing import Literal, TypeAlias

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel,
    QSizePolicy,
    QWidget,
)

from app.ui.widgets.kframe import (
    FrameWrapper,
)
from app.ui.widgets.klayout_box import (
    LayoutWrapper,
)
from app.ui.styles.types import Variant
from app.ui.styles.helpers import set_variant

# ==========================================================
# TYPES
# ==========================================================

FontWeight: TypeAlias = Literal[
    "thin",
    "light",
    "normal",
    "medium",
    "bold",
    "black",
]


# ==========================================================
# TEXT WRAPPER
# ==========================================================

class TextWrapper(FrameWrapper):
    def __init__(
        self,
        *,
        parent: QWidget | None = None,
        text: str = "",
        font_size: int = 14,
        font_weight: FontWeight = ("normal"),
        alignment: Qt.AlignmentFlag = (
            Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        ),
        word_wrap: bool = False,
        selectable: bool = False,
        padding: tuple[int, int, int, int] = (0,0,0,0),
        bg_color: str = ("transparent"),
        color: str | None = None,
        border_radius: int = 0,
        object_name: str | None = None,
        variant: Variant | None = None,
    ) -> None:
        super().__init__(
            parent=parent,
            object_name=object_name,
            bg_color=bg_color,
            border_radius=border_radius,
            layout=LayoutWrapper(
                margins=padding,
            ),
            color=color,
        )
        
        if variant is not None:
            set_variant(self,variant)

        self.label = QLabel()

        self.label.setText(
            text
        )

        self.label.setAlignment(
            alignment
        )

        self.label.setWordWrap(
            word_wrap
        )

        self.label.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Minimum,
        )

        if selectable:
            self.label.setTextInteractionFlags(
                Qt.TextInteractionFlag.
                TextSelectableByMouse
            )

        self._apply_font(
            size=font_size,
            weight=font_weight,
        )

        self.layout_ref.addWidget(
            self.label
        )

    # ======================================================
    # TEXT
    # ======================================================

    def setText(
        self,
        text: str,
    ) -> None:
        self.label.setText(
            text
        )

    def text(
        self,
    ) -> str:
        return self.label.text()

    # ======================================================
    # FONT
    # ======================================================

    def _apply_font(
        self,
        *,
        size: int,
        weight: FontWeight,
    ) -> None:
        font = QFont()

        font.setPointSize(
            size
        )

        font.setWeight(
            self._font_weight(
                weight
            )
        )

        self.label.setFont(
            font
        )

    def setFontSize(
        self,
        size: int,
    ) -> None:
        font = (
            self.label.font()
        )

        font.setPointSize(
            size
        )

        self.label.setFont(
            font
        )

    def setFontWeight(
        self,
        weight: FontWeight,
    ) -> None:
        font = (
            self.label.font()
        )

        font.setWeight(
            self._font_weight(
                weight
            )
        )

        self.label.setFont(
            font
        )

    # ======================================================
    # ALIGNMENT
    # ======================================================

    def setAlignment(
        self,
        alignment: Qt.AlignmentFlag,
    ) -> None:
        self.label.setAlignment(
            alignment
        )

    # ======================================================
    # INTERNALS
    # ======================================================

    def _font_weight(
        self,
        weight: FontWeight,
    ) -> QFont.Weight:
        mapping = {
            "thin": (
                QFont.Weight.Thin
            ),
            "light": (
                QFont.Weight.Light
            ),
            "normal": (
                QFont.Weight.Normal
            ),
            "medium": (
                QFont.Weight.Medium
            ),
            "bold": (
                QFont.Weight.Bold
            ),
            "black": (
                QFont.Weight.Black
            ),
        }

        return mapping[weight]