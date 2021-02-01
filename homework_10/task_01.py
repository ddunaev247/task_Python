# Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы: переопределить магические методы
# сравнения(==, !=, >=, <=, <, >), сложения, вычитания, умножения на число, вывод на экран.

from typing import Union

class MyTime:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other: int) -> Union[int, float]:
       return self.hours == other

    def __ne__(self, other: int) -> Union[int, float]:
        return self.seconds != other

    def __ge__(self, other: int) -> Union[int, float]:
        if isinstance(other, MyTime):
            return self.hours >= other.hours
        elif isinstance(other, (int, float)):
            return self.hours >= other
        else:
            raise TypeError

    def __le__(self, other: int) -> Union[int, float]:
        if isinstance(other, MyTime):
            return self.hours <= other.hours
        elif isinstance(other, (int, float)):
            return self.hours <= other
        else:
            raise TypeError

    def __lt__(self, other: int) -> Union[int, float]:
        if isinstance(other, MyTime):
            return self.hours < other.hours
        elif isinstance(other, (int, float)):
            return self.hours < other
        else:
            raise TypeError

    def __gt__(self, other: int) -> Union[int, float]:
        if isinstance(other, MyTime):
            return self.hours > other.hours
        elif isinstance(other, (int, float)):
            return self.hours > other
        else:
            raise TypeError

    def __add__(self, other: int) -> Union[int, float]:
        if isinstance(other, MyTime):
            return self.seconds + other.seconds
        elif isinstance(other, (int, float)):
            return self.seconds + other
        else:
            raise TypeError

    def __sub__(self, other: int) -> Union[int, float]:
        if isinstance(other, MyTime):
            return self.seconds - other.seconds
        elif isinstance(other, (int, float)):
            return self.seconds - other
        else:
            raise TypeError

    def __mul__(self, other: int) -> Union[int, float]:
        if isinstance(other, MyTime):
            return self.seconds * other.seconds
        elif isinstance(other, (int, float)):
            return self.seconds * other
        else:
            raise TypeError

    def __str__(self) -> str:
        return "It's ok"

def main():
    a = MyTime(12,60,10)
    b = MyTime(14,3,30)
    try:
       print(a == b, a != 13, a + b)
       print(a)
    except TypeError:
        print('use the correct type int, float or object of the MyTime class')

if __name__ == '__main__':
    main()


