#!/usr/bin/python3
import random
number = random.randint(-10000, 1000)
last_digitt = abs(number) % 10
if number < 0:
    last_digitt = -last_digitt
if last_digitt > 5:
    print(f"Last digit of {number} is {last_digitt} and is greater than 5")
elif last_digitt == 0:
    print(f"Last digit of {number} is {last_digitt} and is 0")
else:
    print(f"Last digit of {number} is {last_digitt} and is less than 6 and not 0")
