from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_passwords_checker import Ui_MainWindow
import sys
import Task3


class WordError(Task3.PasswordError):
    pass


def checkLength(password):
    if len(password) < 9:
        raise Task3.LengthError('Пароль должен сожержать больше 8 символов')


def checkLetters(password):
    if not any(map(str.isupper, password)) or not any(map(str.islower, password)):
        raise Task3.LetterError(
            'Пароль должен сожержать буквы обоих регистров')


def checkDigits(password):
    if not any(map(str.isdigit, password)):
        raise Task3.DigitError('Пароль должен сожержать цифры')


def checkCombinations(password):
    combination = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm',
                   'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
    has_comb = False
    for comb in combination:
        for i in range(len(comb) - 3):
            if comb[i: i + 3] in password:
                has_comb = True
    if has_comb:
        raise Task3.SequenceError(
            'Пароль не должен сожержать 3 буквы идущих подряд на клавиатуре')


def checkWords(password):
    with open('./top-9999-words.txt') as words_file:
        words = words_file.readlines()

    words = list(map(lambda x: x.replace('\n', ''), words))

    for word in words:
        if word in password:
            raise WordError('Пароль не должен содержать словарных слов')


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.excps = {}
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Проверка паролей")
        self.setFixedSize(self.width(), self.height())
        self.passwordChecker()

    def passwordChecker(self):
        with open('./top 10000 passwd.txt') as pswds:
            self.pswds = pswds.readlines()

        self.pswds = list(map(lambda x: x.replace('\n', ''), self.pswds))

        for pswd in self.pswds:
            try:
                checkLength(pswd)
            except Task3.PasswordError as error:
                self.excps.update(
                    {type(error).__name__: self.excps.get(type(error).__name__, 0) + 1})

            try:
                checkLetters(pswd)
            except Task3.PasswordError as error:
                self.excps.update(
                    {type(error).__name__: self.excps.get(type(error).__name__, 0) + 1})

            try:
                checkDigits(pswd)
            except Task3.PasswordError as error:
                self.excps.update(
                    {type(error).__name__: self.excps.get(type(error).__name__, 0) + 1})

            try:
                checkCombinations(pswd)
            except Task3.PasswordError as error:
                self.excps.update(
                    {type(error).__name__: self.excps.get(type(error).__name__, 0) + 1})

            try:
                checkWords(pswd)
            except Task3.PasswordError as error:
                self.excps.update(
                    {type(error).__name__: self.excps.get(type(error).__name__, 0) + 1})

        self.showExceptions()

    def showExceptions(self):
        excp = sorted(self.excps.items(), key=lambda x: x[0])
        for key, value in excp:
            self.exceptionsList.appendPlainText(f"{key} - {value}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()

    win.show()
    sys.exit(app.exec())
