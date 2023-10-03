#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating upper- and lower-case."""
k = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - k)), end="")
    k = 32 if k == 0 else 0
