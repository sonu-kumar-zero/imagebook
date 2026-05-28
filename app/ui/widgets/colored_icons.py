from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QColor,
    QIcon,
    QPainter,
    QPixmap,
)


def colored_icon(
    path: Path,
    color: str,
) -> QIcon:
    pixmap = QPixmap(str(path))

    painter = QPainter(pixmap)
    painter.setCompositionMode(
        QPainter.CompositionMode.CompositionMode_SourceIn
    )
    painter.fillRect(
        pixmap.rect(),
        QColor(color),
    )
    painter.end()

    return QIcon(pixmap)