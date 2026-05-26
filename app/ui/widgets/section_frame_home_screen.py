from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class SectionFrame(QFrame):
    def __init__(self, title: str):
        super().__init__()

        self.setObjectName("sectionFrame")

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(
            20,
            20,
            20,
            20,
        )

        title_label = QLabel(title)
        title_label.setObjectName(
            "sectionTitle"
        )

        self.main_layout.addWidget(
            title_label
        )

    def add_widget(
        self,
        widget: QWidget,
    ) -> None:
        self.main_layout.addWidget(
            widget
        )