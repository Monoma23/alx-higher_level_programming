#!/usr/bin/python3
"""thiss is a program remove elemnt c of list"""


def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            print("{:d}".format(y), end=" " if y != x[-1] else "")
        print()
