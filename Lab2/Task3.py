from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from Ui_notebook import Ui_MainWindow
import sys


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.numbers = []

    def initUI(self):
        self.setFixedSize(self.width(), self.height())
        self.addButton.clicked.connect(self.addNumber)
        self.removeButton.clicked.connect(self.removeNumber)

    def addNumber(self):
        item = QListWidgetItem(f"{self.nameLine.text()}\n    {self.numberLine.text()}")
        self.numbersList.addItem(item)
        self.numbers.append(item)

    def removeNumber(self):
        if self.numbers:
            item = self.numbersList.takeItem(self.numbersList.currentRow())
            self.numbers.remove(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())
