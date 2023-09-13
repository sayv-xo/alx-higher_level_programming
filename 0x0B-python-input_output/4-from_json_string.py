#!/usr/bin/python3
"""Return object represented by JSON string"""
import json


def from_json_string(my_str):
    """Returns an object represented by JSON string
    Args:
        my_str: JSON String
    Returns:
        object
    """
    return json.loads(my_str)
