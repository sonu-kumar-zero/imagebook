from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
)

from app.ui.widgets.home_window.HomeContentArea import HomeContentArea
from app.ui.widgets.kframe import (
    FrameWrapper,
)
from app.ui.widgets.klayout_box import (
    LayoutWrapper,
)
from app.ui.widgets.side_bar import SideBar
from app.ui.widgets.top_bar_home_screen import (
    TopBar,
)

from app.utils.constants import CONFIG
from app.ui.styles.helpers import set_variant
from app.ui.styles.stylesheet import APP_STYLE


class HomeWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(CONFIG.WINDOW.TITLE_CAMELCASE)

        self.resize(
            CONFIG.WINDOW.WIDTH,
            CONFIG.WINDOW.HEIGHT,
        )

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.Window
        )

        set_variant(self, "window")

        self.setStyleSheet(APP_STYLE)

        self._setup_ui()

    def _setup_ui(self) -> None:

        # ==================================
        # ROOT FRAME
        # ==================================

        root_layout = LayoutWrapper(
            direction="vertical"
        )

        root = FrameWrapper(
            object_name="root",
            layout=root_layout,
        )

        # ==================================
        # TOP BAR
        # ==================================

        top_bar: QWidget = TopBar(self)

        root_layout.addWidget(top_bar)

        # ==================================
        # BODY FRAME
        # ==================================

        body_layout = LayoutWrapper(
            direction="horizontal",
            margins=(0, 0, 0, 0),
            spacing=20,
        )

        body = FrameWrapper(
            object_name="body",
            layout=body_layout,
        )

        root_layout.addWidget(body, 1)

        # ==================================
        # SIDEBAR
        # ==================================

        side_bar = SideBar()
        body_layout.addWidget(side_bar)

        # ==================================
        # CONTENT FRAME
        # ==================================
        
        content = HomeContentArea()
        body_layout.addWidget(content, 1)


        self.setCentralWidget(root)