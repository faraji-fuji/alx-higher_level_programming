#!/usr/bin/python3
"""
defines a function that returns the dictionary description of
an obj
"""


def class_to_json(obj):
    """ function to get the dict with all attributes of obj

    Args:
        obj (obj): class to get attributes from

    Returns:
        (dict): dictionary with all attributes

    """

    return obj.__dict__
