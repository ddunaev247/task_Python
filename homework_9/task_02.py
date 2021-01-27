# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по умолчанию 0). Методы:
# увеличить скорости(скорость + 5), уменьшение скорости(скорость - 5), стоп(сброс скорости на 0),
# отображение скорости, разворот(изменение знака скорости). Все атрибуты приватные.

class Car:
    def __init__(self, brand, model, release_date, speed = 0) -> None:
        self.__brand = brand
        self.__model = model
        self.__release_date = release_date
        self.__speed = speed

    def increase(self, speed:int):
        """this method will increase speed by +5"""
        self.__speed = speed + 5

    def decrease(self, speed:int):
        """this method will reduce the speed by -5"""
        self.__speed = speed -5

    def slow(self, speed:int):
        """this method will zero the speed"""
        self.__speed = speed * 0

    def print_speed(self):
        """this method will output the speed to the screen"""
        print(self.__speed)

    def reverse_speed(self):
        """this method will change the sign of speed"""
        self.__speed *= -1

def main():
    tesla = Car('Tesla', 'Model S', 2019, 130)
    tesla.increase(133)
    tesla.print_speed()
    tesla.decrease(133)
    tesla.print_speed()
    tesla.slow(122)
    tesla.print_speed()
    tesla.increase(133)
    tesla.reverse_speed()
    tesla.print_speed()

if __name__ == '__main__':
    main()





