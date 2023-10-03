#!/usr/bin/python3
# 8-uppercase.py


def uppercase(str):
    """convert string in uppercase"""
    for w in str:
        if ord(w) >= 97 and ord(w) <= 122:
            w = chr(ord(w) - 32)
        print(f"{w}", end="")
    print("")

