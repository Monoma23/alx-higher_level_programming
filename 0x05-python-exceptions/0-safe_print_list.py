#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nbr_printed = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            nbr_printed += 1
        except IndexError:
            break
    print("")
    return nbr_printed
