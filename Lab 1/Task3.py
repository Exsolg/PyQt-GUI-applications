from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QCheckBox
import sys


class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Checkboxes")
        self.setGeometry(400, 400, 570, 50)
        self.setWindowModified(False)

        self.check_boxes = [
            (QCheckBox("", self), QPushButton(f"{i}", self)) for i in range(5)]

        for i in range(len(self.check_boxes)):
            if i != 0:
                self.check_boxes[i][1].move(
                    self.check_boxes[i - 1][1].x() + 120, 0)
                self.check_boxes[i][0].move(
                    self.check_boxes[i - 1][0].x() + 120, 30)
            else:
                self.check_boxes[i][0].move(
                    self.check_boxes[i - 1][0].x() + 40, 30)
            self.check_boxes[i][0].clicked.connect(self.cboxConnect)

    def cboxConnect(self):
        for i in range(len(self.check_boxes)):
            if self.sender() == self.check_boxes[i][0]:
                if self.check_boxes[i][0].checkState():
                    self.check_boxes[i][1].hide()
                else:
                    self.check_boxes[i][1].show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()

    win.show()
    sys.exit(app.exec())
