#!/usr/bin/python3.5
"""
Matrix Module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices
    Args:
        m_a (list): given matrix a
        m_a (list): given matrix b
    Return:
        list: A matrix, the product of m_a and m_b
    """

    return (np.matmul(m_a, m_b))
