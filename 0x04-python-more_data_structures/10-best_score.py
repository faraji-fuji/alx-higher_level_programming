#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary):
        key_list = sorted(a_dictionary)
        return key_list[-1]
    else:
        return None
