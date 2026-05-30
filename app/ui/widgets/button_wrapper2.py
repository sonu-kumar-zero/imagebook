from __future__ import annotations

from pathlib import Path
from typing import Callable, Literal

from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QIcon, QFont, QMouseEvent, QEnterEvent
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

from app.ui.widgets.text_wrapper import FONT_WEIGHT_MAP, TextWrapper
from app.ui.widgets.load_svg_pixmap import load_svg_pixmap


FontWeight = Literal["thin", "light", "normal", "medium", "bold", "black"]
IconPosition = Literal["left", "right", "only"]


class ButtonWrapper2(QWidget):
    def __init__(
        self,
        text: str = "",
        parent: QWidget | None = None,
        *,
        icon_path: Path | None = None,
        icon_size: int = 18,
        spacing: int = 10,
        object_name: str = "button_wrapper",
        width: int | None = None,
        height: int = 52,
        radius: int = 14,
        padding_x: int = 16,
        font_size: int = 14,
        font_weight: FontWeight = "normal",
        text_color: str = "#FFFFFF",
        bg_color: str = "#7C5CFF",
        hover_color: str = "#8B6CFF",
        pressed_color: str = "#5A3DFF",
        disabled_color: str = "#2E2E2E",
        border_color: str = "transparent",
        border_width: int = 0,
        icon_position: IconPosition = "left",
        alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
        callback: Callable[[], None] | None = None,
    ) -> None:
        super().__init__(parent)

        # -------------------------
        # Core state
        # -------------------------
        self._callback = callback
        self._bg = bg_color
        self._hover = hover_color
        self._pressed = pressed_color
        self._disabled = disabled_color
        self._radius = radius
        self._border = border_color
        self._border_width = border_width
        self._icon_position = icon_position
        self._alignment = alignment

        self.setObjectName(object_name)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # -------------------------
        # Widgets
        # -------------------------
        self.icon_label = QLabel()
        self.text_label = TextWrapper(
            text=text,
            color=text_color,
            font_size=font_size,
            font_weight=font_weight,
        )

        font = QFont()
        font.setPointSize(font_size)
        font.setWeight(FONT_WEIGHT_MAP.get(font_weight, QFont.Weight.Normal))
        self.text_label.setFont(font)

        if icon_path:
            self.icon_label.setPixmap(load_svg_pixmap(
                path=icon_path,
                color=text_color,
                size=icon_size + 8,
            ))
        else:
            self.icon_label.hide()

        # -------------------------
        # Layout (SINGLE LAYOUT ONLY)
        # -------------------------
        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(padding_x, 0, padding_x, 0)
        self._layout.setSpacing(spacing)
        self._layout.setAlignment(alignment)

        self._apply_layout(icon_position)

        # -------------------------
        # Size
        # -------------------------
        if width:
            self.setFixedWidth(width)
        self.setFixedHeight(height)

        # -------------------------
        # Style
        # -------------------------
        self._apply_style(normal=True)

    # ==========================================================
    # Layout logic (NO layout swapping)
    # ==========================================================
    def _apply_layout(self, position: IconPosition):
        self._layout.removeWidget(self.icon_label)
        self._layout.removeWidget(self.text_label)

        if position == "only":
            self.text_label.hide()
            self._layout.addWidget(self.icon_label, alignment=self._alignment)
            return

        self.text_label.show()
        self.icon_label.show()

        if position == "left":
            self._layout.addWidget(self.icon_label, alignment=self._alignment)
            self._layout.addWidget(self.text_label, alignment=self._alignment)

        elif position == "right":
            self._layout.addWidget(self.text_label, alignment=self._alignment)
            self._layout.addWidget(self.icon_label, alignment=self._alignment)

    # ==========================================================
    # Styling engine (STATE BASED)
    # ==========================================================
    def _apply_style(self, normal: bool = False, hover: bool = False, pressed: bool = False, disabled: bool = False):
        bg = self._bg
        if disabled:
            bg = self._disabled
        elif pressed:
            bg = self._pressed
        elif hover:
            bg = self._hover

        self.setStyleSheet(f"""
        QWidget#{self.objectName()} {{
            background-color: {bg};
            border-radius: {self._radius}px;
            border: {self._border_width}px solid {self._border};
        }}
        """)

    # ==========================================================
    # Events (for hover/press feedback)
    # ==========================================================
    def enterEvent(self, event: QEnterEvent):
        self._apply_style(hover=True)
        super().enterEvent(event)

    def leaveEvent(self, event: QEvent):
        self._apply_style()
        super().leaveEvent(event)

    def mousePressEvent(self, event: QMouseEvent):
        self._apply_style(pressed=True)
        if self._callback:
            self._callback()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self._apply_style(hover=True)
        super().mouseReleaseEvent(event)

    # ==========================================================
    # Public API
    # ==========================================================
    def setText(self, text: str):
        self.text_label.setText(text)

    def setIcon(self, icon_path: Path, size: int = 18):
        self.icon_label.setPixmap(QIcon(str(icon_path)).pixmap(size, size))
        self.icon_label.show()

    def setIconPosition(self, position: IconPosition):
        self._icon_position = position
        self._apply_layout(position)

    def setEnabled(self, enabled: bool):
        super().setEnabled(enabled)
        self._apply_style(disabled=not enabled)

    def removeIcon(self):
        self.icon_label.hide()