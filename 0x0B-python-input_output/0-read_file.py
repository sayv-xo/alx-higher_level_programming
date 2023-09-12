#!/usr/bin/python3
"""Function to read a text file"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout
    Args:
        filename: Name of file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
