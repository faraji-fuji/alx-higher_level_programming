#!/usr/bin/python3
"""Defines function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Prints  My name is <first name> <last name>

    Args:
        first_name (str): first name to be printed
        last_name (str): last name to be printed. Empty str by default

    Returns:
        Prints the message formated with the params passed

    Raises:
        TypeError if any of params not str

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
