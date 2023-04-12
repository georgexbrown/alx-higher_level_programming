#!/usr/bin/python3

"""Defines a subclass MyList from a superclass list"""


class MyList(list):
    """Implement ascending sort for the list class"""

    def print_sorted(self):
        """Print a sorted list in ascending order"""
        print(sorted(self))
