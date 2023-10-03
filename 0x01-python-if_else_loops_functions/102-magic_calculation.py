#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(a, b, c):
    """adapte to the bytecode given on the taskk"""
    if a < b:
        return (c)
    if b > c:
        return (a + b)
	else:
        return (a * b - c)
