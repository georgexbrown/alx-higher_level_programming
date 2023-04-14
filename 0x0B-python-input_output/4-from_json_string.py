#!/usr/bin/python3

"""Defines function that returns object represented by JSON string"""
import json


def from_json_string(my_str):

    """Returns object represented by a JSON string
    Args:
        my_str: JSON string to deserialize
    """
    myObj = json.loads(my_str)
    return myObj
