#!/usr/bin/python3
"""thiss is a program remove elemnt c of list"""


def divisible_by_2(my_list=[]):
    objectiff = []
    for k in range(len(my_list)):
        if my_list[k] % 2 == 0:
            objectiff.append(True)
        else:
            objectiff.append(False)

    return (objectiff)
