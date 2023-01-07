#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            end = ""
            if i < len(row) - 1:
                end = " "
            print("{:d}".format(num), end=end)
        print()
