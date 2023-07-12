#!/usr/bin/python3
"""Create object from JSON file"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        obj = json.load(f)
    return obj
