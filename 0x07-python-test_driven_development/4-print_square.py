#!/usr/bin/python3
"""print_square module"""


def print_square(size):
    """
    Function that prints a square with the character '#'

    Args:
        size(int): The size length of the square

    Raises:
        TypeError: if size is not an integer, if size is a\
            float and size is less than 0
        ValueError: if size is less than 0
    """
    if not isinstance(size, int) or (not isinstance(size, float)
            and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for k in range(size):
            print("#", end="")
        print()
