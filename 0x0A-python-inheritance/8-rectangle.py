#!/usr/bin/python3

"""Defines a class that raises an  exception"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Defines a sub class"""


class Rectangle(BaseGeometry):

    """Module instantiation with width and height"""

    def __init__(self, width, height):
        """validating and privatizing width and height"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
