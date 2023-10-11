#!/usr/bin/python3
"""thiss is a program calculate squares of matrix"""


def square_matrix_simple(matrix=[]):
    result = []

    for ligne in matrix:
        new_row = []
        for value in ligne:
            new_row.append(value ** 2)
        result.append(new_row)

    return result
