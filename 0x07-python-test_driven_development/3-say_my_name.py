#!/usr/bin/python3
"""
This module prints ...
"""


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first name> <last name>"
    Args:
    """
    msg = "{} must be a string"

    if type(first_name) is not str:
        raise TypeError(msg.format("first_name"))

    if type(last_name) is not str:
        raise TypeError(msg.format("last_name"))

    print("My name is {} {}".format(first_name, last_name))
