#!/usr/bin/python3

"""Defines function that appends a text file"""


def append_write(filename="", text=""):

    """Returns number of characters added
    Args:
        filename: text file to be opened and written to
        text: content to added to file
    """
    with open(filename, mode='a+', encoding="utf-8") as myFile:
        numOfChar = myFile.write(text)
        return numOfChar
