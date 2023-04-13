#!/usr/bin/python3
""" Defines a class_to_json module """


def class_to_json(obj):
    """
    Returns a dictionary description with simple data structure for JSON 
        serialization of an object

    Args:
        obj: the python object

    Return:
        A dictionary description with simple data structure for JSON 
        serialization of an object
    """
    return obj.__dict__


