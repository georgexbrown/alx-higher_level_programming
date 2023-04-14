#!/usr/bin/python3

"""Defines function that writes object to file via JSON string repr"""
import json


def save_to_json_file(my_obj, filename):

    """Writes object to a text file using JSON string representation
    Args:
        my_obj: object to serialize to file
        filename: text file to be witten
    """
    with open(filename, mode='w', encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
