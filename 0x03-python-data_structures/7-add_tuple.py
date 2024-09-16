#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # pad tuple_a with zero to ensure atleast 2 elements
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0

    # pad tuple_b with zero to ensure atleast 2 elements
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    # Add corresponding elements of tuple_a and tuple_b
    result = (a1 + b1, a2 + b2)
    # return result as tuple
    return result
