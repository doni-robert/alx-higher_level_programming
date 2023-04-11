#!/usr/bin/python3
""" Defines a class Rectangle """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ A class representing a Rectangle """
    def __init__(self, width, height):
        """
        Initialize a new rectangle

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Prints a rectangle description"""
        return "[{}] {}/{}\
                ".format(self.__class__.__name__, self.__width, self.__height)
