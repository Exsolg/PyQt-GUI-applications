from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from Ui_antiplagiary import Ui_MainWindow
import sys
from difflib import SequenceMatcher


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Антиплагиат")
        self.setFixedSize(self.width(), self.height())
        self.equal.clicked.connect(self.equalTexts)
        self.accuracy = QLabel('', self)
        self.statusBar().addPermanentWidget(self.accuracy, 1)

    def equalTexts(self):
        match = SequenceMatcher(None, self.text1.toPlainText().lower(), self.text2.toPlainText().lower()).ratio() * 100
        self.accuracy.setText(f"Совпадение {round(match, 2)}%")
        if match > 80:
            self.statusBar().setStyleSheet('background-color: red')
        elif match > 50:
            self.statusBar().setStyleSheet('background-color: yellow')
        else:
            self.statusBar().setStyleSheet('background-color: green')
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())
