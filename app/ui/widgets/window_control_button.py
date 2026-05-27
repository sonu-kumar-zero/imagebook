from pathlib import Path

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QPushButton,
    QWidget
    )


class WindowControlButton(QPushButton):
    def __init__(
        self,
        icon_path: Path,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

        self.setProperty(
            "variant",
            "window-control",
        )

        self.setFixedSize(40, 40)

        self.setIcon(
            QIcon(str(icon_path))
        )

        self.setIconSize(
            QSize(18, 18)
        )