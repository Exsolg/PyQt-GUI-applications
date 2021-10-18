from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Ui_reg_form import Ui_MainWindow
import sys, Task3, Task5

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Форма регистрации")
        self.setFixedSize(self.width(), self.height())
        self.signButton.clicked.connect(self.checkForm)

    def checkForm(self):
        login = self.loginEdit.text()
        pswd = self.pswdEdit.text()
        phone = self.phoneEdit.text()
        errors = []
        if login:
            try:
                Task3.check_pass(pswd)
            except Task3.PasswordError as error:
                errors.append(error.args[0])

            try:
                Task5.check_number(phone)
            except Task5.NumberError as phone_error:
                errors.append(phone_error.args[0])

            if errors:
                msg = QMessageBox(self)
                msg.setWindowTitle('Ошибка!')
                msg.setText(',\n'.join(errors))
                msg.exec_()
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle('Ошибка!')
            msg.setText('Введите логин.')
            msg.exec_()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())
