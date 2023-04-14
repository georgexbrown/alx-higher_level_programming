#!/usr/bin/python3

"""Defines function that returns JSON rep of object"""
import json


def to_json_string(my_obj):

    """Returns JSON representation of object (string)
    Args:
        my_obj: object to view its json string rep
    """
    stringRep = json.dumps(my_obj)
    return stringRep
