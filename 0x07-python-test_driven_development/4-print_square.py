#!/usr/bin/python3
"""Function that prints a square with the character #
if the type of size is not int raises error
if size is < 0 raises an error
"""


def print_square(size):
    """Function that prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size, end='')
        print()
