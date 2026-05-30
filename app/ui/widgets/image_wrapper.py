from __future__ import annotations

from pathlib import Path
from typing import Literal, TypeAlias

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QResizeEvent
from PySide6.QtWidgets import (
    QLabel,
    QSizePolicy,
    QWidget,
)

# ==========================================================
# TYPES
# ==========================================================

ImageFit: TypeAlias = Literal[
    "contain",
    "cover",
]


# ==========================================================
# IMAGE WRAPPER
# ==========================================================

class ImageWrapper(QLabel):
    def __init__(
        self,
        *,
        parent: QWidget | None = None,
        image_path: str | Path | None = None,
        width: int | None = None,
        height: int | None = None,
        fit: ImageFit = "contain",
        alignment: Qt.AlignmentFlag = (
            Qt.AlignmentFlag.AlignCenter
        ),
        object_name: str | None = None,
    ) -> None:
        super().__init__(parent)

        self.setAlignment(alignment)

        self.setScaledContents(False)

        self._fit: ImageFit = fit
        self._pixmap: QPixmap | None = None

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        if width is not None:
            self.setFixedWidth(width)

        if height is not None:
            self.setFixedHeight(height)

        if object_name:
            self.setObjectName(
                object_name
            )

        if image_path is not None:
            self.setImage(
                image_path
            )

    # ======================================================
    # IMAGE
    # ======================================================

    def setImage(
        self,
        image_path: str | Path,
    ) -> None:
        pixmap = QPixmap(
            str(image_path)
        )

        if pixmap.isNull():
            return

        self._pixmap = pixmap
        self._update_pixmap()

    def clearImage(
        self,
    ) -> None:
        self._pixmap = None
        self.clear()

    # ======================================================
    # INTERNALS
    # ======================================================

    def resizeEvent(
        self,
        event: QResizeEvent,
    ) -> None:
        super().resizeEvent(
            event
        )

        self._update_pixmap()

    def _update_pixmap(
        self,
    ) -> None:
        if self._pixmap is None:
            return

        mode = (
            Qt.AspectRatioMode.
            KeepAspectRatio
        )

        if self._fit == "cover":
            mode = (
                Qt.AspectRatioMode.
                KeepAspectRatioByExpanding
            )

        scaled = (
            self._pixmap.scaled(
                self.size(),
                mode,
                Qt.TransformationMode.
                SmoothTransformation,
            )
        )

        self.setPixmap(
            scaled
        )