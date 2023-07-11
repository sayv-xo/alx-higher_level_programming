#!/usr/bin/python3
"""
This module contains a class Square that inherits from the
subclass Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square thaat inherits from class Rectangle"""
    def __init__(self, size):
        """
        Instantiation of the square
        Args:
            size(int): Size of the square
        """
        super().__init__(size, size)
