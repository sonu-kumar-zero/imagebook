# app/ui/styles/types.py

from typing import Literal


Variant = Literal[
    "card",
    "title",
    "subtitle",
    "image",
    "window",
    "test1",
    "window-control"
]


from typing import Literal

UtilityClass = Literal[
    # =========================
    # BACKGROUNDS
    # =========================
    "bg-app",
    "bg-surface-1",
    "bg-surface-2",
    "bg-surface-3",
    "bg-card",
    "bg-card-hover",
    "bg-red",
    "bg-blue",
    "bg-green",
    "bg-transparent",

    # =========================
    # BORDERS
    # =========================
    "border-soft",
    "border-soft-hover",
    "border-accent",
    "border-accent-hover",

    # =========================
    # RADIUS
    # =========================
    "rounded-card",
    "rounded-image",
    "rounded-button",
    "rounded-input",
    "rounded-full",

    # =========================
    # TEXT
    # =========================
    "text-primary",
    "text-secondary",
    "text-muted",
    "text-disabled",
    "text-accent",

    # =========================
    # TYPOGRAPHY
    # =========================
    "title",
    "subtitle",
    "body",
    "small",

    # =========================
    # EFFECTS
    # =========================
    "shadow-card",
    "shadow-card-hover",
    "glow-accent",

    # =========================
    # SPACING
    # =========================
    "p-sm",
    "p-md",
    "p-lg",
    "gap-sm",
    "gap-md",
    "gap-lg",
]