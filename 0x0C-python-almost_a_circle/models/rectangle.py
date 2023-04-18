#!/usr/bin/python3
""" Define a class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ A class representing a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new rectangle

        Args:
            width: The width of the new rectangle
            height: The height of the new rectangle
            x: The horizontal position of the rectangle
            y: The vertical position of the rectangle
            id(int): The id of the new rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Gets the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width to be value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Gets the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height to be value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gets the x position of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x position to be value """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets the y position of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y position to be value """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance """
        return self.width * self.height

    def display(self):
        """ Prints to stdout the Rectangle instance with the character # """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ Prints a rectangle description"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Updates the attributes """
        list_attr = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Returns the dictionary representation of a rectangle """
        list_attr = ['id', 'width', 'height', 'x', 'y']
        to_dict = {}
        for attr in list_attr:
            to_dict[attr] = getattr(self, attr)
        return to_dict
