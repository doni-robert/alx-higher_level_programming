#!/usr/bin/python3
""" Defines is_same_class module """


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class

    Args:
        obj: the object to examine
        a_class: the specified class

    Return:
        True if the object is an instance, False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
