#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {}".format(number), end="")
if number < 0:
    number = -number
last = number % 10
if last == 0:
    print(" is 0 and is 0")
elif last > 5:
    print(" is {} and is greater than 5".format(last))
else:
    print(" is {} and is less than 6 and not 0".format(last))
