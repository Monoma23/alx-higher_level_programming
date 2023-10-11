#!/usr/bin/python3
"""thiss is a program calculate squares of matrix"""


def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerateur = 0
    denominateur = 0

    for tiple in my_list:
        numerateur += tiple[0] * tiple[1]
        denominateur += tiple[1]
    return (numerateur / denominateur)
