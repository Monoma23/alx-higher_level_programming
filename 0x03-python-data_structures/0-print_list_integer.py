#!/usr/bin/python3
"""thiss is a program that prints ints of lists """


def print_list_integer(my_list=[]):
    for w in range(len(my_list)):
        print("{:d}".format(my_list[w]))
