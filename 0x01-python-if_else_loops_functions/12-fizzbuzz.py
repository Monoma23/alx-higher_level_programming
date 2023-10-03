#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Print numbers from 1 to 100 separated by a space
    For multiples of 3, print Fizz instead of num
    For multiples of 5, print Buzz instead of num
    For multiples of 5 and 3, print FizzBuzz instead of nbre
    """
    for numeroo in range(1, 101):
        if numeroo % 3 == 0 and numeroo % 5 == 0:
            print("FizzBuzz ", end="")
        elif numeroo % 3 == 0:
            print("Fizz ", end="")
        elif numeroo % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numeroo), end="")
