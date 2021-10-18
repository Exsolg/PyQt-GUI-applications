class PasswordError(BaseException):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

class SequenceError(PasswordError):
    pass

def check_pass(password):
    combination = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']

    if len(password) < 9: raise LengthError('Пароль должен сожержать больше 8 символов')
    if not any(map(str.isupper, password)) or not any(map(str.islower, password)): 
        raise LetterError('Пароль должен сожержать буквы обоих регистров')
    if not any(map(str.isdigit, password)): raise DigitError('Пароль должен сожержать цифры')
    has_comb = False
    for comb in combination:
        for i in range(len(comb) - 3):
            if comb[i: i + 3] in password:
                has_comb = True
    if has_comb: raise SequenceError('Пароль не должен сожержать 3 буквы идущих подряд на клавиатуре')
    return 'ok'

if __name__ == '__main__':
    password = input("Введите пароль: ")
    try:
        print(check_pass(password))
    except PasswordError as error:
        print(error.args[0])