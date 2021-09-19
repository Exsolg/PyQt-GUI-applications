from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
import sys


class Win(QWidget):
    morze = {'A': '•—', 'B': '—•••',
             'C': '—•—•', 'D': '—••',
             'E': '•', 'F': '••—•',
             'G': '——•', 'H': '••••',
             'I': '••', 'J': '•———',
             'K': '—•—', 'L': '•—••',
             'M': '——', 'N': '—•',
             'O': '———', 'P': '•——•',
             'Q': '——•—', 'R': '•—•',
             'S': '•••', 'T': '—',
             'U': '••—', 'V': '•••—',
             'W': '•——', 'X': '—••—',
             'Y': '—•——', 'Z': '——••'}

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Morse Code")
        self.setGeometry(400, 400, 450, 90)
        self.setWindowModified(False)

        self.text_box = QLineEdit("", self)
        self.buttons = []

        self.text_box.move((self.width() - self.text_box.width()) / 2, 60)

        for i in range(65, 91):
            self.buttons.append(QPushButton(chr(i), self))
            self.buttons[-1].resize(30, 30)

        for i in range(len(self.buttons)):
            if i < 13:
                self.buttons[i].move(self.buttons[i - 1].x() + 30, 0)
            else:
                if i == 13:
                    self.buttons[i].move(30, 30)
                else:
                    self.buttons[i].move(self.buttons[i - 1].x() + 30, 30)

            self.buttons[i].clicked.connect(self.bindButton)

    def bindButton(self):
        self.text_box.setText(self.text_box.text() +
                              self.morze[self.sender().text()] + " ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()

    win.show()
    sys.exit(app.exec())
