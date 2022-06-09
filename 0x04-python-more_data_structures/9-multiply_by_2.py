#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for elem in list(a_dictionary):
        new_dict[elem] = a_dictionary[elem] * 2
    return new_dict
