
from PySide6.QtWidgets import QHBoxLayout, QWidget, QLabel, QGraphicsOpacityEffect, QGridLayout
from PySide6.QtGui import QPixmap, QMouseEvent, QEnterEvent, QResizeEvent
from PySide6.QtCore import Qt, Signal, QEvent, QPropertyAnimation, QEasingCurve
from app.ui.widgets.frame_wrapper2 import FrameWrapper2
from app.ui.widgets.base_layout import BaseLayout
from app.ui.assets.icons import Icons
from app.ui.widgets.load_svg_pixmap import load_svg_pixmap
from app.ui.widgets.text_wrapper import TextWrapper
from app.ui.styles.theme import theme
from app.ui.styles.utilities import tw

from pathlib import Path
from app.utils.constants import CONFIG

class FaviourateCard(FrameWrapper2):
    clicked = Signal()  # add this signal at class level

    def __init__(
        self,
        header_text: str = "Albums",
        subheader_text: str = "24 albums",
        icon_path: Path = Icons.UPLOAD.path,
        icon_color: str = theme.ACCENT,
        icon_size: int = 36,
        parent: QWidget | None = None,
    ):
        super().__init__(
            parent=parent,
            shape="styled",
            shadow="plain",
            object_name="faviourate-card",
            layout=BaseLayout(
                direction="horizontal",
                margins=(10, 10, 10, 10),
                spacing=10,
            ),
        )
        
        self._header_text = header_text
        self._subheader_text = subheader_text
        self._icon_path = icon_path
        self._icon_color = icon_color
        self._icon_size = icon_size

        self.setStyleSheet(tw("bg-surface-2", "rounded-card"))
        self.setFixedHeight(90)
        self.setCursor(Qt.CursorShape.PointingHandCursor)  # pointer cursor

        # hover animation
        self._bg_effect = QGraphicsOpacityEffect(self)
        self._animation = QPropertyAnimation(self._bg_effect, b"opacity")
        self._animation.setDuration(150)
        self._animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        self._setup_ui()

    def _setup_ui(self) -> None:
        left_layout = BaseLayout(
            direction="horizontal",
            spacing=12,
        )
        left_widget = QWidget()
        left_widget.setFixedHeight(70)
        left_widget.setLayout(left_layout.qlayout)
        _icon: QPixmap = load_svg_pixmap(
            self._icon_path,
            size=self._icon_size,
            color=self._icon_color,
            )

        text_left_layout = BaseLayout(
            direction="vertical",
            spacing=0,
            margins=(0, 0, 0, 0),
        )
        text_left_widget = QWidget()
        text_left_widget.setLayout(text_left_layout.qlayout)
        text_left_widget.setFixedHeight(50)

        header_text_text_left_layout = TextWrapper(
            text=self._header_text,
            font_size=12,
            font_weight="bold",
            color=theme.TEXT_PRIMARY,
            padding=(0, 0, 0, 0),
        )
        subheader_text_text_left_layout = TextWrapper(
            text=self._subheader_text,
            font_size=10,
            font_weight="thin",
            color=theme.TEXT_SECONDARY,
            padding=(0, 0, 0, 0),
        )

        text_left_layout.addWidget(header_text_text_left_layout)
        text_left_layout.addWidget(subheader_text_text_left_layout)

        left_layout.addWidget(QLabel(pixmap=_icon))
        left_layout.addWidget(text_left_widget)
        self.layout_ref.addWidget(left_widget)
        self.layout_ref.addStretch()

        # right chevron
        right_layout = BaseLayout(direction="horizontal", spacing=5)
        self._right_widget = QWidget()
        self._right_widget.setLayout(right_layout.qlayout)
        self._icon_right: QPixmap = load_svg_pixmap(Icons.RIGHT.path, size=24)
        right_layout.addWidget(QLabel(pixmap=self._icon_right))
        self.layout_ref.addWidget(self._right_widget)

    # ── interaction overrides ──────────────────────────────────────────────

    def enterEvent(self, event: QEnterEvent) -> None:
        self.setStyleSheet(tw("bg-surface-3", "rounded-card"))  # lighter on hover
        # slide chevron slightly to the right
        self._right_widget.setContentsMargins(0, 0, 5, 0)
        super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        self.setStyleSheet(tw("bg-surface-2", "rounded-card"))
        self._right_widget.setContentsMargins(0, 0, 0, 0)
        super().leaveEvent(event)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.setStyleSheet(tw("bg-surface-1", "rounded-card"))  # pressed = darker
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.setStyleSheet(tw("bg-surface-3", "rounded-card"))  # back to hover
            if self.rect().contains(event.pos()):
                self.clicked.emit()
        super().mouseReleaseEvent(event)

class FaviourateCardsArea(QWidget):
    BREAKPOINT = CONFIG.SIDEBAR.COLLAPSE_THRESHOLD

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self._is_grid = False
        self._cards: list[FaviourateCard] = []
        self._setup_ui()

    def _setup_ui(self) -> None:
        # root layout just holds the container flush
        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        self._container = QWidget(self)
        root.addWidget(self._container)

        self._cards = [
            FaviourateCard(
                header_text="Albums",
                subheader_text="24 albums",
                icon_path=Icons.UPLOAD.path,
                icon_color="#ff00ff",
            ),
            FaviourateCard(
                header_text="Favorites",
                subheader_text="15 images",
                icon_path=Icons.HEART.path,
                icon_color="#fff00f",
            ),
            FaviourateCard(
                header_text="Collections",
                subheader_text="10 collections",
                icon_path=Icons.BOOKMARK.path,
                icon_color="#f00f00",
            ),
            FaviourateCard(
                header_text="Recently Viewed",
                subheader_text="32 images",
                icon_path=Icons.CLOCK.path,
                icon_color="#22f0ff",
            ),
        ]

        self._apply_horizontal()

    # ── helpers ───────────────────────────────────────────────────────────

    def _detach_cards(self) -> None:
        """Pull cards out of whatever layout owns them right now."""
        layout = self._container.layout()
        if layout is None:
            return
        while layout.count():
            item = layout.takeAt(0)
            if item and item.widget():
                p = item.widget()
                if p:
                    p.setParent(None)
        # orphan the old layout so Qt cleans it up
        QWidget().setLayout(layout)

    # ── layout modes ──────────────────────────────────────────────────────

    def _apply_horizontal(self) -> None:
        self._detach_cards()

        layout = QHBoxLayout(self._container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)

        for card in self._cards:
            card.setFixedHeight(90)
            layout.addWidget(card)

        self._container.setLayout(layout)
        self.setFixedHeight(90)
        self._is_grid = False

    def _apply_grid(self) -> None:
        self._detach_cards()

        layout = QGridLayout(self._container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)

        for i, card in enumerate(self._cards):
            card.setFixedHeight(90)
            layout.addWidget(card, i // 2, i % 2)   # row = i//2, col = i%2

        self._container.setLayout(layout)
        self.setFixedHeight(200)   # 2 × 90 + 20 gap
        self._is_grid = True

    # ── responsive ────────────────────────────────────────────────────────

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        w = self.window().width() if self.window() else self.width()
        should_grid = w < self.BREAKPOINT
        if should_grid and not self._is_grid:
            self._apply_grid()
        elif not should_grid and self._is_grid:
            self._apply_horizontal()