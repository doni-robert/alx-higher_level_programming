#!/usr/bin/python3
"""Defines a lookup module"""


def lookup(obj):
    """
    The function returns the list of available attributes and
        methods of an object

    Args:
        obj: the object in question

    Returns:
        a list of available attributes and methods
    """
    return dir(obj)
