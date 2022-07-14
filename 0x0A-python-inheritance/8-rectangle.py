#!/usr/bin/python3
"""contains class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that defines a rectangle

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle

    """

    def __init__(self, width, height):
        """
        init method for class

        Args:
            width (int): width to be set
            height (int): height to be set
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
