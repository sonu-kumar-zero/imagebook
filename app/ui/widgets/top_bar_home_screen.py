from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QWidget,
)

from app.ui.assets.icons import Icons
from app.ui.widgets.window_control_button import WindowControlButton


class TopBar(QFrame):
    HEIGHT = 70  # realistic UI height

    def __init__(
        self,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

        self.parent_window = parent
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
        menu_button = WindowControlButton(Icons.MENU.path)

        title_label = QLabel("ImageBook")
        title_label.setProperty("variant", "title")

        # Spacer
        spacer = QWidget()
        spacer.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred,
        )

        # Right controls
        minimize_button = WindowControlButton(Icons.MINIMIZE.path)
        maximize_button = WindowControlButton(Icons.MAXIMIZE.path)
        close_button = WindowControlButton(Icons.CROSS.path)

        # Safe parent checks
        if self.parent_window:
            minimize_button.clicked.connect(self.parent_window.showMinimized)
            close_button.clicked.connect(self.parent_window.close)

        maximize_button.clicked.connect(self.toggle_maximize)

        layout.addWidget(menu_button)
        layout.addWidget(title_label)
        layout.addWidget(spacer)

        layout.addWidget(minimize_button)
        layout.addWidget(maximize_button)
        layout.addWidget(close_button)

    def toggle_maximize(self) -> None:
        if not self.parent_window:
            return

        if self.parent_window.isMaximized():
            self.parent_window.showNormal()
        else:
            self.parent_window.showMaximized()

    # -------------------------
    # DRAG LOGIC (FIXED)
    # -------------------------
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if not self.parent_window:
            return

        if event.buttons() & Qt.MouseButton.LeftButton:
            delta = event.globalPosition().toPoint() - self.drag_position

            self.parent_window.move(
                self.parent_window.pos() + delta
            )

            self.drag_position = event.globalPosition().toPoint()