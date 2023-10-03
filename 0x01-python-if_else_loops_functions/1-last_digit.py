#!/usr/bin/python3
import random
number = random.randint(-10000, 1000)
last_digitt = abs(number) % 10
if number < 0:
    last_digitt = -last_digitt
if last_digitt > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digitt))
elif last_digitt == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digitt))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digitt))
