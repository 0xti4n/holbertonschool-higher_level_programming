#!/usr/bin/python3
"""Square that defines a square by
       size = no type value
"""


class Square:
    """Square that defines a square by
       size = no type value
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
