#!/usr/bin/python3
"""thiss is a program returns attributes and methods of an object"""


def is_same_class(obj, a_class):
    """checks if object is instance of class"""
    if type(obj) == a_class:
        return True
    return False
