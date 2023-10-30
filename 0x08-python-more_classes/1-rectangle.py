#!/usr/bin/python3
"""
Defines a rectancle nice encapsulation
"""


class Rectangle:
    """rectangle class def """
    def __init__(self, width=0, height=0):
        """Instantia of w and h"""
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
        """revaeal data w"""
        return self.__width

    @property
    def height(self):
        """revaeal data h"""
        return self.__height

    @width.setter
    def width(self, value):
        """set the  height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the data of  height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
