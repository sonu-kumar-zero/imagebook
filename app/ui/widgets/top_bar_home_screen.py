from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import (
    QMouseEvent,
    QGuiApplication
    )
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QWidget,
)

from app.ui.assets.icons import Icons
from app.ui.widgets.window_control_button import WindowControlButton
from app.ui.styles.helpers import set_variant
from app.ui.styles.utilities import tw
from app.ui.widgets.colored_icons import colored_icon
from app.utils.constants import CONFIG


class TopBar(QFrame):
    HEIGHT = 70  # realistic UI height

    def __init__(
        self,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

        self.parent_window = parent
        self.max_window_size: bool = False
        self.drag_position = QPoint()
        self.setContentsMargins(0, 0, 0, 0)
        self.setFrameShape(QFrame.Shape.NoFrame)

        self.setProperty("variant", "top-bar")

        # ✅ IMPORTANT: let layout control width, fixed height control
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )

        self.setFixedHeight(self.HEIGHT)

        self.setup_ui()

    def setup_ui(self) -> None:
        layout = QHBoxLayout(self)

        layout.setContentsMargins(20, 0, 20, 0)
        layout.setSpacing(12)

        # Left side
        # menu_button = WindowControlButton(Icons.MENU.path)

        title_label = QLabel(CONFIG.WINDOW.TITLE_CAMELCASE)
        set_variant(title_label, "title")
        title_label.setStyleSheet(tw("text-accent"))

        # Spacer
        spacer = QWidget()
        spacer.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred,
        )

        # Right controls
        minimize_button = WindowControlButton(Icons.MINIMIZE.path)
        self.maximize_button = WindowControlButton(Icons.MAXIMIZE.path)
        close_button = WindowControlButton(Icons.CROSS.path)

        # Safe parent checks
        if self.parent_window:
            minimize_button.clicked.connect(self.parent_window.showMinimized)
            close_button.clicked.connect(self.parent_window.close)

        self.maximize_button.clicked.connect(self.toggle_maximize)

        # layout.addWidget(menu_button)
        layout.addWidget(title_label)
        layout.addWidget(spacer)

        layout.addWidget(minimize_button)
        layout.addWidget(self.maximize_button)
        layout.addWidget(close_button)

    def toggle_maximize(self) -> None:
        if not self.parent_window:
            return

        if self.parent_window.isMaximized():
            self.max_window_size = False
            self.parent_window.showNormal()
            self.maximize_button.setIcon(colored_icon(Icons.MAXIMIZE.path))
        else:
            self.max_window_size = True
            self.parent_window.showMaximized()
            self.maximize_button.setIcon(colored_icon(Icons.MAXIMIZE_MID.path))

    # -------------------------
    # DRAG LOGIC (FIXED)
    # -------------------------
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint()
            self.window_position = self.window().pos()

            self.is_dragging = True

    def mouseMoveEvent(self, event: QMouseEvent):
        if not self.is_dragging:
            return

        if event.buttons() & Qt.MouseButton.LeftButton:
            self.maximize_button.setIcon(colored_icon(Icons.MAXIMIZE.path))
            platform = QGuiApplication.platformName()

            # Wayland → use native drag
            if platform == "wayland":
                self.window().windowHandle().startSystemMove()
                self.is_dragging = False
                return

            # X11 / Windows / macOS → manual move
            current = event.globalPosition().toPoint()
            delta = current - self.drag_position

            self.window().move(self.window_position + delta)