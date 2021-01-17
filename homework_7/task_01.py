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
    if per % 2 == 0:
        for i in range(2,per + 1, 2):
            fact2 *= i
    else:
        for i in range(1,per + 1, 2):
            fact2 *= i
    print(f'{per}!!= {fact2}')


def result():
    """This function shows the result for 5 random numbers"""
    num_list = [randint(1, 20) for i in range(5)]
    for num in num_list:
        factorial2(num)


if __name__ == "__main__":
    result()
