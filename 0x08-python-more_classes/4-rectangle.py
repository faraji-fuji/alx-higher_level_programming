#!/usr/bin/python3
"""Defines an empty class Rectangle"""


class Rectangle:
    """Class defininf a Rectangle obj

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle

    """

    def __init__(self, width=0, height=0):
        """Initi method

        Args:
            width (int): value to set width
            height (int): value to set height

        """

        self.width = width
        self.height = height

    def __str__(self):
        """Returns a printable and nice string"""

        if self.__width == 0 or self.__height == 0:
            return ""

        string = ""
        for row in range(self.__height):
            for column in range(self.__width):
                string += "#"
            if row != (self.__height - 1):
                string += "\n"
        return string

    def __repr__(self):
        """Return a string representation of rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """getter method for width"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """returns rectangle permiter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width*2) + (self.__height*2)
