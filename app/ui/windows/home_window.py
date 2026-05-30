from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QWidget,
)

from app.ui.widgets.header_home_screen import Header
from app.ui.widgets.action_card_home_screen import (
    ActionCard,
)
from app.ui.widgets.section_frame_home_screen import (
    SectionFrame,
)
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
from app.ui.styles.utilities import tw


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

        content_layout = LayoutWrapper(
            direction="vertical",
            margins=(30, 0, 30, 30),
            spacing=20,
        )

        content = FrameWrapper(
            object_name="content",
            layout=content_layout,
        )

        body_layout.addWidget(content, 1)

        # ==================================
        # HEADER
        # ==================================

        header = Header(
            title="ImageBook",
            subtitle="Create beautiful image books",
        )

        header.setStyleSheet(tw("title"))

        content_layout.addWidget(header)

        # ==================================
        # ACTIONS
        # ==================================

        actions_layout = LayoutWrapper(
            direction="horizontal",
            spacing=20,
        )

        new_card = ActionCard(
            title="Create New Project",
            description="Start from scratch",
        )

        open_card = ActionCard(
            title="Open Existing Project",
            description="Continue your work",
        )

        actions_layout.addWidget(new_card)
        actions_layout.addWidget(open_card)

        content_layout.addWidget(actions_layout)

        # ==================================
        # RECENT
        # ==================================

        recent = SectionFrame("Recent Projects")

        recent.add_widget(
            QLabel("No recent projects")
        )

        content_layout.addWidget(recent)

        content_layout.addStretch()

        # ==================================
        # FOOTER
        # ==================================

        footer = QLabel("ImageBook v1.0")

        footer.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )

        content_layout.addWidget(footer)

        self.setCentralWidget(root)