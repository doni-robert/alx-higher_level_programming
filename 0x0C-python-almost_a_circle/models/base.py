#!/usr/bin/python3
""" Define a class Base """
import json


class Base:
    """ A class representing a base """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a neew base

        Args:
            id(int): The id of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation

        Args:
            list_dictionaries(list): a list of dictionaries
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes a JSON string representation of list_objs to a file

        Args:
            cls(class): the class name of the object
            list_objs(list): a list of instances who inherits of Base
        """
        pass
