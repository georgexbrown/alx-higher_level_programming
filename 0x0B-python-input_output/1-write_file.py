#!/usr/bin/python3

"""Defines function that writes to  a text file"""


def write_file(filename="", text=""):

    """Returns number of characters written
    Args:
        filename: text file to be opened and written to
        text: content to write to file
    """
    with open(filename, mode='w', encoding="utf-8") as myFile:
        numOfChar = myFile.write(text)
        return numOfChar
