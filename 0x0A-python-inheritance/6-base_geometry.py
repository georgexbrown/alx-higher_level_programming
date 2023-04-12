#!/usr/bin/python3

"""Defines a class that raises an  exception"""


class BaseGeometry():

    """Raises an exception to indicate not implemented"""

    def area(self):
        raise Exception("area() is not implemented")
