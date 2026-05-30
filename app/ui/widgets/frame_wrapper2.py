from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Literal,
    TypeAlias,
    cast,
)

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QSizePolicy,
    QWidget,
)
from app.ui.widgets.base_layout import BaseLayout

if TYPE_CHECKING:
    from app.ui.widgets.klayout_box import (
        LayoutWrapper,
    )

# ==========================================================
# TYPES
# ==========================================================

FrameShape: TypeAlias = Literal[
    "box",
    "panel",
    "styled",
    "hline",
    "vline",
]

FrameShadow: TypeAlias = Literal[
    "plain",
    "raised",
    "sunken",
]


# ==========================================================
# FRAME WRAPPER
# ==========================================================

class FrameWrapper2(QFrame):
    def __init__(
        self,
        *,
        parent: QWidget | None = None,
        layout: BaseLayout | None = None,
        shape: FrameShape = "styled",
        shadow: FrameShadow = "plain",
        object_name: str | None = None,
        min_width: int | None = None,
        min_height: int | None = None,
        max_width: int | None = None,
        max_height: int | None = None,
        fixed_width: int | None = None,
        fixed_height: int | None = None,
        expand_width: bool = True,
        expand_height: bool = True,

        # ==========================
        # STYLING
        # ==========================

        bg_color: str = "transparent",
        color: str | None = None,
        border_radius: int = 0,
        border_width: int = 0,
        border_color: str = (
            "transparent"
        ),
    ) -> None:
        super().__init__(parent)

        self.setAttribute(
            Qt.WidgetAttribute.
            WA_StyledBackground,
            True,
        )

        self.setAutoFillBackground(
            True
        )

        if object_name:
            self.setObjectName(
                object_name
            )

        self.setFrameShape(
            self._get_shape(shape)
        )

        self.setFrameShadow(
            self._get_shadow(shadow)
        )

        self._setup_size(
            min_width=min_width,
            min_height=min_height,
            max_width=max_width,
            max_height=max_height,
            fixed_width=fixed_width,
            fixed_height=fixed_height,
            expand_width=expand_width,
            expand_height=expand_height,
        )

        self._apply_styles(
            bg_color=bg_color,
            color=color,
            border_radius=(
                border_radius
            ),
            border_width=(
                border_width
            ),
            border_color=(
                border_color
            ),
        )

        # ==========================
        # CONVENIENCE LAYOUT
        # ==========================

        if layout is not None:
            self.set_layout(
                layout
            )

    # ======================================================
    # INTERNALS
    # ======================================================

    def _apply_styles(
        self,
        *,
        bg_color: str,
        color: str | None,
        border_radius: int,
        border_width: int,
        border_color: str,
    ) -> None:
        stylesheet = f"""
        QFrame {{
            background-color:
                {bg_color};

            border-radius:
                {border_radius}px;

            border:
                {border_width}px solid
                {border_color};
        }}
        """

        if color is not None:
            stylesheet += f"""
            QLabel {{
                color:
                    {color};
            }}
            """

        self.setStyleSheet(
            stylesheet
        )

    def _get_shape(
        self,
        shape: FrameShape,
    ) -> QFrame.Shape:
        mapping = {
            "box": (
                QFrame.Shape.Box
            ),
            "panel": (
                QFrame.Shape.Panel
            ),
            "styled": (
                QFrame.Shape.
                StyledPanel
            ),
            "hline": (
                QFrame.Shape.HLine
            ),
            "vline": (
                QFrame.Shape.VLine
            ),
        }

        return mapping[shape]

    def _get_shadow(
        self,
        shadow: FrameShadow,
    ) -> QFrame.Shadow:
        mapping = {
            "plain": (
                QFrame.Shadow.Plain
            ),
            "raised": (
                QFrame.Shadow.Raised
            ),
            "sunken": (
                QFrame.Shadow.Sunken
            ),
        }

        return mapping[shadow]

    def _setup_size(
        self,
        *,
        min_width: int | None,
        min_height: int | None,
        max_width: int | None,
        max_height: int | None,
        fixed_width: int | None,
        fixed_height: int | None,
        expand_width: bool,
        expand_height: bool,
    ) -> None:
        if min_width is not None:
            self.setMinimumWidth(
                min_width
            )

        if min_height is not None:
            self.setMinimumHeight(
                min_height
            )

        if max_width is not None:
            self.setMaximumWidth(
                max_width
            )

        if max_height is not None:
            self.setMaximumHeight(
                max_height
            )

        if fixed_width is not None:
            self.setFixedWidth(
                fixed_width
            )

        if fixed_height is not None:
            self.setFixedHeight(
                fixed_height
            )

        horizontal = (
            QSizePolicy.Policy.
            Expanding
            if expand_width
            else QSizePolicy.Policy.
            Preferred
        )

        vertical = (
            QSizePolicy.Policy.
            Expanding
            if expand_height
            else QSizePolicy.Policy.
            Preferred
        )

        self.setSizePolicy(
            horizontal,
            vertical,
        )

    # ======================================================
    # LAYOUT HELPERS
    # ======================================================

    def set_layout(
        self,
        layout: BaseLayout,
    ) -> None:
        self.setLayout(
            layout.qlayout
        )

    @property
    def layout_ref(
        self,
    ) -> "LayoutWrapper":
        return cast(
            "LayoutWrapper",
            self.layout(),
        )

    # ======================================================
    # HELPERS
    # ======================================================

    def hide_frame(
        self,
    ) -> None:
        self.hide()

    def show_frame(
        self,
    ) -> None:
        self.show()

    def collapse_width(
        self,
    ) -> None:
        self.setMaximumWidth(0)

    def expand_width(
        self,
        width: int = 16777215,
    ) -> None:
        self.setMaximumWidth(
            width
        )

    def collapse_height(
        self,
    ) -> None:
        self.setMaximumHeight(0)

    def expand_height(
        self,
        height: int = 16777215,
    ) -> None:
        self.setMaximumHeight(
            height
        )