#!/usr/bin/python3
""" Defines a class BaseGeometry """


class BaseGeometry:
    """ A class representing BaseGeometry """
    pass

    def area(self):
        """ Returns the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value

        Args:
            name: a string label of the value
            value: an integer to be validated
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
