#!/usr/bin/python3
"""This module define file-writing function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8).

    Return: The number of characters written.
    """
    with open(filename, "w", encoding="utf=8") as f:
        return f.write(text)
