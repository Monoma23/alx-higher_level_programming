#!/usr/bin/python3
if __name__ == "__main__":
    """Printt somme of all arguments yoo"""
    import sys

    somme = 0
    for k in range(len(sys.argv) - 1):
        somme += int(sys.argv[k + 1])
    print("{}".format(somme))
