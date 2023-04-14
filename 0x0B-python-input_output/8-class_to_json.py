#!/usr/bin/python3

"""Defines a function that returns dictionary desc for JSON of obj"""


def class_to_json(obj):
    """Returns dictionary decsription with simple data structure for
        JSON serialization of an object
    Args:
        obj: instance of a class
    """

    return obj.__dict__
