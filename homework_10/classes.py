# Создать класс Point, описывающий точку(атрибуты: x,y). Создать класс Figure. Создать три дочерних класса
# Circle(атрибуты: координаты центра(тип Point), радиус; методы: нахождение периметра и площади
# окружности), Triangle(атрибуты: три точки, методы: нахождение площади и периметра), Square(атрибуты:
# две точки, методы: нахождение площади и периметра). При необходимости, создавать все
# необходимые методы, не описанные в задании. Создать список фигур и в цикле подсчитать и вывести
# площади всех фигур на экран в формате: «Тип фигуры» -> «площадь».
from abc import ABC,abstractmethod
from typing import Union

class Point:
    """this class describes the point"""
    def __init__(self, x: Union[int, float], y: Union[int, float]):
        self.x = x
        self.y = y

class Figure(ABC):
    """this class describes a figure

    class contains abstract methods:
    calc_perimetr - perimeter calculation
    calc_square - square calculation
    info_perimetr - displaying information about the perimeter
    info_square - displaying information about the square
    """
    @abstractmethod
    def calc_perimetr(self):
        pass

    @abstractmethod
    def calc_square(self):
        pass

    @abstractmethod
    def info_perimetr(self):
        perimetr = self.calc_perimetr()
        print('perimetr = %s' % (perimetr))

    @abstractmethod
    def info_square(self):
        square = self.calc_square()
        print('square = %s' %(square))

class Circle(Figure):
    """this class describes a Circle

    class contains methods:
    calc_perimetr - perimeter calculation
    calc_square - square calculation
    info_perimetr - displaying information about the perimeter
    info_square - displaying information about the square
    """
    def __init__(self, center: Point, r: Union[int, float]):
        self.center = center
        self.r = r

    def calc_perimetr(self) -> Union[int, float]:
        if self.r > 0:
            perimetr = 2 * 3.14 * self.r
            return perimetr
        return 'radius must be greater than 0'


    def calc_square(self) -> Union[int, float]:
        if self.r > 0:
            square = 3.14 * self.r ** 2
            return square
        return 'radius must be greater than 0'

    def info_perimetr(self):
        perimetr = self.calc_perimetr()
        print('Circle = %s' % (perimetr))

    def info_square(self):
        square = self.calc_square()
        print('Circle -> %s' %(square))

class Triangle(Figure):
    """this class describes a Triangle

    class contains methods:
    calc_perimetr - perimeter calculation
    calc_square - square calculation
    info_perimetr - displaying information about the perimeter
    info_square - displaying information about the square
    """
    __len_katet_ab = None
    __len_katet_ab = None
    __len_katet_ca = None
    __p_perimetr = None
    def __init__(self, vertex_a: Point, vertex_b: Point, vertex_c: Point):
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b
        self.vertex_c = vertex_c
        Triangle.__len_katet_ab = ((self.vertex_b.x - self.vertex_a.x) ** 2 + (self.vertex_b.y - self.vertex_a.y) ** 2) ** 0.5
        Triangle.__len_katet_bc = ((self.vertex_c.x - self.vertex_b.x) ** 2 + (self.vertex_c.y - self.vertex_b.y) ** 2) ** 0.5
        Triangle.__len_katet_ca = ((self.vertex_a.x - self.vertex_c.x) ** 2 + (self.vertex_a.y - self.vertex_c.y) ** 2) ** 0.5

    def calc_perimetr(self) -> Union[int, float]:
        perimetr = Triangle.__len_katet_ab + Triangle.__len_katet_bc + Triangle.__len_katet_ca
        return perimetr

    def calc_square(self) -> Union[int, float]:
        Triangle.__p_perimetr = (Triangle.__len_katet_ab + Triangle.__len_katet_bc + Triangle.__len_katet_ca) / 2
        square = (Triangle.__p_perimetr * ((Triangle.__p_perimetr - Triangle.__len_katet_ab) *
            (Triangle.__p_perimetr - Triangle.__len_katet_bc) * (Triangle.__p_perimetr - Triangle.__len_katet_bc))) ** 0.5
        return square

    def info_perimetr(self):
        perimetr = self.calc_perimetr()
        print('Triangle = %s' % (perimetr))

    def info_square(self):
        square = self.calc_square()
        print('Triangle -> %s' %(square))

class Square(Figure):
    """this class describes a Square

    class contains methods:
    calc_perimetr - perimeter calculation
    calc_square - square calculation
    info_perimetr - displaying information about the perimeter
    info_square - displaying information about the square
    """
    __side = None
    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b
        Square.__side = ((self.point_b.x - self.point_a.x) ** 2 + (self.point_b.y - self.point_a.y) ** 2) ** 0.5

    def calc_perimetr(self) -> Union[int, float]:
        perimetr = Square.__side * 4
        return perimetr

    def calc_square(self) -> Union[int, float]:
        square = Square.__side * 2
        return square

    def info_perimetr(self):
        perimetr = self.calc_perimetr()
        print('Square = %s' % (perimetr))

    def info_square(self):
        square = self.calc_square()
        print('Square -> %s' %(square))







