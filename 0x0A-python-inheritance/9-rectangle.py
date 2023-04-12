#!/usr/bin/python3

"""Imports the super class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Defines a sub class"""


class Rectangle(BaseGeometry):

    """Module instantiation with width and height"""

    def __init__(self, width, height):
        """Validating and privatizing width and height
        Args:
            width(int): width of object
            height(int): height of object
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of class Rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Returns rectangle description for printing"""

        return "[{}] {}/{}".format(
                self.__class__.__name__, self.__width, self.__height)
