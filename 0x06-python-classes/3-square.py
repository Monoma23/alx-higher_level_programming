#!/usr/bin/python3
"""
empty modules
"""


class Square:
    """
    square class with a size init and some exceptions
    """

    def __init__(self, size=0):
        self.__size = size
        try:
            assert type(size) == int
        except(TypeError):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ the area of a square"""
        return self.__size ** 2
