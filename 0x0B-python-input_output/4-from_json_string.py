#!/usr/bin/python3
"""JSON to string object"""
import json


def from_json_string(my_str):
    """Return an object represented by JSON string"""
    return json.loads(my_str)
