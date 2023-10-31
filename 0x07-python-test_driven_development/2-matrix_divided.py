#!/usr/bin/python3
"""
    divides elements of matrix
"""


def matrix_divided(matrix, div):
    """
        build a new matrix with elements divided
    """

    mynouvellematrx = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for h in matrix:
        if len(h) != len(matrix[0]):
            raise TypeError("Each h of the matrix must have the same size")
        transpose = []
        for element in h:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            element = round(element / div, 2)
            transpose.append(element)
        mynouvellematrx.append(transpose)
    return mynouvellematrx
