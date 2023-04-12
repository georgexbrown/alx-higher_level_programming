#!/usr/bin/python3

"""
Defines a function that determines is object is an instance of
    a class that inherited
"""


def inherits_from(obj, a_class):
    """Returns boolean to confirm is an instance
    Args:
        obj: object to check
        a_class: class to be compared with
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
