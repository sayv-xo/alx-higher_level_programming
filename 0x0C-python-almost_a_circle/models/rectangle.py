#!/usr/bin/python3
"""
A class Rectangle that inherits from thr Base class
"""
from base import Base


class Rectangle(Base):
    """
    Defines a class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the rectangle

        Arguments:
            width (int): The width
            height (int): The height
            x (int): x coordinate
            y (int): y coordinate
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
