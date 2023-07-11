#!/usr/bin/python3
"""
Module for the function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Determine if obj is an instance of a class that inherited
    directly or indirectly from a_class.
    Args:
        obj: An object
        a_class: The class
    Returns:
        True if obj is an instance otherwise False
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
