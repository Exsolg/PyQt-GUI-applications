from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_Task1 import Ui_MainWindow
import sys, random



class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Рандоманая строка")
        self.setFixedSize(self.width(), self.height())
        self.loadStr()
        self.randButton.clicked.connect(self.randStr)
    
    def randStr(self):
        if self.strings:
            self.strings = [value for value in self.strings if value]
            string = self.strings[random.randint(0, len(self.strings) - 1)]
            self.textEdit.setPlainText(string)

    def loadStr(self):
        with open('lines.txt', 'r') as file:
            self.strings = file.readlines()
        self.strings = list(map(lambda x: x.replace('\n', ''), self.strings))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())
