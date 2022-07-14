#!/usr/bin/python3
"""module for Student"""


class Student:
    """class that defines a student

    Attr:
        first_name (str): name of student
        last_name (str): last name of student
        age (int): student age

    """

    def __init__(self, first_name, last_name, age):
        """
        init method for student

        Args:
            first_name (str): name of student
            last_name (str): last name of student
            age (int): student age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves the dict of Student instance
        """

        return self.__dict__
