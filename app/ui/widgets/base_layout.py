from __future__ import annotations

from typing import Literal, TypeAlias

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLayout, QWidget


LayoutDirection: TypeAlias = Literal["horizontal", "vertical"]


class BaseLayout:
    """
    Pure layout abstraction (no QWidget dependency).
    Can be nested inside any QWidget or QLayout.
    """

    def __init__(
        self,
        *,
        direction: LayoutDirection = "vertical",
        spacing: int = 0,
        margins: tuple[int, int, int, int] = (0, 0, 0, 0),
        alignment: Qt.AlignmentFlag | None = None,
    ) -> None:

        self.direction = direction
        self._layout: QVBoxLayout | QHBoxLayout = self._create_layout()

        self._layout.setSpacing(spacing)
        self._layout.setContentsMargins(*margins)

        if alignment is not None:
            self._layout.setAlignment(alignment)

    # -----------------------------
    # INTERNAL
    # -----------------------------

    def _create_layout(self) -> QVBoxLayout | QHBoxLayout:
        if self.direction == "horizontal":
            return QHBoxLayout()
        return QVBoxLayout()

    # -----------------------------
    # CORE API
    # -----------------------------

    def addWidget(
        self,
        widget: QWidget,
        stretch: int = 0,
        alignment: Qt.AlignmentFlag | None = None,
    ) -> None:

        if alignment is None:
            self._layout.addWidget(widget, stretch)
        else:
            self._layout.addWidget(widget, stretch, alignment)

    def addLayout(self, layout: QLayout, stretch: int = 0) -> None:
        self._layout.addLayout(layout, stretch)

    def addSpacing(self, value: int) -> None:
        self._layout.addSpacing(value)

    def addStretch(self, stretch: int = 0) -> None:
        self._layout.addStretch(stretch)

    def insertWidget(
        self,
        index: int,
        widget: QWidget,
        stretch: int = 0,
        alignment: Qt.AlignmentFlag | None = None,
    ) -> None:

        if alignment is None:
            self._layout.insertWidget(index, widget, stretch)
        else:
            self._layout.insertWidget(index, widget, stretch, alignment)

    def removeWidget(self, widget: QWidget) -> None:
        self._layout.removeWidget(widget)

    def clear(self) -> None:
        while self._layout.count():
            item = self._layout.takeAt(0)
            w = item.widget() if item else None
            if w:
                w.deleteLater()

    # -----------------------------
    # CONFIG
    # -----------------------------

    def setSpacing(self, spacing: int) -> None:
        self._layout.setSpacing(spacing)

    def setMargins(self, left: int, top: int, right: int, bottom: int) -> None:
        self._layout.setContentsMargins(left, top, right, bottom)

    def setAlignment(self, alignment: Qt.AlignmentFlag) -> None:
        self._layout.setAlignment(alignment)

    # -----------------------------
    # ACCESS
    # -----------------------------

    @property
    def qlayout(self) -> QLayout:
        return self._layout
    