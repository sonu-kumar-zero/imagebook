import sys

# from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
# from app.ui.windows.layout_window import LayoutWindow

from app.ui.windows.home_window import HomeWindow
# from app.ui.windows.splash_screen import SplashScreen
# from app.ui.windows.card_window import CardWindow

def main():
    app = QApplication(sys.argv)

    # splash = SplashScreen()
    #splash.show()

    # window = CardWindow()
    window = HomeWindow()
    # window = LayoutWindow()

    # def show_main_window():
        # splash.close()
    window.show()

    # QTimer.singleShot(
    #     2500,
    #     show_main_window
    # )

    exit_code = app.exec()

    sys.exit(exit_code)


if __name__ == "__main__":
    main()