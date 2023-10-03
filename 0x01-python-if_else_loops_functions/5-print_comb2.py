#!/usr/bin/python3
for nbre in range(0, 100):
    if nbre == 99:
        print("{}".format(nbre))
    else:
        print("{:02}".format(nbre), end=", ")
