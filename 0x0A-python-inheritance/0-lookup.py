#!/usr/bin/python3

"""Defines an object attribute lookup function"""


def lookup(obj):
    """Return a list of an object's available attributes
    Args:
        obj: object to fetch list
    Returns:
        list of available attributes and methods
    """
    return dir(obj)
