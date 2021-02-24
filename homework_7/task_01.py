# Описать функцию fact2(n), вычисляющую двойной факториал: n!! = 1·3·5·...·n, если n — нечетное; n!! =
# 2·4·6·...·n, если n — четное (n > 0 — параметр целого типа). С помощью этой функции найти двойные
# факториалы пяти случайных целых чисел.

from random import randint

def factorial2(per: int) -> int:
    """this function counts the double factorial of a number

    Parameters
    ----------
    per : int
    the number for which the double factorial will be calculated

    """
    fact2 = 1
    assert type(per) == int, 'function passed not a number'
    if per % 2 == 0:
        for i in range(2,per + 1, 2):
            fact2 *= i
    else:
        for i in range(1,per + 1, 2):
            fact2 *= i

    return fact2

def result() -> list:
    """This function shows the result for 5 random numbers"""
    num_list = [6, 4, 9, 7, 5]
    result_list =[]
    for num in num_list:
        result_list.append(factorial2(num))
    assert result_list == [48, 8, 945, 105, 15], 'not a match of the result'
    return result_list

if __name__ == "__main__":
    print(result())
