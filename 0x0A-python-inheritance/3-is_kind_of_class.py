#!/usr/bin/python3
"""
Determine if an object is an instance of the a_class argument,
or of a subclass of the a_class argument
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance or subclass of a_class.
    Args:
        obj: The object
        a_class: The class to check
    Returns:
        True if obj is an instance of, or a subclass of a_class
        Otherwise False
    """
    return isinstance(obj, a_class)
