from abc import ABC,abstractmethod
from typing import Union


class Point:
    """this class describes the point"""
    def __init__(self, x: Union[int, float], y: Union[int, float]):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)


class Figure(ABC):
    """this class describes a figure

    class contains abstract methods:
    calc_perimetr - perimeter calculation
    calc_square - square calculation
    """
    @abstractmethod
    def calc_perimetr(self):
        pass

    @abstractmethod
    def calc_square(self):
        pass


class Circle(Figure):
    """this class describes a Circle

    calc_perimetr - perimeter calculation
    calc_square - square calculation
    >>> a = Point(5,5)
    >>> cir = Circle(a, 5)
    >>> cir.calc_perimetr()
    31.400000000000002
    >>> cir.calc_square()
    78.5
    """

    def __init__(self, center: Point, r: Union[int, float]):
        self.center = center
        self.r = r
        self.name = __class__.__name__

    def calc_perimetr(self) -> Union[float, str]:
        if self.r > 0:
            perimetr = 2 * 3.14 * self.r
            return perimetr
        return 'radius must be greater than 0'


    def calc_square(self) -> Union[float, str]:
        if self.r > 0:
            square = 3.14 * self.r ** 2
            return square
        return 'radius must be greater than 0'


class Triangle(Figure):
    """this class describes a Triangle

    calc_perimetr - perimeter calculation
    calc_square - square calculation

    >>> point1 = Point(1, 1)
    >>> point2 = Point(3, 5)
    >>> point3 = Point(2, 2)
    >>> trean = Triangle(point1, point2, point3)
    >>> trean.calc_perimetr()
    9.048627177541055
    >>> trean.calc_square()
    0.6617700427003875
    """

    def __init__(self, vertex_a: Point, vertex_b: Point, vertex_c: Point):
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b
        self.vertex_c = vertex_c
        self.len_katet_ab = ((self.vertex_b.x - self.vertex_a.x) ** 2 + (self.vertex_b.y - self.vertex_a.y) ** 2) ** 0.5
        self.len_katet_bc = ((self.vertex_c.x - self.vertex_b.x) ** 2 + (self.vertex_c.y - self.vertex_b.y) ** 2) ** 0.5
        self.len_katet_ca = ((self.vertex_a.x - self.vertex_c.x) ** 2 + (self.vertex_a.y - self.vertex_c.y) ** 2) ** 0.5
        self.p_perimetr = (self.len_katet_ab + self.len_katet_bc + self.len_katet_ca) / 2
        self.name = __class__.__name__


    def calc_perimetr(self) -> float:
        perimetr = self.len_katet_ab + self.len_katet_bc + self.len_katet_ca
        return perimetr

    def calc_square(self) -> float:
        square = (self.p_perimetr * ((self.p_perimetr - self.len_katet_ab) *
            (self.p_perimetr - self.len_katet_bc) * (self.p_perimetr - self.len_katet_bc))) ** 0.5
        return square

class Square(Figure):
    """this class describes a Square

    calc_perimetr - perimeter calculation
    calc_square - square calculation

    >>> point2 = Point(3, 5)
    >>> point3 = Point(2, 2)
    >>> squar = Square(point2, point3)
    >>> squar.calc_perimetr()
    12.649110640673518
    >>> squar.calc_square()
    6.324555320336759
    """

    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.side = ((self.point_b.x - self.point_a.x) ** 2 + (self.point_b.y - self.point_a.y) ** 2) ** 0.5
        self.name = __class__.__name__

    def calc_perimetr(self) -> float:
        perimetr = self.side * 4
        return perimetr

    def calc_square(self) -> float:
        square = self.side * 2
        return square


if __name__ == '__main__':
    import doctest
    doctest.testmod()
