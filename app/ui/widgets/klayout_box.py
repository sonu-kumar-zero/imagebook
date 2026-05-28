from __future__ import annotations

from typing import Literal, TypeAlias

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLayout,
    QVBoxLayout,
    QWidget,
)

# ==========================================================
# TYPES
# ==========================================================

LayoutDirection: TypeAlias = Literal[
    "horizontal",
    "vertical",
]

BoxLayoutType: TypeAlias = (
    QHBoxLayout
    | QVBoxLayout
)


# ==========================================================
# BOX LAYOUT WRAPPER (HBox / VBox)
# ==========================================================

class LayoutWrapper(QWidget):
    def __init__(
        self,
        *,
        direction: LayoutDirection = "vertical",
        parent: QWidget | None = None,
        spacing: int = 0,
        margins: tuple[int, int, int, int] = (
            0,
            0,
            0,
            0,
        ),
        alignment: Qt.AlignmentFlag
        | None = None,
    ) -> None:
        super().__init__(parent)

        self.direction: LayoutDirection = (
            direction
        )

        self._layout: BoxLayoutType = (
            self._create_layout()
        )

        self._layout.setSpacing(
            spacing
        )

        self._layout.setContentsMargins(
            *margins
        )

        if alignment is not None:
            self._layout.setAlignment(
                alignment
            )

        self.setLayout(
            self._layout
        )

    # ======================================================
    # INTERNALS
    # ======================================================

    def _create_layout(
        self,
    ) -> BoxLayoutType:
        if (
            self.direction
            == "horizontal"
        ):
            return QHBoxLayout()

        return QVBoxLayout()

    # ======================================================
    # ADD ITEMS
    # ======================================================

    def addWidget(
        self,
        widget: QWidget,
        stretch: int = 0,
        alignment: Qt.AlignmentFlag
        | None = None,
    ) -> None:
        if alignment is None:
            self._layout.addWidget(
                widget,
                stretch,
            )
            return

        self._layout.addWidget(
            widget,
            stretch,
            alignment,
        )

    def addLayout(
        self,
        layout: QLayout,
        stretch: int = 0,
    ) -> None:
        self._layout.addLayout(
            layout,
            stretch,
        )

    def addSpacing(
        self,
        value: int,
    ) -> None:
        self._layout.addSpacing(
            value
        )

    def addStretch(
        self,
        stretch: int = 0,
    ) -> None:
        self._layout.addStretch(
            stretch
        )

    def insertWidget(
        self,
        index: int,
        widget: QWidget,
        stretch: int = 0,
        alignment: Qt.AlignmentFlag
        | None = None,
    ) -> None:
        if alignment is None:
            self._layout.insertWidget(
                index,
                widget,
                stretch,
            )
            return

        self._layout.insertWidget(
            index,
            widget,
            stretch,
            alignment,
        )

    def removeWidget(
        self,
        widget: QWidget,
    ) -> None:
        self._layout.removeWidget(
            widget
        )

    def clear(
        self,
    ) -> None:
        while self._layout.count():
            item = (
                self._layout.takeAt(0)
            )

            if item:
                widget = (item.widget())

                if widget is not None:
                    widget.deleteLater()

    # ======================================================
    # CUSTOMIZATION
    # ======================================================

    def setSpacing(
        self,
        spacing: int,
    ) -> None:
        self._layout.setSpacing(
            spacing
        )

    def setMargins(
        self,
        left: int,
        top: int,
        right: int,
        bottom: int,
    ) -> None:
        self._layout.setContentsMargins(
            left,
            top,
            right,
            bottom,
        )

    def setAlignment(
        self,
        alignment: Qt.AlignmentFlag
    ) -> None:
        self._layout.setAlignment(
            alignment
        )

    @property
    def layout_ref(
        self,
    ) -> BoxLayoutType:
        return self._layout


# ==========================================================
# GRID LAYOUT WRAPPER
# ==========================================================

class GridLayoutWrapper(QWidget):
    def __init__(
        self,
        *,
        parent: QWidget | None = None,
        spacing: int = 0,
        margins: tuple[int, int, int, int] = (
            0,
            0,
            0,
            0,
        ),
        alignment: Qt.AlignmentFlag | None = None,
    ) -> None:
        super().__init__(parent)

        self._layout: QGridLayout = (
            QGridLayout()
        )

        self._layout.setSpacing(
            spacing
        )

        self._layout.setContentsMargins(
            *margins
        )

        if alignment is not None:
            self._layout.setAlignment(
                alignment
            )

        self.setLayout(
            self._layout
        )

    # ======================================================
    # ADD ITEMS
    # ======================================================

    def addWidget(
        self,
        widget: QWidget,
        row: int,
        column: int,
        row_span: int = 1,
        column_span: int = 1,
        alignment: Qt.AlignmentFlag | None = None,
    ) -> None:
        if alignment is None:
            self._layout.addWidget(
                widget,
                row,
                column,
                row_span,
                column_span,
            )
            return

        self._layout.addWidget(
            widget,
            row,
            column,
            row_span,
            column_span,
            alignment,
        )

    def addLayout(
        self,
        layout: QLayout,
        row: int,
        column: int,
        row_span: int = 1,
        column_span: int = 1,
    ) -> None:
        self._layout.addLayout(
            layout,
            row,
            column,
            row_span,
            column_span,
        )

    def setRowStretch(
        self,
        row: int,
        stretch: int,
    ) -> None:
        self._layout.setRowStretch(
            row,
            stretch,
        )

    def setColumnStretch(
        self,
        column: int,
        stretch: int,
    ) -> None:
        self._layout.setColumnStretch(
            column,
            stretch,
        )

    def removeWidget(
        self,
        widget: QWidget,
    ) -> None:
        self._layout.removeWidget(
            widget
        )

    def clear(
        self,
    ) -> None:
        while self._layout.count():
            item = (
                self._layout.takeAt(0)
            )

            if item:
                widget = (
                    item.widget()
                )

                if widget is not None:
                    widget.deleteLater()

    # ======================================================
    # CUSTOMIZATION
    # ======================================================

    def setSpacing(
        self,
        spacing: int,
    ) -> None:
        self._layout.setSpacing(
            spacing
        )

    def setMargins(
        self,
        left: int,
        top: int,
        right: int,
        bottom: int,
    ) -> None:
        self._layout.setContentsMargins(
            left,
            top,
            right,
            bottom,
        )

    def setAlignment(
        self,
        alignment: Qt.AlignmentFlag
    ) -> None:
        self._layout.setAlignment(
            alignment
        )

    @property
    def layout_ref(
        self,
    ) -> QGridLayout:
        return self._layout