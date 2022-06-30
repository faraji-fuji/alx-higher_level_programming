#!/usr/bin/python3
"""defines a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """divides all the elements of a matrix

    Args:
        matrix (list): list of lists containing the integer to be divided
        div (int): divisor

    Returns:
        list: new matrix containing the results

    Raises:
        TypeError: if element's or div's type is different than int or floats,
                   Each row must be of the same size
        ZeroDivisionError: if div eq 0

"""

    new_matrix = []
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix is None:
        raise TypeError(matrix_error)

    if not isinstance(matrix, list):
        raise TypeError(matrix_error)

    if len(matrix) == 0:
        raise TypeError(matrix_error)

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_error)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        sub_list = []
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(matrix_error)
            sub_list.append(round((el / div), 2))
        new_matrix.append(sub_list)
    return new_matrix
