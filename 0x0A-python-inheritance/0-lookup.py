#!/usr/bin/python3
"""
Function that retuns list of all available methods
and attributes of an object
"""


def lookup(obj):
    """
    Returns lists of available attributes and
    methods of an object.
    Arg:
        obj: The object to lookup
    Returns:
        A list object
    """
    return dir(obj)
