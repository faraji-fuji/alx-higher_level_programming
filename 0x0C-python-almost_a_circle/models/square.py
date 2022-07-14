#!/usr/bin/python3
"""
defines the class square, who inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that inherits from Rectangle. It defines a Square

    Attributes:
        __x (int): x position
        __y (int): y position
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Init method for class. It calls the super function to initialize
        Rectangle

        The width and height must be assigned to the value of size

        All width, height, x and y validation inherit from Rectangle
        - same behavior in case of wrong data

        Args:
            size (int): width and height of square
            x (int): x position of square
            y (int): y position of square
            id (int): id of square
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Printable form of class
        """

        args = (self.id, self.x, self.y, self.width)
        return '[Square] ({}) {}/{} - {}'.format(*args)

    @property
    def size(self):
        """
        getter for size
        Returns thee width of Rectangle

        setter validates same as Rectangle's attributes
        setter
        sets width and height
        """

        return self.width

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('width must be > 0')
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            4th argument should be the x attribute
            5th argument should be the y attribute

        Args:
            args (obj): list of arguments
        """
        if args:
            attributes = ('id', 'size', 'x', 'y')
            attributes = list(zip(attributes, args))
            for attr, value in attributes:
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square
        Contain:

        id
        size
        x
        y
        """

        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
