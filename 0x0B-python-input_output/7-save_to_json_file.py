#!/usr/bin/python3
"""defines a function to write a JSON repr of an obj"""
import json


def save_to_json_file(my_obj, filename):
    """Writes the JSON string of the obj to a file

    Args:
        my_obj (obj): obj to be parsed to JSON string
        filename (str): file to be written

    """

    with open(filename, mode="w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
