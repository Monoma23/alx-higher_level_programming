#!/usr/bin/python3
for nbre in range(0, 100):
    if nbre == 99:
        print(f"{nbre}")
    else:
        print(f"{nbre:02}", end=", ")
