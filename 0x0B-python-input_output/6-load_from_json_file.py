#!/usr/bin/python3
""" Defines a load_from_json_file module"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Args:
        filename(str): the JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
