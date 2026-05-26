from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)


class Header(QWidget):
    def __init__(
        self,
        title: str,
        subtitle: str,
    ):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setSpacing(4)

        title_label = QLabel(title)
        title_label.setObjectName("titleLabel")

        subtitle_label = QLabel(subtitle)
        subtitle_label.setObjectName("subtitleLabel")

        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)