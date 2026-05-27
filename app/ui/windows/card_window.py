from typing import Final

from PySide6.QtCore import (
    Qt,
    QEvent,
    QObject
)
from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QScrollArea
)
from PySide6.QtGui import QWheelEvent


from app.ui.styles.helpers import set_variant
from app.ui.styles.stylesheet import APP_STYLE
from app.ui.widgets.top_bar_home_screen import TopBar
from app.ui.assets.images import Images
from app.ui.widgets.image_card_card_screen import ImageCard
from app.ui.styles.utilities import tw

image_paths: list[str] = [
str(Images.IMAGE1.path),
str(Images.IMAGE2.path),
str(Images.IMAGE3.path),
str(Images.IMAGE4.path)
]



class CardWindow(QWidget):
    WINDOW_WIDTH: Final[int] = 1080
    WINDOW_HEIGHT: Final[int] = 720

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Premium Card UI")

        self.resize(
            self.WINDOW_WIDTH,
            self.WINDOW_HEIGHT,
        )

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Window
        )

        set_variant(self,"window")

        self.setStyleSheet(APP_STYLE)

        self.setup_ui()

    def setup_ui(self) -> None:

        cards: list[ImageCard] = [
            ImageCard(image_paths[0], "Mountain Lake", "Peaceful reflection in nature"),
            ImageCard(image_paths[1], "Cyber City", "Premium futuristic design"),
            ImageCard(image_paths[2], "Forest View", "Deep calm and nature vibes"),
            ImageCard(image_paths[0], "Mountain Lake", "Peaceful reflection in nature"),
            ImageCard(image_paths[1], "Cyber City", "Premium futuristic design"),
            ImageCard(image_paths[2], "Forest View", "Deep calm and nature vibes"),
            ImageCard(image_paths[0], "Mountain Lake", "Peaceful reflection in nature"),
            ImageCard(image_paths[1], "Cyber City", "Premium futuristic design"),
            ImageCard(image_paths[2], "Forest View", "Deep calm and nature vibes"),
            ImageCard(image_paths[0], "Mountain Lake", "Peaceful reflection in nature"),
            ImageCard(image_paths[1], "Cyber City", "Premium futuristic design"),
            ImageCard(image_paths[2], "Forest View", "Deep calm and nature vibes"),
        ]

        # ---------------------------
        # ROOT WINDOW LAYOUT
        # ---------------------------
        window_layout = QVBoxLayout(self)
        window_layout.setContentsMargins(0, 0, 0, 0)
        window_layout.setSpacing(0)

        # ---------------------------
        # FULL AREA CONTAINER
        # ---------------------------
        container = QWidget()

        root = QVBoxLayout(container)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)
        root.setAlignment(Qt.AlignmentFlag.AlignTop)

        # ---------------------------
        # TOP BAR
        # ---------------------------
        top_bar = TopBar(self)
        root.addWidget(top_bar)

        # ---------------------------
        # CONTENT SCROLL AREA
        # ---------------------------
        self.scroll_area = QScrollArea(container)
        self.scroll_area.setWidgetResizable(True)

        # ❌ remove duplicate line (you had setHorizontalScrollBarPolicy twice)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.scroll_area.setFrameShape(QScrollArea.Shape.NoFrame)

        # dynamic height based on first card
        self.scroll_area.setFixedHeight(cards[0].sizeHint().height() + 120)

        content_area = QWidget()
        content_area.setStyleSheet(tw("bg-surface-1"))

        content_layout = QHBoxLayout(content_area)
        content_layout.setContentsMargins(30, 0, 30, 0)
        content_layout.setSpacing(30)

        content_layout.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )

        for card in cards:
            content_layout.addWidget(card)

        self.scroll_area.setWidget(content_area)

        # enable wheel → horizontal scroll
        self.scroll_area.viewport().installEventFilter(self)

        root.addWidget(self.scroll_area)

        # ---------------------------
        # ATTACH CONTAINER TO WINDOW
        # ---------------------------
        window_layout.addWidget(container)

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if obj == self.scroll_area.viewport() and event.type() == QEvent.Type.Wheel:
            if isinstance(event, QWheelEvent):
                delta: int = event.angleDelta().y()

                bar = self.scroll_area.horizontalScrollBar()
                bar.setValue(bar.value() - delta)

                return True  # block default vertical scroll

        return super().eventFilter(obj, event)