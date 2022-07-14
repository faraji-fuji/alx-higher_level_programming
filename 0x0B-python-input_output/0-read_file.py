#!/usr/bin/python3
"""contains a function to read a text file"""


def read_file(filename=""):
    """prints the content of a faile

    Args:
        filename (string): file name

    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
