#!/usr/bin/python3
"""
Determine if an object is same class as the one specified
"""


def is_same_class(obj, a_class):
    """
    Determine if object is exactly an instance of the specified
    class.
    Args:
        obj: The object to test
        a_class: The class to compare with
    Returns:
        True is obj is exactly an instance otherwise False
    """
    return True if type(obj) is a_class else False
