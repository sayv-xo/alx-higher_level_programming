#!/usr/bin/python3
"""Appends to a text file"""


def append_write(filename="", text=""):
    """
    Appends string to end of a text file
    Returns:
        number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        count = f.write(text)
    return count
