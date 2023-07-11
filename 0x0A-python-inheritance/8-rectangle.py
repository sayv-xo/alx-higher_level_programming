#!/usr/bin/python3
"""
This module contains a class that inherits from class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from class BaseGeometry"""
    def __init__(self, width, height):
        """
        Instatiate Rectangle with width and height
        Args:
            width(int): The width
            height(int): The height
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
