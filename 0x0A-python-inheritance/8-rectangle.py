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
