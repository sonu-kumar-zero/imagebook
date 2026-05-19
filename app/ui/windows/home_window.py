from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)


class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Book Creator")
        self.resize(900, 600)

        layout = QVBoxLayout()

        title = QLabel("Image Book Creator")

        new_btn = QPushButton("Create New Project")
        open_btn = QPushButton("Open Existing Project")

        layout.addWidget(title)
        layout.addWidget(new_btn)
        layout.addWidget(open_btn)

        self.setLayout(layout)

    def on_file_changed(self, path):
        print("File changed:", path)