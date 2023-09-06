#!/usr/bin/python3
"""
This module contains 'add_integer' function
"""


def add_integer(a, b=98):
    """
    Function that adds two integer or float numbers

    Args:
        a: first number
        b: second number

    Returns:
        The sum of given arguments

    Raises:
        TypeError: If a or b isn't integer or float number
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
