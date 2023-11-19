from abc import ABC, abstractmethod
from typing import List
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return (self.base * self.height) / 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


class AreaCalculator:

    def __init__(self, shapes: List[Shape]):
        if not isinstance(shapes, list):
            raise AssertionError('`shapes` should be of type `list`.')

        self.shapes = shapes

    @property
    def total_area(self):

        return sum(s.calculate_area() for s in self.shapes)


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
