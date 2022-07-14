#!/usr/bin/python3
""" defines function to append text"""


def append_write(filename="", text=""):
    """function to append text a file

    Args:
        filename (str): file to be written
        text (str): text to be append

    Returns:
        (int): chars added

    """

    with open(filename, mode="a", encoding="utf-8") as a_file:
        chars = a_file.write(text)
    return chars
