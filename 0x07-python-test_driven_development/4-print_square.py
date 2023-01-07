#!/usr/bin/python3
"""Print Square Module
"""


def print_square(size):
    """Prints a square with the character '#'
    Args:
        size (int): the size length of the square
    Return: nothing
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
