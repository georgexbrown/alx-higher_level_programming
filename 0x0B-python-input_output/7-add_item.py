#!/usr/bin/python3

"""Defines script that adds all arguments imported to a list"""
import sys


"""Taking arguments passed at runtime and
    importing functions
    """
if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        args = load("add_item.json")
    except FileNotFoundError:
        args = []
    args.extend(sys.argv[1:])
    save(args, "add_item.json")
