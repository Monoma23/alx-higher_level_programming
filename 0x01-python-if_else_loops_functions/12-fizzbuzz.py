#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    """Prints the numeros from 1 to 100 separé by a space

    For multiples of 3, print Fizz insteadd of the numero
    For multiples of 5, print Buzz insteadd of the numero
    For multiples of 5 and 3, prints FizzBuzz insteadd of the numero
    """
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print("FizzBuzz ", end="")
		elif numero % 5 == 0:
            print("Buzz ", end="")	
        elif numero % 3 == 0:
            print("Fizz ", end="")
        else:
            print(f"{numero}", end="")

