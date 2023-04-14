#!/usr/bin/python3

"""Defines function that reads a text file"""


def read_file(filename=""):

    """Returns content of file read to stdout
    Args:
        filename: text file to be opened and read from
    """
    with open(filename, encoding="utf-8") as myFile:
        content = myFile.read()
        print(content, end="")
