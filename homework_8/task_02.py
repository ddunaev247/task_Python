# Создать универсальный декоратор, который меняет порядок аргументов в функции на противоположный.

def my_decor(func):
    def wrapper(*args):
        return func(*args[::-1]) #reverse order of arguments
    return wrapper


@my_decor
def fun_arg(*args):
    """this function takes an unlimited number of arguments and returns them"""

    return args

if __name__ == "__main__":
    print(fun_arg(5, 7, 6 ))
