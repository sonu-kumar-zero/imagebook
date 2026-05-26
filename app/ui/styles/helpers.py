# app/ui/styles/helpers.py

from PySide6.QtWidgets import QWidget

from app.ui.styles.types import Variant


def set_variant(
    widget: QWidget,
    variant: Variant,
) -> None:
    widget.setProperty(
        "variant",
        variant,
    )