#!/usr/bin/python3
"""
function to return available methods and attr
"""


def lookup(obj):
    """
    uses dir to get all the available methods and attributes
    available not only on the obj but its parent and ancestors
    too

    Args:
        obj (obj): obj to pass to dir fun

    returns:
        list: list of methods and attr
    """

    return dir(obj)
