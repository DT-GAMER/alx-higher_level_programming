#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    first_sum = 0
    second_sum = 0

    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a += (0,)

    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b += (0,)

    first_sum += tuple_a[0] + tuple_b[0]
    second_sum += tuple_a[1] + tuple_b[1]
    return (first_sum, second_sum)
