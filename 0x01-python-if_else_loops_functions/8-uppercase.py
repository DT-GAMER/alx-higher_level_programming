#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        if ord(letters) >= ord('a') and ord(letters) <= ord('z'):
            letters = chr(ord(letters) - 32)
    print("{:s}".format(letters), end="")
    print()
