#!/usr/bin/python3
"""
This module contains a class BaseGeometry
"""


class BaseGeometry:
    """Defines a class BaseGeometry"""
    def area(self):
        """Raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the argument value.
        Raises TypeError if value is not an int
        Raises ValueError if value is less than 1
        Args:
            name(str): Name
            value(int): Value
        """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value < 1:
            raise ValueError(f'{name} must be greater than zero')
