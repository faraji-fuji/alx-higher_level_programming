#!/usr/bin/python3
"""contains class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that defines a square

    Attributes:
        size (int): size of square

    """

    def __init__(self, size):
        """
        init method for class

        Args:
            size (int): size to be set
        """
        if self.integer_validator("size", size) is None:
            self.__size = size

        super().__init__(size, size)

    def area(self):
        """Calculates the area of a square"""

        return self.__size * self.__size
