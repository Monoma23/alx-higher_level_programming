#!/usr/bin/python3
"""class student"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict representation of Student"""
        if type(attrs) == list and all(type(el) == str for el in attrs):
            return {w: getattr(self, w) for w in attrs if hasattr(self, w)}
        return self.__dict__
