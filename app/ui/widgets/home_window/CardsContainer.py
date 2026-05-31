from app.ui.widgets.frame_wrapper2 import FrameWrapper2
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import Qt, QPixmap
from app.ui.widgets.base_layout import BaseLayout
from app.ui.widgets.text_wrapper import TextWrapper
from app.ui.widgets.button_wrapper2 import ButtonWrapper2
from app.ui.assets.icons import Icons
from app.ui.styles.theme import theme
from app.ui.widgets.kscroll_area import KScrollArea
from app.ui.widgets.home_window.PremiumCard import PremiumCard
from app.ui.assets.images import Images





class CardsContainer(FrameWrapper2):
    def __init__(
        self,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(
            parent=parent,
            shape="styled",
            shadow="plain",
            object_name="cards-container",
            layout=BaseLayout(
                direction="vertical",
                margins=(0, 0, 0, 0),
                spacing=2,
            ),
        )
        self._setup_ui()
        
    def _setup_ui(self) -> None:
        header_layout = BaseLayout(
            direction="horizontal",
            margins=(0, 0, 0, 0),
            spacing=5,
        )
        header_widget = QWidget()
        header_widget.setLayout(header_layout.qlayout)
        self.layout_ref.addWidget(header_widget)
        
        # create text wrapper for header
        left_text_header = TextWrapper(
            text="My Albums",
            font_size=16,
            font_weight="bold",
        )
        header_layout.addWidget(left_text_header)
        header_layout.addStretch()
        
        # create button wrapper
        upload_button = ButtonWrapper2(
            text="View All",
            icon_path=Icons.RIGHT.path,
            text_color=theme.ACCENT,
            bg_color="transparent",
            callback=lambda: print("View All button clicked!"),
            font_size=12,
            font_weight="medium",
            width=150,
            icon_position="right",
            spacing=5,
            alignment=Qt.AlignmentFlag.AlignRight,
            hover_color=theme.CARD_BG_HOVER,
        )
        header_layout.addWidget(upload_button)
        
        
        # now we need a horizontal scroll area to hold the cards
        cards_holder_scroll_area = KScrollArea(
            direction="horizontal",
            margins=(0, 0, 0, 0),
            spacing=10,
        )
        cards_holder_scroll_area.setFixedHeight(260)  # set a fixed height for the cards area
        self.layout_ref.addWidget(cards_holder_scroll_area)
        
        _cards_list:list[PremiumCard] = [
            PremiumCard(
                header="Travel Diaries",
                subheader="128 imags",
                pixmap=QPixmap(Images.IMAGE1.path),
            ),
            PremiumCard(
                header="Family Moments",
                subheader="256 images",
                pixmap=QPixmap(Images.IMAGE2.path),
            ),
            PremiumCard(
                header="Nature's Beauty",
                subheader="512 images",
                pixmap=QPixmap(Images.IMAGE3.path),
            ),
            PremiumCard(
                header="Cityscapes",
                subheader="64 images",
                pixmap=QPixmap(Images.IMAGE4.path),
            ),
            PremiumCard(
                header="Travel Diaries",
                subheader="128 imags",
                pixmap=QPixmap(Images.IMAGE1.path),
            ),
            PremiumCard(
                header="Family Moments",
                subheader="256 images",
                pixmap=QPixmap(Images.IMAGE2.path),
            ),
            PremiumCard(
                header="Nature's Beauty",
                subheader="512 images",
                pixmap=QPixmap(Images.IMAGE3.path),
            ),
            PremiumCard(
                header="Cityscapes",
                subheader="64 images",
                pixmap=QPixmap(Images.IMAGE4.path),
            ),
        ]

        # now we need cards
        for card in _cards_list:
            cards_holder_scroll_area.addWidget(card)
