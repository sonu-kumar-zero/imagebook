from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QSizePolicy, QWidget

from app.ui.widgets.kbutton_wrapper import ButtonWrapper
from app.ui.widgets.kframe import FrameWrapper
from app.ui.widgets.klayout_box import LayoutWrapper
from app.utils.constants import CONFIG

from dataclasses import dataclass
from pathlib import Path
from app.ui.assets.icons import Icons

@dataclass
class NavigationItem:
    key: str
    text: str
    iconPath: Path | None = None

class SideBar(FrameWrapper):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(
            parent=parent,
            object_name="sidebar",
            fixed_width=CONFIG.SIDEBAR.WIDTH,
            expand_width=False,
            layout=LayoutWrapper(
                direction="vertical",
                margins=(30, 20, 0, 20),
                spacing=15))

        self.buttons: dict[str, ButtonWrapper] = {}

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
            button = ButtonWrapper(
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
                frame=FrameWrapper(
                    object_name=(
                        "sidebar_button_frame"
                    ),
                    layout=LayoutWrapper(
                        direction="horizontal",
                        margins=(24, 0, 24, 0),
                        spacing=18,
                    ),
                ),
            )
            self.buttons[item.key] = button

            setattr(
                self,
                f"{item.key}_btn",
                button,
            )

            layout.addWidget(button)

    def _create_button(self, text: str) -> QPushButton:
        button = QPushButton(text)

        button.setObjectName("sidebar_button")
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setMinimumHeight(48)
        button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        return button

    def _separator(self) -> None:
        self.layout_ref.addWidget(FrameWrapper(object_name="sidebar_separator", shape="hline"))