import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyButton(QPushButton):
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        super().__init__(*args, **kwargs)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, e):
        print("dans le bouton", e.x())


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        self.setMouseTracking(True)
        self.button = MyButton(self, text="cliquer moi")
        self.button.clicked.connect(self.on_button_click)

    def mouseMoveEvent(self, e):
        print(e.x())

    def on_button_click(self):
        print("clicked")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
