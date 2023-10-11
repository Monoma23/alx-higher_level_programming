#!/usr/bin/python3
"""thiss is a program calculate squares of matrix"""


def square_matrix_map(matrix=[]):
    return (list(map(lambda line: list(map(lambda colonne: colonne**2, line)), matrix)))
