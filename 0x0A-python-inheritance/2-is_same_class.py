#!/usr/bin/python3
"""function is_same_class"""


def is_same_class(obj, a_class):
    """Checks is an obj is instance of a_class

    Args:
        obj (obj): obj to be evaluated
        a_class (class): instance of obj

    Returns:
        True if it's instance, False otherwise
    """

    return True if type(obj) == a_class else False
