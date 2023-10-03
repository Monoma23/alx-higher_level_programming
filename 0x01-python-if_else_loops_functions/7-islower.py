#!/usr/bin/python3
# 7-islower.py


def islower(c):
    """let's check for lowercase chars"""
    if ord(c) <= 122 and ord(c) >= 97:
        return True
    else:
        return False
