#!/usr/bin/python3
if __name__ == "__main__":
    """thiss is a program that prints nbr and  list of its arguments. """
    import sys
    nbre_arguments = len(sys.argv) - 1
    if nbre_arguments == 0:
        print("0 arguments.")
    elif nbre_arguments == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[0]))
    else:
        print("{} arguments:".format(nbre_arguments))
        for k in range(nbre_arguments):
            print("{}: {}".format(k + 1, sys.argv[k + 1]))
