#!/usr/bin/python3
"""
    function display something
"""


def print_square(size):
    """
        print a square using character
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for h in range(size):
        for k in range(size):
            print("#", end="")
        print()
