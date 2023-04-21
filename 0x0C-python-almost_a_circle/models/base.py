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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes a JSON string representation of list_objs to a file

        Args:
            cls(class): the class name of the object
            list_objs(list): a list of instances who inherits of Base
        """
        list_dic = []
        if list_objs is None:
            json_string = []
        else:
            for obj in list_objs:
                list_dic.append(obj.to_dictionary())
            json_string = obj.to_json_string(list_dic)
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation

        Args:
            json_string: a string representing dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all the attributes already set

        Args:
            cls: The class of the instance
            dictionary: key value pair arguments of attributes
        """
        if dictionary is not None:
            if cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        if not filename:
            return []
        with open(filename) as f:
            read_file = f.read()
            list_dic = cls.from_json_string(read_file)
            list_objs = [cls.create(**dic) for dic in list_dic]
            return list_objs
