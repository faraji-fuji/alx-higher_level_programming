#!/usr/bin/python3
"""defines a function to write to a file"""


def write_file(filename="", text=""):
    """writes the text to a file

    Args:
        filename (str): file to be created or overwritted
        text (str): text to be written

    Returns:
        (int): number of chars written

    """

    with open(filename, mode="w", encoding="utf-8") as a_file:
        chars = a_file.write(text)
    return chars
