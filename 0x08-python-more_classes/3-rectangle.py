#!/usr/bin/python3
"""
defines a rectangle with private att
"""


class Rectangle:
    """rectangle class def"""
    def __init__(self, width=0, height=0):
        """instantiation of rzctangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve width data"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width field"""
        self.__width = value
        try:
            assert type(self.__width) == int
        except BaseException:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """retrieve height field"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height field"""
        self.__height = value
        try:
            assert type(self.__height) == int
        except BaseException:
            raise ValueError("height must be >= 0")

    def area(self):
        """returns the area field"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter field"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """print rectangle using # character"""
        if self.__height == 0 or self.__width == 0:
            return ""
        for w in range(self.__height):
            for k in range(self.__width):
                print("#", end="")
            if w != self.__height - 1:
                print()
        return ""
