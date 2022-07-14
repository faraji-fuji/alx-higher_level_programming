#!/usr/bin/python3
"""Define class Base"""
import json
from turtle import Screen, RawTurtle, done
import random


class Base:
    """
    This class is the “base” of all other
    classes in this project. The goal of it is to manage
    id attribute in all your future classes

    Attributes:
        __nb_objects (int): number of instances
        id (int): id of instance. id if arg passed, __nb_obj otherwise
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init method for class

        Args:
            id (int): id of instance. It's never the same
        """
        if not id:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries:

        Args:
            list_dictionaries (list): list of dictionaries to convert

        return:
            json representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries, skipkeys=True, indent=2)

    @staticmethod
    def from_json_string(json_string):
        """
        gets the python list of the JSON string representation json_string

        Args:
            json_string (json): JSON representation of a list with all
                                the dictionaries

        return:
            (obj): python obj of JSON string
        """

        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string, encoding="utf-8")

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares using turtle module

        Args:
            list_rectangles (list): list of rectangles to draw
            list_squares (list): list of squares to draw
        """

        screen = Screen()
        screen.setup()
        screen.bgcolor("black")
        colors = ["cyan", "red", "blue", "white",
                  "purple", "green", "brown", "#285078"]
        square = RawTurtle(screen)
        rectangle = RawTurtle(screen)
        # square.speed(10)
        # rectangle.speed(10)
        for sq in list_squares:
            square.penup()
            square.home()
            square.color(random.choice(colors))
            square.goto(sq.x, sq.y)
            square.pendown()
            square.begin_fill()
            i = 0
            while i < 4:
                square.forward(sq.size)
                square.left(90)
                i += 1
            square.end_fill()
        square.hideturtle()

        for rect in list_rectangles:
            rectangle.penup()
            rectangle.home()
            rectangle.color(random.choice(colors))
            rectangle.goto(rect.x, rect.y)
            rectangle.pendown()
            i = 0
            while i < 2:
                rectangle.forward(rect.width)
                rectangle.left(90)
                rectangle.forward(rect.height)
                rectangle.left(90)
                i += 1
        rectangle.hideturtle()
        done()
            



        

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:

        list_objs is a list of instances who inherits of Base

        If list_objs is None, save an empty list

        The filename must be: <Class name>.json

        use the static method to_json_string (created before)

        overwrite the file if it already exists
        """

        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_list_dicts = Base.to_json_string(list_dicts)
                file.write(json_list_dicts)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes on dictionary already set

        Args:
            dictionary(dict): dictionary with attributes to be set

        Return:
            (obj): instance with all attributes set
        """

        # create dummy instance to call update
        if cls.__name__ == 'Rectangle':
            instance = cls(5, 5)
        else:
            instance = cls(5)

        # update instance attributes with update method
        instance.update(**dictionary)

        return instance

    @classmethod
    def load_from_file(cls):
        """
        save_to_file writes a list of instance's attributes to a json file.
        This method reads the file, get the python object and creates
        new instances according to each dictionary on the python
        list gotten from the file

        Return:
            (list): list with instances(dicts)
        """

        try:
            filename = '{}.json'.format(cls.__name__)
            with open(filename, encoding="utf-8") as file:
                json_list = file.read()

                dictionaries_list = cls.from_json_string(json_list)
                list_instances = [cls.create(**dictionary)
                                  for dictionary in dictionaries_list]
                return list_instances
        except FileNotFoundError:
            return []
