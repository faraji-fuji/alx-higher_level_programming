#!/usr/bin/python3
""" Declaration of Square class """


class Square():
    """Declare protected attribue"""

    def __init__(self, size):
        """__init__ method to declarate private attr

        Args:
            size (int): size of square

        """
        self.__size = size
