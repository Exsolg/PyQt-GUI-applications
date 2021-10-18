def check_pass(password):
    combination = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']

    if len(password) > 8:
        if any(map(str.isupper, password)) and any(map(str.islower, password)):
            if any(map(str.isdigit, password)):
                has_comb = False
                for comb in combination:
                    for i in range(len(comb) - 3):
                        if comb[i: i + 3] in password:
                            has_comb = True
                if not has_comb:
                    return 'ok'
    return "error"

password = input("Введите пароль: ")
print(check_pass(password))

