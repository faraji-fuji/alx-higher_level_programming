#!/usr/bin/python3
""" defines a function to create an obj from JSON str"""
import json


def load_from_json_file(filename):
    """creates an obj from a json file

    Args:
        filename (str): json file

    Returns:
        (obj): obj created from JSON file

    """

    with open(filename, encoding="utf-8") as a_file:
        return json.load(a_file)
