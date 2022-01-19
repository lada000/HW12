from math import pi

class Point:
    def __init__(self, x , y):
        self._x = x
        self._y = y

class Figure():
    def __init__(self, x):
        self.cord = x

class Circle(Figure):
    def __init__(self, x, rad_len):
        super().__init__(x)
        self._rad_len = rad_len

    def get_perimeter(self):
        perimeter = 2 * pi * self._rad_len
        return perimeter

    def get_area(self):
        area = pi * self._rad_len**2
        return area

class Triange(Point, Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

    def get_perimeter(self):
        print(self._x)

a = Point(3, 5)
a1 = Point(2, 4)
a2 = Point(5, 8)
b = Circle(a, 10)
c = Triange(2, 4)
c.get_perimeter()
