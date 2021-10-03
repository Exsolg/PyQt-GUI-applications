from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
from Ui_rocks import Ui_MainWindow
import sys


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initInput()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Камни")
        self.setFixedSize(self.width(), self.height())
        self.steps.buttonClicked.connect(self.game)
        self.startGame()

    def initInput(self):
        self.startGame()
        num, check = QInputDialog.getInt(self, 'Ввод',
            'Введите кол-во камней:', 0, 0)
        if check:
            self.bunch = num
            self.rocks.setText("Камней в куче " + str(num))
    
    def game(self, button):
        self.bunch -= int(button.text())
        self.rocks.setText("Камней в куче: " + str(self.bunch))

        if self.hasWon('Вы победили'):
            return

        self.computerStep()

    def computerStep(self):
        for button in self.steps.buttons():
            button.setEnabled(False)

        if self.bunch % 4 == 0:
            self.bunch -= 1
        else:
            self.bunch -= self.bunch % 4

        self.rocks.setText("Камней в куче: " + str(self.bunch))

        self.hasWon('Компьютер победил')

        for button in self.steps.buttons():
            button.setEnabled(True)

    def hasWon(self, winner):
        if self.bunch == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Игра закончена")
            msg.setText(winner)
            msg.exec_()
            self.initInput()
            return True

        elif self.bunch < 0:
            self.initInput()
            return True

    def startGame(self):
        self.bunch = 20
        self.rocks.setText("Камней в куче: " + str(self.bunch))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())
