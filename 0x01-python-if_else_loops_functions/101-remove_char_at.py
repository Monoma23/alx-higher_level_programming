#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(str, n):
    """creer une copie of the str without character in position n."""
    if n < 0:
        return (str)
    return (str[0:n] + str[n+1:])

