#!/usr/bin/python3
"""
This module contains the function to print a square with the character '#'
"""


def print_square(size):
    """
    Function that prints a square withthe character #

    Args:
        size: size of square to print

    Returns:
        Nothing

    Raises:
        TypeError: if size is not an integer number
        ValueError: if size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
