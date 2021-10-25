from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Ui_Task3 import Ui_MainWindow
import sys, re, os.path



class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Считывание из файла")
        self.setFixedSize(self.width(), self.height())
        self.numbers = []
        self.readButton.clicked.connect(self.loadNumbers)
        self.countButton.clicked.connect(self.countNumbers)

    def saveFile(self):
        with open("output.txt", 'w') as out:
            out.write(self.textEdit.toPlainText())
    
    def countNumbers(self):
        self.textEdit.setPlainText('')
        if self.numbers:
            self.textEdit.appendPlainText(f'Max: {max(self.numbers)}')
            self.textEdit.appendPlainText(f'Min: {min(self.numbers)}')
            self.textEdit.appendPlainText(f'Avg: {sum(self.numbers) / len(self.numbers)}')
            self.saveFile()

    def loadNumbers(self):
        self.textEdit.setPlainText('')
        name = self.lineEdit.text()
        if name and os.path.exists(name):
            with open(name, 'r') as file:
                self.numbers = file.read()

            self.numbers = " ".join(self.numbers.split())
            self.numbers = re.split(" |\n|\t", self.numbers)
            try:
                self.numbers = list(map(int, self.numbers))
            except ValueError:
                self.showMessage("Ошибка!", "Неверный формат данных.")
                self.numbers = []
                return

            self.showMessage("Успех!", "Данные загружены.")
        else:
            self.showMessage("Ошибка!", "Указанный файл не существует.")

    def showMessage(self, title, message):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())
