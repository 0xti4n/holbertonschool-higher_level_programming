#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Write an empty class BaseGeometry."""


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("height", self.__height)
        super().integer_validator("width", self.__width)
