#!/usr/bin/python3
"""
    function display something
"""


def say_my_name(first_name, last_name=""):
    """
        print name full reciproque of user
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    if first_name == "" and last_name == "":
        return None
    print("My name is {} {}".format(first_name, last_name))
