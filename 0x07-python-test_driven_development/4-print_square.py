#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size (int): size of square

    Returns:
        prints the square

    Raises:
        TypeError: if size is not an integer or if it's a float
        ValueError: if size < 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
