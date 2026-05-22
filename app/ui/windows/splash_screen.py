from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QApplication,
)

from app.utils.paths import ASSETS_DIR


class SplashScreen(QWidget):
    WIDTH = 900
    HEIGHT = 550

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PicBook")

        self.setFixedSize(
            self.WIDTH,
            self.HEIGHT,
        )

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.setup_ui()

    def showEvent(self, event):
        super().showEvent(event)

        # Run after actual show
        QTimer.singleShot(
            0,
            self.center_window,
        )

    def center_window(self):
        screen = self.screen()

        if screen is None:
            screen = QApplication.primaryScreen()

        screen_geometry = screen.availableGeometry()

        frame_geometry = self.frameGeometry()

        frame_geometry.moveCenter(
            screen_geometry.center()
        )

        self.move(frame_geometry.topLeft())

    def setup_ui(self):
        self.background = QLabel(self)

        self.background.setGeometry(
            0,
            0,
            self.WIDTH,
            self.HEIGHT,
        )

        pixmap = QPixmap(
            str(
                ASSETS_DIR / "splash_screen_picbook.png"
            )
        )

        if pixmap.isNull():
            print("Failed to load splash image")
            return

        self.background.setPixmap(
            pixmap.scaled(
                self.WIDTH,
                self.HEIGHT,
                Qt.AspectRatioMode.IgnoreAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )

        self.loading_label = QLabel(
            "Loading your creativity...",
            self,
        )

        self.loading_label.setStyleSheet("""
            color: #ff0000;
            font-size: 16px;
            font-family: Segoe UI;
            background: transparent;
        """)

        self.loading_label.adjustSize()

        self.loading_label.move(
            (
                self.WIDTH
                - self.loading_label.width()
            ) // 2,
            500,
        )