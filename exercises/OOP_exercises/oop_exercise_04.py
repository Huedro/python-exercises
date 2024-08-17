# Write a python program to create a class that represents a shape.
# Include methods to calculate its area and perimeter. Implement subclasses for
# differents shapes like circle, triangle and square.

from abc import ABC, abstractmethod
import math


class Shape:

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ^ 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

    def perimeter(self):
        return self.base * 3


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ^ 2

    def perimeter(self):
        return self.side * 4


print("Circle | Radius = 5")
circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
print()

print("Triangle | Base = 4, Height = 6")
triangle = Triangle(4, 6)
print("Area:", triangle.area())
print("Perimeter:", triangle.perimeter())
print()

print("Square | Sides = 4")
square = Square(4)
print("Area:", square.area())
print("Perimeter:", square.perimeter())
