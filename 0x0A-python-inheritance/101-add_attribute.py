#!/usr/bin/python3
"""add new attribute if possible"""


def add_attribute(obj, attr_name, attr_value):
    """add att if possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
