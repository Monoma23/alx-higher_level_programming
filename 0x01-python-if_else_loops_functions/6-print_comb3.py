#!/usr/bin/python3
# 6-print_comb3.py

"""Afficher all possible differents combinations _2 digits in ascend order.

    The two digits must be abslotly different
    """
for chiffre_1 in range(0, 10):
    for chiffre_2 in range(chiffre_1 + 1, 10):
        if chiffre_1 == 8 and chiffre_2 == 9:
            print("{}{}".format(chiffre_1, chiffre_2))
        else:
            print("{}{}".format(chiffre_1, chiffre_2), end=", ")
