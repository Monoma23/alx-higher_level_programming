#!/usr/bin/python3
"""
defines a rectangle classs
"""


class Rectangle:
    """rectangle class def"""

    def __init__(self, width=0, height=0):
        """instantiation of rect"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve width field"""
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
        """returns  perimeter field"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """print rectangle using # characterr"""
        if self.__width == 0 or self. __height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
        return ""

    def __repr__(self):
        """repr method that allow create new instance using #"""
        return "Rectangle(" + str(self.__width) +\
            ", " + str(self.__height) + ")"

    def __del__(self):
        """delete a rectangle wlasss see you"""
        print("Bye rectangle...")
