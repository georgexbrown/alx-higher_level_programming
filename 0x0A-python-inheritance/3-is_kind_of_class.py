#!/usr/bin/python3

"""
Defines a function that determines is object is an instance of
    a class that inherited
"""


def is_kind_of_class(obj, a_class):
    """Returns True/False to confirm is an instance or not
    Args:
        obj: object to check
        a_class: class to be compared with
    """

    if isinstance(obj, a_class):
        return True
    return False
