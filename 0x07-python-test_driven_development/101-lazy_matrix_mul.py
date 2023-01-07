#!/usr/bin/python3
"""Module lazy_matrix_mul"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """matrix_mul
        Args: m_a, m_b
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')
    if not isinstance(m_a[0], list):
        raise TypeError('m_a must be a list of lists')
    if not isinstance(m_b[0], list):
        raise TypeError('m_b must be a list of lists')

    for i in range(len(m_a)):
        for j in range(len(m_a[i])):
            if not isinstance(m_a[i][j], (int, float)):
                raise TypeError('m_a should contain only integers or floats')

    for w in range(len(m_b)):
        for z in range(len(m_b[w])):
            if not isinstance(m_b[w][z], (int, float)):
                raise TypeError('m_b should contain only integers or floats')

    width_m_a = set([len(k) for k in m_a])
    if len(width_m_a) != 1:
        raise TypeError('each row of m_a must be of the same size')
    width_m_b = set([len(k) for k in m_b])
    if len(width_m_b) != 1:
        raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    return numpy.matrix(m_a) * numpy.matrix(m_b)

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
