#!/usr/bin/python3
"""python files task 1"""
import json


def save_to_json_file(my_obj, filename):
    """writes  object to a text file"""
    with open(filename, mode= "w" ) as file:
        json.dump(my_obj, file)
