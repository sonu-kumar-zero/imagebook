from __future__ import annotations

from typing import Literal, TypeAlias

from PySide6.QtCore import QEvent, QObject, Qt
from PySide6.QtGui import QWheelEvent
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLayout,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)
from app.ui.styles.scroll_bar_stylesheet import PREMIUM_SCROLLBAR_QSS

ScrollDirection: TypeAlias = Literal[
    "horizontal",
    "vertical",
]

LayoutType: TypeAlias = QHBoxLayout | QVBoxLayout


class KScrollArea(QScrollArea):
    def __init__(
        self,
        *,
        direction: ScrollDirection = "vertical",
        parent: QWidget | None = None,
        widget_resizable: bool = True,
        frame_shape: QFrame.Shape = QFrame.Shape.NoFrame,
        horizontal_scrollbar_policy: Qt.ScrollBarPolicy = (
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        ),
        vertical_scrollbar_policy: Qt.ScrollBarPolicy = (
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        ),
        spacing: int = 30,
        margins: tuple[int, int, int, int] = (
            30,
            0,
            30,
            0,
        ),
        alignment: Qt.AlignmentFlag = (
            Qt.AlignmentFlag.AlignTop
        ),
        enable_wheel_scroll: bool = True,
    ) -> None:
        super().__init__(parent)

        self.direction: ScrollDirection = direction
        self.enable_wheel_scroll: bool = enable_wheel_scroll

        self.content: QWidget = QWidget(self)
        self._layout: LayoutType

        self.setWidgetResizable(widget_resizable)
        self.setFrameShape(frame_shape)
        self.setStyleSheet(PREMIUM_SCROLLBAR_QSS)

        self.setHorizontalScrollBarPolicy(
            horizontal_scrollbar_policy
        )
        self.setVerticalScrollBarPolicy(
            vertical_scrollbar_policy
        )

        self._build_ui(
            spacing=spacing,
            margins=margins,
            alignment=alignment,
        )

        if self.enable_wheel_scroll:
            self.viewport().installEventFilter(self)

    def _build_ui(
        self,
        *,
        spacing: int,
        margins: tuple[int, int, int, int],
        alignment: Qt.AlignmentFlag ,
    ) -> None:
        self._layout = self._create_layout()

        self._layout.setSpacing(spacing)
        self._layout.setContentsMargins(*margins)
        self._layout.setAlignment(alignment)

        self.content.setLayout(self._layout)
        self.setWidget(self.content)

    def _create_layout(self) -> LayoutType:
        if self.direction == "horizontal":
            return QHBoxLayout()

        return QVBoxLayout()

    def addWidget(
        self,
        widget: QWidget,
        stretch: int = 0,
        alignment: Qt.AlignmentFlag | None = None,
    ) -> None:
        if alignment is None:
            self._layout.addWidget(widget, stretch)
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
        self._layout.addLayout(layout, stretch)

    def addStretch(
        self,
        stretch: int = 0,
    ) -> None:
        self._layout.addStretch(stretch)

    def insertWidget(
        self,
        index: int,
        widget: QWidget,
        stretch: int = 0,
        alignment: Qt.AlignmentFlag | None = None,
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

    def clear(self) -> None:
        while self._layout.count():
            item = self._layout.takeAt(0)
            if item:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def eventFilter(
        self,
        obj: QObject,
        event: QEvent,
    ) -> bool:
        if (
            self.enable_wheel_scroll
            and obj == self.viewport()
            and event.type() == QEvent.Type.Wheel
            and isinstance(event, QWheelEvent)
        ):
            delta: int = event.angleDelta().y()

            if self.direction == "horizontal":
                scrollbar = self.horizontalScrollBar()
            else:
                scrollbar = self.verticalScrollBar()

            scrollbar.setValue(
                scrollbar.value() - delta
            )

            return True

        return super().eventFilter(obj, event)