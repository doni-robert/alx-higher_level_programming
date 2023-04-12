#!/usr/bin/python3
""" Defines a from_json_string module"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string

    Args:
        my_str: the string
    Return:
        Returns an object
    """
    return json.loads(my_str)
