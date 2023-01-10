#!/usr/bin/python3
"""This module defines text reading function"""


def read_file(filemame=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding="utf=8") as f:
        print(f.read(), end="")
