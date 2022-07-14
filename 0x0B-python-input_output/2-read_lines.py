#!/usr/bin/python3
"""defines function to read n lines of a file"""


def read_lines(filename="", nb_lines=0):
    """Function to read n lines

    Args:
        filename (str): file to be read
        nb_lines (int): number of lines to read

    """

    with open(filename, mode="r", encoding="utf-8") as a_file:
        if nb_lines <= 0:
            print(a_file.read(), end="")
        else:
            for i in range(nb_lines):
                print(a_file.readline(), end="")
