from pathlib import Path

from PySide6.QtCore import QEasingCurve, QSize, Qt, QPropertyAnimation, QEvent
from PySide6.QtGui import QIcon, QEnterEvent
from PySide6.QtWidgets import QPushButton, QWidget


class WindowControlButton(QPushButton):
    def __init__(self, icon_path: Path, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setFixedSize(40, 40)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setIcon(QIcon(str(icon_path)))
        self.setIconSize(QSize(18, 18))

        # animation setup
        self._anim = QPropertyAnimation(self, b"iconSize")
        self._anim.setDuration(120)

    def enterEvent(self, event: QEnterEvent):
        self._animate_icon(QSize(22, 22))  # scale up
        super().enterEvent(event)

    def leaveEvent(self, event:QEvent):
        self._animate_icon(QSize(18, 18))  # scale back
        super().leaveEvent(event)

    def _animate_icon(self, target_size: QSize):
        self._anim.stop()
        self._anim.setStartValue(self.iconSize())
        self._anim.setEndValue(target_size)
        self._anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._anim.start()