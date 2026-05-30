from __future__ import annotations

from collections.abc import Callable

from PySide6.QtCore import Qt
from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QSizePolicy,
    QWidget,
)

from app.ui.widgets.klayout_box import (
    LayoutWrapper,
)
from app.ui.widgets.kframe import FrameWrapper
from pathlib import Path
from app.ui.widgets.load_svg_pixmap import load_svg_pixmap
from app.ui.widgets.text_wrapper import TextWrapper, FontWeight

class ButtonWrapper(QWidget):

    def __init__(
        self,
        text: str = "",
        parent: QWidget | None = None,
        *,
        frame: FrameWrapper | None = None,
        icon_path: Path | None = None,
        icon_size: int = 20,
        spacing: int = 12,
        object_name: str = "button_wrapper",
        width: int | None = None,
        height: int = 52,
        radius: int = 16,
        padding_x: int = 20,
        font_size: int = 14,
        font_weight: FontWeight = "normal",
        text_color: str = "#FFFFFF",
        bg_color: str = "#7C5CFF",
        hover_color: str = "#9374FF",
        pressed_color: str = "#5A3DFF",
        border_color: str = "transparent",
        border_width: int = 0,
        alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeft,
        callback: Callable[[], None]
        | None = None,
    ) -> None:
        super().__init__(parent)

        root = LayoutWrapper(
            direction="vertical",
            margins=(padding_x, 0, padding_x, 0),
            spacing=spacing,
            alignment=alignment,
        )
        

        self.setLayout(root.layout_ref)

        self.button = QPushButton()
        self.button.setObjectName(
            object_name
        )

        self.button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )

        if width is not None:
            self.button.setFixedWidth(width)

        self.button.setFixedHeight(height)

        # ==========================
        # SIMPLE MODE
        # ==========================
        if frame is None:
            self.button.setText(text)

        # ==========================
        # CUSTOM CONTENT MODE
        # ==========================
        else:
            frame.layout_ref.setContentsMargins(padding_x, 0, padding_x, 0)
            frame.layout_ref.setSpacing(spacing)
            
            if icon_path:
                icon_label = QLabel()

                pixmap = load_svg_pixmap(
                    path=icon_path,
                    color=text_color,
                )

                icon_label.setPixmap(
                    pixmap.scaled(
                        icon_size,
                        icon_size,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation,
                    )
                )

                frame.layout_ref.addWidget(
                    icon_label
                )

            text_label = TextWrapper(
                text=text,
                color=text_color,
                font_size=font_size,
                font_weight="normal",
            )

            frame.layout_ref.addWidget(text_label)

            # Put custom widget inside button
            frame.setParent(self.button)

            frame.setAttribute(
                Qt.WidgetAttribute
                .WA_TransparentForMouseEvents,
                True,
            )
            frame.resize(self.button.size())

            self.frame = frame

        self.button.setStyleSheet(
            f"""
            QPushButton#{object_name} {{
                background-color:
                    {bg_color};

                color:
                    {text_color};

                border:
                    {border_width}px
                    solid
                    {border_color};

                border-radius:
                    {radius}px;

                font-size:
                    {font_size}px;

                font-weight:
                    {font_weight};
            }}

            QPushButton#{object_name}:hover {{
                background-color:
                    {hover_color};
            }}

            QPushButton#{object_name}:pressed {{
                background-color:
                    {pressed_color};
            }}

            QLabel {{
                color:
                    {text_color};

                font-size:
                    {font_size}px;

                font-weight:
                    {font_weight};
            }}
            """
        )

        root.layout_ref.addWidget(
            self.button
        )

        if callback:
            self.button.clicked.connect(
                callback
            )

    def resizeEvent(self, event:QResizeEvent) -> None:
        if hasattr(self, "frame"):
            self.frame.setGeometry(
                self.button.rect()
            )

        super().resizeEvent(event)