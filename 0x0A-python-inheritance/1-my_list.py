#!/usr/bin/python3
"""Defines a class MyList"""


class MyList(list):
    """ A class representing MyList"""

    def __init__(self):
        """ Initialize a new MyList"""
        list.__init__(self)

    def print_sorted(self):
        """ Prints a sorted list """
        print(sorted(self))
