from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from Ui_Task4 import Ui_MainWindow
import sys


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.currentFile = None

    def initUI(self):
        self.setWindowTitle("Блокнот")
        self.setFixedSize(self.width(), self.height())
        self.openAction.triggered.connect(self.openNote)
        self.saveAction.triggered.connect(self.saveNote)
        self.createAction.triggered.connect(self.createNote)

    def openNote(self):
        self.currentFile = QFileDialog.getOpenFileName(None, 'Open File', './', "*.txt")[0]
        if self.currentFile and self.currentFile != '':
            with open(self.currentFile, "r+") as file:
                self.textBrowser.setPlainText(file.read())

    def saveNote(self):
        if self.currentFile and self.currentFile != '':
            with open(self.currentFile, "w") as file:
                file.write(self.textBrowser.toPlainText())

    def createNote(self):
        new_file = QFileDialog.getSaveFileName(None, 'Create New File', './', "*.txt")[0]
        if new_file != '':
            self.textBrowser.setPlainText("")
            self.currentFile = new_file


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())
