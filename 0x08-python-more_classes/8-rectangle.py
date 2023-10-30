#!/usr/bin/python3
"""
defines a rectangle classs
"""


class Rectangle:
    """rectangle class definition"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instantiation of a rectabgle"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        """it returns the perimeter field  """
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """it prints rectangle using # charac"""
        if self.__width == 0 or self. __height == 0:
            return ""
        for k in range(self.__height):
            for j in range(self.__width):
                print(Rectangle.print_symbol, end="")
            print()
        return ""

    def __repr__(self):
        """repr methode to allow create new instance  using #"""
        return "Rectangle(" + str(self.__width) +\
            ", " + str(self.__height) + ")"

    def __del__(self):
        """delete a rectangle instancee"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the biggest rect based on area already"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
