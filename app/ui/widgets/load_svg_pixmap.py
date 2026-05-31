from pathlib import Path

from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import Qt
from app.ui.styles.theme import theme
import re

# def load_svg_pixmap(
#     path: Path,
#     color: str = theme.ACCENT,
#     size: int = 24,
# ) -> QPixmap:
#     svg_text = path.read_text(encoding="utf-8")

#     # Replace stroke color
#     svg_text = svg_text.replace(
#         'stroke="currentColor"',
#         f'stroke="{color}"'
#     )


#     pixmap = QPixmap(size, size)
#     pixmap.fill(Qt.GlobalColor.transparent)

#     painter = QPainter(pixmap)

#     renderer = QSvgRenderer(
#         QByteArray(svg_text.encode())
#     )
#     renderer.render(painter)

#     painter.end()

#     return pixmap


def load_svg_pixmap(
    path: Path,
    color: str = theme.ACCENT,
    size: int = 24,
    mode: str = "stroke",  # "stroke" | "fill"
) -> QPixmap:
    svg_text = path.read_text(encoding="utf-8")

    if mode == "stroke":
        svg_text = svg_text.replace(
            'stroke="currentColor"',
            f'stroke="{color}"'
        )
    elif mode == "fill":
        # Remove all stroke attributes
        svg_text = re.sub(r'\bstroke(?:-\w+)?="[^"]*"', '', svg_text)
        # Replace any fill value (except "none") with the target color
        svg_text = re.sub(r'\bfill="[^"]*"', f'fill="{color}"', svg_text)

    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)

    painter = QPainter(pixmap)

    renderer = QSvgRenderer(
        QByteArray(svg_text.encode())
    )
    renderer.render(painter)

    painter.end()

    return pixmap