#!/usr/bin/python3
""" Defines is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of the specified class or of an
        inherited class of the specified class

    Args:
        obj: the object to examine
        a_class: the specified class

    Return:
        True if the object is an instance, False otherwise
    """
    return isinstance(obj, a_class)
