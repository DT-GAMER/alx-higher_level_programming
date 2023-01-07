#!/usr/bin/python3

def no_c(my_string):
    llist = []
    for letter in my_string:
        if letter not in "cC":
            llist.append(letter)
    return "".join(llist)
