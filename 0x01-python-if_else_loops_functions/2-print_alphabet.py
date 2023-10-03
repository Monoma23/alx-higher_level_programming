#!/usr/bin/python3
# 2-print_alphabet.py

"""let's Print alphabets in lowercase, without a new line."""
for w in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(w)), end='')
