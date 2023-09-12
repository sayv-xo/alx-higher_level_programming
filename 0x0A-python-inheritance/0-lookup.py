#!/usr/bin/python3
"""This module contains a function to return attributes
and methods of an object"""


def lookup(obj):
    """Function to return a list of attributes and methods of an object
    Args:
        obj: The object
    Returns:
        List of available attributes and objects
    """
    return dir(obj)
