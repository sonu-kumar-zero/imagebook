from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
from app.ui.widgets.qcolor import Color

# class LayoutWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Layout Window")

#         widget = Color("red")
#         self.setCentralWidget(widget)


# class LayoutWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Layout Window")

#         layout = QVBoxLayout()
#         layout.addWidget(Color("blue"))
#         layout.addWidget(Color("red"))
#         layout.addWidget(Color("green"))

#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)


class LayoutWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Window")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.addLayout(layout2)
        layout1.addLayout(layout3)
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("green"))
        layout2.addWidget(Color("blue"))

        layout3.addWidget(Color("cyan"))
        layout3.addWidget(Color("purple"))
        layout3.addWidget(Color("yellow"))
        

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
        layout1.setSpacing(0)
        layout1.setContentsMargins(0,0,0,0)

