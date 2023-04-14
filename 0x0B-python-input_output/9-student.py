#!/usr/bin/python3

"""Defines a class Student"""


class Student:
    """Instantiation with first_name, last_name and age"""

    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name: the first name of object
            last_name: the last name of object
            age: the age of object
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Defines a function that returns dictionary desc for JSON of obj"""

    def to_json(self):
        """Returns dictionary decsription with simple data structure for
            JSON serialization of an object
        Args:
            obj: instance of a class
        """

        return self.__dict__
