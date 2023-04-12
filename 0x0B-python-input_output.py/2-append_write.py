#!/usr/bin/python3
""" Defines an append_write module"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file

    Args:
        filename(str): the file to be added to
        text(str): the text to be added

    Return:
        Returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
