#!/usr/bin/python3
"""
Module composed by a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', ':' characters
    Args:
        text: given string
    Return:
        No return
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    for delim in ['.', '?', ':']:
        arr = text.split(delim)
        arr = [x.strip(" ") for x in arr]
        text = (delim + '\n\n').join(arr)

    print(text, end='')
