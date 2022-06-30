#!/usr/bin/python3
"""Define a function that adds to integers"""


def add_integer(a, b=98):
    """Function to return the add of two integers

    Args:
        a (int): first integer
        b (int): second integer. )8 by default

    Returns:
        int: computed value (a + b)

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
