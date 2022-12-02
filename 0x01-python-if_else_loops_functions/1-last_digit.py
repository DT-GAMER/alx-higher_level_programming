#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    ldigit = number % 10
else:
    ldigit = number % -10

    print("Last digit of", number, "is", ldigit, end=" ")

    if ldigit > 5:
        print("and is greater than 5")
    elif ldigit == 0:
        print("and is 0")
    elif ldigit < 6:
        print("and is less than 6 and not 0")
