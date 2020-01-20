#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Write an empty class BaseGeometry."""


class Square(Rectangle):
    """Funcion"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return ('[Square] {}/{}'.format(self.__size, self.__size))
