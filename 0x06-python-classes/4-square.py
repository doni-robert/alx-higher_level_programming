#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """ A class to represent a square """

    def __init__(self, size=0):
        """
        Initialize a new square

        Args:
            size(int): The size of the new square
        """

        self.size = size

    def area(self):
        """Returns the current square area"""

        return self.__size ** 2

    @property
    def size(self):
        """Gets the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
