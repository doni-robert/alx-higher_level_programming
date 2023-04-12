#!/usr/bin/python3
""" Defines a write_file module"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
        filename(str): the file to be written to
        text(str): the text to be written

    Return:
        Returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
