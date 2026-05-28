from typing import Final

from PySide6.QtCore import (
    Qt,
    QEvent,
    QObject
)
from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)
from PySide6.QtGui import QWheelEvent


from app.ui.styles.helpers import set_variant
from app.ui.styles.stylesheet import APP_STYLE
from app.ui.widgets.top_bar_home_screen import TopBar
from app.ui.assets.images import Images
from app.ui.widgets.image_card_card_screen import ImageCard
from app.ui.widgets.card_window.horizontal_card_scroll_area import HorizontalCardScrollArea
from app.ui.widgets.kscroll_area import KScrollArea

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
        ]

        cards1: list[ImageCard] = [
            ImageCard(image_paths[0], "Mountain Lake", "Peaceful reflection in nature"),
            ImageCard(image_paths[1], "Cyber City", "Premium futuristic design"),
            ImageCard(image_paths[2], "Forest View", "Deep calm and nature vibes"),
            ImageCard(image_paths[0], "Mountain Lake", "Peaceful reflection in nature"),
            ImageCard(image_paths[1], "Cyber City", "Premium futuristic design"),
            ImageCard(image_paths[2], "Forest View", "Deep calm and nature vibes"),
        ]

        cards2: list[ImageCard] = [
            ImageCard(image_paths[0], "Mountain Lake", "Peaceful reflection in nature"),
            ImageCard(image_paths[1], "Cyber City", "Premium futuristic design"),
            ImageCard(image_paths[2], "Forest View", "Deep calm and nature vibes"),
            ImageCard(image_paths[0], "Mountain Lake", "Peaceful reflection in nature"),
            ImageCard(image_paths[1], "Cyber City", "Premium futuristic design"),
        ]

        # ---------------------------
        # ROOT WINDOW LAYOUT
        # ---------------------------
        window_layout = QVBoxLayout(self)
        window_layout.setContentsMargins(0, 0, 0, 0)
        window_layout.setSpacing(0)

        # ---------------------------
        # PAGE SCROLL AREA
        # ---------------------------
        page_scroll = KScrollArea(
            direction="vertical",
            spacing=30,
            margins=(60, 0, 60, 0),
            alignment=Qt.AlignmentFlag.AlignTop,
            parent=self,
            vertical_scrollbar_policy=(
                Qt.ScrollBarPolicy.ScrollBarAlwaysOn
            )
        )

        # ---------------------------
        # TOP BAR
        # ---------------------------
        top_bar = TopBar(self)
        window_layout.addWidget(top_bar)

        # ---------------------------
        # HORIZONTAL CARD SECTIONS
        # ---------------------------
        scroll_area = HorizontalCardScrollArea(
            cards=cards,
            index=0,
        )

        scroll_area1 = HorizontalCardScrollArea(
            cards=cards1,
            index=1,
        )

        scroll_area2 = HorizontalCardScrollArea(
            cards=cards2,
            index=2,
        )

        page_scroll.addWidget(scroll_area)
        page_scroll.addWidget(scroll_area1)
        page_scroll.addWidget(scroll_area2)

        # ---------------------------
        # ATTACH TO WINDOW
        # ---------------------------
        window_layout.addWidget(page_scroll)

        # optional instance refs
        self.page_scroll = page_scroll
        self.scroll_area = scroll_area
        self.scroll_area1 = scroll_area1
        self.scroll_area2 = scroll_area2

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if obj == self.scroll_area.viewport() and event.type() == QEvent.Type.Wheel:
            if isinstance(event, QWheelEvent):
                delta: int = event.angleDelta().y()

                bar = self.scroll_area.horizontalScrollBar()
                bar.setValue(bar.value() - delta)

                return True  # block default vertical scroll

        return super().eventFilter(obj, event)