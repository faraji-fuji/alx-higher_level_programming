#!/usr/bin/python3
""" Write a class Square that defines a square """


class Square:
    """ Defines a Square.

    Attributes:
        __size (int): Size of square.

    """
    def __init__(self, size=0):
        """ Assign attributes with the args passed

        Args:
            size (int): size of square

        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns Square's area"""
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
