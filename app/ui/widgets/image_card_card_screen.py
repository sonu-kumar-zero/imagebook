from PySide6.QtCore import (
    Qt,
    QEvent,
    Property,
    QPropertyAnimation,
    QEasingCurve,
)
from PySide6.QtGui import QPixmap, QEnterEvent
from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QGraphicsDropShadowEffect,
)

from typing import Final
from app.ui.styles.helpers import set_variant
from app.ui.styles.utilities import tw


class ImageCard(QFrame):
    CARD_WIDTH: Final[int] = 320
    CARD_HEIGHT: Final[int] = 420
    IMAGE_HEIGHT: Final[int] = 250

    def __init__(self, image_path: str, title: str, subtitle: str) -> None:
        super().__init__()

        self.image_path = image_path
        self.title_text = title
        self.subtitle_text = subtitle

        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # cache base image
        self.base_pixmap = QPixmap(self.image_path)

        self._image_scale = 1.0

        set_variant(self, "card")
        self.setFixedSize(self.CARD_WIDTH, self.CARD_HEIGHT)

        self.setup_ui()
        self.setup_shadow()
        self.setup_animation()

    # ---------------- UI ----------------
    def setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)

        self.image_label = QLabel()
        set_variant(self.image_label, "image")
        self.image_label.setFixedHeight(self.IMAGE_HEIGHT)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._render_image()

        title_label = QLabel(self.title_text)
        set_variant(title_label, "title")
        # dprint(__file__, tw("text-secondary"))
        title_label.setStyleSheet(tw("text-accent"))

        subtitle_label = QLabel(self.subtitle_text)
        set_variant(subtitle_label, "subtitle")

        text_layout = QVBoxLayout()
        text_layout.setSpacing(6)
        text_layout.addWidget(title_label)
        text_layout.addWidget(subtitle_label)

        layout.addWidget(self.image_label)
        layout.addLayout(text_layout)
        layout.addStretch()

    # ---------------- Image render ----------------
    def _render_image(self) -> None:
        if self.base_pixmap.isNull():
            return

        scaled = self.base_pixmap.scaled(
            int(500 * self._image_scale),
            int(300 * self._image_scale),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.image_label.setPixmap(scaled)

    # ---------------- Shadow ----------------
    def setup_shadow(self) -> None:
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(50)
        shadow.setOffset(0, 12)
        shadow.setColor(Qt.GlobalColor.black)
        self.setGraphicsEffect(shadow)

    # ---------------- Animation ----------------
    def setup_animation(self) -> None:
        self.anim = QPropertyAnimation(self, b"imageScale")
        self.anim.setDuration(240)  # slightly smoother than 220
        self.anim.setEasingCurve(QEasingCurve.Type.OutCubic)

    # ---------------- Property ----------------
    def get_imageScale(self):
        return self._image_scale

    def set_imageScale(self, value: float):
        self._image_scale = value
        self._render_image()

        # IMPORTANT: forces smoother repaint cycle
        self.image_label.update()

    imageScale = Property(float, get_imageScale, set_imageScale)

    # ---------------- Hover ----------------
    def enterEvent(self, event: QEnterEvent) -> None:
        self.anim.stop()
        self.anim.setStartValue(self._image_scale)
        self.anim.setEndValue(1.05)
        self.anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        self.anim.stop()
        self.anim.setStartValue(self._image_scale)
        self.anim.setEndValue(1.0)
        self.anim.start()
        super().leaveEvent(event)