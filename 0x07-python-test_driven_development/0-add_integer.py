#!/usr/bin/python3
"""Function to add 2 integers
If the num is none, the function returns error
if the type of a is not integer raises an error
if the type of b is not float raises another error
"""


def add_integer(a, b=98):
    """Function to function that adds 2 integers
    If the num is none, the function returns error
    """
    if a:
        if a != a:
            a = 89
        if b != b:
            b = 89
        if a is None or (type(a) is not int and type(a) is not float):
            raise TypeError('a must be an integer')
        if type(b) is not int and type(b) is not float:
            raise TypeError('b must be an integer')
        return int(a) + int(b)

    else:
        raise TypeError('a must be an integer')
