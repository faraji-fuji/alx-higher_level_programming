#!/usr/bin/python3
"""defines a function to return number of lines of a text file"""


def number_of_lines(filename=""):
    """function to return number of lines
    of a file

    Args:
        filename (str): file to be read

    Returns:
       (int): number of lines
    """
    counter = 0
    with open(filename, mode="r", encoding="utf-8") as a_file:
        for line in a_file:
            counter += 1
        return (counter)
