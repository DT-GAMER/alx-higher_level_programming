#!/usr/bin/python3
"""Integer Addition
contains a function for adding integers
"""


def matrix_divided(matrix, div):
    """Divides real number elements of a matrix
    Args:
        matrix: a list of list of integers or float
        div: a divistor number
    Returns:
        A new matrix with the result of the division
    """

    not_matrix = 'matrix must be a matrix (list of lists) of integers/floats'

    # Matrix must be a list, matrix cannot be []
    if not matrix or type(matrix) is not list:
        raise TypeError(not_matrix)

    must_be_eq_size = 'Each row of the matrix must have the same size'
    size = None

    for row in matrix:
        # row must be a list, row cannot be []
        if not row or type(row) is not list:
            raise TypeError(not_matrix)

        # Size of the rows in the matrix must be equal
        if size is not None and size != len(row):
            raise TypeError(must_be_eq_size)

        # Check that each of the elements in row is number
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(not_matrix)

        size = len(row)

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(elem / div, 2) for elem in row] for row in matrix]
