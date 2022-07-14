#!/usr/bin/python3
"""function inherits_from"""


def inherits_from(obj, a_class):
    """Checks is an obj is instance of a class that inherited from the a_class

    Args:
        obj (obj): obj to be evaluated
        a_class (class): instance of obj

    Returns:
        True if it's instance, False otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
