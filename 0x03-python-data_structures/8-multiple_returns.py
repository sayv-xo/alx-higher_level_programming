#!/usr/bin/python3
"""Return length of string and first character"""


def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
