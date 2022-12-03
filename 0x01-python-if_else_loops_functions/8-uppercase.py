#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        num_eqv = ord(letters)
        if num_eqv >= ord('a') and num_eqv <= ord('z'):
            letters = chr(ord(letters) - 32)
    print("{:s}".format(letters), end="")
    print()
