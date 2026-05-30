from PySide6.QtWidgets import  QSizePolicy, QWidget
from PySide6.QtCore import  Qt
from PySide6.QtGui import  QResizeEvent


from app.utils.constants import CONFIG

from dataclasses import dataclass
from pathlib import Path
from app.ui.assets.icons import Icons
from app.ui.widgets.button_wrapper2 import ButtonWrapper2
from app.ui.widgets.frame_wrapper2 import FrameWrapper2
from app.ui.widgets.base_layout import BaseLayout

@dataclass
class NavigationItem:
    key: str
    text: str
    iconPath: Path | None = None

class SideBar(FrameWrapper2):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(
            parent=parent,
            object_name="sidebar",
            fixed_width=CONFIG.SIDEBAR.WIDTH,
            expand_width=False,
            layout=BaseLayout(
                direction="vertical",
                margins=(20, 20, 0, 20),
                spacing=15))

        self.buttons: dict[str, ButtonWrapper2] = {}
        self._collapsed_auto: bool = False

        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = self.layout_ref

        navigation_items: list[NavigationItem] = [
            NavigationItem(key="home", text="Home", iconPath=Icons.HOME.path),
            NavigationItem(key="explore", text="Explore", iconPath=Icons.EXPLORE.path),
            NavigationItem(key="gallery", text="My Gallery", iconPath=Icons.GALLERY.path),
            NavigationItem(key="collections", text="Collections", iconPath=Icons.COLLECTIONS.path),
            NavigationItem(key="favorites", text="Favorites", iconPath=Icons.FAVORITES.path),
            NavigationItem(key="upload", text="Upload", iconPath=Icons.UPLOAD.path),
        ]

        self._add_buttons(navigation_items)

        layout.addStretch()

        footer_items: list[NavigationItem] = [
            NavigationItem(key="settings", text="Settings", iconPath=Icons.SETTINGS.path),
            NavigationItem(key="profile", text="Profile", iconPath=Icons.USER.path),
        ]

        self._add_buttons(footer_items)

    def _add_buttons(
        self,
        items: list[NavigationItem],
    ) -> None:
        layout = self.layout_ref

        for item in items:
            button = ButtonWrapper2(
                text=item.text,
                height=54,
                radius=18,
                bg_color="transparent",
                hover_color=(
                    "rgba(255,255,255,0.06)"
                ),
                pressed_color=(
                    "rgba(124,92,255,0.16)"
                ),
                icon_path=item.iconPath,
                spacing=18,
                alignment=Qt.AlignmentFlag.AlignLeft,
            )
            
            self.buttons[item.key] = button

            setattr(
                self,
                f"{item.key}_btn",
                button,
            )

            layout.addWidget(button)

    def _separator(self) -> None:
        self.layout_ref.addWidget(FrameWrapper2(object_name="sidebar_separator", shape="hline"))
        
    def set_collapsed(self, collapsed: bool) -> None:
        if collapsed:
            self.setFixedWidth(CONFIG.SIDEBAR.COLLAPSE_WIDTH)
        else:
            self.setFixedWidth(CONFIG.SIDEBAR.WIDTH)
        for button in self.buttons.values():
            if collapsed:
                button.setAlignment(Qt.AlignmentFlag.AlignCenter)
            else:
                button.setAlignment(Qt.AlignmentFlag.AlignLeft)
            button.set_collapsed(collapsed)
    
    def resizeEvent(self, event:QResizeEvent) -> None:
        super().resizeEvent(event)

        parent = self.parentWidget()
        if not parent:
            return

        self._update_collapse_state(parent.width())
        
    def _update_collapse_state(self, width: int) -> None:
        should_collapse = width < CONFIG.SIDEBAR.COLLAPSE_THRESHOLD

        # avoid repeated re-apply (important for performance + flicker)
        if should_collapse == self._collapsed_auto:
            return

        self._collapsed_auto = should_collapse
        self.set_collapsed(should_collapse)