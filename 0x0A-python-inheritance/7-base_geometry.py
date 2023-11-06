#!/usr/bin/python3
"""thiss is a program returns attributes and methods of an object"""


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
