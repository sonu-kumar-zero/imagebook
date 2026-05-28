PREMIUM_SCROLLBAR_QSS = """
/* =========================
   VERTICAL SCROLLBAR
========================= */

QScrollBar:vertical {
    background: transparent;
    width: 10px;
    margin: 4px 2px 4px 2px;
    border: none;
}

QScrollBar::handle:vertical {
    background: rgba(255, 255, 255, 70);
    min-height: 40px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background: rgba(255, 255, 255, 110);
}

QScrollBar::handle:vertical:pressed {
    background: rgba(255, 255, 255, 140);
}

/* remove arrow buttons */
QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
    border: none;
    background: transparent;
}

/* remove page jump area */
QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: transparent;
}


/* =========================
   HORIZONTAL SCROLLBAR
========================= */

QScrollBar:horizontal {
    background: transparent;
    height: 10px;
    margin: 2px 4px 2px 4px;
    border: none;
}

QScrollBar::handle:horizontal {
    background: rgba(255, 255, 255, 70);
    min-width: 40px;
    border-radius: 5px;
}

QScrollBar::handle:horizontal:hover {
    background: rgba(255, 255, 255, 110);
}

QScrollBar::handle:horizontal:pressed {
    background: rgba(255, 255, 255, 140);
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
    width: 0px;
    border: none;
    background: transparent;
}

QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal {
    background: transparent;
}
"""