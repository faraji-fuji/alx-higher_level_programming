#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new_list = set(my_list)
    for elem in new_list:
        sum += int(elem)
    return sum