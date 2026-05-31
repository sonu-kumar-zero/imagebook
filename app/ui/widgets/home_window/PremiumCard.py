from PySide6.QtWidgets import (
    QWidget, QFrame, QVBoxLayout,
    QHBoxLayout, QLabel
)
from PySide6.QtCore import (
    Qt, Signal, QEasingCurve,
    QSize, QRect, QEvent
)
from PySide6.QtGui import (
    QPixmap, QPainter, QPainterPath, QColor,
    QMouseEvent, QEnterEvent,  QPaintEvent
)
from app.ui.styles.utilities import tw
from app.ui.widgets.text_wrapper import TextWrapper
from app.ui.styles.theme import theme
from app.ui.widgets.load_svg_pixmap import load_svg_pixmap
from app.ui.assets.icons import Icons

class _LikeButton(QFrame):
    toggled = Signal(bool)

    def __init__(
        self, 
        parent: QWidget | None = None, 
        icon_size: int = 30 
            ) -> None:
        super().__init__(
            parent=parent
        )
        self.setFrameShape(QFrame.Shape.NoFrame)
        self._icon_size_prm = icon_size
        self.setFixedSize(self._icon_size_prm, self._icon_size_prm)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self._liked = False
        self._hovered = False
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._icon_label = QLabel(self)
        self._icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._icon_label.setGeometry(0, 0, self._icon_size_prm, self._icon_size_prm)
        self._icon_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        self.setObjectName("LikeButton")

        self.setStyleSheet(f"""
        QFrame#LikeButton {{
            background: rgba(255, 255, 255, 0.25);
            border-radius: {self._icon_size_prm // 2}px;
        }}
        """)
        self._icon_label.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground,
            True
        )
        
        self._update_icon()

    def is_liked(self) -> bool:
        return self._liked

    def set_liked(self, value: bool) -> None:
        self._liked = value
        self._update_icon()

    def _update_icon(self) -> None:
        if self._liked:
            color = "#ff0000"
        elif self._hovered:
            color = theme.APP_BG
        else:
            color = "#000000"

        pixmap = load_svg_pixmap(
            path=Icons.HEART.path,
            color=color,
            size=self._icon_size_prm - 6,
            mode=self._liked and "fill" or "stroke"
        )
        self._icon_label.setPixmap(pixmap)

    def enterEvent(self, event: QEnterEvent) -> None:
        self._hovered = True
        self._update_icon()
        super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        self._hovered = False
        self._update_icon()
        super().leaveEvent(event)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self._liked = not self._liked
            self._update_icon()
            self.toggled.emit(self._liked)
        super().mousePressEvent(event)
        
class _ImageArea(QFrame):
    """
    100×100 image container with:
      - clipped rounded corners
      - hover scale animation on the pixmap
      - like button (top-right)
      - a public bottom-left slot (QHBoxLayout) for badges / tags
    """

    def __init__(
        self,
        parent: QWidget | None = None,
        image_width: int = 220,
        image_height: int = 200,
        ) -> None:
        super().__init__(parent)
        self.setObjectName("image-area")
        self.setFixedSize(QSize(image_width, image_height))   # card width, image height

        self._pixmap: QPixmap | None = None
        self._scale: float = 1.0

        # ── scale animation ───────────────────────────────────────────────
        # We animate a plain float property via a QVariantAnimation workaround
        # by driving it through a lambda.
        from PySide6.QtCore import QVariantAnimation
        self._anim = QVariantAnimation(self)
        self._anim.setDuration(220)
        self._anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._anim.valueChanged.connect(self._on_scale_changed)

        # ── like button ───────────────────────────────────────────────────
        self.like_btn = _LikeButton(self)        
        self.like_btn.move(
            self.width() - self.like_btn.width() - 8, 8
        )
        self.like_btn.raise_()

        # ── bottom-left slot ──────────────────────────────────────────────
        self._slot_widget = QWidget(self)
        self._slot_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self._slot_layout = QHBoxLayout(self._slot_widget)
        self._slot_layout.setContentsMargins(8, 0, 8, 8)
        self._slot_layout.setSpacing(4)
        self._slot_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        self._slot_widget.setGeometry(
            0,
            self.height() - 40,
            self.width(),
            40,
        )
        self._slot_widget.raise_()

    # ── public API ────────────────────────────────────────────────────────

    def set_image(self, pixmap: QPixmap) -> None:
        self._pixmap = pixmap
        self.update()

    @property
    def slot_layout(self) -> QHBoxLayout:
        """Insert any QWidget here; it appears bottom-left over the image."""
        return self._slot_layout

    # ── animation callbacks ───────────────────────────────────────────────

    def _on_scale_changed(self, value: float) -> None:
        self._scale = value
        self.update()

    def _animate_to(self, target: float) -> None:
        self._anim.stop()
        self._anim.setStartValue(self._scale)
        self._anim.setEndValue(target)
        self._anim.start()

    def enterEvent(self, event: QEnterEvent) -> None:
        self._animate_to(1.08)
        super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        self._animate_to(1.0)
        super().leaveEvent(event)

    # ── rendering ────────────────────────────────────────────────────────

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

        # clip to rounded rect
        clip_path = QPainterPath()
        clip_path.addRoundedRect(0, 0, self.width(), self.height(), 10, 10)
        painter.setClipPath(clip_path)

        if self._pixmap and not self._pixmap.isNull():
            # scale pixmap around centre
            w, h = self.width(), self.height()
            sw = int(w * self._scale)
            sh = int(h * self._scale)
            scaled = self._pixmap.scaled(
                sw, sh,
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation,
            )
            # centre-crop
            sx = (scaled.width() - w) // 2
            sy = (scaled.height() - h) // 2
            painter.drawPixmap(0, 0, scaled, sx, sy, w, h)
        else:
            # placeholder
            painter.fillRect(0, 0, self.width(), self.height(), QColor("#e5e7eb"))
            painter.setPen(QColor("#9ca3af"))
            painter.drawText(
                QRect(0, 0, self.width(), self.height()),
                Qt.AlignmentFlag.AlignCenter,
                "No Image",
            )

        painter.end()


class PremiumCard(QFrame):
    """
    A premium media card widget.

    Signals
    -------
    clicked       — emitted when the card body is clicked
    like_toggled  — emitted with (bool) when the heart is toggled

    Layout
    ------
    ┌──────────────────────────────┐
    │  image area  (180×140)       │
    │  [♥] ← top-right overlay     │
    │  [slot widgets] ← btm-left   │
    ├──────────────────────────────┤
    │  Header                      │
    │  Subheader                   │
    └──────────────────────────────┘
    """

    clicked = Signal()
    like_toggled = Signal(bool)

    # _NORMAL_STYLE = """
    #     QFrame#premium-card {
    #         border: 1px solid rgba(0,0,0,0.07);
    #         border-radius: 14px;
    #     }
    # """
    # _HOVER_STYLE = """
    #     QFrame#premium-card {
    #         border: 1px solid rgba(0,0,0,0.13);
    #         border-radius: 14px;
    #     }
    # """
    # _PRESS_STYLE = """
    #     QFrame#premium-card {
    #         background: #f9fafb;
    #         border: 1px solid rgba(0,0,0,0.13);
    #         border-radius: 14px;
    #     }
    # """

    def __init__(
        self,
        header: str = "",
        subheader: str = "",
        pixmap: QPixmap | None = None,
        parent: QWidget | None = None,
        card_width: int = 220,
        card_image_height: int = 200,
    ) -> None:
        super().__init__(parent)
        self.setObjectName("premium-card")
        self._card_width = card_width
        self._card_image_height = card_image_height
        self.setFixedWidth(card_width)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(tw("bg-surface-1", "rounded-card"))

        # drop-shadow feel via elevation anim on the border opacity (style swap)
        self._pressed = False

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── image ─────────────────────────────────────────────────────────
        self._image_area = _ImageArea(
            self,
            image_width=self._card_width
            )
        self._image_area.like_btn.toggled.connect(self.like_toggled)
        if pixmap:
            self._image_area.set_image(pixmap)
        root.addWidget(self._image_area)

        # ── text ──────────────────────────────────────────────────────────
        text_area = QWidget(self)
        text_layout = QVBoxLayout(text_area)
        text_layout.setContentsMargins(12, 10, 12, 12)
        text_layout.setSpacing(3)

        self._header_label = TextWrapper(
            text=header,
            word_wrap=True,
            font_size=14,
            font_weight="bold",
            color=theme.ACCENT
            )

        self._subheader_label = TextWrapper(
            text=subheader,
            word_wrap=True,
            font_size=11,
            color=theme.TEXT_SECONDARY
        )

        text_layout.addWidget(self._header_label)
        text_layout.addWidget(self._subheader_label)
        root.addWidget(text_area)

    # ── public API ────────────────────────────────────────────────────────

    def set_header(self, text: str) -> None:
        self._header_label.setText(text)

    def set_subheader(self, text: str) -> None:
        self._subheader_label.setText(text)

    def set_image(self, pixmap: QPixmap) -> None:
        self._image_area.set_image(pixmap)

    @property
    def slot_layout(self) -> QHBoxLayout:
        """QHBoxLayout anchored bottom-left over the image. Add any QWidget."""
        return self._image_area.slot_layout

    def set_liked(self, value: bool) -> None:
        self._image_area.like_btn.set_liked(value)

    def is_liked(self) -> bool:
        return self._image_area.like_btn.is_liked()

    # ── interactions ──────────────────────────────────────────────────────

    def enterEvent(self, event: QEnterEvent) -> None:
        self.setStyleSheet(tw("bg-surface-2", "rounded-card"))
        super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        self.setStyleSheet(tw("bg-surface-1", "rounded-card"))
        super().leaveEvent(event)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self._pressed = True
            self.setStyleSheet(tw("bg-card", "rounded-card"))
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton and self._pressed:
            self._pressed = False
            self.setStyleSheet(tw("bg-surface-1", "rounded-card"))
            if self.rect().contains(event.pos()):
                self.clicked.emit()
        super().mouseReleaseEvent(event)