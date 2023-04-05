#!/usr/bin/python3
""" Define a class rectangle """


class Rectangle:
    """ A class representing a rectangle. """

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width as value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height as value"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints a representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return
        for h in range(self.__height):
            for w in range(self.__width):
                print("#", end="")
            print()
        return ("")
