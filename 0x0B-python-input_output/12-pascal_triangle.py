#!/usr/bin/python3
"""defines a function to print pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s
    triangle of n:

    Args:
        n (int): number of lines of triangle

    Return:
        (list): list of lists with corresponding
        val
    """

    new_list = []
    if n <= 0:
        return new_list
    else:
        for index in range(n):
            new_list.append([])
            if index == 0:
                new_list[index].append(1)
            else:
                previous_list = new_list[index - 1]
                current_list = new_list[index]
                for i, number in enumerate(previous_list):
                    if i == 0:
                        current_list.append(1)
                    else:
                        current_integer = previous_list[i]
                        previous_integer = previous_list[i - 1]
                        new_integer = current_integer + previous_integer
                        current_list.append(new_integer)
                current_list.append(1)
        return new_list
