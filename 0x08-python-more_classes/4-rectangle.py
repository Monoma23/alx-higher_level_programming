#!/usr/bin/python3
"""
defines a rectangle class
"""


class Rectangle:
    """rectangle class definit"""

    def __init__(self, width=0, height=0):
        """instantiation of rectangle """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve width field """
        return self.__width

    @property
    def height(self):
        """retrieve height field """
        return self.__height

    @width.setter
    def width(self, value):
        """sets width field"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height field"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area field"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter field"""
        perimeter = 0
        if self.__height is not 0 or self.__width is not 0:
            perimeter = self.__width * 2 + self.__height * 2
        return perimeter

    def __str__(self):
        """print rectangle using # character"""
        sttrg_ = ""
        if self.__width == 0 or self. __height == 0:
            return ""
        for h in range(self.__height):
            if h < (self.__height - 1):
                sttrg_ += ("#" * self.__width) + "\n"
            else:
                sttrg_ += ("#" * self.__width)
        return sttrg_

    def __repr__(self):
        """repr attribute methd that allow create new instance with #"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
