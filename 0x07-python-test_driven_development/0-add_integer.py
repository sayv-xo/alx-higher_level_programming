#!/usr/bin/python3
"""
This is the "0-add_integer" module

The module has one function, add_integer(). For example,
>>> add_integer(1, 68)
69
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Float arguments are casted to integer before addition is performed

    Args:
        a(int or float): Int or float to add
        b(int): Default argument with value of 98

    Raises:
        TypeError if either a or b is not int or float

    Returns:
        The sum of a and b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
