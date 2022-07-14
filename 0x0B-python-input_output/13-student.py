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

    def to_json(self, attrs=None):
        """
        retrieves the dict of Student instance
        if attrs is a list of strs, then it returns only the attributes names
        contained in the list

        Args:
            attrs (list): list with the name of the attribues

        Returns:
            (dict): dictionary containing the attrs
        """

        if attrs is not None:
            if isinstance(attrs, list):
                if all(isinstance(attr, str) for attr in attrs):

                    # using filter function

                    # new_dict = dict(filter(lambda ele: elem[0] in attrs,
                    # self.__dict__.items()))

                    # using dict comprehension

                    new_dict = {k: v for k, v in self.__dict__.items()
                                if k in attrs}

                    # using for's

                    # for attr in attrs:
                    # if attr in self.__dict__.keys():
                    #  new_dict[attr] = self.__dict__[attr]
        else:
            new_dict = self.__dict__

        return new_dict

    def reload_from_json(self, json):
        """replace all attrs of the instance with the ones within the json

        Args:
            json (dict): dictionary containing all the attributes to replaces

        """

        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
