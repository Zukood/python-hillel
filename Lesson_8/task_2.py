import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def calculate_area(self):
        side1 = math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)
        side2 = math.sqrt((self.point3.x - self.point2.x) ** 2 + (self.point3.y - self.point2.y) ** 2)
        side3 = math.sqrt((self.point1.x - self.point3.x) ** 2 + (self.point1.y - self.point3.y) ** 2)
        semiperimeter = (side1 + side2 + side3) / 2
        area = math.sqrt(semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3))
        return area


class Square:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def calculate_area(self):
        side = math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)
        area = side ** 2
        return area


# Пример
point1 = Point(0, 0)
point2 = Point(0, 4)
point3 = Point(3, 0)

triangle = Triangle(point1, point2, point3)
triangle_area = triangle.calculate_area()
print(triangle_area)  # Вывод: 6.0

square = Square(point1, point2)
square_area = square.calculate_area()
print(square_area)  # Вывод: 16.0
