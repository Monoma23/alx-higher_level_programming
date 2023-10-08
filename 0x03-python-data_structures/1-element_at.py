#!/usr/bin/python3
"""thiss is a program retrieves elemnt of list"""


def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        return (my_list[idx])
