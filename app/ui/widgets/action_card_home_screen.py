from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QSizePolicy,
)


class ActionCard(QFrame):
    def __init__(
        self,
        title: str,
        description: str,
        button_text: str = "Continue",
    ):
        super().__init__()

        self.setObjectName("actionCard")

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(14)

        title_label = QLabel(title)
        title_label.setObjectName("cardTitle")

        desc_label = QLabel(description)
        desc_label.setObjectName("cardDescription")
        desc_label.setWordWrap(True)

        self.button = QPushButton(button_text)
        self.button.setMinimumHeight(42)

        layout.addWidget(title_label)
        layout.addWidget(desc_label)
        layout.addStretch()
        layout.addWidget(self.button)