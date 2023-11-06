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

    def area(self):
        """implementing area funct"""
        return self.__width * self.__height

    def __str__(self):
        """return string"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)


class Square(Rectangle):
    """this square class inherit from Rectangle"""
    def __init__(self, size):
        """Square constructor"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of square"""
        return self.__size * self.__size

    def __str__(self):
        """return string"""
        return '[Square] {}/{}'.format(self.__size, self.__size)
