#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        tuple_c = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
        return tuple_c
    if len(tuple_a) < 2:
        tuple_c = (0, 0) if len(tuple_a) == 0 else (tuple_a[0], 0)
    else:
        tuple_c = tuple_a
    if len(tuple_b) < 2:
        tuple_d = (0, 0) if len(tuple_b) == 0 else (tuple_b[0], 0)
    else:
        tuple_d = tuple_b
    tuple_e = (tuple_c[0] + tuple_d[0], tuple_c[1] + tuple_d[1])
    return tuple_e

