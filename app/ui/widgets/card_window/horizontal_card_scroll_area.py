from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from app.ui.widgets.image_card_card_screen import ImageCard
from app.ui.widgets.kscroll_area import KScrollArea


class HorizontalCardScrollArea(KScrollArea):
    def __init__(
        self,
        cards: list[ImageCard],
        parent: QWidget | None = None,
        index: int = 0,
    ) -> None:
        super().__init__(
            direction="horizontal",
            parent=parent,
            spacing=30,
            margins=(30, 0, 30, 0),
            alignment=(
                Qt.AlignmentFlag.AlignLeft
                | Qt.AlignmentFlag.AlignVCenter
            ),
        )

        self.cards: list[ImageCard] = cards
        self.index: int = index

        self._build_cards()
        self._set_dynamic_height()

    def _build_cards(self) -> None:
        for card in self.cards:
            self.addWidget(card)

    def _set_dynamic_height(self) -> None:
        if not self.cards:
            return

        first_card: ImageCard = self.cards[0]

        self.setFixedHeight(
            first_card.sizeHint().height() + 120
        )