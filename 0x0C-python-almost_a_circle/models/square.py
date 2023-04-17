#!/usr/bin/python3
""" Define a class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class representing a square """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new square

        Args:
            width: The width of the new square
            height: The height of the new square
            x: The horizontal position of the square
            y: The vertical position of the square
            id(int): The id of the new square
        """
        super().__init__(size, size, x, y, id=None)

    @property
    def size(self):
        """ Gets the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets the size as value """
        self.width = value
        self.length = value

    def __str__(self):
        """ Prints a rectangle description"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        """ Updates the attributes """
        list_attr = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Returns the dictionary representation of a square """
        list_attr = ['id', 'size', 'x', 'y']
        to_dict = {}
        for attr in list_attr:
            to_dict[attr] = getattr(self, attr)
        return to_dict
