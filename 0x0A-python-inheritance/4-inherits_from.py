#!/usr/bin/python3
"""thiss is a program returns attributes and methods of an object"""


def inherits_from(obj, a_class):
    """checks if obj is an instance of an
    inherited class of the specified class
    """
    if issubclass(type(obj), a_class) == True and type(obj) != a_class:
        return True
    return False
