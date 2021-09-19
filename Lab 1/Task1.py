from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
import sys


class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mover")
        self.setGeometry(400, 400, 400, 50)
        self.setWindowModified(False)

        self.l_field = QLineEdit("", self)
        self.r_field = QLineEdit("", self)
        self.change_button = QPushButton("->", self)

        self.r_field.setDisabled(True)
        self.r_field.move(260, 0)
        print(self.width())
        self.change_button.move(
            (self.width() - self.change_button.width()) / 2, 0)
        self.change_button.setBaseSize(self.change_button.sizeHint())

        self.change_button.clicked.connect(self.changeWidget)

    def changeWidget(self):
        if self.l_field.text() != "":
            self.change_button.setText("<-")
            self.l_field.setDisabled(True)
            self.r_field.setDisabled(False)
            self.r_field.setText(self.l_field.text())
            self.l_field.setText("")
        elif self.r_field.text() != "":
            self.change_button.setText("->")
            self.l_field.setDisabled(False)
            self.r_field.setDisabled(True)
            self.l_field.setText(self.r_field.text())
            self.r_field.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()

    win.show()
    sys.exit(app.exec())
