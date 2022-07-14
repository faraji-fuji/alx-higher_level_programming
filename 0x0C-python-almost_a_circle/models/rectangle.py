#!/usr/bin/python3
"""Defines class Rectangle who inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """
    Class that inherits from base. It defines a Rectangle

    Attributes:
        __width (int): width of rectangle
        __height (int): height of rectangle
        __x (int): x position
        __y (int): y position
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init for rectangle class. It initializes the super class(base)
        with id so the Base class manage it

        Args:
            width (id): width value of attr
            height (id): height value of attr
            x (id): x value of attr
            y (id): y value of attr
            id (int): id to be passed to super class
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        Printable form of class
        """

        args = (self.id, self.__x, self.__y, self.__width, self.__height)
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(*args)

    # Setters and getters for all attributes
    @property
    def width(self):
        """
        getter for width

        Setter validates it's integer and not 0 or less
        """

        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            Rectangle.raise_typeError('width')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        """
        getter for height

        Setter validates it's integer and not 0 or less
        """

        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            Rectangle.raise_typeError('height')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def x(self):
        """
        getter for x

        Setter validates it's integer and not less than 0
        """

        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            Rectangle.raise_typeError('x')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        """
        getter for x

        Setter validates it's integer and not less than 0
        """

        if not isinstance(y, int):
            Rectangle.raise_typeError('y')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """
        calculates the area of a rectangle

        Return:
            area (int): width * height

        """

        return self.__width * self.__height

    def display(self):
        """
        print to stdout the instance with the char #
        based on the width (columns) and height (rows)

        x and y can be also used to move the rectangle
        in x (horizontal) and y (vertical) position

        >>> r1 = Rectangle(5,5)
        >>> r1.display()
        #####
        #####
        #####
        #####
        #####

        >>> r1 = Rectangle(5, 5, 2, 2)
        >>> r1.display()
        <BLANKLINE>
        <BLANKLINE>
          #####
          #####
          #####
          #####
          #####
        """

        # Moves the rectangle in y position
        for y in range(self.__y):
            print("")
        # Lines to be printed
        for line in range(self.__height):
            # moves the rectangle in x position
            for x in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                # prints the rectangle
                print("#", end="")
            # Jumps to the other line
            print("")

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute

        Args:
            args (obj): list of arguments
        """
        if args:
            attributes = ('id', 'width', 'height', 'x', 'y')
            attributes = list(zip(attributes, args))
            for attr, value in attributes:
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a rectangle
        Contain:

        id
        width
        height
        x
        y
        """

        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}

    # static methods
    @staticmethod
    def raise_typeError(attribute):
        """
        Method to raise TypeError when value is not
        instance of int.

        Args:
            attribute (str): attribute that couldn't be set
        """

        raise TypeError('{} must be an integer'.format(attribute))
