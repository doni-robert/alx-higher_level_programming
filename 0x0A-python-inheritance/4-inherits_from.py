#!/usr/bin/python3
""" Defines inherits_from module """


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance a class that inherited directly or
        indirectly from the specified class

    Args:
        obj: the object to examine
        a_class: the specified class

    Return:
        True if the object is an instance, False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
