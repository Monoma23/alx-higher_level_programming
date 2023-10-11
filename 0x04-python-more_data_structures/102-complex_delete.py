#!/usr/bin/python3
"""thiss is a program calculate squares of matrix"""


def complex_delete(a_dictionary, value):
    keyList = list(a_dictionary.keys())
    for k in keyList:
        if a_dictionary[k] == value:
            del a_dictionary[k]
    return (a_dictionary)
