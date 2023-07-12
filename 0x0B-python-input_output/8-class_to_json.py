#!/usr/bin/python3
"""Return dict repr"""


def class_to_json(obj):
    """Return dict representation of simple data structure"""
    return vars(obj)
