#!/usr/bin/python3
""" Write a class Square that defines a square """


class Square:
    """ Defines a Square.

    Attributes:
        __size (int): Size of square.

    """
    def __init__(self, size=0, position=(0, 0)):
        """ Assign attributes with the args passed

        Args:
            size (int): size of square
            position (obj): 2 positiv integers

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        msg = "position must be a tuple of 2 positive integers"
        if len(position) != 2:
            raise TypeError(msg)
        for i in position:
            if not isinstance(i, int) or i < 0:
                raise TypeError(msg)
        self.__position = position

    def area(self):
        """Returns Square's area"""
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for bl in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for l in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
