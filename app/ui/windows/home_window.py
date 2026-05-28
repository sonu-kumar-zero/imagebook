from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
)

from app.ui.widgets.header_home_screen import Header
from app.ui.widgets.action_card_home_screen import ActionCard
from app.ui.widgets.section_frame_home_screen import SectionFrame
from app.utils.constants import CONFIG
from app.ui.styles.helpers import set_variant
from app.ui.widgets.klayout_box import LayoutWrapper
from app.ui.widgets.top_bar_home_screen import TopBar
from app.ui.styles.stylesheet import APP_STYLE
from app.ui.styles.utilities import tw

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(CONFIG.WINDOW.TITLE_CAMELCASE)
        self.resize(CONFIG.WINDOW.WIDTH, CONFIG.WINDOW.HEIGHT)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint 
            | Qt.WindowType.Window
        )
        set_variant(self, "window")
        self.setStyleSheet(APP_STYLE)
        self._setup_ui()


    def _setup_ui(self)->None:

        root = LayoutWrapper(
            direction="vertical",
        )

        top_bar = TopBar(self)
        root.addWidget(top_bar)

        container2 = LayoutWrapper(direction="vertical", margins=(30,0,30,30), spacing=20)
        root.addWidget(container2)

        header = Header(
            title="ImageBook",
            subtitle="Create beautiful image books",
        )
        header.setStyleSheet(tw("title"))
        container2.addWidget(header)
    
        actions_layout = LayoutWrapper(
            direction="horizontal",
            spacing=20
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

        container2.addWidget(actions_layout)

        recent = SectionFrame("Recent Projects")
        recent.add_widget(QLabel("No recent projects"))

        container2.addWidget(recent)

        container2.addStretch()

        footer = QLabel("ImageBook v1.0")
        footer.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )

        container2.addWidget(footer)

        self.setCentralWidget(root)