#!/usr/bin/python3
"""A class Student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialise the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves representation of student"""
        return vars(self)
