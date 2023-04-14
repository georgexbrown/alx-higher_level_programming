#!/usr/bin/python3
"""This module defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file
    """
    text = ""
    with open(filename) as myFile:
        for line in myFile:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as myFile2:
        myFile2.write(text)
