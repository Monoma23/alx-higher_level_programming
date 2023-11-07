#!/usr/bin/python3
"""python files task 1"""


def read_file(filename=""):
    """Read from a file"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
