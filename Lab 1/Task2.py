from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
import sys


class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Eval")
        self.setGeometry(400, 400, 400, 50)
        self.setWindowModified(False)

        self.l_field = QLineEdit("", self)
        self.r_field = QLineEdit("", self)
        self.equal = QPushButton("Equal", self)

        self.r_field.move(260, 0)
        self.equal.move((self.width() - self.equal.width()) / 2, 0)
        self.equal.setBaseSize(self.equal.sizeHint())

        self.equal.clicked.connect(self.changeWidget)

    def changeWidget(self):
        if self.l_field.text() != "":
            self.r_field.setText(str(eval(self.l_field.text())))
            self.l_field.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()

    win.show()
    sys.exit(app.exec())
