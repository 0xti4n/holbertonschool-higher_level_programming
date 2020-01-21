#!/usr/bin/python3
"""function that returns the number
of lines of a text file
"""


def number_of_lines(filename=""):
    """function"""
    with open(filename, mode="r") as f:
        number = 0
        while True:
            line = f.readline()
            if not line:
                break
            number += 1
        return number
