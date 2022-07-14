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

        if self.integer_validator("width", width) is None:
            self.__width = width
        if self.integer_validator("height", height) is None:
            self.__height = height

    def __str__(self):
        """returns the string representation of the object. This method is
        called when print() or str() function is invoked on an object."""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Calculates the area of a rectangle"""

        return self.__width * self.__height
