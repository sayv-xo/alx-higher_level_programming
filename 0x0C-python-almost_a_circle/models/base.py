#!/bin/usr/python3
"""Defines a model class Base"""
import csv
import json
import turtle


class Base:
    """
    Defines a class Base
    Private Class Attributes:
        __nb_object (int): Number of instances of Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base
        Args:
            id (int): The identity of the new Base
        """
        if id:
            self.id = id
        else:

            Base.__nb_objects += 1
            self.id = Base.__nb_objects
