#!/usr/bin/python3

"""Defines a class that raises an  exception"""


class BaseGeometry():

    """Raises an exception to indicate not implemented"""

    def area(self):
        raise Exception("area() is not implemented")

    """Raise exceptions at validation error"""

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
