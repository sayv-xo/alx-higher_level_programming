#!/usr/bin/python3
"""Write into a text file"""


def write_file(filename="", text=""):
    """
    Writes a string into a text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)
    return count
