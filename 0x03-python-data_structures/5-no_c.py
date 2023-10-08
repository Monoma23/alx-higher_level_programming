#!/usr/bin/python3
"""thiss is a program remove elemnt c of list"""


def no_c(my_string):
    new_lst = [h for h in my_string if h != 'c' and h != 'C']
    return ("".join(new_lst))
