#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for elem in new_list:
        if elem == search:
            new_list[my_list.index(elem)] = replace
    return new_list
