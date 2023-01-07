#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test suite for max_integer function
    """
    def test_function(self):
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
    
    def test_one_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_neg(self):
        self.assertEqual(max_integer([-3, -1, -10, -2]), -1)

    def test_large_list(self):
        self.assertEqual(max_integer([
            3245, 323232, 2132323, 3233, 221,
            21323, 32323, 3323, 54545, 323, 23,
            3233, 7566, 43434, 42434, 45, 324, 3]), 2132323)

    def test_very_large_values(self):
        self.assertEqual(max_integer([
            float("inf"), 8903283926, 89892382683283
            ]), float("inf"))

    def test_very_small_values(self):
        self.assertEqual(max_integer([
            float("-inf"), 0, -1
            ]), 0)

    def test_empty_list(self):
        self.assertNotEqual(max_integer([]), 0)
        self.assertEqual(max_integer([]), None)

    def test_empty_args(self):
        self.assertEqual(max_integer(), None)

    def test_string(self):
        self.assertEqual(max_integer(['C', 'is', 'fun']), 'is')

    def test_string_arg(self):
        self.assertEqual(max_integer('PyIsFun'), 'y')

    def test_number_arg(self):
        with self.assertRaises(TypeError):
            max_integer(1)
            max_integer(-1)

    def test_tuple_arg(self):
        self.assertEqual(max_integer((0, 1, 2, 3)), 3)

    def test_tuple_in_list_arg(self):
        with self.assertRaises(TypeError):
            max_integer([0, (0, )])
