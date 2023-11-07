#!/usr/bin/python3
"""python files task 1"""


def append_write(filename="", text=""):
    """append to a file"""
    with open(filename, encoding="utf-8", mode="a+") as file:
        return file.write(text)
