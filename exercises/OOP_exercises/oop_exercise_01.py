# Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return math.pi * self.radius**2

    def Perimeter(self):
        return 2 * math.pi * self.radius


radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print("Area:", circle.Area())
print("Perimeter:", circle.Perimeter())
