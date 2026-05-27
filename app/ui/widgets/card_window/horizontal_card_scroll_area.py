from PySide6.QtCore import Qt, QEvent, QObject
from PySide6.QtWidgets import QScrollArea, QWidget, QHBoxLayout
from PySide6.QtGui import QWheelEvent
from app.ui.widgets.image_card_card_screen import ImageCard


class HorizontalCardScrollArea(QScrollArea):
    def __init__(self, cards: list[ImageCard], parent: QWidget | None = None, index: int = 0):
        super().__init__(parent)

        self.cards = cards

        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFrameShape(QScrollArea.Shape.NoFrame)

        self._build_ui()
        self.viewport().installEventFilter(self)

    def _build_ui(self) -> None:
        content = QWidget(self)

        layout = QHBoxLayout(content)
        layout.setContentsMargins(30, 0, 30, 0)
        layout.setSpacing(30)
        layout.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )

        for card in self.cards:
            layout.addWidget(card)

        content.setLayout(layout)
        self.setWidget(content)

        # dynamic height based on first card
        if self.cards:
            self.setFixedHeight(self.cards[0].sizeHint().height() + 120)

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if obj == self.viewport() and event.type() == QEvent.Type.Wheel:
            if isinstance(event, QWheelEvent):
                delta = event.angleDelta().y()
                self.horizontalScrollBar().setValue(
                    self.horizontalScrollBar().value() - delta
                )
                return True

        return super().eventFilter(obj, event)