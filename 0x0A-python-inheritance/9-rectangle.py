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
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a description of rectangle"""
        return f'[Rectangle] {self.__width}/{self.__height}'
