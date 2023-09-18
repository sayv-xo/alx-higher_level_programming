#!/usr/bin/python3
"""Base class for all other classes"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialiaze the class
        Args:
            id: Class ID
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects