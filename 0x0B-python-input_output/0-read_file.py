#!/usr/bin/python3
"""
This module contains a function to read a file
and print the contents to stdout
"""


def read_file(filename=""):
    """
    Read a text file and print it to stdout
    Args:
        filename: Name of file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
