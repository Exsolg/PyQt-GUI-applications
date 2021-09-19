from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
import sys


class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        self.setGeometry(400, 400, 407, 60)
        self.setWindowModified(False)

        self.counter = 0
        self.operators = []
        self.memories = []
        self.last_oper = None
        self.enter = QLineEdit("", self)

        for action in ["+", "-", "*", "/", "="]:
            self.operators.append(QPushButton(action, self))
            self.operators[-1].resize(30, 30)

        self.operators[0].move(
            (self.width() - self.operators[0].width()) / 2 - 60, 30)
        for i in range(0, len(self.operators)):
            if i != 0:
                self.operators[i].move(self.operators[i - 1].x() + 30, 30)
            self.operators[i].clicked.connect(self.getResult)

        self.enter.move((self.width() - self.enter.width()) / 2 - 20, 0)

    def getResult(self):
        for oper in self.operators:
            if self.sender() == oper:
                if self.counter == 0:
                    if oper.text() != '=':
                        if self.isNumber(self.enter.text()):
                            self.enter.setText(self.enter.text() + oper.text())
                            self.last_oper = oper.text()
                            self.memories.append(
                                self.enter.text().split(oper.text())[0])
                            self.counter += 1
                            self.enter.setFocus()
                    else:
                        self.memories.append(self.enter.text())
                        self.counter = 0
                        self.memories = []
                        self.enter.setFocus()
                elif self.counter == 1:
                    self.memories.append(
                        self.enter.text().split(self.last_oper)[1])
                    self.calc()
                    self.last_oper = None
                    self.memories = []
                    self.counter = 0
                    self.getResult()

    def calc(self):
        if self.memories[1] == '0':
            self.enter.setText("Division by zero")
        else:
            mean = eval(str(self.memories[0]) +
                        self.last_oper + str(self.memories[1]))
            self.enter.setText(str(mean))

    def isNumber(self, str):
        try:
            float(str)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()

    win.show()
    sys.exit(app.exec())
