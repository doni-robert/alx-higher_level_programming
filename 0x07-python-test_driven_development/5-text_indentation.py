#!/usr/bin/python3
""" text_indentation module"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of\
            these characters ., ? and :

    Args:
        text(str): The original text

    Raises:
        TypeError: if text is not a string
    """
    string = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for c in text:
        string += c
        if c == '.' or c == '?' or c == ':':
            print(string.strip())
            print()
            string = ""
    print(string.strip(), end="")
