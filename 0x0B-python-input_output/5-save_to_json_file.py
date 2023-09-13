#!/usr/bin/python3
"""Write object to a file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file using JSON rep"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
