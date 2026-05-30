from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget,
    QPushButton, QLabel, QSizePolicy, QApplication
)
from PySide6.QtCore import (
    Qt, QPropertyAnimation, QEasingCurve, QPoint, 
    QParallelAnimationGroup, QTimer, QEvent, QSize
)
from PySide6.QtGui import (
    QPixmap, QPainter, QColor, QFont, QPaintEvent,
    QResizeEvent, QEnterEvent, QIcon
)
import sys
from app.utils.constants import CONFIG
from app.ui.widgets.load_svg_pixmap import load_svg_pixmap
from app.ui.assets.icons import Icons


CAROUSEL_HEIGHT = CONFIG.CAROUSEL.HEIGHT
ANIMATION_DURATION = CONFIG.CAROUSEL.ANIMATION_DURATION
AUTO_SCROLL_INTERVAL = CONFIG.CAROUSEL.AUTO_SCROLL_INTERVAL


class ImageSlide(QLabel):
    """A single slide that displays an image with aspect-ratio-contain scaling."""

    def __init__(self, pixmap: QPixmap | None = None, placeholder_text: str = "No Image", parent: QWidget | None = None):
        super().__init__(parent)
        self._pixmap = pixmap
        self._placeholder_text = placeholder_text
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMinimumHeight(CAROUSEL_HEIGHT)
        self.setStyleSheet("background-color: #1a1a1a;")

    def setSlidePixmap(self, pixmap: QPixmap):
        self._pixmap = pixmap
        self.update()

    def paintEvent(self, event: QPaintEvent):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        rect = self.rect()

        if self._pixmap and not self._pixmap.isNull():
            # Scale to fill container, cropping overflow (cover behavior)
            scaled = self._pixmap.scaled(
                rect.size(),
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            )
            # Center-crop: offset so excess is cropped equally on both sides
            x = (rect.width() - scaled.width()) // 2
            y = (rect.height() - scaled.height()) // 2
            painter.setClipRect(rect)
            painter.drawPixmap(x, y, scaled)
        else:
            painter.fillRect(rect, QColor("#1a1a1a"))
            painter.setPen(QColor("#555555"))
            font = QFont("Arial", 14)
            painter.setFont(font)
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, self._placeholder_text)

        painter.end()

class NavButton(QPushButton):
    """Styled left/right navigation arrow button."""

    def __init__(self, direction: str, parent: QWidget | None = None):
        """
        Args:
            direction: "left" or "right"
        """
        super().__init__(parent)

        icon_path = Icons.LEFT.path if direction == "left" else Icons.RIGHT.path
        pixmap = load_svg_pixmap(icon_path, color="white", size=24)
        self.setIcon(QIcon(pixmap))
        self.setIconSize(QSize(24, 24))

        self.setFixedSize(44, 44)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.15);
                border: 1.5px solid rgba(255, 255, 255, 0.3);
                border-radius: 22px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.30);
                border-color: rgba(255, 255, 255, 0.6);
            }
            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0.45);
            }
            QPushButton:disabled {
                background-color: rgba(255, 255, 255, 0.05);
                border-color: rgba(255, 255, 255, 0.1);
            }
        """)

        # Disabled state needs a dimmed icon — QIcon modes handle this,
        # but since load_svg_pixmap bakes in the color, set it manually
        disabled_pixmap = load_svg_pixmap(icon_path, color="rgba(255,255,255,0.2)", size=24)
        icon = QIcon()
        icon.addPixmap(pixmap, QIcon.Mode.Normal)
        icon.addPixmap(disabled_pixmap, QIcon.Mode.Disabled)
        self.setIcon(icon)


class DotIndicator(QWidget):
    """Dot pagination indicator bar."""

    def __init__(self, count: int, parent: QWidget | None = None):
        super().__init__(parent)
        self._count = count
        self._current = 0
        self.setFixedHeight(20)
        # safer placement for transparency flag
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)

        # optional but recommended for custom-painted widgets
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

    def setCurrent(self, index: int):
        self._current = index
        self.update()

    def setCount(self, count: int):
        self._count = count
        self._current = min(self._current, count - 1)
        self.update()

    def paintEvent(self, event: QPaintEvent):
        if self._count <= 1:
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        dot_size = 7
        gap = 10
        total_w = self._count * dot_size + (self._count - 1) * gap
        start_x = (self.width() - total_w) // 2
        y = self.height() // 2

        for i in range(self._count):
            x = start_x + i * (dot_size + gap) + dot_size // 2
            if i == self._current:
                painter.setBrush(QColor("#ffffff"))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawEllipse(QPoint(x, y), dot_size // 2, dot_size // 2)
            else:
                painter.setBrush(QColor("#555555"))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawEllipse(QPoint(x, y), dot_size // 2 - 1, dot_size // 2 - 1)

        painter.end()


class ImageCarousel(QWidget):
    """
    Horizontal image carousel with slide animation.

    Usage:
        carousel = ImageCarousel()
        carousel.addImage(QPixmap("photo1.jpg"))
        carousel.addImage(QPixmap("photo2.jpg"))
        carousel.addPixmapFromPath("photo3.png")

        # Add to your vertical layout:
        your_vertical_layout.addWidget(carousel)
    """

    def __init__(self, parent: QWidget | None =None):
        super().__init__(parent)
        self._slides: list[ImageSlide] = []
        self._current_index = 0
        self._animating = False
        
        # ── Auto-scroll timer ──────────────────────────────────────────
        self._auto_timer = QTimer(self)
        self._auto_timer.setInterval(AUTO_SCROLL_INTERVAL)
        self._auto_timer.timeout.connect(self._auto_advance)

        self.setFixedHeight(CAROUSEL_HEIGHT)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setStyleSheet("background-color: #111111; border-radius: 8px;")

        self._build_ui()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Slide area + nav buttons overlay ──────────────────────────
        slide_area = QWidget(self)
        slide_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        slide_area.setStyleSheet("background: transparent;")

        # Stack for slides
        self._stack = QStackedWidget(slide_area)
        self._stack.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self._stack.setStyleSheet("background: transparent;")

        # Nav buttons (absolute positioned over the stack)
        self._btn_left = NavButton("left", slide_area)
        self._btn_right = NavButton("right", slide_area)
        self._btn_left.clicked.connect(self._go_prev)
        self._btn_right.clicked.connect(self._go_next)

        # Layout slide area: stack fills, buttons float
        slide_layout = QHBoxLayout(slide_area)
        slide_layout.setContentsMargins(0, 0, 0, 0)
        slide_layout.addWidget(self._stack)

        root.addWidget(slide_area, 1)

        # ── Dot indicator ───────────────────────────────────────────────
        self._dots = DotIndicator(0, self)
        root.addWidget(self._dots)

        # Position nav buttons after layout is set
        self._slide_area = slide_area
        self._reposition_buttons()
        self._update_controls()

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        self._reposition_buttons()

    def _reposition_buttons(self):
        margin = 12
        btn_y = (CAROUSEL_HEIGHT - 44) // 2 - 10  # vertically center in slide area
        self._btn_left.move(margin, btn_y)
        self._btn_right.move(self.width() - 44 - margin, btn_y)
        self._btn_left.raise_()
        self._btn_right.raise_()

    # ── Public API ────────────────────────────────────────────────────

    def addImage(self, pixmap: QPixmap, placeholder: str = "Image"):
        """Add a QPixmap as a new slide."""
        slide = ImageSlide(pixmap, placeholder)
        self._slides.append(slide)
        self._stack.addWidget(slide)
        self._dots.setCount(len(self._slides))
        self._update_controls()

    def addPixmapFromPath(self, path: str):
        """Load an image from a file path and add it as a slide."""
        pixmap = QPixmap(path)
        if pixmap.isNull():
            self.addImage(QPixmap(), f"Failed: {path}")
            pass
        else:
            self.addImage(pixmap)

    def addPlaceholder(self, text: str = "Slide"):
        """Add an empty placeholder slide (useful for testing)."""
        self.addImage(QPixmap(), text)

    def currentIndex(self) -> int:
        return self._current_index

    def count(self) -> int:
        return len(self._slides)

    # ── Navigation ────────────────────────────────────────────────────

    def _go_prev(self):
        if self._current_index > 0 and not self._animating:
            self._animate_to(self._current_index - 1, direction="right")

    def _go_next(self):
        if self._current_index < len(self._slides) - 1 and not self._animating:
            self._animate_to(self._current_index + 1, direction="left")

    def goToIndex(self, index: int):
        if 0 <= index < len(self._slides) and index != self._current_index and not self._animating:
            direction = "left" if index > self._current_index else "right"
            self._animate_to(index, direction)

    def _animate_to(self, next_index: int, direction: str):
        if not self._slides:
            return

        self._animating = True
        w = self._stack.width()

        current_slide = self._slides[self._current_index]
        next_slide = self._slides[next_index]

        # Place next slide just off-screen
        offset = w if direction == "left" else -w
        next_slide.setParent(self._stack)
        next_slide.setGeometry(offset, 0, w, self._stack.height())
        next_slide.show()
        next_slide.raise_()

        # Animate current slide out
        anim_out = QPropertyAnimation(current_slide, b"pos")
        anim_out.setDuration(ANIMATION_DURATION)
        anim_out.setStartValue(QPoint(0, 0))
        anim_out.setEndValue(QPoint(-offset, 0))
        anim_out.setEasingCurve(QEasingCurve.Type.OutCubic)

        # Animate next slide in
        anim_in = QPropertyAnimation(next_slide, b"pos")
        anim_in.setDuration(ANIMATION_DURATION)
        anim_in.setStartValue(QPoint(offset, 0))
        anim_in.setEndValue(QPoint(0, 0))
        anim_in.setEasingCurve(QEasingCurve.Type.OutCubic)

        group = QParallelAnimationGroup(self)
        group.addAnimation(anim_out)
        group.addAnimation(anim_in)

        def on_finished():
            # Commit the stack state
            self._stack.setCurrentWidget(next_slide)
            current_slide.setGeometry(0, 0, w, self._stack.height())
            self._current_index = next_index
            self._animating = False
            self._update_controls()
            self._dots.setCurrent(self._current_index)

        group.finished.connect(on_finished)
        group.start()

    def _update_controls(self):
        count = len(self._slides)
        self._btn_left.setEnabled(self._current_index > 0)
        self._btn_right.setEnabled(self._current_index < count - 1)
        self._btn_left.setVisible(count > 1)
        self._btn_right.setVisible(count > 1)
        self._dots.setVisible(count > 1)


    # ── Mouse hover: pause / resume ───────────────────────────────────

    def enterEvent(self, event: QEnterEvent):
        super().enterEvent(event)
        self._auto_timer.stop()

    def leaveEvent(self, event: QEvent):
        super().leaveEvent(event)
        self._start_auto_scroll()

    # ── Auto-scroll helpers ───────────────────────────────────────────

    def _start_auto_scroll(self):
        """Start the timer only when there are multiple slides."""
        if len(self._slides) > 1:
            self._auto_timer.start()

    def _auto_advance(self):
        if self._animating:
            return
        next_index = (self._current_index + 1) % len(self._slides)
        self._animate_to(next_index, direction="left")


# ── Demo ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Main window with a vertical layout (mirrors your real app)
    window = QWidget()
    window.setWindowTitle("Image Carousel Demo")
    window.resize(800, 600)
    window.setStyleSheet("background-color: #1e1e2e;")

    vbox = QVBoxLayout(window)
    vbox.setContentsMargins(20, 20, 20, 20)
    vbox.setSpacing(16)

    # ── Add the carousel to your vertical layout ──
    carousel = ImageCarousel()
    vbox.addWidget(carousel)

    # Add placeholder slides (replace with real QPixmap paths in your app)
    colors = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6"]
    labels = ["Slide 1", "Slide 2", "Slide 3", "Slide 4", "Slide 5"]

    for color, label in zip(colors, labels):
        # Create a solid-color pixmap as a stand-in for real images
        px = QPixmap(400, 250)
        px.fill(QColor(color))
        painter = QPainter(px)
        painter.setPen(QColor("white"))
        font = QFont("Arial", 20, QFont.Weight.Bold)
        painter.setFont(font)
        painter.drawText(px.rect(), Qt.AlignmentFlag.AlignCenter, label)
        painter.end()
        carousel.addImage(px, label)

    # Rest of your vertical layout content
    info = QLabel("↑  Carousel sits inside a QVBoxLayout and takes full width at 300 px height")
    info.setStyleSheet("color: #888; font-size: 12px;")
    info.setAlignment(Qt.AlignmentFlag.AlignCenter)
    vbox.addWidget(info)

    vbox.addStretch()

    window.show()
    sys.exit(app.exec())