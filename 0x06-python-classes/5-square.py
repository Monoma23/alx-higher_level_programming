#!/usr/bin/python3
"""
empty modules
"""


class Square:
    """
    square class with a size init and some exceptions
    """
    def __init__(self, size=0):
        """private instance attrib
        parameters
        -------------------------
        size : integer ifnot TypeError o valueError
        """
        self.__size = size

    @property
    def size(self):
        """
        to retrieve
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        to set a private instance attribute
        """
        self.__size = value
        try:
            assert type(value) == int
        except(TypeError):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        public instance method
        returns  square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        print a  sqaure with # syntx
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
