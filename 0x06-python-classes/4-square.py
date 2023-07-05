#!/usr/bin/python3
"""
Define a class Square
"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Create a private class instance size
        Args:
            size: the size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """Return size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of the square
        Args:
            value: size of the square
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """Return the area of the square"""
        size = self.__size
        return size * size
