#!/usr/bin/python3
"""
A class that inherit a list.
Public instance method `print_sorted` to print the list
in ascending order.
"""


class MyList(list):
    """
    MyList inherits a list.
    Args:
        list: The list to inherit
    """
    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
