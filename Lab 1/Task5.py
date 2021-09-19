from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QPushButton, QLabel
import sys


class Win(QWidget):
    order = {}

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Menu")
        self.setGeometry(400, 400, 400, 500)
        self.setWindowModified(False)

        self.cheque = QPlainTextEdit("", self)
        self.menu = []
        self.dishes = [("Салат", 200), ("Суп", 550), ("Чиз-кейк", 100)]

        for dish, _ in self.dishes:
            self.menu.append([QLabel(dish, self), QPushButton(
                "Добавить", self), QPushButton("Убрать", self)])

        for i in range(len(self.menu)):
            self.menu[i][0].move(40, self.menu[i - 1][0].y() + 30)
            self.menu[i][1].move(120, self.menu[i - 1][1].y() + 30)
            self.menu[i][2].move(250, self.menu[i - 1][2].y() + 30)
            self.menu[i][1].clicked.connect(self.update)
            self.menu[i][2].clicked.connect(self.update)

        self.cheque.move(40, 200)
        self.cheque.resize(320, 250)

    def update(self):
        for i in range(len(self.menu)):
            if self.sender() == self.menu[i][1]:
                self.order.update({
                    self.menu[i][0]: self.order.get(self.menu[i][0], 0) + 1})
            elif self.sender() == self.menu[i][2]:
                if self.menu[i][0] in self.order:
                    if self.order.get(self.menu[i][0]) > 0:
                        self.order.update(
                            {self.menu[i][0]: self.order.get(self.menu[i][0], 0) - 1})
                        if self.order.get(self.menu[i][0]) == 0:
                            del self.order[self.menu[i][0]]
                    else:
                        del self.order[self.menu[i][0]]

        self.showCheque()

        if not self.order:
            self.cheque.setPlainText("\t                Чек")

    def showCheque(self):
        cheque_sum = 0
        self.cheque.setPlainText("\t                Чек\nБлюдо\tКол-во\tЦена")
        for dish, value in self.order.items():
            for meal, cost in self.dishes:
                if dish.text() == meal:
                    cheque_sum += cost * value
                    self.cheque.appendPlainText(
                        dish.text() + "\t" + str(value) + f"\t{cost * value}")

        self.cheque.appendPlainText(f"Итого:\t\t{cheque_sum}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()

    win.show()
    sys.exit(app.exec())
