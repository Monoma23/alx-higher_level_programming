#!/usr/bin/python3
"""thiss is a program remove elemnt c of list"""


def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
