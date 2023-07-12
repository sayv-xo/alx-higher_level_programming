#!/usr/bin/python3
"""Save to JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text string, using JSON representation
    Args:
        my_obj: Python object to write to
        filename: Name of file to write to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
