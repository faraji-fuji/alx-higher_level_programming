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
