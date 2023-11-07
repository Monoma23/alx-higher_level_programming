#!/usr/bin/python3
"""python files task 1"""


def write_file(filename="", text=""):
    """write to a file"""
    with open(filename, encoding="utf-8", mode="w+") as file:
        return file.write(text)
