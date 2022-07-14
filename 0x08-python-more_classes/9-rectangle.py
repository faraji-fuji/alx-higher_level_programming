#!/usr/bin/python3
"""Defines an empty class Rectangle"""


class Rectangle:
    """Class defininf a Rectangle obj

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
        number_of_instances (int): counter of instances created

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initi method

        Args:
            width (int): value to set width
            height (int): value to set height

        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns a printable and nice string"""

        if self.__width == 0 or self.__height == 0:
            return ""

        string = ""
        for row in range(self.__height):
            for column in range(self.__width):
                string += str(self.print_symbol)
            if row != (self.__height - 1):
                string += "\n"
        return string

    def __repr__(self):
        """Return a string representation of rectangle"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @classmethod
    def square(cls, size=0):
        """returns new instance with width == height == size

        Args:
            size (int): value of width and size

        Returns:
            (Rectangle): new instance

        """
        return cls(size, size)

    def area(self):
        """returns rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """returns rectangle permiter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width*2) + (self.__height*2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare the area of two different instances
        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle

        Returns:
            (Rectangle): rectangle with highest area

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1

        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
