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
                margins=(30, 0, 30, 30),
                spacing=20,
            ),
        )
        
        self.setStyleSheet(tw("bg-surface-1"))
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        

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


        self.layout_ref.addWidget(footer)
        pass