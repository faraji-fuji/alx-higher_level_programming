#!/usr/bin/python3
"""module for class BaseGeometry"""


class BaseGeometry():
    """
    defines a method to raise an exception
    """

    def area(self):
        """
        raise an exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
