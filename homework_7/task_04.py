# Вычислить значения нижеприведенной функции в диапазоне значений x от -10 до 10 включительно с
# шагом, равным 1. В качестве результат вывести на экран значение функции y при каждом x из указанного диапазона
def fun_y(per: int) -> int:
    """This function will return the 'y' value for 'x' from the range

    Parameters
    ----------
    per : int

    Result
    ----------
    The result is a number, depending on 'x' """
    result_y = 0
    if per <= 5 and per >= -5:
        result_y = per ** 2
    elif per < -5:
        result_y = 2 * abs(per) - 1
    elif per > 5:
        result_y = per * 2
    return result_y


def result():
    """This function will show the result"""

    for num in range(-10,11,1):
        print(f'y= {fun_y(num)}, x= {num}')


if __name__ == "__main__":
    result()
