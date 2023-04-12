#!/usr/bin/python3

"""
Defines a function that determines is object is an instance of a class
"""


def is_same_class(obj, a_class):
    """Returns boolean to confirm is an instance
    Args:
        obj: object to check
        a_class: class to be compared with
    """

    if type(obj) == a_class:
        return True
    return False
