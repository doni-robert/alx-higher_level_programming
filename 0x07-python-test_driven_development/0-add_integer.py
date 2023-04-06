#!/usr/bin/python3
""" Add integer module"""


def add_integer(a, b=98):
    """
    Adds 2 integers

    Args:
        a (int or float): The first parameter
        b (int or float): The second parameter

    Returns:
        The sum of the two integers

    Raises:
        TypeError: if parameters not a or b
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int): 
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
