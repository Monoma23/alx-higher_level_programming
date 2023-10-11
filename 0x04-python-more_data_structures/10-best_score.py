#!/usr/bin/python3
"""thiss is a program calculate squares of matrix"""


def best_score(a_dictionary):
    if not a_dictionary:
        return None

    nice_key = max(a_dictionary, key=lambda k: a_dictionary[k])
    return nice_key
