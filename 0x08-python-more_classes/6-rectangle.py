#!/usr/bin/python3
"""
defines a rectangle classs
"""


class Rectangle:
    """rectangle class definition"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """instantiation off a rectangmz"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieve width field"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width field """
        self.__width = value
        try:
            assert type(self.__width) == int
        except BaseException:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """retrieve height vfield"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets heigh fieldt"""
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
        """print rectangle using # chara"""
        if self.__width == 0 or self. __height == 0:
            return ""
        for k in range(self.__height):
            for w in range(self.__width):
                print("#", end="")
            print()
        return ""

    def __repr__(self):
        """repr meth to allooww create new instance of rec using #"""
        return "Rectangle(" + str(self.__width) +\
            ", " + str(self.__height) + ")"

    def __del__(self):
        """delete a rectangle instance yo"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
