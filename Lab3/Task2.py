def check_password(password):
    combination = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']

    try:
        assert len(password) > 8, "Длина пароля должна быть больше 8 символов"
        assert any(map(str.isupper, password)) and any(map(str.islower, password)), "Пароль должен содержать заглавные и строчные буквы"
        assert any(map(str.isdigit, password)), "Пароль должен содержать цифры"
        has_comb = False
        for comb in combination:
            for i in range(len(comb) - 3):
                if comb[i: i + 3] in password:
                    has_comb = True
        assert not has_comb, "Пароль не должен содержать 3 букв идущих подряд на клавиатуре"
        return 'ok'
    except AssertionError as error:
        return f'error: {error.args[0]}'
    
password = input("Введите пароль: ")
print(check_password(password))