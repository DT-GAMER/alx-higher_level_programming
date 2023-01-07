#!/usr/bin/python3
"""
Matrix Module
"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices
    Args:
        m_a (list): given matrix a
        m_a (list): given matrix b
    Return:
        list: A matrix, the product of m_a and m_b
    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the lists of m_a or m_b don't have integers or floats
        ValueError: if m_a or m_b can't be multiplied
    """

    must_be_a_list = '{} must be a list'

    # Matrices must be a list
    if type(m_a) is not list:
        raise TypeError(must_be_a_list.format("m_a"))

    if type(m_b) is not list:
        raise TypeError(must_be_a_list.format("m_b"))

    must_be_a_list_of_lists = '{} must be a list of lists'

    # Matrices must be a list of lists
    for elem in m_a:
        if type(elem) is not list:
            raise TypeError(must_be_a_list_of_lists.format("m_a"))

    for elem in m_b:
        if type(elem) is not list:
            raise TypeError(must_be_a_list_of_lists.format("m_b"))

    only_contain_int_float = '{} should contain only integers or floats'

    # Matrices must contain only integers and float
    for row in m_a:
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(only_contain_int_float.format("m_a"))

    for row in m_b:
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(only_contain_int_float.format("m_b"))

    must_be_same_size = "each row of {} must be of the same size"

    # Matrices must have row of the same size
    col_a = None
    for row in m_a:
        if col_a is not None and col_a != len(row):
            raise TypeError(must_be_same_size.format("m_a"))
        col_a = len(row)

    col_b = None
    for row in m_b:
        if col_b is not None and col_b != len(row):
            raise TypeError(must_be_same_size.format("m_b"))
        col_b = len(row)

    cant_be_empty = "{} can't be empty"

    # Matrices can't be empty i.e [], or [[]]
    if m_a:
        for elem in m_a:
            if not elem:
                raise ValueError(cant_be_empty.format("m_a"))
    else:
        raise ValueError(cant_be_empty.format("m_a"))

    if m_b:
        for elem in m_b:
            if not elem:
                raise ValueError(cant_be_empty.format("m_b"))
    else:
        raise ValueError(cant_be_empty.format("m_b"))

    # Number of columns in Matrix a but equal number of rows in Matrix b
    if col_a != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    # Transpose b
    m_b_t = [[row[i] for row in m_b] for i in range(col_b)]

    # Multiply m_a and m_b
    return [
        [sum(row[i] * col[i] for i in range(col_a)) for col in m_b_t]
        for row in m_a]
