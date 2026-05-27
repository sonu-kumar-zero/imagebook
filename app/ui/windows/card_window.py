from typing import Final

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QFrame,
    QGraphicsDropShadowEffect,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from app.ui.styles.helpers import set_variant
from app.ui.styles.stylesheet import APP_STYLE
from app.ui.widgets.top_bar_home_screen import TopBar
from app.ui.assets.images import Images


class ImageCard(QFrame):
    CARD_WIDTH: Final[int] = 320
    CARD_HEIGHT: Final[int] = 420
    IMAGE_HEIGHT: Final[int] = 250

    def __init__(
        self,
        image_path: str,
        title: str,
        subtitle: str,
    ) -> None:
        super().__init__()

        self.image_path: str = image_path
        self.title_text: str = title
        self.subtitle_text: str = subtitle

        set_variant(self, "card")

        self.setFixedSize(
            self.CARD_WIDTH,
            self.CARD_HEIGHT,
        )

        self.setup_ui()
        self.setup_shadow()

    def setup_ui(self) -> None:
        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            20,
            20,
            20,
            20,
        )

        layout.setSpacing(16)

        image_label = self._build_image()

        title_label = QLabel(
            self.title_text,
        )
        set_variant(
            title_label,
            "title",
        )

        subtitle_label = QLabel(
            self.subtitle_text,
        )
        set_variant(
            subtitle_label,
            "subtitle",
        )

        text_layout = QVBoxLayout()
        text_layout.setSpacing(6)

        text_layout.addWidget(
            title_label,
        )

        text_layout.addWidget(
            subtitle_label,
        )

        layout.addWidget(
            image_label,
        )

        layout.addLayout(
            text_layout,
        )

        layout.addStretch()

    def _build_image(self) -> QLabel:
        image_label = QLabel()

        set_variant(
            image_label,
            "image",
        )

        image_label.setFixedHeight(
            self.IMAGE_HEIGHT,
        )

        image_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )

        pixmap = QPixmap(
            self.image_path,
        )

        if not pixmap.isNull():
            image_label.setPixmap(
                pixmap.scaled(
                    500,
                    300,
                    Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )

        return image_label

    def setup_shadow(self) -> None:
        shadow = QGraphicsDropShadowEffect(
            self,
        )

        shadow.setBlurRadius(50)
        shadow.setOffset(0, 12)

        shadow.setColor(
            Qt.GlobalColor.black,
        )

        self.setGraphicsEffect(
            shadow,
        )

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

        self.setProperty("variant", "window")

        self.setStyleSheet(APP_STYLE)

        self.setup_ui()

    def setup_ui(self) -> None:
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
        container.setProperty("variant", "test1")

        root = QVBoxLayout(container)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)
        root.setAlignment(Qt.AlignmentFlag.AlignTop)

        # ---------------------------
        # TOP BAR
        # ---------------------------
        top_bar = TopBar(container)
        root.addWidget(top_bar)

        # ---------------------------
        # CONTENT AREA
        # ---------------------------
        content_layout = QHBoxLayout()
        content_layout.setContentsMargins(0,0,0,0)
        content_layout.setSpacing(30)

        image_paths: list[str] = [
            str(Images.IMAGE1.path),
            str(Images.IMAGE2.path),
            str(Images.IMAGE3.path),
            str(Images.IMAGE4.path)
        ]

        cards: list[ImageCard] = [
            ImageCard(image_paths[0], "Mountain Lake", "Peaceful reflection in nature"),
            ImageCard(image_paths[1], "Cyber City", "Premium futuristic design"),
            ImageCard(image_paths[2], "Forest View", "Deep calm and nature vibes"),
        ]

        content_layout.addStretch()

        for card in cards:
            content_layout.addWidget(card)

        content_layout.addStretch()

        root.addLayout(content_layout)

        # ---------------------------
        # ATTACH CONTAINER TO WINDOW
        # ---------------------------
        window_layout.addWidget(container)