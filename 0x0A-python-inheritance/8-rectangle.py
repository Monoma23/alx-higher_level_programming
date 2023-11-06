#!/usr/bin/python3
"""Rectangle class"""


class BaseGeometry:
    """not empty"""
    def area(self):
        """just simply raising exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """child of BaseGeometry"""
    def __init__(self, width, height):
        """constructorr"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
