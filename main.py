import sys

from PySide6.QtWidgets import QApplication

from app.ui.windows.home_window import HomeWindow
from app.services.file_watcher import FileWatcher


def main():
    app = QApplication(sys.argv)

    window = HomeWindow()

    # Attach watcher to window
    window.watcher = FileWatcher("./projects")

    window.watcher.file_changed.connect(
        window.on_file_changed
    )

    window.watcher.start()

    window.show()

    exit_code = app.exec()

    window.watcher.stop()

    sys.exit(exit_code)


if __name__ == "__main__":
    main()