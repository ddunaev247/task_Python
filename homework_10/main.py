# Создать класс Point, описывающий точку(атрибуты: x,y). Создать класс Figure. Создать три дочерних класса
# Circle(атрибуты: координаты центра(тип Point), радиус; методы: нахождение периметра и площади
# окружности), Triangle(атрибуты: три точки, методы: нахождение площади и периметра), Square(атрибуты:
# две точки, методы: нахождение площади и периметра). При необходимости, создавать все
# необходимые методы, не описанные в задании. Создать список фигур и в цикле подсчитать и вывести
# площади всех фигур на экран в формате: «Тип фигуры» -> «площадь».

from classes import *

def main():
    try:
        point1 = Point(1, 1)
        point2 = Point(3, 5)
        point3 = Point(2, 2)
        cir = Circle(point1, 5)
        trean = Triangle(point1, point2, point3)
        squar = Square(point2, point3)
        list_figure = [cir, trean, squar]
        for figure in list_figure:
            print(f'{figure.name} - {"%.2f" % figure.calc_square()}')
    except TypeError:
        print('check the values you are passing')

if __name__ == '__main__':
    main()