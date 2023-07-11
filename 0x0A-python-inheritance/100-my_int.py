#!/usr/bin/python3
"""A stubborn class"""


class MyInt:
    """A class MyInt"""
    def __eq__(self, other):
        """Reverse true"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Reverse false"""
        return int(self) == int(other)
