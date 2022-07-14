#!/usr/bin/python3
"""defines a function to return a JSON repr of an obj"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an
    obj
    """

    return json.dumps(my_obj)
