#!/usr/bin/python3
"""Function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file
    Args:
        filename: Name of file
        text: String to write
    Return:
        Number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
