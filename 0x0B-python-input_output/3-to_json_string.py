#!/usr/bin/python3
""" Defines a to_json_string module"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object file

    Args:
        my_obj: the object
    Return:
        Returns the JSON representation
    """
    return json.dumps(my_obj)
