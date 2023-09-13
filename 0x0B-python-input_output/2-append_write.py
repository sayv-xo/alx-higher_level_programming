#!/usr/bin/python3
"""Function that appends string to end of a file"""


def append_write(filename="", text=""):
    """Appends string to end of a txt file
    Args:
        filename: Name of file
        text: String to append
        Return: Number of chars added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
