# Описать функцию для перевода десятичного числа в двоичное. Описать бесконечный цикл, в котором
# запрашивать у пользователя число и переводить его в двоичную систему. Признак окончания работы
# программы - введенное пользователем число 0.
def translate_to_2(per: int) -> str:
    """This function converts a number from the 10th system to the 2th

    Parameters
    ----------
    per : int

    Input
    ----------
    The user enters the number that needs to be translated into the 2nd system

    Result
    ----------
    The result will be a number in the 2nd system written as a string"""

    number_in_2 = ''
    assert type(per) == int, 'function passed not a number'
    while per > 0:
        number_in_2 = str(per % 2) + number_in_2
        per = per // 2
    return number_in_2


def result() -> None:
    """This function shows the result and checks the number"""
    while True:
        number = input('enter the number: ')
        if number == '0': break
        if number.isdigit() == False:
            print('you entered not a number')
        else:
            print(translate_to_2(int(number)))


if __name__ == "__main__":
    result()
