#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple_a = tuple_a[:]
    new_tuple_b = tuple_b[:]
    if len(tuple_a) > 2:
        new_tuple_a = tuple_a[:2]
    if len(tuple_a) == 1:
        new_tuple_a = tuple_a + (0,)
    if len(tuple_a) == 0:
        new_tuple_a = tuple_a + (0, 0)
    if len(tuple_b) > 2:
        new_tuple_b = tuple_b[:2]
    if len(tuple_b) == 1:
        new_tuple_b = tuple_b + (0,)
    if len(tuple_b) == 0:
        new_tuple_b = tuple_b + (0, 0)
    a, b = new_tuple_a
    c, d = new_tuple_b
    e = a + c
    f = b + d
    tuple_c = e, f
    return tuple_c
