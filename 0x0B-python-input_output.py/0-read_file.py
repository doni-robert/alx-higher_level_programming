#!/usr/bin/python3
""" Defines a read_file module """


def read_file(filename=""):
    """
    Reads a textfile and prints it to stdout

    Args:
        filename(str): the file to be read
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
