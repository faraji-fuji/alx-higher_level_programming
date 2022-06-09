#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_list = sorted(a_dictionary)
    new_dict = {}
    for elem in my_list:
        new_dict[elem] = a_dictionary[elem]
    for k, v in new_dict.items():
        print("{}: {}".format(k, v))
