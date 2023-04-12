#!/usr/bin/python3

"""Importing super class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


"""Defining the sub class Square to inherit Rectangle"""


class Square(Rectangle):

    """Module instantiation with size"""

    def __init__(self, size):
        """Validating and privatizing size

        Args:
            size(int): both length and width of square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
