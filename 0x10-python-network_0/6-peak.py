#!/usr/bin/python3
"""finding peakk"""


def find_peak(list_of_integers):
    """Return the lowest peakk from a list."""
    if list_of_integers == []:
        return None

    sizze = len(list_of_integers)
    if sizze == 1:
        return list_of_integers[0]
    elif sizze == 2:
        return max(list_of_integers)

    midd = int(sizze / 2)
    peakk = list_of_integers[midd]
    if peakk > list_of_integers[midd - 1] and peakk > list_of_integers[midd + 1]:
        return peakk
    elif peakk < list_of_integers[midd - 1]:
        return find_peak(list_of_integers[:midd])
    else:
        return find_peak(list_of_integers[midd + 1:])
