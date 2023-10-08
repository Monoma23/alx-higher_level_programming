#!/usr/bin/python3
"""thiss is a program retrieves elemnt of list"""


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for j in my_list:
        print("{:d}".format(j)
