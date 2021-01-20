# Создать декоратор для функции, которая принимает список чисел. Декоратор должен производить
# предварительную проверку данных - удалять все четные элементы из списка.

def my_decor(func)
    def wrapper(l_num):
        return func([i for i in l_num if i % 2]) #filtering a list of numbers
    return wrapper


@my_decor
def f_accepts_list_num(list_num: list) -> list:
    """this function takes a list of numbers and returns it

    Input
    -----
    list of numbers

    Result
    ------
    list of numbers
    """
    return list_num

if __name__ == "__main__":
    print(f_accepts_list_num([22,11,0,8,5,118]))
