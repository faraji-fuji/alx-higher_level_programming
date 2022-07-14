#!/usr/bin/python3
"""function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Checks is an obj is instance of a_class or it's parent

    Args:
        obj (obj): obj to be evaluated
        a_class (class): instance of obj

    Returns:
        True if it's instance, False otherwise
    """

    return True if isinstance(obj, a_class) else False
