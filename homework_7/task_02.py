# Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"), т.е. таким,
# которое читается одинаково слева направо и справа налево. (Определить функцию, позволяющую
# распознавать слова палиндромы.)

def polindrom():
    """This function show palindromes and their number in a line

    The string is split into words, after each word is checked for compliance with the condition

    Input
    ---------
    The user enters the string at will

    Result
    ---------
    Аs a result, the words polyindroms and their number are displayed

    """
    words = []
    count = 0
    stoka = str(input('введите строку: '))
    for word in stoka.split():
        if word == word[::-1]:
            words.append(word)
            count += 1
    if count == 0:
        print('нет полиндромов')
    else:
        print(f'слова полиндромы:{words}, количество полиндоромов: {count}')


if __name__ == "__main__":
    polindrom()
