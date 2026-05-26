from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)

from app.ui.widgets.header_home_screen import Header
from app.ui.widgets.action_card_home_screen import ActionCard
from app.ui.widgets.section_frame_home_screen import SectionFrame
from app.ui.styles.home_style import HOME_STYLE


class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ImageBook")
        self.resize(1080, 720)

        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet(HOME_STYLE)

        root = QVBoxLayout()
        root.setContentsMargins(40, 30, 40, 30)
        root.setSpacing(25)

        header = Header(
            title="ImageBook",
            subtitle="Create beautiful image books",
        )

        root.addWidget(header)

        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(20)

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

        root.addLayout(actions_layout)

        recent = SectionFrame("Recent Projects")
        recent.add_widget(QLabel("No recent projects"))

        root.addWidget(recent)

        root.addStretch()

        footer = QLabel("ImageBook v1.0")
        footer.setAlignment(
            Qt.AlignmentFlag.AlignRight
        )

        root.addWidget(footer)

        self.setLayout(root)