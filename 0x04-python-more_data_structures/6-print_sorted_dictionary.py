#!/usr/bin/python3
"""thiss is a program calculate squares of matrix"""


def print_sorted_dictionary(a_dictionary):
    ordred_keys = sorted(a_dictionary.keys())
    for key in ordred_keys:
        print("{}: {}".format(key, a_dictionary[key]))
