#!/usr/bin/python3
"""adds all arguments to a python list, and save them to a file"""
import json
from sys import argv


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
filename = "add_item.json"

try:
    a_list = load_from_json_file(filename)
except Exception as e:
    a_list = []

for arg in argv[1:]:
    a_list.append(arg)

save_to_json_file(a_list, filename)
