#!/usr/bin/python3

"""Defines function that creates object from a JSON file"""
import json


def load_from_json_file(filename):

    """Creates an object from a JSON file
    Args:
        filename: JSON file to deserialize
    """
    with open(filename, mode='r', encoding="utf-8") as myFile:
        myObj = json.load(myFile)
        return myObj
