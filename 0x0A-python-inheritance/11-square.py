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
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns description of square"""
        return f'[Square] {self.__size}/{self.__size}'
