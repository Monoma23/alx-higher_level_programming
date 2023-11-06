#!/usr/bin/python3
"""thiss is a program returns attributes and methods of an object"""


class MyList(list):
    """inherit from other class"""
    def print_sorted(self):
        """print ordered members of list"""
        print(sorted(self))
