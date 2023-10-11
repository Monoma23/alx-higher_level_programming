#!/usr/bin/python3
"""thiss is a program calculate squares of matrix"""


def search_replace(my_list, search, replace):
    other_list = my_list.copy()
    for e in range(len(other_list)):
        if other_list[e] == search:
            other_list[e] = replace
    return other_list
