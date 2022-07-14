#!/usr/bin/python3
"""module for class MyList"""


class MyList(list):
    """
    Class that inherits from List
    """

    def print_sorted(self):
        """
        prints the list but sorted
        """
        sort_list = self[:]
        print(sorted(sort_list))
