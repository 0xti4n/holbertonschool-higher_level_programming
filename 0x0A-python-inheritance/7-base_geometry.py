#!/usr/bin/python3
"""Write an empty class BaseGeometry."""


class BaseGeometry:
    """Function"""
    def area(self):
        """function"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """function"""
        if type(value) is not int:
            raise TypeError('{} must be and integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
