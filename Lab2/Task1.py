from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_flag import Ui_MainWindow
import sys


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Флаги")
        self.setFixedSize(self.width(), self.height())
        self.pushButton.clicked.connect(self.showColors)

    def showColors(self):
        self.plainTextEdit.setPlainText("")

        for group in [self.firstGroup, self.secondGroup, self.thirdGroup]:
            for button in group.buttons():
                if button.isChecked():
                    self.plainTextEdit.appendPlainText(button.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())
