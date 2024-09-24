#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    '''Abstract class Shape with abstract methods area and perimeter'''

    @abstractmethod
    def area(self):
        '''function that calculates an area'''
        pass

    @abstractmethod
    def perimeter(self):
        '''function that calculates a perimeter'''
        pass


class Circle(Shape):
    '''Circle class inheriting from Shape and
    implementing area and perimeter'''

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    '''Rectangle class inheriting from Shape and
    implementing area and perimeter'''

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    '''Function that displays the area and perimeter of a geometric Shape'''
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
