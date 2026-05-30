from pathlib import Path

from PySide6.QtGui import (
    QColor,
    QIcon,
    QPainter,
)
from app.ui.widgets.load_svg_pixmap import load_svg_pixmap
from app.ui.styles.theme import theme


def colored_icon(
    path: Path,
    color: str = theme.ACCENT,
) -> QIcon:
    pixmap = load_svg_pixmap(path, color)

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