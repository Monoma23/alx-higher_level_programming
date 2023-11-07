#!/usr/bin/python3
"""class student"""


def pascal_triangle(n):
    """presentatin of tr pascal trianngle"""
    if n <= 0:
        return []
    tr = [[] for w in range(n)]
    for w in range(n):
        for k in range(w + 1):
            if k < w:
                if k == 0:
                    tr[w].append(1)
                else:
                    tr[w].append(tr[w - 1][k] + tr[w - 1][k - 1])
            elif k == w:
                tr[w].append(1)
    return tr
