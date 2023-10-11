#!/usr/bin/python3
"""thiss is a program calculate squares of matrix"""


def multiply_by_2(a_dictionary):
    nouveau_dict = a_dictionary.copy()
    keysList = list(nouveau_dict.keys())

    for k in keysList:
        nouveau_dict[k] *= 2
    return (nouveau_dict)
