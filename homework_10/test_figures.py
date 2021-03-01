import unittest
from classes import Point, Figure, Circle, Triangle, Square

class Test_Figures(unittest.TestCase):
    def setUp(self) -> None:
        self.point1 = Point(3,2)
        self.point2 = Point(4,1)
        self.point3 = Point(5,4)
        self.circle = Circle(self.point1,5)
        self.triangle = Triangle(self.point1, self.point2, self.point3)
        self.square = Square(self.point2, self.point3)


    def test_calc_perimetr(self)-> None:
        self.assertEqual(self.circle.calc_perimetr(), 31.400000000000002), 'test not passed'
        self.assertEqual(self.triangle.calc_perimetr(), 7.404918347287666), 'test not passed'
        self.assertEqual(self.square.calc_perimetr(), 12.649110640673518), 'test not passed'


    def test_calc_square(self)-> None:
        self.assertEqual(self.circle.calc_square(), 78.5), 'test not passed'
        self.assertEqual(self.triangle.calc_square(), 1.572302755514848), 'test not passed'
        self.assertEqual(self.square.calc_square(), 6.324555320336759), 'test not passed'


if __name__ == '__main__':
    unittest.main()