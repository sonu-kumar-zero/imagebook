from pathlib import Path

from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import Qt
from app.ui.styles.theme import theme
from app.core.logger import dprint


def load_svg_pixmap(
    path: Path,
    color: str = theme.ACCENT,
    size: int = 24,
) -> QPixmap:
    svg_text = path.read_text(encoding="utf-8")
    dprint(__file__, f"SVG text: {svg_text[:200]}...")  # Debug: print the first 100 characters of the SVG

    # Replace stroke color
    svg_text = svg_text.replace(
        'stroke="currentColor"',
        f'stroke="{color}"'
    )

    dprint(__file__, f"Modified SVG text: {svg_text[:200]}...")  # Debug: print the modified SVG text

    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)

    painter = QPainter(pixmap)

    renderer = QSvgRenderer(
        QByteArray(svg_text.encode())
    )
    renderer.render(painter)

    painter.end()

    return pixmap