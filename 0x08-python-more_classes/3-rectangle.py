#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a rectangle with height and width"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of rectangle"""
        height = self.__height
        width = self.__width
        if height == 0 or width == 0:
            return 0
        return 2 * height + 2 * width

    def __str__(self):
        """Defines string representation of rectangle"""
        string = ""
        height = self.__height
        width = self.__width
        if height != 0 and width != 0:
            string = '\n'.join(['#' * width] * height)
        return string
