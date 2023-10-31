#!/usr/bin/python3
""" 
    tests start
"""


def add_integer(a, b=98):
    """
        add two ints with some type conditions
    """
    try:
        assert type(a) in (int, float)
    except:
        raise TypeError("a must be an integer")
    try:
        assert type(b) in (int, float)
    except:
        raise TypeError("b must be an integer")
    if(type(a) == float):
        a = int(a)
    if(type(b) == float):
        b = int(b)
    return a+b
