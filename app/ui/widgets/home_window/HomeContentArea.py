from PySide6.QtWidgets import QWidget

from app.ui.widgets.kframe import (
    FrameWrapper,
)
from app.ui.widgets.klayout_box import (
    LayoutWrapper,
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap 
from PySide6.QtWidgets import (
    QWidget,
    
)

from app.ui.widgets.kframe import (
    FrameWrapper,
)
from app.ui.widgets.klayout_box import (
    LayoutWrapper,
)

from app.ui.styles.utilities import tw
from app.ui.widgets.text_wrapper import TextWrapper
from app.ui.styles.theme import theme
from app.ui.widgets.kscroll_area import KScrollArea
from app.ui.widgets.home_window.GreetingContainer import GreetingContainer
from app.ui.widgets.horizontal_carousal import ImageCarousel
from app.ui.assets.images import Images


class HomeContentArea(FrameWrapper):

    def __init__(
        self,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(
            parent=parent,
            shape="styled",
            shadow="plain",
            object_name="home-content-area",
            layout=LayoutWrapper(
                direction="vertical",
                margins=(10, 0, 10, 10),
                spacing=20,
            ),
        )
        
        self.setStyleSheet(tw("bg-surface-1"))
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        
        scroll_container = KScrollArea(
            direction = "vertical",
            margins = (0,10,0,0),
            spacing = 20,
        )
        
        greeting_container = GreetingContainer()
        scroll_container.addWidget(greeting_container)

        # carousal
        carousal_container = ImageCarousel()
        scroll_container.addWidget(carousal_container)
        for image in [Images.IMAGE1.path, Images.IMAGE2.path, Images.IMAGE3.path, Images.IMAGE4.path]:
            carousal_container.addImage(QPixmap(str(image)))


        # ==================================
        # FOOTER
        # ==================================

        footer = TextWrapper(
            text="ImageBook v1.0",
            alignment=Qt.AlignmentFlag.AlignRight,
            font_size = 10,
            font_weight = "thin",
            color = theme.TEXT_SECONDARY,
        )
        scroll_container.addWidget(footer)


        self.layout_ref.addWidget(scroll_container)
