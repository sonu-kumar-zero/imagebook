from PySide6.QtWidgets import QWidget

from app.ui.widgets.kframe import (
    FrameWrapper,
)
from app.ui.widgets.klayout_box import (
    LayoutWrapper,
)

from PySide6.QtCore import Qt
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
from app.ui.widgets.kbutton_wrapper import ButtonWrapper
from app.ui.assets.icons import Icons


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
        )
        
        greeting_container = FrameWrapper(
            layout=LayoutWrapper(
                direction="horizontal"
            ),
            max_height=60,
        )
        scroll_container.addWidget(greeting_container)
        
        greeting_section = FrameWrapper(
            layout=LayoutWrapper(
                direction="vertical",
                spacing=0,
            ),
        )
        greeting_container.layout_ref.addWidget(greeting_section)
        
        welcome_text = TextWrapper(
            text="Welcome Back, Sonu Kumar!",
            font_size=12,
            font_weight="bold",
        )
        greeting_section.layout_ref.addWidget(welcome_text)
        message_text = TextWrapper(
            text="Discover and manage your image collection with ease.",
            font_size=10,
            color=theme.TEXT_SECONDARY,
        )
        greeting_section.layout_ref.addWidget(message_text)
        
        greeting_container.layout_ref.addStretch()
        
        upload_section = FrameWrapper(
            layout=LayoutWrapper(
                direction="horizontal",
                spacing=10,
            ),
        )
        greeting_container.layout_ref.addWidget(upload_section)

        upload_button = ButtonWrapper(
            text="New Album",
            icon_path=Icons.ADD.path,
            text_color=theme.TEXT_PRIMARY,
            bg_color=theme.ACCENT,
            frame=FrameWrapper(
                layout=LayoutWrapper(
                    direction="horizontal",
                    spacing=5,
                    alignment=Qt.AlignmentFlag.AlignCenter,
                ),
            ),
            alignment=Qt.AlignmentFlag.AlignCenter,
            callback=lambda: print("New Album button clicked!"),
        )
        
        upload_section.layout_ref.addWidget(upload_button)

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
