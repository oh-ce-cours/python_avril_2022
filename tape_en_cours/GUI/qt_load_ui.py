import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic
from metier import traitement_donnees
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        uic.loadUi("mainwindow.ui", self)  # Load the .ui file
        self.show()  # Show the GUI
        self.pushButton.clicked.connect(self.on_click)

    # def on_click(self):
    #     print("on m'a cliqué")
    #     try:
    #         self.label.setText(
    #             str(
    #                 int(self.textEdit.toPlainText())
    #                 + int(self.textEdit_2.toPlainText())
    #             )
    #         )
    #     except ValueError:
    #         self.label.setText("Des nombres SVP")
    #     print("on a mis a jour la valeur")

    def on_click(self):
        res = traitement_donnees(
            self.textEdit.toPlainText(),
            self.textEdit_2.toPlainText(),
            update_ui=self.set_progress_value,
        )
        self.label.setText(res)

    def set_progress_value(self, value):
        self.progressBar.setValue(value)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
