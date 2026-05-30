from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from app.ui.widgets.text_wrapper import TextWrapper
from app.ui.styles.theme import theme
from app.ui.assets.icons import Icons
from app.ui.widgets.button_wrapper2 import ButtonWrapper2
from app.ui.widgets.frame_wrapper2 import FrameWrapper2
from app.ui.widgets.base_layout import BaseLayout


class GreetingContainer(FrameWrapper2):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(
            parent=parent,
            layout=BaseLayout(
                direction="horizontal"
            ),
            max_height=60,
        )
        
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        greeting_section = FrameWrapper2(
            layout=BaseLayout(
                direction="vertical",
                spacing=0,
            ),
        )
        self.layout_ref.addWidget(greeting_section)
        
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
        
        self.layout_ref.addStretch()
        
        upload_section = FrameWrapper2(
            layout=BaseLayout(
                direction="horizontal",
                spacing=10,
                alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
            ),
        )
        self.layout_ref.addWidget(upload_section)
        
        upload_button = ButtonWrapper2(
            text="New Album",
            icon_path=Icons.ADD.path,
            text_color=theme.TEXT_PRIMARY,
            bg_color=theme.ACCENT,
            callback=lambda: print("New Album button clicked!"),
            font_size=12,
            font_weight="medium",
            width=180,
        )
        
        upload_section.layout_ref.addWidget(upload_button)