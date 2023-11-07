#!/usr/bin/python3
"""python files task 1"""
import json


def load_from_json_file(filename):
    """writes  object to a text file"""
    with open(filename, mode="r") as file:
        return json.load(file)
