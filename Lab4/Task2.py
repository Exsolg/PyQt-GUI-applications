from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_Task1 import Ui_MainWindow
import sys


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Вывод строк")
        self.setFixedSize(self.width(), self.height())
        self.loadStr()
        self.randButton.setText('Output')
        self.randButton.clicked.connect(self.randStr)
    
    def randStr(self):
        self.textEdit.setPlainText('')
        if self.strings:
            self.strings = [value for value in self.strings if value]
            self.textEdit.appendPlainText('Нечетные:')
            for i in range(1, len(self.strings), 2):
                self.textEdit.appendPlainText('\t' + self.strings[i])

            self.textEdit.appendPlainText('Четные:')
            for i in range(0, len(self.strings), 2):
                self.textEdit.appendPlainText('\t' + self.strings[i])

    def loadStr(self):
        with open('lines.txt', 'r') as file:
            self.strings = file.readlines()
        self.strings = list(map(lambda x: x.replace('\n', ''), self.strings))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())
