#!/usr/bin/python3
"""defines a function that returns an obj represented by a JSON
string
"""
import json


def from_json_string(my_str):
    """returns an obj represented by a JSON string

    Args:
        my_str (str): JSON string to be parsed

    Returns:
        (obj): python obj
    """

    return json.loads(my_str)
