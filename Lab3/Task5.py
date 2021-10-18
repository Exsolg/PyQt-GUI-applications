import re


class NumberError(BaseException):
    pass

class LengthError(NumberError):
    pass

class FormatError(NumberError):
    pass

class CountryCodeError(NumberError):
    pass

class OperatorCodeError(NumberError):
    pass


def get_clear_number(number):
    clear_phone = re.sub(r'\D', '', number)
    result = re.match(r'^[78]?\d{10}$', clear_phone)
    try:
        return result.string
    except AttributeError:
        return None

def check_number(number: str):
    region_codes = [list(range(910, 920)), list(range(980, 990)), 
                    list(range(920, 940)), list(range(902, 907)),
                    list(range(960, 970))]

    number = ''.join(number.split())
    if ((number.count('(') > 1 or number.count(')') > 1)
    or ('(' in number and ')' not in number)
    or (')' in number and '(' not in number)
    or (number[0] == '-' or number[-1] == '-' or '--' in number)
    or (number.find('(') > number.find(')'))):
        raise FormatError("неверный формат")

    if number[0] != '8' and number[:2] != '+7':
        raise CountryCodeError("неверный код страны")
    
    number = get_clear_number(number)
    if number is None or len(number) != 11:
        raise LengthError("неверное кол-во цифр")

    is_valid_operator = False
    for oper in region_codes:
        for code in oper:
            if str(code) in number[1:4]:
                is_valid_operator = True
                break
    
    if not is_valid_operator:
        raise OperatorCodeError("неверный код оператора")
    
    return '+7' + number[1:]


if __name__ == '__main__':
    numbers = ['+7(902)123-4567',
                '8(902)1-2-3-45-67',
                '504))635(22))9 9',
                '8--9019876543-22-3--4',
                '87393))985942',
                '79623 8)487',
                '9914273 13-87',
                '8846776422',
                '+1(916)123-4567',
                '+7171((806243',
                '9(754310--4-5',
                '+71113253136',
                '864357))4 92 8 2',
                '8 114356 30',
                '+79700830356',
                '8(916) 12 4 32-6 7']

    for number in numbers:
        try:
            print(f'{number} - {check_number(number)}', end=' ')
        except NumberError as e:
            print(number + " - " + e.args[0], end=" ")
        print("")
